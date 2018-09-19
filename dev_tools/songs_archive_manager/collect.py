import h5py
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from sys import argv

if len(argv) < 3:
	print("python collect.py <path/to/songs/hdf5> <col_file_name>.col [--ignore <lines to be ignored in songs list>]")
	exit()

ignore = ["Spotify", ""]
if len(argv) > 3 and argv[3] == "--ignore"
	for i in range(4, len(argv)):
		ignore.append(argv[i])

counter = 0

songs = {}

ip = ""

lines = open(argv[2], "r").read().split("\n")
idx = 0

options = Options()
options.add_argument("--headless")

while True:
	ip = lines[idx]
	idx += 1
	if ip == "":
		continue
	if ip == "--end":
		break
	if ip[0] == "-" and ip[1] == "-":
		ip = ip[2:]
		print("Genre:", ip)
		songs[ip] = []
		while True:
			if not counter % 30:
				driver = webdriver.Firefox(firefox_options=options)

			song_name = lines[idx]
			idx += 1

			if song_name == "--end":
				break
			if song_name in ignore:
				continue

			print("Song:", song_name)

			song_name = list(song_name)
			for i in range(len(song_name)):
				if song_name[i] == "\t" or song_name[i] == " ":
					song_name[i] = "+"
				elif not song_name[i].isalnum():
					song_name[i] = ""
			song_name = "".join(song_name)

			driver.get("http://youtube.com/results?search_query=" + song_name)
			WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "title-wrapper")))
			src = driver.page_source
			link = "https://youtube.com/" + re.findall(r"watch.v=[\w]+", src)[0]
			songs[ip].append([song_name, link])

			print("Link:", link)

			counter += 1
			if not counter % 30:
				driver.close()

lines.close()

with h5py.File(argv[1], "w") as file:
	file.create_dataset("songs", data=songs)