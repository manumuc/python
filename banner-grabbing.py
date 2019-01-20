Usage of script: python <script_name.py> 

#!/usr/bin/python  
# Figure 1 shows how to run this script.  
# Before running the script make sure you put your ip address in the script.  
# You need some basic python skills to work with this script. Everything is self explanatory. 
#https://www.unixmen.com/a-simple-banner-grabbing-script-in-python-to-network-admins/ 

import socket   
import sys   
import os   

#grab the banner   

def grab_banner(ip_address,port):   
      try:   
           s=socket.socket()   
           s.connect((ip_address,port))   
           banner = s.recv(1024)   
           print ip_address + ':' + banner   
      except:   
           return   

def checkVulns(banner):   
      if len(sys.argv) >=2:   
           filename = sys.argv[1]   
           for line in filename.readlines():   
                line = line.strip('\n')   
                if banner in line:   
                     print "%s is vulnerable" %banner   
                else:   
                     print "%s is not vulnerable"   
 
def main():   
      portList = [21,22,25,80,110]   
      for x in range(0,255):   
           for port in portList:   
                ip_address = '192.168.0.' + str(x)   
                grab_banner(ip_address,port)   
if __name__ == '__main__':   
      main()   
