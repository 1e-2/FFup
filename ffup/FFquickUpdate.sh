#!/bin/bash

# Display a warning message
echo "[WARNING]: This script is intended for developers only!"
echo "New extensions might break the WebUI."
echo "It's recommended to use FFup for safer updating with recovery options."
read -p "Press [Enter] to continue..."

# Function to pull all subdirectories
gitUpdate() {
    for d in ./* ; do
        if [ -d "$d" ]; then
            cd "$d"
            if [ -d ".git" ]; then
                echo "Pulling $d"
                git pull
            fi
            cd ..
        fi
    done
}

# Check for ./custom_nodes directory
if [ -d "./custom_nodes" ]; then
    echo "Detecting UI..."
    echo "ComfyUI found! Updating nodes."
    cd custom_nodes
    gitUpdate
    cd ..
    exit
fi

# Check for ./extensions directory
if [ -d "./extensions" ]; then
    echo "Detecting UI..."
    echo "Automatic 1111 found! Updating extensions."
    cd extensions
    gitUpdate
    cd ..
    exit
fi

# Check for ./ComfyUI/custom_nodes directory
if [ -d "./ComfyUI/custom_nodes" ]; then
    echo "ComfyUI found! Updating nodes..."
    cd ComfyUI/custom_nodes
    gitUpdate
    cd ../..
    exit
fi

# If none of the above paths are found, prompt the user for a path
echo "No known UI detected."
read -p "Enter UI location: " path
if [ -d "$path" ]; then
    cd "$path"
    gitUpdate
    cd ..
fi
