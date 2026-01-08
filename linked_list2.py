class node:
    def __init__(self,data):
        self.data= data
        self.prev = None
        self.next = None
class  linklist:
    def __init__(self):
        self.head =None

    def insert_at_beginning(self,data):
       new_node = node(data)

       if self.head:
           self.head.prev=new_node
           new_node.next = self.head
           
       self.head = new_node
       print(f"{data} insert at bigning")
    def insert_at_end(self,data):
        new_node = node(data)

        if not self.head:
            self.head = new_node
            print(f"{data } insert at first node ")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"{data} insert at end")


    def delete(self, key):
    
        if not self.head:
            print("List empty!")
            return

        temp = self.head

        if temp.data == key:
            # self.head = temp.next
            if temp.next:
                self.head = temp.next
                self.head.prev = None
            print(f"{key} deleted.")
            return
        
        while temp and temp.data != key:
            temp = temp.next
            if not temp.next:
                print(f"{key} not found.")
                return

        # if not temp:
        #     print(f"{key} not found.")
        #     return

        # IMPORTANT
        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

        print(f"{key} deleted.")

        
    def delete_at_pos(self,index):
       if not self.head:
        print("List empty!")
        return

       if index < 0:
        print("Invalid index!")
        return

       temp = self.head
       if index == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"Node at index {index} deleted.")
            temp = None
            return
       current_index = 0

       while temp and current_index < index:
           temp = temp . next
           current_index += 1
       if not temp :
           print("index is out of reang")
           return
       if temp.next:
           temp.prev = temp.prev
       if temp.prev:
           temp.prev.next = temp.next

       print(f"node index at {index} deleted")
       temp =None           


    def search(self,key,):
        temp = self.head
        pos = 1
        while temp :
            if temp.data == key:
                print(f"{key} is found{pos}")
                return
            pos += 1
            temp = temp.next
        print(f"{key} not found")
    def display(self):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} --> ",end="")
            temp = temp.next
        print("none")



ll= linklist()

while True:
    print("\n-- Linked List Menu --")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Search")
    print("4. delete")
    print("5. delete at position")
    print("6. Display")
    print("7. Exit")
    
    choice = int(input("enter your choise :"))

    if choice == 1:
        data=(int(input("Enter data: ")))
        ll.insert_at_beginning(data)
    elif choice == 2:
        data = (int(input("Enter data: ")))
        ll.insert_at_end(data)
    elif choice == 3:
        data =(int(input("Enter value to search: ")))
        ll.search(data)

    elif choice == 4:
        data = int(input("what deta delet you :"))
        ll.delete(data)
    elif choice == 5:
       index = int(input("enter your delete pos :"))

       ll.delete_at_pos(index)
    
    elif choice == 6:
        ll.display()
    elif choice == 7:
        print("Thank you! Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")

        
