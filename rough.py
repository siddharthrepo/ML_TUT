class Node:
    def __init__(self , data=None , next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def traverse(self):
        itr = self.head
        while itr != None:
            print(itr.data)
            itr = itr.next
    
    def insert_at_first(self,new_data):
        node = Node(new_data , self.head)
        self.head = node

    def insert_at_end(self , data):
        if self.head == None:
            self.head = Node(data , None)
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = Node(data , None)



        



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(11)
    ll.insert_at_end(12)
    ll.traverse()
