lucky_numbers = [8, 4, 42, 16, 23, 15]
friends = ["Kevin", "Kevin", "Karen", "Jim", "Oscar", "Toby"]

#extend function adds a list to the end of another list
#friends.extend(lucky_numbers)
#print(friends)

#append function adds individual ellements to the end of a list
lucky_numbers.append(13)
print(lucky_numbers)

#insert adds an item to the middle of a list and then pushes every thing else up 1 idex
friends.insert(1, "Kelly")
print(friends)

#remove an element
friends.remove("Kelly")
print(friends)

#clear: reset the list
#friends.clear()
#print(friends)

#remove the last item off of list
friends.pop()
print(friends)

#find a certain value in list
print(friends.index("Karen"))

#cound the number of times a value occurs within a list
friends.count("Kevin")

#sort list in accending order
lucky_numbers.sort()
print(lucky_numbers)

#reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

#create a new list by copying an existing list
friends2 = friends.copy()
print(friends2)