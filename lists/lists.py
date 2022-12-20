
animals = ["Cow", "Pig", "Dog", "Cat", "Duck"] 
#          0        1       2       3       4
#each element in the list has an index value 
print(animals)
print(animals[0])
print(animals[-1])

#grab elements 1 and every element after that
print(animals[1:])

#acces the elements between an index up to (but not includning) the last element
print(animals[1:3])


#modify a value in a list
animals[0]= "Snake"
print(animals)