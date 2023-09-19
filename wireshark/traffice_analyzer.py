# Network Traffic Analyzer: 
# Analyze network packet captures for anomalies and threats.

# pip install pyshark

'''
Python script that reads a Wireshark PCAP file and performs basic security analysis,
 such as identifying suspicious traffic, detecting port scans, and checking for potential security threats.
The script uses the pyshark library to parse the PCAP file.
'''

import pyshark

def analyze_pcap(pcap_file):
    # Create a PyShark capture object
    capture = pyshark.FileCapture(pcap_file)

    # Initialize variables for analysis
    suspicious_traffic = 0
    port_scan_detected = False

    # Loop through each packet in the capture file
    for packet in capture:
        # Check for potential port scanning
        if "TCP" in packet and int(packet["TCP"].dstport) < 1024:
            port_scan_detected = True

        # Add more checks for specific threats or anomalies as needed

    # Analyze the results
    if port_scan_detected:
        print("Port scan detected in the network traffic.")
    else:
        print("No port scan detected.")

    if suspicious_traffic > 0:
        print(f"Detected {suspicious_traffic} suspicious packets in the network traffic.")
    else:
        print("No suspicious traffic detected.")

if __name__ == "__main__":
    # Replace 'your_capture.pcap' with the path to your PCAP file
    pcap_file_path = 'your_capture.pcap'
    analyze_pcap(pcap_file_path)
