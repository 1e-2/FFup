import os
import sys
import subprocess
import platform
from datetime import datetime


def get_file_size_kb(filename):
    return os.path.getsize(filename) // 1024

def get_git_details(path):
    current_commit = subprocess.getoutput(f'git -C {path} rev-parse HEAD')
    remote_commit_output = subprocess.getoutput(f'git -C {path} ls-remote origin -h refs/heads/master')
    remote_commit = remote_commit_output.split()[0] if remote_commit_output else "Unknown"
    return current_commit, remote_commit

def display_progress_bar(iteration, total, prefix='', length=40):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end='\r')
    if iteration == total:
        print()

def check_for_updates(path):
    repos_to_update = []
    updated_repos = []
    up_to_date_repos = []

    all_repos = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and os.path.exists(os.path.join(path, d, '.git'))]

    for idx, dir_name in enumerate(all_repos, 1):
        display_progress_bar(idx, len(all_repos), prefix="Checking for updates")
        
        dir_path = os.path.join(path, dir_name)
        current_commit, remote_commit = get_git_details(dir_path)
            
        if remote_commit != "Unknown" and current_commit != remote_commit:
            repos_to_update.append((dir_name, current_commit, remote_commit))
        else:
            up_to_date_repos.append((dir_name, current_commit))

    if repos_to_update:
        print("\nRepositories that can be updated:\n")
        for repo, current, latest in repos_to_update:
            print(f"Name of git: {repo}")
            print(f"Current commit: {current}")
            print(f"Can be updated to: {latest}")
            print("******")
        print(f"\n{len(repos_to_update)} objects can be updated.")
        proceed = input("Proceed? Y/N: ").strip().lower()
        if proceed == 'y':
            # Create a full recovery snapshot
            recovery_filename = "FFup-recoveryLAST.txt"
            create_recovery_snapshot(path, recovery_filename)
            print(f"\nAuto Recovery file created as {recovery_filename}.")

            # Update the repositories
            for idx, (repo, current, latest) in enumerate(repos_to_update, 1):
                display_progress_bar(idx, len(repos_to_update), prefix="Updating repositories")
                subprocess.run(['git', 'pull'], cwd=os.path.join(path, repo))
                updated_repos.append((repo, current, latest))

        # Generate summary
        with open("FFup-summary.txt", "w") as f:
            f.write("Update Summary:\n")
            
            f.write("\nUpdated:\n")
            for repo, current, latest in updated_repos:
                f.write(f"{repo} [old hash: {current} -> updated to: {latest}]\n")
            
            f.write("\nUp to date:\n")
            for repo, commit in up_to_date_repos:
                f.write(f"{repo} [git hash: {commit}]\n")
            
            f.write(f"\nUpdated Repositories: {len(updated_repos)}\n")
            f.write(f"Repositories Already Up-to-Date: {len(up_to_date_repos)}\n")

        print("\nUpdate Summary:")
        print(f"Updated Repositories: {len(updated_repos)}")
        print(f"Repositories Already Up-to-Date: {len(up_to_date_repos)}")
        recovery_file_size = get_file_size_kb("FFup-recoveryLAST.txt")
        print(f"Auto Recovery file created. (Space wasted for recovery: {recovery_file_size}KB)")
        print("To revert changes use FFup-recoveryLAST.txt")
        print("Results saved at FFup-summary.txt")
    else:
        print("\nAll repositories are up-to-date.")
        # Generate summary for up-to-date repos
        with open("FFup-summary.txt", "w") as f:
            f.write("Update Summary:\n")
            f.write("\nUp to date:\n")
            for repo, commit in up_to_date_repos:
                f.write(f"{repo} [git hash: {commit}]\n")
            f.write(f"Repositories Already Up-to-Date: {len(up_to_date_repos)}\n")

def create_recovery_snapshot(path, auto=False):
    if auto:
        filename = "FFup-recoveryLAST.txt"
    else:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"FFup-recovery{timestamp}.txt"
    
    all_repos = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and os.path.exists(os.path.join(path, d, '.git'))]

    with open(filename, "w") as f:
        for idx, dir_name in enumerate(all_repos, 1):
            display_progress_bar(idx, len(all_repos), prefix="Creating recovery snapshot")
            dir_path = os.path.join(path, dir_name)
            current_commit, _ = get_git_details(dir_path)
            f.write(f"{dir_name} {current_commit}\n")
    
    if not auto:
        print(f"Recovery snapshot saved as {filename} (Space wasted: {get_file_size_kb(filename)}KB)")

