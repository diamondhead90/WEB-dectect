#!/usr/bin/python
import os,sys
import requests
from Wappalyze import Wappalyzer, WebPage
wappalyzer = Wappalyzer.latest()
import texttable
clear = lambda : os.system('tput reset')
clear()
#Define Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Print Welcome
print bcolors.BOLD + """
\ \      / / \  |  _ \  / ___| / ___|  / \  | \ | |
 \ \ /\ / / _ \ | | | | \___ \| |     / _ \ |  \| |
  \ V  V / ___ \| |_| |  ___) | |___ / ___ \| |\  |
   \_/\_/_/   \_\____/  |____/ \____/_/   \_\_| \_|                                                                   
\n""" + bcolors.ENDC
#Define check link web site
def check_element(link):
	try:
		webpage = WebPage.new_from_url(link)
		result = wappalyzer.analyze(webpage)
		if len(list(result)) == 0:
			print bcolors.BOLD + link + bcolors.ENDC + ': ' +  bcolors.FAIL + 'Cant find technology in site' + bcolors.ENDC
		else:
			element = list(result)
			print bcolors.BOLD + link + bcolors.ENDC + ': ' + bcolors.FAIL + ', '.join(element) + bcolors.ENDC
	except requests.exceptions.ConnectionError:
		print bcolors.BOLD + link + bcolors.ENDC + ': ' + bcolors.FAIL + 'Site cant access' + bcolors.ENDC
	except Exception, e:
		print bcolors.BOLD + link + bcolors.ENDC + ':' + bcolors.FAIL +  'Time out' + bcolors.ENDC

def check_file(link_file):
	with open(link_file,'r') as file:
		for lines in file.read().split():
			try:
				if 'http' in lines:
					print lines
				elif ':443' in lines:
					link ='https://' + lines
					check_element(link)
				else:
					link ='http://' + lines
					check_element(link)
			except requests.exceptions.ConnectionError:
				print bcolors.BOLD + link + bcolors.ENDC + ': ' + bcolors.FAIL + 'Site cant access' + bcolors.ENDC
			except Exception, e:
				print bcolors.BOLD + link + bcolors.ENDC + ':' + bcolors.FAIL +  'Time out' + bcolors.ENDC
#Define import link
def main():
	print "1: " + bcolors.OKGREEN + "Scan with website" + bcolors.ENDC
	print "2: " + bcolors.OKGREEN + "Set with file:" + bcolors.ENDC
	user_choice = raw_input('Select an Option:')
	if user_choice=='1':
		website = raw_input('Insert website need scan: ')
		if 'http' not in website:
			print bcolors.FAIL + "[!] " + bcolors.ENDC + 'Link website wrong'
			sys.exit()
		else:
			check_element(website)
	elif user_choice=='2':
		file = raw_input('Insert file have link need scan: ')
		if os.path.isfile(file):
			check_file(file)
		else:
			print bcolors.FAIL + "[!] " + bcolors.ENDC + 'File not exits'
	                sys.exit()
if __name__ == '__main__':
	try:
        	main()
    	except KeyboardInterrupt:
        	print '\n Exit check techonology in web'
        sys.exit()
