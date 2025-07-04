@echo off
setlocal

:: Set the version and installer URL
set "PYTHON_VERSION=3.10.0"
set "INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%INSTALLER%"

:: Check if real Python is already installed
where python | findstr /i "WindowsApps" >nul
if %errorlevel% equ 0 (
    echo Python is NOT properly installed. Proceeding to download...
) else (
    echo Real Python is already installed.
    goto install_requirements
)

:: Download Python installer
echo Downloading Python %PYTHON_VERSION%...
curl -o "%TEMP%\%INSTALLER%" %PYTHON_URL%
if %errorlevel% neq 0 (
    echo ERROR: Failed to download Python.
    pause
    exit /b 1
)

:: Install Python silently for all users and add to PATH
echo Installing Python...
start /wait "" "%TEMP%\%INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
if %errorlevel% neq 0 (
    echo ERROR: Python installation failed!
    pause
    exit /b 1
)

:: Use known path after install
set "PYTHON_EXE=C:\Program Files\Python310\python.exe"

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python not found at expected location.
    pause
    exit /b 1
)

echo Python installed successfully.

:: Upgrade pip
"%PYTHON_EXE%" -m ensurepip
"%PYTHON_EXE%" -m pip install --upgrade pip

:install_requirements
:: Use the same Python executable to install requirements
echo Installing dependencies...
"%PYTHON_EXE%" -m pip install -r "%~dp0requirements.txt"
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

echo ✅ All done!
pause
