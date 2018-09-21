import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from sys import argv

if len(argv) < 3:
	print("python sam.py <path/to/songs/database>.pkl <sng_file_name>.sng")
	exit()

# fancy log printing stuff
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

with open(argv[2], "r") as sng:
	sng_text = sng.read().split("\n")

GLOBAL = 0
SONGS = 1

songs = {}
options = Options()
options.add_argument("--headless")

scope = GLOBAL
genre = ""
for line in sng_text:
	if line == "--end":
		if scope == GLOBAL:
			exit()
		else:
			scope = GLOBAL
	elif line[:2] == "--":
		scope = SONGS
		genre = line[2:]
		songs[genre] = []
		print("{}[INFO\t]{} Starting genre: {}".format(bcolors.OKGREEN, bcolors.ENDC, genre))
	else:
		if scope == SONGS:
			print("{}[{}\t]{} Song: {}".format(bcolors.OKGREEN, genre, bcolors.ENDC, line))
			query = "".join([character if character.isalnum() or character == " " else "" for character in line]).replace(" ", "+")
			search_page = "https://www.youtube.com/results?search_query=" + query
			print("{}[INFO\t]{} Loading browser driver".format(bcolors.OKGREEN, bcolors.ENDC))
			driver = webdriver.Firefox(firefox_options=options)
			driver.set_page_load_timeout(10)
			print("{}[INFO\t]{} Fetching link from: {}".format(bcolors.OKGREEN, bcolors.ENDC, search_page))
			try:
				driver.get(search_page)
			except:
				driver.execute_script("window.stop();")
			link = "http://www.youtube.com/" + re.findall(r"watch.v=[\w|-]+", driver.page_source)[0]
			driver.close()
			print("{}[INFO\t]{} Link captured: {}".format(bcolors.OKGREEN, bcolors.ENDC, link))
			print()
			songs[genre].append([line, link])

with open(argv[1], "wb") as file:
	pickle.dump(songs, file)
	print("Save successful")