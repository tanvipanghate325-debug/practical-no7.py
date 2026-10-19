 #--Singly Linked List--- 
class Node:    
     def __init__(self, data):        
       self.data = data        
       self.next = None  
class LinkedList:   
  def __init__(self):        
   self.head = None     
def insert(self, data):        
  new_node = Node(data)         
  new_node.next = self.head         
  self.head = new_node      
def display(self):        
 temp = self.head         
 while temp:            
  print(temp.data, end=" -> ")            
temp = temp.next        
print("None")  
ll = LinkedList() 
ll.insert(10) 
ll.insert(20) 
ll.insert(30)  
ll.display() 

#---Doubly linked list---
class Node:     
  def __init__(self, data):         
   self.data = data         
   self.prev = None        
   self.next = None 

#---Circular linked list---
class Node: 
  def init(self, data): self.data = data 
  self.next = None

class CircularLinkedList: 
  def init(self): 
    self.head = None

def insert(self, data):
  
  new_node = Node(data)

if not self.head: self.head = newnode 
newnode.next = self.head
else:
temp = self.head

while temp.next != self.head:
  temp = temp.next

temp.next = newnode 
newnode.next = self.head

def display(self): 
  if not self.head: print("List is empty") 
  return

temp = self.head

while True: print(temp.data, end=" -> ") 
temp = temp.next

if temp == self.head: 
  break

print("(back to head)")

cll = CircularLinkedList()
cll.insert(5) 
cll.insert(10) 
cll.insert(15)

cll.display()