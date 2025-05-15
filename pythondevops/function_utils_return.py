import os
import datetime

def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)


def run_command(command): #defining a function
    return os.system(command)

#run_command("df -h") #calling a function
run_command("date")
run_command("uptime")


