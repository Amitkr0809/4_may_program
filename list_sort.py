list = ["q","a","f","b","c"]
list.sort()
print(list)
list.sort(reverse = True)
print(list)

list1 = [2,10,90,0,98,5,3]
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)
list1.reverse()
print(list1)

list2 = ["banana", "Orange", "Kiwi", "cherry","A"]
list2.sort()
print(list2)

list3 = ["banana", "Orange", "Kiwi", "cherry"]
list3.sort(key = str.lower)
print(list3)