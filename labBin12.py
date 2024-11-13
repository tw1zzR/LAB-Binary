import pickle

file = open('data.bin', 'rb')
load_bindata = pickle.load(file)
print(load_bindata)
