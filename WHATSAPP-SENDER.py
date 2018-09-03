#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ______        ___   _    _  _____ ____    _    ____  ____  
  / __ \ \      / / | | |  / \|_   _/ ___|  / \  |  _ \|  _ \ 
 / / _` \ \ /\ / /| |_| | / _ \ | | \___ \ / _ \ | |_) | |_) |
| | (_| |\ V  V / |  _  |/ ___ \| |  ___) / ___ \|  __/|  __/ 
 \ \__,_| \_/\_/  |_| |_/_/   \_\_| |____/_/   \_\_|   |_|    
  \____/                                                      
\n[$] BUGS WHATSAPP MESSAGES SENDER.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL SCRIPT -- ) #

print bugs
driver = webdriver.Chrome('')
driver.get('https://web.whatsapp.com/')
start = raw_input('\n[X] PRESS ENTER TO START AFTER SKIPPING [QR] CODE.')
time.sleep(1)
print ''
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
nums_list = str(raw_input('[X] ENTER YOUR NUMBERS LIST WITHOUT [+] && WITH COUNTRY CODE X> '))
nums_file = open(nums_list,'r')
file = open(str(raw_input('[X] ENTER YOUR MESSAGE FILE X> ')),'r')
message = file.read()
message_type = raw_input('[X] IS YOUR MESSAGE ARABIC ? [Y/N] X> ')
print ''
if message_type == 'y' or 'Y':
	message = message.encode('utf-8')
	message = message.decode('unicode-escape')
elif message_type == 'n' or 'N':
	pass
else:
	print '[X] THE SCRITP STOPPED PLEASE ENTER A VALID CHOICE.'
	time.sleep(100000)
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
sent = 0
for num in nums_file:
	sent+=1
	num = num.strip()
	url = 'https://web.whatsapp.com/send?phone='+num
	driver.get(url)
	if int(sent) == 1:
		pass
	else:
		alert = driver.switch_to_alert()
		alert.accept()
	time.sleep(10)
	text = driver.find_element_by_class_name('_2bXVy')
	text.send_keys(message)
	send = driver.find_element_by_class_name('_2lkdt')
	send.click()
	print '[X] THE MESSAGE NUMBER HAS BEEN SENT TO [ '+num+' ].'
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
# //THE SCRIPT WORKS FINE WITH [ENGLISH MESSAGES].
# //IF YOU NEED ITO SEND A MESSAGE WITH ARABIC .. PLEASE CONVERT IT TO UNICODE HOW ?
# //LIKE THIS = \u0625\u0633\u0643\u0631\u0628\u062a \u0625\u0631\u0633\u0627\u0644 \u0631\u0633\u0627\u0626\u0644 \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u0648\u0627\u062a\u0633\u0627\u0628 \u0627\u0644\u062a\u0644\u0642\u0627\u0626\u064a
# //THE SCRIPT PROGRAMMED WITH SELENIUM->[WEBDRIVER].
# //THE SCRIPT CAN SEND EACH MESSAGE IN RANGE 13SECONDS.
# //BEFORE STARTING THE SCRIPT GIVE YOU AND INPUT TO ASK YOU IF YOUR MESSAGE WITH ARABIC OR NOT.
# //YOU HAVE TO MAKE THE QR CODE FROM YOUR MOBILE TO START WORKING.
# //PLEASE CHECK ALL YOUR PHONE NUMBERS VALIDATION .. BECAUSE IF ONE OF IT WAS9 ERROR OR DON'T WORKING .. THE SCRIPT WILL BE STOPPED AND VIEWED AN ERROR FOR YOU.
# //PLEASE RUN THE SCRIPT ON A VPS [RDP] BECAUSE IT SLEEPS JUST 10S TO START THE SENDING MESSAGES .. IF YOUR INTERNET IS SLOW PLEASE ADD MORE SECONDS ON THE SLEEP IN LINE [60].
# //DON'T FORGET TO CHANGE YOUR SELENIUM DIR IN [driver] VARIABLE.
# //IF YOU WANT TO SEE MY SCRIPTS [ VISIT MY ACC ON GITHUB [@SIRBUGS] ].
# //PROGRAMMED WITH [ S I R . B U G S ].
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
