import os
import sys
import subprocess
import platform
import time

# Function to install packages via pip
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Error: Failed to install {package}.")
        sys.exit(1)

# Function to rotate screen using xrandr on Linux
def rotate_screen_linux():
    try:
        subprocess.call("xrandr --output eDP-1 --rotate right", shell=True)
        time.sleep(0.3)
        subprocess.call("xrandr --output eDP-1 --rotate inverted", shell=True)
        time.sleep(0.3)
        subprocess.call("xrandr --output eDP-1 --rotate normal", shell=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to rotate screen using xrandr.")
        sys.exit(1)

# Function to rotate screen using rotatescreen on Windows
def rotate_screen_windows():
    try:
        import rotatescreen
        screen = rotatescreen.get_primary_display()
        for i in range(1, 9):
            screen.rotate_to(i * 90 % 360)
            time.sleep(0.3)
    except ImportError:
        print("Error: Failed to import rotatescreen library on Windows.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Function to rotate screen using Quartz on macOS
def rotate_screen_macos():
    try:
        import Quartz.CoreGraphics as CG
        # Create rotation transformation for macOS
        screen = CG.CGEventCreate(None)  # Placeholder, Quartz doesn't directly support screen rotation
        print("Rotation on macOS not directly supported by Quartz. No rotation performed.")
    except ImportError:
        print("Error: Failed to import Quartz library on macOS.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Check the operating system and handle accordingly
def check_os_and_install():
    current_os = platform.system()

    if current_os == "Windows":
        print("Windows OS detected. Rotating screen using rotatescreen.")
        try:
            install_package("rotatescreen")
        except subprocess.CalledProcessError:
            print("Error: Unable to install rotatescreen. Make sure you have pip installed.")
            sys.exit(1)

    elif current_os == "Linux":
        print("Linux OS detected. Using xrandr to rotate the screen.")
        try:
            # Install xrandr if it's not already installed
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "x11-xserver-utils"])
        except subprocess.CalledProcessError:
            print("Error: Failed to install xrandr. Make sure you have the correct permissions.")
            sys.exit(1)

    elif current_os == "Darwin":
        print("macOS detected. Using Quartz to handle rotation.")
        # No installation required for macOS, Quartz is part of macOS
    else:
        print("Unsupported OS")
        sys.exit(1)

# Main script execution
def main():
    check_os_and_install()  # Install the required packages (if needed)
    
    current_os = platform.system()
    
    if current_os == "Linux":
        rotate_screen_linux()  # Rotate screen using xrandr on Linux
    elif current_os == "Windows":
        rotate_screen_windows()  # Rotate screen using rotatescreen on Windows
    elif current_os == "Darwin":
        rotate_screen_macos()  # Rotate screen on macOS (though Quartz doesn't directly support it)
    else:
        print("Rotation logic not implemented for this OS.")
        sys.exit(1)

if __name__ == "__main__":
    main()

