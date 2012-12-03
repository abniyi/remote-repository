#pingip check the status of an ip or range of ips using ICMP protocol
#This script make use of operating system ping command
#it also uses os.popen() function to open a pipe to or from command. 
import os
import time
import sys
#from netaddr import *
class pingips():
  """
    This script report on the status of an ip address or range of ip addresses
    return active, if the ip address is up and running and inactive otherwise
    For a single ip address, just write python PingIPs.py 192.168.1.1 and for range of
    address use the CIDR notation for example python PingIPs.py 192.168.3.56/27
 
    This script calculates the range of IPs available for this IP and 
    subnet mask, network base address and broadcast address
  """
  newIp = None
  rangeCIDR=None
  def __init__(self, ip):
     self.newIp=ip
     self.validateIP()
  # validate that the ip given by convert it to binary
  def validateIP(self):
     pos = self.newIp.find("/")
     octets=None
     if pos != -1:
	octets= self.newIp[:pos]
	self.rangeCIDR=self.newIp[pos:]    
     try:
        self.ip2binary(self.newIp)
     except Exception, err:
        print "Error when converting to binary, ip not in the right format"
     return "Ip is in the right format"
  
  # convert an IP address from its 32 binary digit representation
  def ip2binary(ip):
     binlist=""
     count=0
     try:
        octets = ip.split(".")
        for octet in octets:
           if octet != "":
               binlist+=decimal2binary(int(octet),8)
	       count+=1
               if count == 4:
                  break
            
        while count < 4:
             binlist += "00000000"
	     count +=1
     return binlist

   # convert a decimal number to binary rep
   
  def decimal2binary(num, digits=None):
     



if __name__=='__main__':
   # this only accepts an argument
   try:
     newIP = sys.argv[1]
     newIP = "192.168.1.1/25"
     result = pingips(newIP)
     
   except Exception,err:
     print " read the documentation for help on how to run the script"
     print err
#     sys.exit()


   

