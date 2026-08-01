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
        if index < 0 or index >= self.size:
            return -1
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            else:
                curr = curr.next    # keep following pointer O(n) time
                i += 1
        return -1

    def addAtHead(self, val: str) -> None:
        newNode = ListNode(val, self.head, None)
        if self.head:
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def addAtTail(self, val: str) -> None:
        newNode = ListNode(val, None, self.tail)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1
    
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

    def get_size(self):
        return self.size


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.linkedList = MyLinkedList()
        self.cur_idx = 0
        self.linkedList.addAtHead(homepage)

    def visit(self, url: str) -> None:
        # clear all entries ahead of the current
        while self.linkedList.get_size() > self.cur_idx + 1:
            self.linkedList.deleteAtIndex(self.cur_idx + 1)

        self.linkedList.addAtTail(url)
        self.cur_idx += 1

    def back(self, steps: int) -> str:
        self.cur_idx = max(self.cur_idx - steps, 0)
        return self.linkedList.get(self.cur_idx)

    def forward(self, steps: int) -> str:
        self.cur_idx = min(self.linkedList.get_size() - 1, steps + self.cur_idx)
        return self.linkedList.get(self.cur_idx)


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)