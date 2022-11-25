from socket import *
import sys
import time

# Getting input from user
host = input("Enter a remote host to scan: ")
hostIP = gethostbyname(host)
print ("Please wait, scanning remote host", hostIP)

# Obtaining time since epoch
startTime = time.time()

try:
    for port in range(1, 5000):
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        if s.connect_ex((hostIP, port)) == 0:
            print("Port " + str(port) + " is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved")
    sys.exit()
except socket.error:
    print("\nServer not responding")
    sys.exit()

# Printing time required for process to complete
print('Scanning Completed in ' + time.time() - startTime + " seconds")