# Contents
- [Fix mirrorlist](#fix-mirrorlist)
- [Fn keys in QTerminal](#fn-keys-in-qterminal)
- [Git](#git)

## Fix mirrorlist
```bash
sudo reflector --country Russia --latest 15 --age 2 --fastest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

## Fn keys in QTerminal  
If the function keys do not work, use the following alternatives:  
| Key | Alt 1 | Alt 2 |
|----|-------|--------|
| F1 | Alt+1 | Esc 1  |
| F2 | Alt+2 | Esc 2  | 
| F3 | Alt+3 | Esc 3  |
| F4 | Alt+4 | Esc 4  |
| F5 | Alt+5 | Esc 5  |
| F6 | Alt+6 | Esc 6  |
| F7 | Alt+7 | Esc 7  |
| F8 | Alt+8 | Esc 8  |


## Git
### Checkout single branch (works correctly on Git 2.37):
```bash
git clone -b <remoteBranch> --single-branch --depth 1 ssh://username@servername.net:serverport/PathToProject <FolderName>
```
### Checkout single commit
```bash
# make a new blank repository in the current directory
git init
# add a remote
git remote add origin url://to/source/repository
# fetch a commit (or branch or tag) of interest
# Note: the full history up to this commit will be retrieved unless 
#       you limit it with '--depth=...' or '--shallow-since=...'
git fetch origin <sha1-of-commit-of-interest>
# reset this repository's master branch to the commit of interest
git reset --hard FETCH_HEAD
```
