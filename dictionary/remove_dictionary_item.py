#Ex 1
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
thisdict.pop("model")
print(thisdict)
#Output: {"brand":"Ford","year":1964}

#Ex 2
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
thisdict.popitem()
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang'}

#Ex 3
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
del thisdict["model"]
print(thisdict)
#Output: {"brand":"Ford","year":1964}

#Ex 4
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
thisdict.clear()
print(thisdict)
#Output: {}