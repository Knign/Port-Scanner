#!/usr/bin/python3

from socket import *
import sys
import time
startTime = time.time()

host = input("Enter a remote host to scan: ")
hostIP = gethostbyname(host)
print ("Please wait, scanning remote host", hostIP)

try:
    for port in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        if s.connect_ex((hostIP, port)) == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()

except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
    sys.exit()

except socket.error:
    print("\n Server not responding")
    sys.exit()

print('Scanning Completed in ', time.time() - startTime)
