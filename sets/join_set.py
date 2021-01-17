set1 = {"a","b","c"}
set2 = {"d","e","f"}
set3 = set1.union(set2)
print(set3)  #output:{'a', 'e', 'c', 'f', 'd', 'b'}

set1 = {"a","b","c"}
set2 = {"d","e","f"}
set1.update(set2)
print(set1)     #output:{'a', 'e', 'c', 'f', 'd', 'b'}

set1 ={"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.intersection_update(set2)
print(set1)     #output:{'apple'}

set1 ={"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1)     #output:{'cherry', 'banana', 'microsoft', 'google'}
