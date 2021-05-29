import socket
import termcolor

def scan(targets, ports):
    print('\n' + 'Starting Scan For ' + str(targets))
    for port in range(1,ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print ("[+] port open: " + str(port))
        sock.close()
    except:
        #print ("[-] port closed: " + str(port))
        pass


targets = input("[*] Enter targets to scan (split them with ,): ")
ports = int(input("[*] How many port you want to scan: "))

if "," in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets",'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)

