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

class log:
    def __init__(self,path=""):
        """path -   Enter Path to see logs of repozitory"""
        if path!="":
            os. chdir(path)
        log_list=subprocess.check_output(['git' ,'log'],shell=True).decode('utf-8')
        log_lines=log_list.split('\n')
        log_lines = [line for line in log_lines if line != '']
        index=-1
        commit_list=[]
        while index<len(log_lines)-1:
            index+=1
            if len(log_lines[index].split()[1])==40 and log_lines[index].split()[0]=='commit':
                commit_portion={}
                commit_portion['id']=log_lines[index].split()[1].strip()
            elif log_lines[index].split()[0]!='Author:' and log_lines[index].split()[0]!='Date:' and log_lines[index].split()[0]!='Merge:':
                commit_portion['message']=log_lines[index].strip()
                commit_list.append(commit_portion)
                commit_portion={}
            else:
                commit_portion[log_lines[index].split()[0][:-1]]=log_lines[index].split()[1:]
        self.commit_list=commit_list
        self.author=[commit_dict['Author'] for commit_dict in commit_list]
        self.message=[commit_dict['message'] for commit_dict in commit_list]
        self.id=[commit_dict['id'] for commit_dict in commit_list]

def add_origin(origin,path):
    """origin -  add the remote point name """
    """url    -  add url to connect with remote repositary"""
    subprocess.call(['git','remote','add',origin,path])
    
def git_push(origin,branch):
    """origin -  mantion the remote point name to push"""
    """branch -  branch name from where to push"""
    subprocess.call(['git','push',origin,branch])

class status:
    def __init__(self,path=""):
        """path -   Enter Path to see logs of repozitory"""
        if path!="":
            os. chdir(path)
        file_names=subprocess.check_output(['git' ,'status'],shell=True).decode('utf-8')
        file_names=file_names.split('\n')
        file_names = [line.strip() for line in file_names if line != '']
        file_status=['new','Untracked','Modified']
        #return file,status
    def __printtags(self,inputext):
        inputext=inputext.split('\n')
        inputext=[inputfile[2:] for inputfile in inputext if inputfile != '']
        return inputext
    def modified(self):
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--modified'],shell=True).decode('utf-8'))
    def cached(self):
        return self.__printtags(subprocess.check_output(['git','ls-files','-t'],shell=True).decode('utf-8'))
    def untracked(self):
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--others'],shell=True).decode('utf-8'))
    def deleted(self):
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--deleted'],shell=True).decode('utf-8'))
    def staged(self):
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--stage'],shell=True).decode('utf-8'))
    def ignored(self):
        '''ignored files'''
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--ignored'],shell=True).decode('utf-8'))
    def unmerged(self):
        '''unmerged files'''
        return self.__printtags(subprocess.check_output(['git','ls-files','-t','--unmerged'],shell=True).decode('utf-8'))
