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

echo -n "# Remove old kernels "
dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r | cut -f1,2 -d"-"` | grep -e [0-9] | xargs sudo apt-get --dry-run remove
dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r | cut -f1,2 -d"-"` | grep -e [0-9] | xargs sudo apt-get -y remove

echo -n "# Update script completed "
