import os
from utils import run_tasks


if __name__ == '__main__':
    current_directory = os.getcwd()
    run_tasks(current_directory, os.path.dirname(current_directory))
