import pickle

with open('cars_data.bin', 'rb') as file:
    cars_data = pickle.load(file)

for number, owner in cars_data.items():
    print(f"Number: {number}, Owner: {owner}")