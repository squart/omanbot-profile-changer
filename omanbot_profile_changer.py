#!/usr/bin/python
#  -*- coding: utf-8 -*-
#  Nimbuzz: yuyb0y@nimbuzz.com
#  coded by Yuyb0y (yuyb0y@mail.com)
#  OmanBot Profile Changer v1.0
#  www.omanbot.com
#   ____                          ____        _   
#  / __ \                        |  _ \      | |  
# | |  | |_ __ ___   __ _ _ __   | |_) | ___ | |_ 
# | |  | | '_ ` _ \ / _` | '_ \  |  _ < / _ \| __|
# | |__| | | | | | | (_| | | | | | |_) | (_) | |_ 
#  \____/|_| |_| |_|\__,_|_| |_| |____/ \___/ \__|

import xmpp
import random
import time
import threading
import traceback

CONFIG = 'nickname.txt'
fp = file(CONFIG)
exec fp in globals()
fp.close()

User_Nick = unicode(User_NickName, encoding='utf-8')
count = Change_Counter
time_c = Change_Time

resources = ['Nimbuzz_Symbian', 'Nimbuzz_MIDP', 'nimbuzzdesktop', 'Android']

def OmanBot_Profile_Changer(resources, time_c):
	print "[!] connect to Nimbuzz server.."
	cnx = xmpp.Client('nimbuzz.com', debug=False)
	time.sleep(2)
	print "[!] Please wait.."
	cnx.connect( server=('o.nimbuzz.com',5222) )
	time.sleep(2)
	print "[+] Connected."
	Nimbuzz_id = raw_input("Please Enter your Nimbuzz ID: ")
	user = Nimbuzz_id
	if Nimbuzz_id.count("@"):
		print "[-] Please write your Nimbuzz id without (@nimbuzz.com)."
	else:
		time.sleep(2)
		password = raw_input("Please Enter your Nimbuzz Password: ")
		res = random.choice(resources)
		time.sleep(2)
		print "[-] Try to login using (" +res+ ") resources.."
		time.sleep(2)
		print "[-] Try to login using your Nimbuzz ID ("+user+").."
		time.sleep(2)
		if cnx.auth(user, password, "OmanBot"+str( int( time.time() ) ) ):
			status = 'OmanBot Profile Changer coded by yuyb0y'
			pres = xmpp.protocol.Presence(status=status)
			cnx.send(pres)
			print "[+] You are logged in successfully."
			time.sleep(2)
			print "[-] Try to get your NickName from (/omanbot-profile-changer/nickname.txt) file.."
			time.sleep(2)
			if User_Nick == '':
				print "[!] You don't write your NickName in (/omanbot-profile-changer/nickname.txt) file."
				time.sleep(2)
				print "[!] Please Try again."
				time.sleep(2)
			elif len(User_Nick) > 60:
				print "[!] Please You can\'t write NickName > 60 Character."
				time.sleep(2)
				print "[!] Please Try again."
			else:
				time.sleep(2)
				print "[+] Great, I'm ready to work."
				time.sleep(2)
				print "[+] Please wait.."
				User_Nick_len = len(User_Nick)
				nick_name = User_Nick
				nick_le = len(nick_name)
				nick_count = 0
				for num in range(count):
					for p in nick_name:
						nick_count += 1
						try:
							v = nick_name[0:nick_count]
							pres = xmpp.protocol.Presence(status=v)
							cnx.send(pres)
							print "[+] NickName changed."
							time.sleep(time_c)
							if not nick_count == nick_le:
								pass
							else:
								nick_count = 0
						except:
							print "[!] There is a problem to change NickName."
							time.sleep(2)
							print "[!] Please Try again."
							exit()
							#print "letter: "+nick_name[0:nick_count]
				else:
					print "[+] Finish."
					print "[+] NickName has been changed "+str(count)+" times."
		else:
			print "[!] Incorrect Username OR Password."
			time.sleep(2)
			print "[!] Please Try again."

while True:
	OmanBot_Profile_Changer(resources, time_c)