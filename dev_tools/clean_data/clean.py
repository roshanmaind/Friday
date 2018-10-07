import h5py
from sys import argv

me = ["Mark", "Blank", "mark", "wasd", "0" * 100, ""]
users = [me]
for i in range(len(users)):
	for j in range(6):
		users[i][j] = users[i][j].encode("utf8")

with h5py.File("data/friday/users.hdf5", "w") as file:
	file.create_dataset("users", data=users)

likes = [[["mark".encode("utf8"), str("0" * 100).encode("utf8"), "".encode("utf8")]]]
dislikes = [[["mark".encode("utf8"), str("0" * 100).encode("utf8"), "".encode("utf8")]]]

with h5py.File("data/friday/likes.hdf5", "w") as file:
	for u in likes:
		uname = str(u[0][0])
		file.create_dataset(uname[2:len(uname)-1], data=u)

with h5py.File("data/friday/dislikes.hdf5", "w") as file:
	for u in dislikes:
		uname = str(u[0][0])
		file.create_dataset(uname[2:len(uname)-1], data=u)