#!/bin/bash

# Add repositories
add-apt-repository -y universe
add-apt-repository -y multiverse

# Update package lists
apt-get update

# Install common penetration testing tools
apt-get install -y nmap wireshark netcat nikto hydra john metasploit-framework aircrack-ng sqlmap
# You can add more tools based on your requirements

echo "Common penetration testing tools installed."
