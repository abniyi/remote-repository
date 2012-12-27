#pingip check the status of an ip or range of ips using ICMP protocol
#This script make use of operating system ping command
#it also uses os.popen() function to open a pipe to or from command. 
import os
import time
import sys
from netaddr import IPNetwork
from threading import Thread
import optparse
import Queue
import subprocess
"""
    This script report on the status of an ip address or range of ip addresses
    return active, if the ip address is up and running and inactive otherwise
    For a single ip address, just write python PingIPs.py 192.168.1.1 and for range of
    address use the CIDR notation for example python PingIPs.py 192.168.3.56/27
 
    This script calculates the range of IPs available for this IP and 
    subnet mask, network base address and broadcast address using netaddr by
    David P.D Moss. 
    Note: Thread has been used to speed up the process but the result doesn't return sequentially
"""
def validateIP(newIp):
    validateIP = IPNetwork(newIp)
    status = False
    if validateIP:
       print "====== Validation Result ========"
       print "Ip Address: %s" % str(validateIP.ip)
       print "Network Address: %s" % str(validateIP.network)
       print "Broadcast: %s" % str(validateIP.broadcast)
       print "Netmask: %s" % str(validateIP.netmask)
       print "Size: %s" % str(validateIP.size)
       print "================================"
       status = True
       return status

    else :
       print "Error: Invalid Address Given!"
       return status

queue = Queue.Queue()
class pingips(Thread):
  
  newIp = None
  status = False
  parameter = ("Active", "Inactive", "No response")
  newline = ""
  returnCodeTotal=None
  def __init__(self, queue):
     Thread.__init__(self) # thread has been used to speed up the process
     self.queue = queue
  def run(self):
      while True:
        newIP = self.queue.get() # grap the next ip on the queue
        cmd = "ping -c 1 " + newIP
        process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        process.wait()
        returnCodeTotal = process.returncode
        if returnCodeTotal == 0:
	  print "IP: processed by %s [%s => %s]" % (self.getName(),newIP, self.parameter[0])
        elif returnCodeTotal == 1:
          print "IP: processed by %s [%s => %s]" % (self.getName(), newIP, self.parameter[1])
        else:
          print "IP: processed by %s [%s => %s]" % (self.getName(), newIP, self.parameter[2])
       
        #signals to queue job is done
        self.queue.task_done() 


  
def main():
    """ Runs program and handles command line options"""
    optOutput = optparse.OptionParser(description = ' check if an IP or range of IP address(es) are active or inactive',
					    prog='PingIPs',
					    version = 'PingIps 3.0',
					    usage =' example:python PingIPs.py  192.168.3.1 or 192.168.3.0/24')
    options, args = optOutput.parse_args()
    if len(args) == 1:
        newIP = sys.argv[1]
	try:
	  check = validateIP(newIP)
	  ip_list = list(IPNetwork(newIP))
	except Exception, err:
	   print "Error, Invalid Ip Address"
           sys.exit()
     	if check:
          for i in range(10):
            t = pingips(queue)
            t.setDaemon(True)
            t.start()
      	  for ip in ip_list:
            queue.put(str(ip))
          
	  queue.join()
    else:
	optOutput.print_help()
	

if __name__=='__main__':
   main()


   
