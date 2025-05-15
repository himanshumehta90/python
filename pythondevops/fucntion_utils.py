import os

def check_cpu(command): #defining a function
    print(os.system(command))

def check_date(command):
    print(os.system(command))

def uptime(command):
    print(os.system(command))

def hostname(command):
    print(os.system(command))



check_cpu("df -h") #calling a function
check_date("date")
uptime("uptime")
hostname("hostname")