import subprocess
import os


if __name__ == '__main__':
    current_directory = os.getcwd()
    root_directory = os.path.dirname(current_directory)
    subprocess.run(['pytest', os.path.relpath(current_directory, root_directory)], cwd=root_directory)
