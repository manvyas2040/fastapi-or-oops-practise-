class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None
    
    def insert_at_bignig(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                 temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            print(f"{data} insert at bigning")  

    def delete(self,key):
        if not self.head:
            print("empty list")
            return
        temp = self.head
        perv = None

        if self.head == key:
            if temp.next == self.head:
                self.head =None
                print(f"{key} is deleted")
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = temp.next
            last.next = self.head
            del temp
            print(f"{key} is deleted") 
            return
                
