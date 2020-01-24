#! /usr/bin/python

import subprocess 
import time 
import os 

#Calling the script file

print "Starting file .sh.."
time.sleep(2)
subprocess.call("./sleep.sh")
print "End the file :D "

print("\n")

# Calling the command

os.system("echo hola")
