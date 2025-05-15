import subprocess #run subprocesses through python

def terraform_run(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE) #refer to https://docs.python.org/3/library/subprocess.html
    print(process.stdout.decode())

directory = "/home/protivitiadmin/python/python/pythondevops/terraform"
#command = f"terraform -chdir={directory} init"
#command = f"terraform -chdir={directory} plan"
#command = f"terraform -chdir={directory} apply -auto-approve"
command = f"terraform -chdir={directory} destroy -auto-approve"
print(command)
terraform_run(command)