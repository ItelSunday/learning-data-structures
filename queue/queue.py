class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = [] 

  def enqueue(self, item):
    self.storage.insert(self.size, item)
    self.size += 1
  
  def dequeue(self):
        if self.size > 0:

            self.size -= 1
            return self.storage.pop()
        return None

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