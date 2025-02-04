from Node import Node

class DoublyLinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None

  # TODO: append()
  #Add to the end of the linked list
  def append(self, new_data):
    if self.head is None:#empty linked list
      new_node = Node(new_data)
      self.head = new_node
      self.tail = new_node
    else:
      #create a new node
      new_node = Node(new_data)
      #set new node previous to tail
      new_node.previous = self.tail
      #set tail.next to new node
      self.tail.next = new_node
      #move tail to new node
      self.tail = new_node

  # TODO: insert()
  def insert(self, item, index):
    pass

  # TODO: remove()
  def remove(self, value):
    pass

  # TODO: update()
  #Find and existing node with data == item and update with new value
  #traverse to find node
  #replace the data with value
  #hint: look at find() for singly linked list
  def update(self, item, value):
    pass

  # TODO: find()
  def find(self, item):
    pass