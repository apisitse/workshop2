thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
#output:['apple', 'cherry']

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
#output:['apple', 'cherry']

thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)
#output:['apple', 'banana'] 

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)
#output:['banana', 'cherry']

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)
#output:[]