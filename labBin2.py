import shelve

dict_cars = {
    "AI1327CA": "Ruslan Shevchenko",
    "AI2254KI": "Stanislav Ponomarenko",
    "AA8440MN": "Ivan Brovarenko",
    "AA5252UI": "Lev Vasilchuk",
    "AM9205IM": "Dmitriy Melnichenko",
    "AM8832AA": "Mikhail Tarashchuk",
    "AX1783BV": "Denis Romanchenko",
    "AX2020XA": "Valery Zakharchuk",
    "CB9090MB": "Vasily Vasiliev",
    "CB6321PH": "Konstantin Gnatyuk"
}

with shelve.open('cars_data') as file:
    file['cars'] = dict_cars