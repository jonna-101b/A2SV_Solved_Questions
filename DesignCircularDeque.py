class DoublyLikedList:
    def __init__(self, val: int, prev: None, next: None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.max_size = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.max_size:
            node = DoublyLikedList(value, self.tail, self.head)

            if self.head is None:
                self.head = node
                self.head.prev = node
                self.head.next = self.head
                self.tail = node

            else:
                self.head.prev = node
                self.head = self.head.prev
                self.tail.next = self.head
        
            self.size += 1
            return True

        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.max_size:
            node = DoublyLikedList(value, self.tail, self.head)

            if self.head is None:
                self.head = node
                self.head.prev = node
                self.head.next = self.head
                self.tail = node

            else:
                self.tail.next = node
                self.tail = self.tail.next
                self.head.prev = self.tail
        
            self.size += 1
            return True

        return False

    def deleteFront(self) -> bool:
        if self.head:
            if self.size == 1:
                self.head = self.tail = None

            else:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.head.prev = self.tail

            self.size -= 1
            return True

        return False

    def deleteLast(self) -> bool:
        if self.head:
            if self.size == 1:
                self.head = self.tail = None

            else:
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
                self.tail.next = self.head
            
            self.size -= 1
            return True

        return False

    def getFront(self) -> int:
        if self.head:
            return self.head.val

        return -1

    def getRear(self) -> int:
        if self.tail:
            return self.tail.val

        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
