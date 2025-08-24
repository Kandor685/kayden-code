fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(reverse= True)
print(fruits)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)
print(thislist)

def myfunc(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key= myfunc)
print(thislist)

fruits = ["orange", "Mango", "Kiwi", "pineapple", "Banana"]
fruits.sort(key = str.lower)
print(fruits)

fruits = ["orange", "Mango", "Kiwi", "pineapple", "Banana"]
fruits.reverse()
print(fruits)

fruits = ["orange", "Mango", "Kiwi", "pineapple", "Banana"]
copyfruits = fruits.copy()
print(copyfruits)
print("##################################################")
copyfruits = list(fruits)
print(copyfruits)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    
print(list1)

list1.extend(list2)
print(list1)

