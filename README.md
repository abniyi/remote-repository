Notice:
--------------------------------------------------------------------------
This simple script report on the status of an IP address or range of IP Addresses.
It return active, if the ping is successful and the IP is up and running and inactive otherwise.
It also validate the IP or IP range by printing the IP address, Network Address, Broadcast Address
   Netmask, Size
Usage:
------------------------------------------------------------------------
$python PingIPs.py 192.168.1.1 # test for single IP address

or

$python PingIPs.py 192.168.3.56/27 # test for range of IP address
Requirement:
----------------------------------------------------------------------
This script require the use of netaddr written by David P.D Moss module to be installed
Output:
----------------------------------------------------------------------------
Each Ip is running in parallel using a thread for optimisation purpose, however the result doesn't return sequentially

$python PingIPs.py 192.168.3.0/30

-------Validation Result------

IP Address: 192.168.3.0

Network Address: 192.168.3.0

Broadcast: 192.168.3.3

Netmask: 255.255.255.255

size: 4

--------------------------------
IP: 192.168.3.0 => No response

IP: 192.168.3.1 => Active

IP: 192.168.3.2 => Inactive

IP: 192.168.3.3 => Inactive
