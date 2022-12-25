from socket import *
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="Simple port scanner")

# Obtain the host
parser.add_argument("host", help="Host to scan")

# Obtain the port range
# If no arguments are parsed, the default port range (1-65535) is selected
parser.add_argument("-p,", "--ports", default="1-65535", help="Port range to scan. Default is 1-65535 (all ports)")

args = parser.parse_args()
host, port_range = args.host, args.ports

print("Please wait, scanning ", host)

# Obtain starting port and ending port from range
start_port, end_port = port_range.split("-")
start_port, end_port = int(start_port), int(end_port)

# Obtain time since epoch
startTime = time.time()

# Scan ports
def portscan():
    try:
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        # Work through the port range
        for port in range(start_port, end_port):
            # Check if port is open
            # s.connect_ex() returns an error instead of raising exception
            if s.connect_ex((host, port)) == 0:
                print("Port " + str(port) + " is open")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    except gaierror:
        print("\nHostname Could Not Be Resolved")
        sys.exit()
    except error:
        print("\nServer not responding")
        sys.exit()

portscan()

# Print time required for process to complete
print('Scanning Completed in ' + str(time.time() - startTime) + ' seconds')