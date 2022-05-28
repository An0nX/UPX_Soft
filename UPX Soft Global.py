import glob
import os
from os import walk
from time import sleep
import ctypes
from win32api import GetLogicalDriveStrings
from colorama import Fore
from config import *

ctypes.windll.kernel32.SetConsoleTitleW('UPX Soft by httpshotmaker')

def clean():
	os.system('cls' if os.name == 'nt' else 'clear')

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
		ctypes.windll.kernel32.SetConsoleTitleW('UPX Soft by httpshotmaker')
		root = "".join(root)
		targetPattern = rf"{root}\*.exe"
		soft = glob.glob(targetPattern)
		if soft == list():
			continue
		if f'{os.getenv("SystemDrive")}' in root:
			continue
		i += 1
		ctypes.windll.kernel32.SetConsoleTitleW(f'Folders found: {i}')
		for j in soft:
			clean()
			banner()
			print(Fore.GREEN + '')
			ctypes.windll.kernel32.SetConsoleTitleW(f'Working with {j}')
			os.system(f'upx --best "{j}"')
		clean()
		banner()
