#!/bin/bash

echo -n "# Update package index files "
apt-get update
echo -n "# Install updates "
apt-get dist-upgrade -y
apt-get upgrade -y
apt-get install -f
echo -n "# Remove unused packages "
apt-get autoclean
apt-get autoremove -y
apt-get clean

dpkg --purge `COLUMNS=300 dpkg -l "*" | egrep "^rc" | cut -d" " -f3`

echo -n "# Update script completed "
