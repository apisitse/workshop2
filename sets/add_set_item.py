thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
#output {'cherry', 'apple', 'banana', 'orange'}

thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
#output  {'cherry', 'papaya', 'mango', 'apple', 'banana', 'pineapple'}