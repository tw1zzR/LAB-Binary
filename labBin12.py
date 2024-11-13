import pickle

with open('data.bin', 'rb') as file:
    load_bindata = pickle.load(file)

print(load_bindata)