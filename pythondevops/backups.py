#automated backups using python backup --> compress --> copy -->

import shutil
import datetime
import os

def backup_files(source, destination):
    today =datetime.datetime.today()
    backup_file_name=os.path.join(destination,f"backup {today}.tar.gz") #f stands for formatted string
    shutil.make_archive(backup_file_name.replace('tar.gz',''),'gztar',source)

source = "/home/protivitiadmin/python/python/pythondevops"
destination = "/home/protivitiadmin/backups"
backup_files(source,destination)
