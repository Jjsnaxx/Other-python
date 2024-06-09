#lists

groceries = ["milk", "eggs", "steak"]

print(groceries[0])

del groceries[0]

print(groceries[0])

groceries = ["cheese"] + groceries

print(groceries)

print(groceries.index("steak"))

print(groceries.reverse)



List1= ['A', 'B', 'C', 'D', 'E']

print(List1.count('E'))

List1.append('E')

print(List1)

List1.pop()

print(List1)

print("------------------------------------")

List1= ['A', 'B', 'C', 'D', 'E']

List4 = List1

print(List4)
print(List1)

List4[1] = "X"

print(List4)
print(List1)

List4 = List1.copy() 

List4[1] = "A"

print(List4)
print(List1)

print("------------------------------------")

List5= ['1', '2', '3']

List6= list(map(float,List5))

print(List6)
