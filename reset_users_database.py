import h5py

me = ["Roshan", "Maind", "roshanmaind", "123123123", "N"]
me = [s.encode("utf8") for s in me]
users = [me]

with h5py.File("data/friday/users.hdf5", "w") as file:
    file.create_dataset("users", data=users)

