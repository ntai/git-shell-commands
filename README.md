# git-shell-commands
git-shell-commands written in Python (3.8)

Currently there are only 3 commands.

- help: Shows help message

- list: List existing repositories

- create-repo: Creates an empty repository

With list and create-repo, my needs for starting a new repo on private server is met. 

## list
lists the directory of git repos.

## create-repo
creates a new repo. If the parent directory does not exist, it will create.

All operation should be done as user "git". 

## Usage
by having "git-shell-commands" directory under the home directory of user "git", and by setting the shell of "git" user to "git-shell", logging into the server as "git", "git-shell" uses the executables in "git-shell-commands" as the commands. 
