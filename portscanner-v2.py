from socket import *
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="Simple port scanner")

# Obtain the host
parser.add_argument("host", help="Host to scan.")

# Obtain the port range
# If no arguments are parsed, the default port range (1-65535) is selected
parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan. Default is 1-65535 (all ports)")

args = parser.parse_args()
host, port_range = args.host, args.port_range

print("Please wait, scanning remote host", host)

# Obtain starting port and ending port from range
start_port, end_port = port_range.split("-")
start_port, end_port = int(start_port), int(end_port)

# Obtain time since epoch
startTime = time.time()

# Find the services
def printServiceOnPort():
    try:
        # Work through the port range
        for port in range(start_port, end_port):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)
            # Check if port is open
            # s.connect_ex() returns an error instead of raising exception
            if s.connect_ex((host, port)) == 0:
                print("PORT\r\r\t\t\t\tSERVICE")
                match port:
                    case 7:
                        print(str(port) + "\r\r\t\t\techo")
                    case 20:
                        print(str(port) + "\r\r\t\t\tftp")
                    case 21:
                        print(str(port) + "\r\t\t\t\tftp")
                    case 22:
                        print(str(port) + "\r\t\t\t\tssh")
                    case 23:
                        print(str(port) + "\r\t\t\t\ttelnet")
                    case 25:
                        print(str(port) + "\r\t\t\t\tsmtp")
                    case 26:
                        print(str(port) + "\r\t\t\t\trsftp")
                    case 53:
                        print(str(port) + "\r\t\t\t\tdns")
                    case 67:
                        print(str(port) + "\r\t\t\t\tdhcp")
                    case 68:
                        print(str(port) + "\r\t\t\t\tdhcp")
                    case 69:
                        print(str(port) + "\r\t\t\t\ttftp")
                    case 80:
                        print(str(port) + "\r\t\t\t\thttp")
                    case 88:
                        print(str(port) + "\r\r\t\t\tkerberos")
                    case 102:
                        print(str(port) + "\r\r\t\t\tiso-tsap")
                    case 110:
                        print(str(port) + "\r\t\t\t\tpop3")
                    case 111:
                        print(str(port) + "\r\t\t\t\trpc")
                    case 119:
                        print(str(port) + "\r\t\t\t\tnntp")
                    case 123:
                        print(str(port) + "\r\t\t\t\tntp")
                    case 135:
                        print(str(port) + "\r\t\t\t\tmicrosoft epmap")
                    case 137:
                        print(str(port) + "\r\t\t\t\tnetbios-ns")
                    case 139:
                        print(str(port) + "\r\t\t\t\tsmb/samba or netbios-ssn")
                    case 143:
                        print(str(port) + "\r\t\t\t\timap4")
                    case 161:
                        print(str(port) + "\r\t\t\t\tsnmp")
                    case 194:
                        print(str(port) + "\r\t\t\t\tirc")
                    case 381:
                        print(str(port) + "\r\t\t\t\thp openview")
                    case 383:
                        print(str(port) + "\r\t\t\t\thp openview")
                    case 389:
                        print(str(port) + "\r\t\t\t\tldap")
                    case 443:
                        print(str(port) + "\r\t\t\t\thttps")
                    case 445:
                        print(str(port) + "\r\t\t\t\tsmb/samba or microsoft-ds")
                    case 464:
                        print(str(port) + "\r\t\t\t\tkerberos")
                    case 512:
                        print(str(port) + "\r\t\t\t\texec")
                    case 513:
                        print(str(port) + "\r\t\t\t\tlogin")
                    case 514:
                        print(str(port) + "\r\t\t\t\tshell")
                    case 587:
                        print(str(port) + "\r\t\t\t\tsmtp")
                    case 593:
                        print(str(port) + "\r\t\t\t\tmicrosoft dcom")
                    case 691:
                        print(str(port) + "\r\t\t\t\tms exchange")
                    case 993:
                        print(str(port) + "\r\t\t\t\timaps")
                    case 1025:
                        print(str(port) + "\r\t\t\t\tmicrosoft rpc")
                    case 1099:
                        print(str(port) + "\r\t\t\t\trmiregistry")
                    case 1194:
                        print(str(port) + "\r\t\t\t\topenvpn")
                    case 1524:
                        print(str(port) + "\r\t\t\t\tingreslock")
                    case 1589:
                        print(str(port) + "\r\t\t\t\tcisco vqp")
                    case 1725:
                        print(str(port) + "\r\t\t\t\tsteam")
                    case 1812:
                        print(str(port) + "\r\t\t\t\tradius")
                    case 2082:
                        print(str(port) + "\r\t\t\t\tcpanel")
                    case 2083:
                        print(str(port) + "\r\t\t\t\tradsec, cpanel")
                    case 2049:
                        print(str(port) + "\r\t\t\t\tnfs")
                    case 2121:
                        print(str(port) + "\r\t\t\t\tccproxy-ftp")
                    case 2483:
                        print(str(port) + "\r\t\t\t\toracle db")
                    case 2484:
                        print(str(port) + "\r\t\t\t\toracle db")
                    case 2967:
                        print(str(port) + "\r\t\t\t\tsymantec av")
                    case 3074:
                        print(str(port) + "\r\t\t\t\txbox live")
                    case 3306:
                        print(str(port) + "\r\t\t\t\tmysql")
                    case 3632:
                        print(str(port) + "\r\t\t\t\tdistccd")
                    case 5432:
                        print(str(port) + "\r\t\t\t\tpostgresql")
                    case 5900:
                        print(str(port) + "\r\t\t\t\trfb/vnc server")
                    case 6000:
                        print(str(port) + "\r\t\t\t\tx11")
                    case 6665:
                        print(str(port) + "\r\t\t\t\tirc")
                    case 6667:
                        print(str(port) + "\r\t\t\t\tirc")
                    case 6669:
                        print(str(port) + "\r\t\t\t\tirc")
                    case 6697:
                        print(str(port) + "\r\t\t\t\tircu-s")
                    case 7547:
                        print(str(port) + "\r\t\t\t\tcwmp")
                    case 7547:
                        print(str(port) + "\r\t\t\t\tcwmp")
                    case 8009:
                        print(str(port) + "\r\t\t\t\tajp13")
                    case 8080:
                        print(str(port) + "\r\t\t\t\thttp")
                    case 8086:
                        print(str(port) + "\r\t\t\t\tkaspersky av")
                    case 8087:
                        print(str(port) + "\r\t\t\t\tkaspersky av")
                    case 8222:
                        print(str(port) + "\r\t\t\t\tvmware server")
                    case 8787:
                        print(str(port) + "\r\t\t\t\tmsgsrvr")
                    case 9100:
                        print(str(port) + "\r\t\t\t\tpdl")
                    case 18182:
                        print(str(port) + "\r\t\t\t\topsec-ufp")
                    case _:
                        print(str(port) + "\r\t\t\t\tunassigned")

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    except gaierror:
        print("\nHostname Could Not Be Resolved")
        sys.exit()
    except error:
        print("\nServer not responding")
        sys.exit()

if __name__ == '__main__':
    printServiceOnPort()

# Print time required for process to complete
print('Scanning Completed in ' + str(time.time() - startTime) + " seconds")