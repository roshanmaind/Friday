This dev tool is used to manage the songs archive.


The main script of this module is the file named "sam.py". The sam.py script takes as input the songs database pickle and a .sng file in the the same directory as the script.
sam.py's job is to read the text file with extension .sng which has names of songs written following a certain rules and sorted by genre, take the names of the songs in the 
.sng file, fetch the YouTube links of the songs and properly create a Python Dictionary with the song names and corresponding YouTube links under the genres as Dictonary keys.
The rules of the sng file are given at the bottom of this README.


Along with the main sam.py script, this tool comes with several other supporting utility scripts which help writing the .sng files following the .sng files' rules. These 
supporting scripts are different for different songs related websites. Currently, the tool comes with one supporting script for billboard.com named "billboard_fetch.py".
This particular script takes as input, 
	1. The billboard chart name of a music genre (for "https://www.billboard.com/charts/jazz-songs", chart name would be "jazz-songs"),
	2. Name of the .sng file (with extension) and,
	3. The name of the genre to be written in the songs database
The script loads the website and fetches the names of the songs in that genre and writes them in the .sng file. The new data is appended to existing contents if any.


Rules of .sng files:-

* A genre of songs should be written only once. If written multiple times, only the last block of the genre will be read.
* Each genre should start with one line reading exactly "--<genre>" where <genre> is the genre of the songs in that block.
* A genre block is ended with a line containing exactly the text "--end".
* Any text outside genre blocks is ignored
* Every song name should be written in exactly one line. The line should contain the name of the song and the artist seperated by " ~ "