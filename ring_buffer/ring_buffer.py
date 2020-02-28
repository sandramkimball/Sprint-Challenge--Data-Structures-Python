from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage < self.capacity:
            self.storage.append(item)

        if self.storage == self.capacity:
            self.current = 0
            self.storage.pop(current)
            self.storage.append(item)
            self.storage.current = item
            # current = oldest, current[i+]

    def get(self):
        list_buffer_contents = []
        # if list_buffer_contents contains None:
        #     None[i] = 0        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
