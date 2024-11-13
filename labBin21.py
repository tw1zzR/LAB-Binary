import shelve

with shelve.open('cars_data') as file:
    cars_data = file['cars']

for number, owner in cars_data.items():
    print(f"Number: {number}, Owner: {owner}")