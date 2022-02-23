import subprocess
print(subprocess.check_output(['echo' ,'%cd%'],shell=True).decode('utf-8'))
def clone(path):
    subprocess.call(['git','clone',path])
def addtostage(path):
    """path -   Add Path of file to Move on staging area"""
    try:
        subprocess.call(['git','add',path])
    except:
        pass