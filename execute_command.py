# Simple program to execute commands in Windows, Linux or Mac on the target machine
# set your payload and send to the target
# Author Rocken2k 
 
import subprocess

command = "" # here your command
subprocess.Popen(command, shell=True)