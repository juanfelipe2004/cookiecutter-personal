import subprocess

MESAGE_COLOR = "\x1b[34m"
print(f'{MESAGE_COLOR}initializing a git repository...')

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

git_path = f"{{cookiecutter.git_path}}"

if git_path.startswith('git@github.com'):
    subprocess.call(['git', 'remote', 'add', 'origin', f"{{cookiecutter.git_path}}"])
    subprocess.call(['git', 'pull', 'origin', 'master'])
    subprocess.call(['git', 'push', 'origin', 'master'])
else:
    print("No valid entry, please check your git path")