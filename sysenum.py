import paramiko

#target_system = "localhost"
#user = "root"
#password = "toor"

commands = [ "uname -a" , "id", "df -h" ]

client = paramiko.SSHClient()

remoteServerDetails = open("remoteservers.csv","r")
for i in remoteServerDetails.readlines():
    
    line=i.strip()
    ls=line.split(",")
  
    print("Target System: ", "%s"%ls[0] )
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("%s"%ls[0], port="%s"%ls[1], username="%s"%ls[2], password="%s"%ls[3])

#      print("[!} Cannot connect to SSH Server: " %ls[0])
    
    for command in commands:
        print("-"*30, command, "-"*30)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
             print (err)
       
print("="*100)



#print("Target System: ", target_system )
#for command in commands:
#    print("-"*20, command, "-"*20)
#    stdin, stdout, stderr = client.exec_command(command)
#    print(stdout.read().decode())
#    err = stderr.read().decode()

