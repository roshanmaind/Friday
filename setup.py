import sys
from os import system
from os import getcwd

if sys.platform == "linux":
	print("Found a Linux Operating System")
	print("This setup script only supports Debian based distros of Linux as of now.")
	print("Enter 'y' to continue if you're using a Debian based distro ('n' to exit): ", end="")
	if input().upper() != "Y":
		exit()

	print('''
You may be prompted to enter sudo (root user) password
This setup will install on your machine the following softwares and packages:-
1. OpenGL
2. python3-pip
3. watson developer cloud
4. cython
5. kivy
6. h5py
7. python-twitter
8. Selenium
9. requests_oauthlib
10. geckodriver

The softwares or packages that already exist will be skipped.

Do you wish to continue? (Y/N):''', end=" ")
	if input().upper() != "Y":
		exit()
	print("\nInitiating OpenGL installation...")
	system("sudo apt-get install mesa-utils freeglut3 freeglut3-dev")

	print("\nInitiating python3-pip installation...")
	system("sudo apt install python3-pip")

	print("\nInstalling required python3 modules...")
	system("pip3 install -r requirements.txt")

	print("Modules installation finished.")

	print("Installing geckodriver")

	system("wget https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-arm7hf.tar.gz")
	system("tar -xvzf geckodriver*")
	system("chmod +x geckodriver")
	system("echo 'export PATH=$PATH:" + getcwd() +"' >> ~/.bashrc")

	print("Installation Complete!")
	print("Run Friday.py to use the app.")



elif sys.platform[:3] == "win":
	print('''
Windows OS detected...

This setup will install on your machine the following modules:-
1. watson developer cloud
2. cython
3. kivy
4. h5py
5. python-twitter
6. Selenium
7. requests_oauthlib

The modules that already exist will be skipped.

Do you wish to continue? (Y/N):''', end=" ")
	choice = input()
	if choice.upper() != "Y":
		exit()

	print("\nInstalling required python3 modules...")
	system("pip3 install -r requirements.txt")

	print("Modules installation finished.")


else:
	print('''
We are sorry. Friday does not support any other OS than a Debian based Linux distro and Windows 
right now. Support for other operating systems will soon be available! Stay tuned.
You may check the github repository of Friday on github.com/roshanmaind/Friday and raise
an issue requesting other OS support if there is no existing similar issue on the repository.

Thank you!''')
