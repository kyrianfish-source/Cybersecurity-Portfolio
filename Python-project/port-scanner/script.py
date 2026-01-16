# Simple Port Scanner
# This script checks if common ports are open on a target system.

import socket

target = "127.0.0.1"
ports = [22, 80, 443, 3306]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    sock.close()
