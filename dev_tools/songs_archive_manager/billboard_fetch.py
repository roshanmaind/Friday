from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import re
from sys import argv

if len(argv) < 4:
	print("python billboard_fetch.py <chart name> <sng_file_name>.sng <genre>")
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

print(bcolors.OKGREEN + "[INFO\t]" + bcolors.ENDC + " Loading options for browser...")
options = Options()
options.add_argument("--headless")
print(bcolors.OKGREEN + "[OK\t]" + bcolors.ENDC + " Loaded options for browser.")

print(bcolors.OKGREEN + "[INFO\t]" + bcolors.ENDC + " Loading browser driver...")
driver = webdriver.Firefox(firefox_options=options)
driver.set_page_load_timeout(10)
print(bcolors.OKGREEN + "[OK\t]" + bcolors.ENDC + " Loaded broswer driver.")

print(bcolors.OKGREEN + "[INFO\t]" + bcolors.ENDC + " Loading website {}...".format("https://www.billboard.com/charts/" + argv[1]))
try:
	driver.get("https://www.billboard.com/charts/" + argv[1])
except:
	driver.execute_script("window.stop();")
print(bcolors.OKGREEN + "[OK\t]" + bcolors.ENDC + " Website loaded.")

src = driver.page_source
print(bcolors.OKGREEN + "[OK\t]" + bcolors.ENDC + " Page source code copied.")

print(bcolors.OKGREEN + "[INFO\t]" + bcolors.ENDC + " Closing driver...")
driver.close()
print(bcolors.OKGREEN + "[OK\t]" + bcolors.ENDC + " Driver closed.")

lines = src.split("\n")

sng_text = ["\n"]

sng_text.append("--{}".format(argv[3]))

for i in range(len(lines)):
	if lines[i] == '<div class="chart-list-item__text-wrapper">':
		block = [lines[x] for x in range(i, i + 12)]
		song = " ~ ".join([line for line in block if line[0] != "<" and line[1] != "<"])
		if song[0] == " ":
			song = song[1:]
		song = song.replace("&amp;", "&")
		sng_text.append(song)
	elif '<div class="chart-number-one__title">' in lines[i]:
		song = lines[i][37:len(lines[i]) - 6] + " ~ "
		j = i + 1
		while any([x == "<" for x in lines[j][:2]]):
			j += 1
		song += lines[j]
		if song[0] == " ":
			song = song[1:]
		song = song.replace("&amp;", "&")
		sng_text.append(song)

sng_text.append("--end")

with open(argv[2], "a+") as sng:
	sng.write("\n".join(sng_text))