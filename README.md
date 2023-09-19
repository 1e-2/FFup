
# FFup - 🚀 Snapshot Batch Updater for WebUI 1111 Extensions & ComfyUI Nodes
![60% Works](https://img.shields.io/badge/60%25%20of%20the%20Time-It%20Works%20Every%20Time-green)

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Repo Size](https://img.shields.io/github/repo-size/1e-2/FFup)
![Coffee Level](https://img.shields.io/badge/Coffee%20Level-110%25-brown)
![Stress Level](https://img.shields.io/badge/Stress%20Level-Endurable-green)
![License](https://img.shields.io/github/license/1e-2/FFup)
![Forks](https://img.shields.io/github/forks/1e-2/FFup?style=social)
![Followers](https://img.shields.io/github/followers/1e-2?label=Follow&style=social)


🚫 **Tired of breaking your UI due to an inc ompatible extension?**
🔍 **Seeking an efficient way to keep your WebUI1111 Extensions & ComfyUI Nodes updated with last min gits?** 🔄

**Meet FFup** - Your go-to solution! 🤟 🥃

FFup is an unofficial simple batch updater crafted to handle easaly the last working git hashes of the extensions. Not only does it streamline the update process, but it also prioritizes safety. Before making any changes, FFup diligently creates recovery snapshots, ensuring you always have a way back.

🔑 **Key Benefits**:
1. 🔄 **Smooth Updates**: FFup keeps your bleeding edge dev system envirement up-to-date with the rapid evolution of nodes and extensions.
2. 🛡 **Safety First**: Updates can sometimes cause hiccups. With FFup's recovery snapshots, you can easily roll back to a stable state in seconds.
3. 💼 **Developer-Friendly**: Designed for development environments, FFup ensures you're always equipped with the latest tools without the risk of breaking your setup.


**Note**: Before updating, ensure the UI isn't actively using the folders. This guarantees a seamless git pull for each repository.

![Screenshot_301](https://github.com/1e-2/FFup/assets/50985923/40643270-d172-441e-b3f6-e23809a870f3)


## Overview
![ComfyUI](https://img.shields.io/badge/Supports-ComfyUI-green)
![AUTOMATIC1111](https://img.shields.io/badge/Supports-AUTOMATIC1111-green)
![Recovery Snapshots](https://img.shields.io/badge/Feature-Recovery%20Snapshots-blue)
![Quick Update](https://img.shields.io/badge/Mode-Quick%20Update-yellow)
![Cross-Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey)

`FFup` is a Python tool crafted for batch updating the extensions for AUTOMATIC1111 WebUI and the custom nodes for ComfyUI. But that's not all; it offers a safety net allowing you to easily revert to previous versions in case the new updates break your GUI. 

Features:
- **Batch Update**: Check and pull updates for all the installed repositories in one go.
- **Recovery Snapshots**: Before any major action, FFup creates a few kb in size snapshot, ensuring you have a safety net.
- **Easy Restoration**: The devs made a mistake and crashed your UI? No problem! You can easily revert to a previous state using FFup option 2.
- **Detailed Reports**: Always stay informed. After every operation, FFup provides a detailed report, saved as `FFup-summary.txt`.
- **Quick Modes**: For developers or those in a hurry, quick batch and bash scripts are available for swift updates without backups.

## Quick Start: No Installation Needed 🚀

You don't necessarily have to perform a full installation to enjoy the power of FFup. Here's a hassle-free way to get started:

1. **Position Yourself Right**: Ensure you're in the base directory of the UI you're looking to update.

2. **Grab the Code**:
   Clone the FFup repository with:
   ```bash
   git clone https://github.com/1e-2/FFup
   ```

3. **Run & Update**:
   Dive into the directory and choose your mode of operation:
   - For the comprehensive FFup experience with backup options:
     ```bash
     python FFup.py
     ```
     or use the provided batch/shell scripts for the full version:
     ```bash
     ./FFup.bat   # On Windows
     ./FFup.sh    # On Linux/Mac
     ```

   - For the speedsters who want a quick update (performing git pull on all extensions/nodes) without backups:
     ```bash
     ./FFquickUpdate.bat   # On Windows
     ```

📌 **Note**: The quick update method is swift, but doesn't create backup snapshots. Use it if you're confident or if you're in a test environment.


## Installation

### From PyPI 

You'll be able to easily install `FFup` via pip:

```bash
pip install FFup
```

# USAGE


## 🛠 Normal mode Operations: Taking Control with FFup

### Step into the FFup World:

1. **Navigate to Your Desired Base Directory**: This should be where your main root directory of the UI reside.


2. **"Unleash" FFup**: By just typing FFup will launching the script, FFup jumps into action. It has an innate ability to detect which interface you're operating on - be it the `AUTOMATIC1111 WebUI Extensions` or the `ComfyUI Custom Nodes`.

```bash
cd R:\autoKOR\stable-diffusion-webui
FFup
```

```bash
cd R:\ComfyUI
FFup
```
   
   If, for some reason, it feels lost (can't auto-detect the UI), don't fret! It'll politely ask you for the correct path.

### Now, let's explore what FFup lays on the table:

### 1. **Check for updates**: 

Imagine having a personal assistant that keeps tabs on all your extensions or nodes. That's exactly what this option offers! FFup meticulously checks the current git hashes of your extensions/nodes and juxtaposes them with the latest available on their respective remote repositories.

You're then presented with a neat summary that provides insights into:

- Repositories raring to be updated.
- A comparison of the current commit vs. the newest kid on the block (latest commit).

But wait, there's more! If updates beckon, FFup ensures it doesn't take any step without your green signal. On receiving your thumbs up:

- It becomes your safety net by creating an auto-recovery snapshot, aptly named `FFup-recoveryLAST.txt`, solely for those extensions/nodes in the updating queue.
- Riding on this safety cushion, it confidently updates the repositories.
- The cherry on top? Post the update action, it crafts a detailed summary report named `FFup-summary.txt`, showcasing the updates and any repositories that were already in their prime (up-to-date).

### 2. **Create recovery snapshot**: 

Think of this as your time machine! This option empowers you to manually snapshot the current state of all your extensions/nodes. In essence, you're capturing a moment in their timeline. These memories are preserved as `FFup-recovery[timestamp].txt`.

### 3. **Restore from snapshot**: 

Ever wished to turn back time? Here's your chance! If a need arises to revert to a cherished previous state:

- FFup showcases all the recovery snapshots you've accumulated over time.
- It's your turn to pick a memory.
- Upon selection, FFup painstakingly ensures each extension/node reverts to the exact git hash immortalized in that snapshot.

### **Navigational Aids**:

For those moments when you're contemplating your next move or want to bow out gracefully:

- Opt for `0` - and you'll be ushered back to the previous menu.
- Choose `00` - and FFup will take a bow, exiting the stage (application).
  
![Screenshot_300](https://github.com/1e-2/FFup/assets/50985923/b4ab1680-15ad-47e5-b24c-9bc56dcb93d3)

## ⚠️ Quick Update Mode: For Developers

FFup's quick update mode is designed specifically for developers who require a rapid update mechanism. This mode directly updates all repositories without creating any recovery snapshots.

**Warning**: Using the quick update mode comes with risks:

- 🚫 **No Recovery Snapshots**: Unlike the standard mode, this mode does not create any recovery snapshots before updating. If a new update causes issues, there's no automated way to revert back.
- ⚠️ **Potential for Breakage**: New extensions or updates might introduce incompatibilities or break the WebUI.

Given these risks, this mode is best suited for:

1. Experienced users familiar with manual recovery.
2. Environments where potential breakage is acceptable or expected.

For most users, it's recommended to use FFup's default mode which provides safety mechanisms like recovery snapshots.

### How to Use Quick Update Mode:

Navigate to the desired directory and run:

```bash
FFup --fast
```
![Screenshot_302](https://github.com/1e-2/FFup/assets/50985923/22c2477d-d645-40b1-ae18-3ad6ed223946)
![Screenshot_294](https://github.com/1e-2/FFup/assets/50985923/94201290-0d75-4dc8-8b55-596490848d7a)

⚠️ **Caution**: The quick scripts bypass the recovery snapshot creation. They're designed for swift 0-day updates in development environments where backups aren't crucial.

Remember, FFup's is about precision. Instead of bulky folder backups, FFup uses git hashes, ensuring recovery is quick to the previous hash that worked with your instalation, precise, and space-efficient. It's modern recovery for modern interfaces!

🚫 **Important Considerations**:

- 📌 **Seamless Pull ≠ Flawless Extension**: While FFup ensures a seamless git pull for each repository, this doesn't guarantee that the latest version of an extension will work flawlessly. If a developer pushes a version with bugs or issues, you might encounter them.
  
- ⏮ **Reverting**: In cases where an update causes issues, you can effortlessly revert back to a previous, stable state using the snapshots created by FFup. Alternatively, you can wait for the extension developer to push a fix.

- 🛡 **Liability**: Please understand that while we aim to provide a tool that facilitates ease and safety, we cannot be held responsible for any unforeseen issues or conflicts that may arise from using FFup. The script is shared "as is" and is intended for edge-case development environments where users are testing the latest nodes and extensions.

- 💼 **No Unintended Alterations**: FFup respects the integrity of your setup. It doesn't modify, change, or interfere with your UI's virtual environment or any other environments. All updates are strictly performed using `git pull` on individual extensions, ensuring transparency and reliability.


## Contributing

Feel free to fork the repository, make changes, and open a pull request. All contributions are welcome!



 🥃 to a ~seamless updating experience! 🚀

**P.S.** This README was crafted with a dash of humor and a sprinkle of tech by... 🤖. If you found any typos, blame the humans!



## License

This project is licensed under the MIT License. See [LICENSE](https://github.com/1e-2/FFup/blob/main/LICENSE) for details.

## Author

- **1e-2** - [GitHub](https://github.com/1e-2)
- **idlebg** - [GitHub](https://github.com/idlebg)
For any additional questions or comments, please [open an issue](https://github.com/1e-2/FFup/issues/new).

And as always, keep updating and stay comfy!

###  🌐 **Contact Information**

The **FFusion.ai** project is proudly maintained by **Source Code Bulgaria Ltd** & **Black Swan Technologies**.

📧 Reach us at [di@ffusion.ai](mailto:di@ffusion.ai) for any inquiries or support.

#### 🌌 **Find us on:** 

- 🐙 [GitHub](https://github.com/1e-2)
- 😊 [Hugging Face](https://huggingface.co/FFusion/)
- 💡 [Civitai](https://civitai.com/user/idle/models)

🔐 **Security powered by** [Comodo.BG](http://Comodo.BG) & [Preasidium.CX](http://Preasidium.CX)

🚀 Marketing by [Гугъл.com](http://Гугъл.com)

📩 [![Email](https://img.shields.io/badge/Email-enquiries%40ffusion.ai-blue?style=for-the-badge&logo=gmail)](mailto:enquiries@ffusion.ai)

🌍 Sofia Istanbul London

![ffusionai-logo](https://github.com/1e-2/FFup/assets/50985923/58886947-704e-4391-8f0d-2c5d742beb0f)


