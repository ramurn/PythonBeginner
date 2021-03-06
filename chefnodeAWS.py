#Purpose: Update chef note hosts if your chef hostname & IPs are hosted in AWS and are changing every time, it starts up
#Date: 17-Aug-2018

from os import system

def ipVal(obj):
    while True:
            count = 0
            for i in obj.split("."):
                if not i:
                    i=999
                if (int(i) >= 1 and int(i) <= 255):
                    count += 1
            if ((len(obj.split("."))) == 4 and count == 4):
                return obj
                break
            else:
                obj=input("Incorrect Option. enter Valid IP: ")

mpub=input("Enter ChefMaster Public IP: ")
mpub=ipVal(mpub)
mpvt=input("Enter ChefMaster Pvt IP   : ")
mpvt=ipVal(mpvt)
wpub=input("Enter ChefWS Public IP    : ")
wpub=ipVal(wpub)
wpvt=input("Enter ChefWS Pvt IP       : ")
wpvt=ipVal(wpvt)

def setPubVal (var):
    varval=var+"           ec2-"+str(var.split(".")[0])+"-"+str(var.split(".")[1])+"-"+str(var.split(".")[2])+"-"+str(var.split(".")[3])+".us-east-2.compute.amazonaws.com"
    return varval

def setPvtVal (var):
    varval=var+"           ip-"+str(var.split(".")[0])+"-"+str(var.split(".")[1])+"-"+str(var.split(".")[2])+"-"+str(var.split(".")[3])+".us-east-2.compute.amazonaws.com"
    return varval


mpubVal=setPubVal(mpub)
wpubVal=setPubVal(wpub)
mpvtVal=setPvtVal(mpvt)
wpvtVal=setPvtVal(wpvt)

print ("\nBacking up /etc/hosts file with todays date")
system("cp -p /etc/hosts /etc/hosts.`date +%Y%m%d-%H%M`")

print ("Removing old amazonaws.com entris in /etc/hosts file")
system("sed -i '/amazonaws.com/d' /etc/hosts")

with open ('/etc/hosts','a') as hf:
    hf.write("\n")
    hf.write(mpubVal)
    hf.write("\n")
    hf.write(mpvtVal)
    hf.write("\n")
    hf.write(wpubVal)
    hf.write("\n")
    hf.write(wpvtVal)
    hf.write("\n")

print ("/etc/hosts file is updated with new entries \n")
system("cat /etc/hosts | grep amazonaws.com")
print(" ")
