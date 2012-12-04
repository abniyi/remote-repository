#pingip check the status of an ip or range of ips using ICMP protocol
#This script make use of operating system ping command
#it also uses os.popen() function to open a pipe to or from command. 
import os
import time
import sys
from netaddr import *
from threading import Thread
import optparse


def validateIP(newIp):
    validateIP = IPNetwork(newIp)
    if validateIP:
       status = True
       print "====== Validation Result ========"
       print "Ip Address: %s" % str(validateIP.ip)
       print "Network Address: %s" % str(validateIP.network)
       print "Broadcast: %s" % str(validateIP.broadcast)
       print "Netmask: %s" % str(validateIP.netmask)
       print "Size: %s" % str(validateIP.size)
       print "================================"
       return True

    else :
       print "Error: Invalid Address Given!"
       return False
class pingips(Thread):
  """
    This script report on the status of an ip address or range of ip addresses
    return active, if the ip address is up and running and inactive otherwise
    For a single ip address, just write python PingIPs.py 192.168.1.1 and for range of
    address use the CIDR notation for example python PingIPs.py 192.168.3.56/27
 
    This script calculates the range of IPs available for this IP and 
    subnet mask, network base address and broadcast address using google netaddr by
    David P.D Moss. 
    Note: Thread has been used to speed up the process but the result doesn't return sequentially
  """
  newIp = None
  status = False
  parameter = ("Active", "Inactive", "No response")
  newline = ""
  def __init__(self, ip):
     Thread.__init__(self) # thread has been used to speed up the process
     self.newIp=ip
    
  def run(self):
      cmd = "ping -c 2 " + self.newIp
      outp = os.popen(cmd, "r")
      for line in outp.readlines():
	self.newline+=line
      if "ttl" in self.newline:
	print "IP: %s => %s" % (self.newIp, self.parameter[0])
      elif "Unreachable" in self.newline:
        print "IP: %s => %s" % (self.newIp, self.parameter[1])
      else:
        print "IP: %s => %s" % (self.newIp, self.parameter[2])
 


  
def main():
    """ Runs program and handles command line options"""
    optOutput = optparse.OptionParser(description = ' check if an IP or range of IP address(es) are actives in inactives',
					    prog='PingIPs',
					    version = 'PingIps 3.0',
					    usage =' example: %prog [192.168.3.1 or 192.168.3.0/24]')
    options, args = optOutput.parse_args()
    if len(args) == 1:
        newIP = sys.argv[1]
	check = validateIP(newIP)
	ip_list = list(IPNetwork(newIP))
     	if check:
      	  for ip in ip_list:
	    ip = str(ip)
	    ipPingResult = pingips(ip)
            ipPingResult.start()
    else:
	p.print_help()
	

if __name__=='__main__':
   main()


   

