import os
import platform

# Function to get the Desktop path, or fallback to home directory if Desktop doesn't exist
def get_desktop_path():
    current_os = platform.system()

    if current_os == "Windows":
        # Windows Desktop path
        desktop_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop')
    elif current_os == "Linux":
        # Linux Desktop path (common for most distros)
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        print("Unsupported OS")
        return None

    # Check if Desktop directory exists
    if os.path.isdir(desktop_path):
        return desktop_path
    else:
        # If Desktop doesn't exist, fall back to home directory
        print(f"Desktop not found, using home directory: {os.path.expanduser('~')}")
        return os.path.expanduser('~')  # Use home directory as fallback

# Get Desktop or fallback directory
desktop = get_desktop_path()

if desktop:
    for i in range(500):
        new_folder = 'Virus' + str(i)
        folder_path = os.path.join(desktop, new_folder)
        
        # Uncomment the next line to create 500 directories (Warning: This can create a lot of directories!)
        os.mkdir(folder_path)
        print(f"Would create folder: {folder_path}")  # Prints the folder path (for testing purposes)
else:
    print("Error: Could not determine the desktop or fallback directory.")

