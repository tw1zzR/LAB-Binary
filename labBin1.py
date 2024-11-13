import pickle

# Take data
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

list1 = []

# Take even numbers
for number in range(a,b):
    if number % 2 == 0:
        list1.append(number)
    else:
        continue

# Take numbers with ending 6
six_list = []

for even_number in list1:
    if int(str(even_number)[-1]) == 6:
        six_list.append(even_number)
    else:
        continue

# Saving
file = open('data.bin', 'wb')
pickle.dump(six_list, file)
file.close()