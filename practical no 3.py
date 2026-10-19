numbers=[10,20,30,40,50]
print("First element of the list:",numbers[0])
print("Last element of the list:",numbers[-1])

numbers[2]=35
print("Updated list:",numbers)
numbers.insert(1,15)
print("After insertion:",numbers)

numbers.remove(40)
del numbers[0]
print("After deletion:",numbers)
print("Length of the list:",len(numbers))
print("Maximum value in the list:",max(numbers))
print("Minimum value in the list:",min(numbers))
numbers.sort()
print("sorted list:",numbers)