from DoublyLinkedList import DoublyLinkedList


# Example:  12 ↔️ 200 ↔️ 19 ↔️ 49

dll = DoublyLinkedList()
dll.append(10)
print(dll.head.data)
dll.append(12)
print(dll.head.next)
print(dll.head.next.previous.data)
