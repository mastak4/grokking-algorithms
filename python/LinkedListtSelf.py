class Node:
    item = None
    next = None

    def __init__(self, item, next) -> None:
        pass

class LinkedList:
    
    nodes = []
    head = None
    
    def __init__(self) -> None:
        pass

    def add(self, item):
        new = Node(item, None)
        if self.head == None:
            self.head = new
        else:
            last = self.head
            while last.next != None:
                last = last.next
    
    def delete(self, index):
        
