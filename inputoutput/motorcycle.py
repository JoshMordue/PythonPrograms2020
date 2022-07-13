import shelve

with shelve.open('bike') as bike:
    bike["make"] = "Honda"
    bike["colour"] = "blue"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["colour"])