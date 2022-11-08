import socket
import subprocess
import sys
import pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#Blank your screen
subprocess.call("clear", shell=True)

#ask for input
remoteServer = input(str("Enter IP Address: "))
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print("_" * 60)
print("Please Wait, Scanning Remote Host"), remoteServerIP
print("_" * 60)

#check the date and time the scan was started
t1 = datetime.now()

#Using the range function specify the ports
#Also we will do error handling

try:

    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:    Open".format(port))
            sock.close()

except KeyboardInterrupt:
    print("You Pressed CTRL+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

#Checking Time Again
t2 = datetime.now()

#Calculate the difference in time to know how long the scan took
total = t2 - t1
#Printing the information on the screen
print("Scanning Complete in: ", total)
