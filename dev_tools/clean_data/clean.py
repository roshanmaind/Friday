import h5py
from sys import argv

if len(argv) == 1:
	print("python clean.py <full/path/to/users/database>.hdf5")
	exit()

me = ["Roshan", "Maind", "roshanmaind", "123123123", "N"]
me = [s.encode("utf8") for s in me]
users = [me]

with h5py.File(argv[1], "w") as file:
	file.create_dataset("users", data=users)
