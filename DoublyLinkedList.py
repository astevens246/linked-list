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
    # Create new node
    new_node = Node(item)
    
    # Empty linked list
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      return
    
    # If index is 0, insert at beginning
    if index == 0:
      new_node.next = self.head
      self.head.previous = new_node
      self.head = new_node
      return
    
    # Traverse down the list
    current = self.head   
    count = 0
    while current is not None: # initiates the traversal
        if count == index - 1: # if the index is the one we want to insert at
          new_node.next = current.next # set the new node's next to the current node's next
          new_node.previous = current # set the new node's previous to the current node
          current.next = new_node # set the current node's next to the new node
          if new_node.next: # if the new node has a next
              new_node.next.previous = new_node # set the new node's next's previous to the new node    
          return # return the new node
        current = current.next # move to the next node
        count += 1 # increment the count    
  

  # TODO: update()
  #Find and existing node with data == item and update with new value
  #traverse to find node
  #replace the data with value
  #hint: look at find() for singly linked list
  def update(self, item, value):
    current = self.head # set the current node to the head
    
    # Traverse until we find the item
    while current and current.data != item: # while the current node is not None and the current node's data is not the item
      current = current.next # move to the next node
    
    # If item found, update its value
    if current: # if the current node is not None
      current.data = value # set the current node's data to the value

  # TODO: find()
  def find(self, item):
    current = self.head # start at the beginning
    index = 0 # keep track of the spot
    
    # Traverse until we find the item
    while current: # go through the list
      if current.data == item: # find the item
        return index # return the position
      current = current.next
      index += 1
    
    # Item not found
    return -1 # if the item wasn't found