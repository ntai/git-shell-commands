#!/usr/local/bin/python3.8

import os
import subprocess

def get_home_dir():
    return os.path.expanduser("~git")

def get_git_dirs(dir=None):
    if dir is None:
        dir = get_home_dir()
        pass
    git_dirs = []
    for item in os.listdir(dir):
        a_path = os.path.join(dir, item)
        if not os.path.isdir(a_path):
            continue
        if item[-4:] != ".git":
            git_dirs = git_dirs + get_git_dirs(a_path)
            continue
        cmd = 'git --git-dir="{}" rev-parse --is-bare-repository'.format(a_path)
        git = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if git.returncode == 0:
            if git.stdout == b'true\n':
                git_dirs.append(a_path)
                pass
            pass
        else:
            print(git.stderr)
            pass
        pass

    return git_dirs 
