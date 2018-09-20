import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from sys import argv

if len(argv) < 3:
	print("python collect.py <path/to/songs/database>.hdf5 <col_file_name>.col")
	exit()

ignore = [""]

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
		if ip == "--ignore":
			idx += 1
			while lines[idx] != "--end":
				ip = lines[idx]
				ignore.append(ip)
				idx += 1
			print("Ignoring the following:-")
			print(ignore)

			idx += 1
			continue

		ip = ip[2:]
		print("Genre:", ip)
		songs[ip] = []
		while True:
			if not counter % 30:
				driver = webdriver.Firefox(firefox_options=options)
			if lines[idx].isdigit():
				idx += 1
				continue
			song_name = lines[idx]
			
			if song_name == "--end":
				break
			if song_name in ignore:
				idx += 1
				continue

			actual_song_name = lines[idx+1] + " ~ " + lines[idx + 2]
			print("Song:", actual_song_name)

			idx += 3

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
			link = "http://www.youtube.com/" + re.findall(r"watch.v=[\w|-]+", src)[0]
			songs[ip].append([actual_song_name.encode("utf8"), link.encode("utf8")])

			print("Link:", link)

			counter += 1
			if not counter % 30:
				driver.close()

print(songs)

with open(argv[1], "wb") as file:
	pickle.dump(songs, file)
