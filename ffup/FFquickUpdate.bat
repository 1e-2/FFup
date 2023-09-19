@echo off
setlocal

REM Display a warning message
echo [WARNING] This script is intended for developers only!
echo New extensions might break the WebUI.
echo It's recommended to use FFup for safer updating with recovery options.
pause

REM Check for \custom_nodes directory
if exist .\custom_nodes (
    echo Detecting UI...
    echo ComfyUI found! Updating nodes.
    cd custom_nodes
    call :gitUpdate
    cd ..
    exit /b
)

REM Check for \extensions directory
if exist .\extensions (
    echo Detecting UI...
    echo Automatic 1111 found! Updating extensions.
    cd extensions
    call :gitUpdate
    cd ..
    exit /b
)

REM Check for \ComfyUI\custom_nodes directory
if exist .\ComfyUI\custom_nodes (
    echo ComfyUI found! Updating nodes...
    cd ComfyUI\custom_nodes
    call :gitUpdate
    cd ..\..
    exit /b
)

REM If none of the above paths are found, prompt the user for a path
echo No known UI detected.
set /p path="Enter UI location: "
if not "%path%"=="" (
    cd %path%
    call :gitUpdate
    cd ..
)

exit /b

REM Function to pull all subdirectories
:gitUpdate
for /d %%i in (*) do (
    cd %%i
    if exist .git (
        echo Pulling %%i
        git pull
    )
    cd ..
)
exit /b
