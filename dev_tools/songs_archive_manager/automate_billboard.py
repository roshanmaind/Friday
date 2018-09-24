from os import system
from sys import argv

if len(argv) < 2:
	print("python dev_tools/songs_archive_manager/automate_billboard.py <sng_file_name>.sng")

path = argv[0][:len(argv[0]) - 21]

system("rm " + path + argv[1])

system("python " + path + "billboard_fetch.py " + " dance-electronic-songs " + path + argv[1] + " edm")
system("python " + path + "billboard_fetch.py " + " country-songs " + path + argv[1] + " country")
system("python " + path + "billboard_fetch.py " + " pop-songs " + path + argv[1] + " pop")
system("python " + path + "billboard_fetch.py " + " classical-albums " + path + argv[1] + " classical")
system("python " + path + "billboard_fetch.py " + " rock-songs " + path + argv[1] + " rock")
system("python " + path + "billboard_fetch.py " + " jazz-songs " + path + argv[1] + " jazz")
system("python " + path + "billboard_fetch.py " + " greatest-hot-100-singles " + path + argv[1] + " goat")
system("python " + path + "billboard_fetch.py " + " r-b-hip-hop-songs " + path + argv[1] + " hip-hop")