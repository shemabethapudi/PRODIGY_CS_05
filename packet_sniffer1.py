from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src} -> Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        if Raw in packet:
            print(f"Payload: {packet[Raw].load}\n")
        else:
            print("No Payload\n")

print("Starting packet capture... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=False)
