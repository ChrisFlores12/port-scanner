import socket
import sys
import ipaddress
import threading

# global variable

# There are 65535 ports in total, but we will scan only the first 1024 ports (common ports only)
MAX_PORT = 1024
open_ports = []

def worker(target, port):
    # we are going to use this fuinction to only scan one port at a time, and we will use threads to scan multiple ports at the same time
    
    try:
        # create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set the type of scoket we are creating, in this case we are creating a TCP socket

        # set how long the socker will wait for a response before timing out in seconds
        sock.settimeout(5)

        # connect to target ip and port, if the connection is successful
        result = sock.connect_ex((target, port)) # returns 0 if connection is sucessful

        # check if the connection was successful
        if result == 0:
            print(f'Port {port} is open.')
            open_ports.append(port) # add the port to the list of open ports

    except socket.error as e:
        print(f'Error occurred while scanning port {port}: {e}')
    finally:
        sock.close() # close the socket connection

def scan_ports(target):
    # scan the target for open ports
    for port in range(1, MAX_PORT + 1):

        # create a new thread for each port to be scanned
        thread = threading.Thread(target=worker, args=(target, port)) # we are telling it what function to run and what arguments to pass to that function
        thread_list.append(thread) # add the thread to the list of threads
        thread.start() # start the thread

    # wait for all threads to finish
    for thread in thread_list:
        thread.join()

# collect target IP address or hostname from user
if (len(sys.argv) != 2):
    print('Command line argument is missing. Please provide the target IP address or hostname.')
    sys.exit(1)

# save the target IP address or hostname in a variable
target = sys.argv[1] # target ip that will be scanned

# check if the target is a valid ip address or hostname
if ipaddress.ip_address(target):
    print(f'IP address {target} is valid.')
else:
    print(f'IP address {target} is not valid.')

# scan the target for open ports
print('Scanning...')

thread_list = []

scan_ports(target)

# print the list of open ports found
open_ports.sort()  # sort the list of open ports in ascending order
print(f'Open ports found: {open_ports}')