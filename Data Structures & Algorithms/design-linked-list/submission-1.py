class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        # using a size parameter would have been super helpful
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            else:
                curr = curr.next    # keep following pointer O(n) time
                i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head, None)
        if self.head:
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, None, self.tail)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # use your previous functions!
        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        i = 0
        curr = self.head
        while curr:
            if i == index:
                newNode = ListNode(val, curr, curr.prev)
                curr.prev.next = newNode
                curr.prev = newNode
                self.size += 1
                return
            else:
                curr = curr.next
                i += 1


        # if exactly at the end    
        if i == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index >= self.size:
            return

        if index == 0:
            if not self.head.next:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.size -= 1
            return

        i = 0
        curr = self.head
        while curr:
            if i == index:
                if curr.next:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                else:
                    curr.prev.next = None
                    self.tail = curr.prev
                self.size -= 1
                return   
            else: 
                i += 1   
                curr = curr.next  


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)