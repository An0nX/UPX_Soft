import glob
import os
from win32api import GetLogicalDriveStrings
from os import walk
from time import sleep
from colorama import init, Fore, Back, Style
from config import *

os.system(f'title UPX Soft by httpshotmaker')

def clean():
	try:
		os.system('clear')
	except:
		os.system('cls')

clean()

def banner():
	print(Fore.RED +
		'  __    __  .______   ___   ___         _______.  ______    _______ .___________.\n',
		'|  |  |  | |   _  \  \  \ /  /        /       | /  __  \  |   ____||           |\n',
		'|  |  |  | |  |_)  |  \  V  /        |   (----`|  |  |  | |  |__   `---|  |----`\n',
		'|  |  |  | |   ___/    >   <          \   \    |  |  |  | |   __|      |  |     \n',
		"|  `--'  | |  |       /  .  \     .----)   |   |  `--'  | |  |         |  |     \n",
		' \______/  | _|      /__/ \__\    |_______/     \______/  |__|         |__|     \n',
		'by httpshotmaker\n\n'
		)
banner()
print(Fore.GREEN + 'Работа программы может занять длительное время, ожидайте')

i = 0
for drive in GetLogicalDriveStrings().split('\000')[:-1]:
	sleep(drv)
	for root, _, _ in walk(drive):
		sleep(fol)
		os.system(f'title UPX Soft by httpshotmaker')
		root = "".join(root)
		targetPattern = rf"{root}\*.exe"
		soft = glob.glob(targetPattern)
		if soft == list():
			continue
		if f'{os.getenv("SystemDrive")}\\Windows' in root or f'{os.getenv("SystemDrive")}\\$Recycle.Bin' in root or f'{os.getenv("SystemDrive")}\\Program Files' in root or f'{os.getenv("SystemDrive")}\\Program Files (x86)' in root or f'{os.getenv("SystemDrive")}\\PerfLogs' in root or f'{os.getenv("SystemDrive")}\\ProgramData' in root or rf'{os.getenv("SystemDrive")}\\Users\*\AppData' in root:
			continue
		i += 1
		os.system(f'title Folders found: {i}')
		for j in soft:
			clean()
			banner()
			print(Fore.GREEN + '')
			os.system(f'title Working with {j}...')
			os.system(f'upx --best "{j}"')
		clean()
		banner()