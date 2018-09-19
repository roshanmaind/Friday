import sys
from os import system

if sys.platform == "linux":
	print('''
Found linux OS. Assuming a Debian based distro...

You may be prompted to enter sudo (root user) password
This setup will install on your machine the following softwares and packages:-
1. OpenGL
2. python3-pip
3. watson developer cloud
4. cython
5. kivy
6. h5py
7. python-twitter

The softwares or packages that already exist will be skipped.

Do you wish to continue? (Y/N):''', end=" ")
	choice = input()
	if choice.upper() != "Y":
		exit()
	print("\nInitiating OpenGL installation...")
	system("sudo apt-get install mesa-utils freeglut3 freeglut3-dev")

	print("\nInitiating python3-pip installation...")
	system("sudo apt install python3-pip")

	print("\nInstalling required python3 modules...")
	system("pip3 install -r requirements.txt")

	print("Modules installation finished.")



else:
	print('''
We are sorry. Friday does not support any other OS than a Debian based Linux distro as of now.
Support for other operating systems will soon be available! Stay tuned.
You may check the github repository of Friday on github.com/roshanmaind/Friday and raise
an issue requesting other OS support if there is no existing similar issue on the repository.

Thank you!''')
