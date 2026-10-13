# Python TCP Port Scanner

## Overview

This project is a simple TCP port scanner written in Python. It scans the first 1,024 TCP ports on a specified IP address to identify which ports are open.

The script uses Python's `socket` library to test TCP connections and `threading` to scan multiple ports concurrently. It also uses `sys` to accept command-line arguments and `ipaddress` for IP address validation.

This project demonstrates fundamental networking and cybersecurity concepts, including TCP connections, open ports, socket programming, and multithreading.

## Features

- **TCP port scanning:** Checks ports 1–1024, including many commonly used service ports.
- **Multithreading:** Scans multiple ports concurrently to improve performance.
- **Connection timeouts:** Sets a five-second timeout for connection attempts.
- **Error handling:** Reports socket errors encountered during scanning.
- **Results summary:** Collects open ports and displays them in ascending order.
- **Command-line input:** Allows the user to specify a target IP address.

## Requirements

- Python 3
- A terminal or command-line interface
- Permission to scan the target system

No additional packages are required because the script uses Python's standard library.

## Installation

1. Install Python 3 if it is not already installed.
2. Save the script as `port_scanner.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.

## How to Run

Run the scanner using the following command:

```bash
python3 port_scanner.py 127.0.0.1
```

On Windows, you may use:

```bash
python port_scanner.py 127.0.0.1
```

The address `127.0.0.1` refers to your own computer and is a useful starting point for testing.

To scan another authorised system, replace the IP address with the target address:

```bash
python3 port_scanner.py 192.168.1.10
```

Only scan systems you own or have explicit permission to assess.

## Example Output

The results depend on which services are listening on the target system.

```text
IP address 127.0.0.1 is valid.
Scanning...
Port 22 is open.
Port 80 is open.
Open ports found: [22, 80]
```

An open port means that a TCP connection was successfully established. It does not necessarily mean that the service is vulnerable.

## How It Works

1. **Target input:** Reads the target IP address from a command-line argument.
2. **Socket creation:** Creates a TCP socket using Python's `socket` library.
3. **Connection attempt:** Uses `connect_ex()` to attempt a connection to each port.
4. **Multithreading:** Creates threads to scan multiple ports concurrently.
5. **Result collection:** Adds successfully connected ports to a list.
6. **Output:** Sorts and displays the open ports.

The scanner checks ports 1–1024, which include commonly used ports such as SSH (22), SMTP (25), HTTP (80), and HTTPS (443).

## Why This Is Good Practice in Cybersecurity

### 1. Identifying exposed services

Port scanning helps identify which network services are accessible on a system. This gives administrators a better understanding of their network's attack surface.

### 2. Reducing the attack surface

Unnecessary open ports can expose services to unwanted connections. Identifying them allows administrators to investigate and restrict access where appropriate.

### 3. Supporting vulnerability assessments

Port scanning is often an early step in an authorised security assessment. The results can help determine which services require further investigation.

### 4. Learning networking fundamentals

This project provides practical experience with TCP, sockets, ports, IP addresses, connection timeouts, and concurrent programming.

### 5. Encouraging responsible security practices

Scanning systems with permission helps security professionals identify potential risks while respecting organisational policies and applicable laws.

## Limitations

- Only scans ports 1–1024.
- Checks TCP ports, not UDP ports.
- Does not identify the services or versions running on open ports.
- Cannot determine whether an open service is vulnerable.
- Creating 1,024 threads simultaneously can consume unnecessary system resources.
- IP address validation and shared-result handling need improvement in the current implementation.

## Future Improvements

Possible improvements include:

- Correct IP address validation and hostname support.
- A configurable port range.
- A limit on concurrent threads.
- Improved error handling.
- Service identification for open ports.
- Exporting results to a text or CSV file.
- Thread-safe result collection.

## Disclaimer

This project is intended for educational purposes and authorised security testing only. Scan systems and networks only when you own them or have permission to test them. Unauthorised scanning may violate organisational policies or applicable laws.

## Conclusion

This project demonstrates how Python can be used to build a basic TCP port scanner. It introduces important networking concepts and shows how port scanning can support defensive cybersecurity by identifying exposed services and helping administrators understand their systems' network exposure.