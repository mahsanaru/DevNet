{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\csgray\c0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \CocoaLigature0 import getpass\
import telnetlib\
\
HOST = "192.168.122.71"\
user = input("Enter your telnet username: ")\
user = user.rstrip()\
password = getpass.getpass()\
\
tn = telnetlib.Telnet(HOST)\
\
tn.read_until(b"Username: ")\
tn.write(user.encode('ascii') + b"\\n")\
print(password)\
if password:\
    tn.read_until(b"Password: ")\
    tn.write(password.encode('ascii') + b"\\n")\
\
tn.write(b"enable\\n")\
tn.write(b"cisco\\n")\
tn.write(b"conf t\\n")\
tn.write(b"int loop0\\n")\
tn.write(b"ip address 1.1.1.1 255.255.255.255\\n")\
tn.write(b"int loop1\\n")\
tn.write(b"ip address 2.2.2.2 255.255.255.255\\n")\
tn.write(b"router ospf 1\\n")\
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\\n")\
tn.write(b"end\\n")\
tn.write(b"exit\\n")\
\
print(tn.read_all().decode('ascii'))}