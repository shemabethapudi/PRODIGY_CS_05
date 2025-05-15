# PRODIGY_CS_05
# Packet Sniffer Tool

## What is this?

This project is a simple packet sniffer written in Python. It captures and analyzes network packets on your machine, displaying useful information such as:

- Source IP address
- Destination IP address
- Protocol number
- Payload data (if available)

**Note:** This tool is meant for educational purposes and should only be used on networks you have permission to monitor.

---

## How to run

1. Make sure you have Python 3 installed on your system.
2. Run the script with administrative privileges (required to capture packets):

```bash
sudo python3 packet_sniffer1.py
Sample output:
Starting packet capture... Press Ctrl+C to stop.
Source IP: 192.168.0.101 -> Destination IP: 104.120.134.78
Protocol: 6
Payload: b'\x17\x03\x03\x00\x13\x1eq\n\xd21\xea}...'

Source IP: 192.168.0.101 -> Destination IP: 74.125.24.188
Protocol: 6
No Payload

