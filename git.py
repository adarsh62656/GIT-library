import subprocess
import os
def clone(path):
    x=subprocess.Popen(['git','clone',path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = x.communicate()
    print(stdout.decode('utf-8'), stderr.decode('utf-8'))
def addtostage(path):
    """path -   Add Path of file to Move on staging area"""
    x=subprocess.Popen(['git','add',path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = x.communicate()
    print(stdout.decode('utf-8'), stderr.decode('utf-8'))
def pri(process):
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8'), stderr.decode('utf-8'))
def rmstage(path):
    """path -   Add Path of file to remove from staging area"""
    pri(subprocess.Popen(['git','rm','-f',path], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    print(path,": Removed Successfuly")
def commit(message):
    """message -   Enter Commit Message"""
    pri(subprocess.Popen(['git','commit','-m',message], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
def gitinit(path=""):
    """path -   Enter Path to initialize empty repozitory"""
    if path=="":
        pri(subprocess.Popen(['git','init'], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    else:
        pri(subprocess.call(['git','init',path], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
def log(path=""):
    """path -   Enter Path to see logs of repozitory"""
    os. chdir(path)
    print(subprocess.check_output(['git' ,'log'],shell=True).decode('utf-8'))
def add_origin(origin,path):
    """origin -  add the remote point name """
    """url    -  add url to connect with remote repositary"""
    subprocess.call(['git','remote','add',origin,path])
def git_push(origin,branch):
    """origin -  mantion the remote point name to push"""
    """branch -  branch name from where to push"""
    subprocess.call(['git','push',origin,branch])
def status(path=""):
    """path -   Enter Path to see logs of repozitory"""
    if not path=="":
        os. chdir(path)
    print(subprocess.check_output(['git' ,'status'],shell=True).decode('utf-8'))
