from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.track = 0
    def append(self, item):

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents = []

        item = self.storage.head
        if self.storage.length < 1:
            return list_buffer_contents
        else: 
            while item.next: 
                list_buffer_contents.append(item.value)
                item = item.next
            list_buffer_contents.append(item.value)
            return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.storage = [0]*capacityself.track = 0 

    def append(self, item):
        if len(self.storage) < self.capacity: 
            self.storage.append(item)
            self.track += 1 
        else: 
            self.storage[self.track % self.capacity] = itemself.track += 1

    def get(self):
        return [i for i in self.storage if i]
