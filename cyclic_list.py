class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circuliclist:
    def __init__(self):
        self.head = None

    def insert_at_bigning(self,data):   
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
        print(f"{data } insert at bigning")
   
    def delete(self,key):
        if not self.head :
            print("empty list ")
            return

        temp = self.head
        prev = None

        if temp.data == key:
            if temp.next == self.head:
                self.head = None
                print(f"{key} is deleted ")
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = temp.next
            last.next = self.head
            del temp
            print(f"{key} is deleted")
            return
    
        prev = temp
        temp = temp.next    
        while temp != self.head:
            if temp.data == key :
                prev.next = temp.next 
                del temp
                print(f"{key} is deleted")
                return
            prev = temp
            temp = temp.next 
        print(f"{key} is not found") 
        
    def search(self,key):
        if not self.head:
            print("list empty")
            return
        temp = self.head
        
        while True:
            if temp.data == key:
                print(f"{key} is found")
                return
            temp = temp.next
            if temp == self.head:
                    break
        print(f"{key} not found")    

    def display(self):
        if not self.head:
            print("list is empty")
            return
        
        temp = self.head
        while True:
            print(temp.data,end="-->")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")

cl = circuliclist()

while True:
    print("1 inser at bigning")
    print("2 delete ")
    print("3 search")
    print("4 display")
    print("5 exit ")

    choise = int(input("enetr a your choise : "))
    if choise == 1:
        data = int(input("insert your data "))
        cl.insert_at_bigning(data)
    elif choise == 2:
        data = int(input("  delete your num : "))
        cl.delete(data)
    elif choise == 3:
        data = int(input("search your data : "))
        cl.search(data)
    elif choise == 4:
        cl.display()
    elif choise == 5:
        print("_exit_")
        break
    else:
        print("invalid choise...")


