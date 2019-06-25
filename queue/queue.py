class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = [] 

  def enqueue(self, item):
    self.storage.append(item) #add item at the end
  
  def dequeue(self):
    if self.storage == 0:
        return self.storage.pop(0)
       #. pop() removes last element of an array, and returns elements
     

  def len(self):
    return self.size

#Queues are simple and intuitive to use and implement
#list or collection with the restriction that insertion can be be performed at one end(rear)
# and deletion can be performed at other end (front)

#Operations: front(), IsEmpty()
#Enqueue(), add item to the back 
#Dequeue(), remove/returm item from the front
#Time complexity // O(1)

#Implementation of Queues using Array and Linkedlist