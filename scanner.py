import socket #for socket library and for open port
import sys #for input a ip or port from user
from datetime import datetime #for calculate running time
import pyfiglet #for clean our terminal screen and also you should install with sudo pip install pyfiglet 
import subprocess #dont forget :)
#clean our screen
subprocess.call('clear',shell=True)

print("-" * 63)
banner=pyfiglet.figlet_format('Port Scanner') #For our banner when start program that beatiful starter this is
print(banner)
print(" " * 42 + 'By Emin Karadeniz')
print("-" * 63)

#Input for ip
target=input('Target server ip address: ')#its gonna take input from us
targetIp=socket.gethostbyname(target)

#Start time calculate as now 
t1 = datetime.now()
minPort=int(input('Minimum Port: ')) #port start minimum value 
maxPort=int(input('Maximum Port: ')) #max value port #should be int dont forget

#Starter message
print("-" * 50)
print("                               ")
print("Ports Scaning.. Target IP: ",targetIp)
print("-" * 50)
try:
    for port in range(minPort,maxPort):   #ourport range every port will check and start again from begi
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #afinet is ipv4 and sockstream is tcp (3 handshake)
        r=s.connect_ex((targetIp,port))  #make connection
        if r == 0:
            print("Port {} open. ".format(port))
        else:
            print("Port {} close.".format(port))
        s.close()

except KeyboardInterrupt:                 #this except and others are error message those are comman
    print('Wrong keyboard input')
    sys.exit()    

except socket.gaierror:
    print('Ip couldnt resolved')
    sys.exit()

except socket.error:
    print('Couldent connect target')
    sys.exit()

t2= datetime.now()   #taking finish time
total = t2- t1       #and calculate how long run this program
print("Total time: ",total) #lets check
