#!/bin/bash

# Add repositories
add-apt-repository -y universe
add-apt-repository -y multiverse

# Update package lists
apt-get update

# Install common bug bounty tools
apt-get install -y dirb gobuster sublist3r wpscan sqlmap ffuf nikto nmap jq

echo "Common bug bounty tools installed."
