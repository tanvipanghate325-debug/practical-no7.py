t=(10,20,30)
print("Tuple element:",t[1])
s={1,2,3,4}
s.add(5)
s.remove(2)
print("Set:",s)

student={"name":"John","age":20,"course":"Python"}
print("Name:",student["name"])
print("Age:",student["age"])
print("Course:",student["course"])

del student["age"]
print("Updated Dictionary:",student)

print("Dictionary Keys:",student.keys())
print("Dictionary Values:",student.values())
print("Dictionary Items:",student.items())