def restore_from_snapshot(path):
    # List all FFup-recovery*.txt files in the current directory
    files = [f for f in os.listdir() if f.startswith("FFup-recovery") and f.endswith(".txt")]
    if not files:
        print("No recovery files found.")
        return
    for idx, filename in enumerate(files, 1):
        print(f"{idx}. {filename}")
    choice = int(input("Select a file to restore from: ").strip())
    if choice < 1 or choice > len(files):
        print("Invalid choice.")
        return
    recovery_file = files[choice - 1]

    with open(recovery_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            repo_name, commit_hash = line.strip().split()
            repo_path = os.path.join(path, repo_name)
            if os.path.exists(repo_path):
                subprocess.run(['git', 'checkout', commit_hash], cwd=repo_path)
            else:
                print(f"Directory {repo_name} does not exist. Skipping...")

    print(f"Restored repositories from {recovery_file}")

def main():
    root_dir = os.getcwd()
    path = ""

    if os.path.exists(os.path.join(root_dir, 'custom_nodes')):
        print("Detecting UI...")
        print("ComfyUI found!")
        path = os.path.join(root_dir, 'custom_nodes')
    elif os.path.exists(os.path.join(root_dir, 'extensions')):
        print("Detecting UI...")
        print("Automatic 1111 found!")
        path = os.path.join(root_dir, 'extensions')
    elif os.path.exists(os.path.join(root_dir, 'ComfyUI', 'custom_nodes')):
        print("ComfyUI folder found...")
        path = os.path.join(root_dir, 'ComfyUI', 'custom_nodes')
    else:
        user_path = input("No known UI detected.\nEnter UI base|root location: ")
        if os.path.exists(user_path):
            path = user_path
        else:
            print(f"Path {user_path} does not exist.")
            return

    while True:
        print("Select an option:")
        print("1. Check for updates")
        print("2. Create recovery snapshot")
        print("3. Restore from snapshot")
        print("00. Exit")
        choice = input("Enter choice (1/2/3/00): ").strip()

        if choice == "1":
            check_for_updates(path)
            break
        elif choice == "2":
            create_recovery_snapshot(path)
            break
        elif choice == "3":
            recovery_choice = restore_from_snapshot(path)
            if recovery_choice == "go_back":
                continue
            else:
                break
        elif choice == "00":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 00.")

def restore_from_snapshot(path):
    # List all FFup-recovery*.txt files in the current directory
    files = [f for f in os.listdir() if f.startswith("FFup-recovery") and f.endswith(".txt")]
    if not files:
        print("No recovery files found.")
        return "go_back"
    for idx, filename in enumerate(files, 1):
        print(f"{idx}. {filename}")
    print("0 - go back to the previous menu")
    print("00 - Exit")
    choice = input("Select a file to restore from: ").strip()
    if choice == "0":
        return "go_back"
    elif choice == "00":
        exit()
    elif choice.isdigit() and 1 <= int(choice) <= len(files):
        recovery_file = files[int(choice) - 1]
        with open(recovery_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                repo_name, commit_hash = line.strip().split()
                repo_path = os.path.join(path, repo_name)
                if os.path.exists(repo_path):
                    subprocess.run(['git', 'checkout', commit_hash], cwd=repo_path)
                else:
                    print(f"Directory {repo_name} does not exist. Skipping...")
        print(f"Restored repositories from {recovery_file}")
    else:
        print("Invalid choice.")
        return "go_back"

def execute_fast_version():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == "Windows":
        bat_path = os.path.join(current_dir, "FFquickUpdate.bat")
        subprocess.run([bat_path], shell=True)
    else:  # Assuming Unix-like system
        sh_path = os.path.join(current_dir, "FFquickUpdate.sh")
        subprocess.run(["bash", sh_path], shell=True)

if __name__ == "__main__":
    if "--fast" in sys.argv:
        execute_fast_version()
    else:
        main()
