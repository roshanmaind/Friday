import h5py
import os

root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path) - 23]

me = ["Roshan", "Maind", "roshanmaind", "123123123", "N"]
me = [s.encode("utf8") for s in me]
users = [me]

with h5py.File(str(root_path + "data/friday/users.hdf5"), "w") as file:
	file.create_dataset("users", data=users)
