#!/bin/bash

# Add repositories
#add-apt-repository -y ppa:example/ppa  # Replace with the actual repository
#add-apt-repository -y "deb http://repo.example.com/ubuntu focal main"  # Replace with the repository URL

# Update package lists after adding repositories
apt-get update -y

# Upgrade
apt-upgrade -y

# Install packages from the added repositories
apt-get install -y nmap httpx  # Replace with the actual package names

echo "APT packages installed"

