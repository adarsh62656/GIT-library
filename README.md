
# Github Library

```git``` is a library that can be used to run git commands in python.

## Installation
Paste ```git.py``` file in the ```Lib``` folder of the path retreved from ```os.path.dirname(sys.executable)```

## Usage

```python
import git

# clones repository from the "url"
git.clone(url)
```
### Git init
```python
# initialize empty repository on current location
git.gitinit()
```
### Git add
```python
# adds files to the stage from the "path".
git.addtostage(path)
```
### Git rm
```python
#remove "file" from staging area
git.rmstage(file)
```
### Git commit
```python
#commits with the "message"
git.commit(message)
```
### Git remote add origin
```python
'''

origin -  add the remote point name 
url    -  add url to connect with remote repositary
'''
git.add_origin(origin,path)
```
### Git push
```python
'''
origin -  mantion the remote point name to push
branch -  branch name from where to push"""
'''
git.push(origin,path)
```
### Git status
```python 
from git import status
```
To get modified files use:
```python
status.modified()
```
To get cached files use:
```python
status.cached()
```
To get untracked files use:
```python
status.untracked()
```
To get deleted files use:
```python
status.deleted()
```
To get staged files use:
```python
status.staged()
```


### Git log
```python
#importing log class from git library
from git import log
```
`log.commit_data()`  function can be used to find particular log details based on its `commit id` or `commit message`.
 ```
 # Using commit Message:
 log().commit_data('Create README.md')
```
 ```
 # Using commit ID:
 log().commit_data('70bca60c7a99f7cb10d9beb6d4550d6904a012a9')
```
