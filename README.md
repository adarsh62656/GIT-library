# Github Library

```git``` is a library that can be used to run git commands in python.


## Usage

```python
import git

# clones repository from the "url"
git.clone(url)

# initialize empty repository on current location
git.gitinit()

# adds files to the stage from the "path".
git.addtostage(path)

#remove "file" from staging area
git.rmstage(file)

#commits with the "message"
git.commit(message)

#to see the logs of repo
git.log()

'''

origin -  add the remote point name 
url    -  add url to connect with remote repositary
'''
git.add_origin(origin,path)

'''
origin -  mantion the remote point name to push
branch -  branch name from where to push"""
'''
git.push(origin,path)

'''
path -   Enter Path to see logs of repozitory
'''
git.status()
```
