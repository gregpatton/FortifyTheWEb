# Fortify The Web framework
#
# ______         _   _  __    _______ _       __          __  _     
#|  ____|       | | (_)/ _|  |__   __| |      \ \        / / | |    
#| |__ ___  _ __| |_ _| |_ _   _| |  | |__   __\ \  /\  / /__| |__  
#|  __/ _ \| '__| __| |  _| | | | |  | '_ \ / _ \ \/  \/ / _ \ '_ \ 
#| | | (_) | |  | |_| | | | |_| | |  | | | |  __/\  /\  /  __/ |_) |
#|_|  \___/|_|   \__|_|_|  \__, |_|  |_| |_|\___| \/  \/ \___|_.__/ 
#                           __/ |                                   
#                          |___/       
#
# description:       FortifyTheWeb Framework core
# author:            @semprix, @shipcod3, @httphacker, @napz
# platform:          Python
# version:            0.1

#
# Begin
#

# Required Python libs

import ping, time, sys, urllib2, subprocess, socket

from termcolor import colored, cprint

# Load auxiliary

sys.path.append(r'auxiliary')
from banner import *
from timer import *
from colors import *

# Load modules

sys.path.append(r'modules/recon')
from grabheader import *
from urlcrawler import *

# Check if target is within the argument

if len(sys.argv) <= 2 :
  print
  exitbanner()

else:

# Fortify the Web when ready
    startbanner()


# Run stage 1 banner
    stage1banner()

# Check host if alive

if sys.argv[2] == '80':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        s.connect((sys.argv[1], 80))
        print "[*] Using port 80 on target"
        print "[*] Checking if http port (80) on target is open"
        printout (' >> HTTP port on target is open', GREEN)
        printout (' >> Marking for http testing', GREEN)
        print ""
        grabheader()
        print ""
        urlcrawler()
        printout ('[*] Crawl finishing....', GREEN)
    except socket.error as e:
        printout (' >> Target seems to be down or port has been blocked', RED)
        s.close()


elif sys.argv[2] == '443':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        s.connect((sys.argv[1], 443))
        print "[*] Using port 443 on target"
        print "[*] Checking https port (443) on target is open"
        printout (' >> HTTPS port on target is open', GREEN)
        printout (' >> Marking for https testing', GREEN)
        print ""
        grabheader()
        print ""
        urlcrawler()
        printout ('[*] Crawl finishing....', GREEN)
    except socket.error as e:
        printout (' >> Target seems to be down or port has been blocked', RED)
        s.close()

else:
        printout (' [!] Target does not have default http(s) port', RED)
        time.sleep(3) # Give a little time to sleep


# Load modules for testing

print "[*] Shutting down......"
time.sleep(4)
print 'Scan finished'
timer()