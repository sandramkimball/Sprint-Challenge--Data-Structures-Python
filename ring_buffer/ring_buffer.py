from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # self.storage[self.current] = item
        if len(self.storage) == self.capacity:
            if self.current == None:
                self.current = self.storage.tail
            self.current.value = item
            # self.storage.tail = self.current
            self.current = self.current.prev
            # self.storage.add_to_head(item)
            # self.storage.remove_from_head()
            # current = oldest, current[i+]
        else:
            self.storage.add_to_head(item)

    def get(self):
        list_buffer_contents = []

        if len(self.storage) <= 0:
            return list_buffer_contents

        current = self.storage.tail
        list_buffer_contents.append(current.value)

        while current.prev:
            current = current.prev
            list_buffer_contents.append(current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
