#lets print cpu disk load using python libraries(os library): to print system level commands

import os #importing a new library into your code
print(os.system('df -h | grep tmpfs'))
print(os.system('uname -a'))
print(os.system('hostnamectl '))
print(os.system('uptime'))
print(os.system('free -h'))