import os
import subprocess


if __name__ == '__main__':
    current_directory = os.getcwd()
    for file in os.listdir(current_directory):
        if file.startswith('lab'):
            lab_directory = os.path.join(current_directory, file)
            run_path = 'run_lab_tasks.py'
            print(f'======= RUNNING {lab_directory} TASKS =======')
            subprocess.run(['python', run_path], cwd=lab_directory)
            print('\n\n\n\n')
