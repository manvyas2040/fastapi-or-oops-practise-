class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linklist:
    def __init__(self):
        self.head=None

    def insert_at_beginung(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head =new_node
        print(f"data insert in bedining {data}")

    def insert_at_end(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            print(f"inserted {data} at the begning")
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        print(f"inserted {data} at the end")
    
    def insert_after_value(self,target,data):
        temp =self.head
        while temp and temp.data != target:
            temp =temp.next

        if not temp :
            print(f"{target} not found ")
            return
        new_node = node(data)
        new_node.next=temp.next
        temp.next = new_node
        print(f"{data} insert after {target}")

    def insert_at_position(self,data,positison):
        if positison <= 0:
            print("invalid pos...")
            return
        new_node = node(data)
        if positison == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"{data} data insert.")
            return
        temp = self.head
        corrent_pos = 1
        while temp and corrent_pos <positison -1:
            temp =temp.next
            corrent_pos += 1
        if not temp :      
            print("position is out of range ")
            return
        new_node.next = temp.next
        temp.next = new_node
        print(f"{data} is inserted  at position {positison}")
        


    def delete_by_value(self, key): 
      temp=self.head
      if temp and temp.data == key:
          self.head = temp.next
          temp =None
          return

      prev =None
      while temp and temp.data != key:
          prev = temp
          temp = temp.next
      if temp is None :
          print(f"{key} not found")      
          return
      prev.next = temp.next
      temp= None
      print(f"{key} deleted...")

    def search(self, key):
        temp = self.head
        pos = 1
        while temp :
            if temp.data == key:
                print(f"{key} is found at {pos} ")
                return
            pos += 1
            temp = temp.next
        print(f"{key} not found")

    def display(self): 
        if not self.head:
            print("linked list is emplty")
            return
        corrent= self.head
        while corrent:
            print(f"{corrent.data} --> ", end="")
            corrent=corrent.next
        print("none")


ll=linklist()       

while True:
    print("---link list menu ---")
    print("insert at begining element")
    print("insert at end element")
    print("Insert After a Value")
    print("Insert at Specific Position")
    print("delete element")
    print("search element")
    print("disply element")
    print("exiting")

    choise=int(input("enter your choise = "))


    if choise == 1:
        data=int(input("insert an element at begining : "))
        ll.insert_at_beginung(data)

    elif choise == 2:
        data=int(input("insert an element at end : "))
        ll.insert_at_end(data)

    elif choise == 3:
        target=int(input("enter your target : "))
        data = int(input("enter your data :"))
        ll.insert_after_value(target,data)

    elif choise == 4:
        data = int(input("enter your data :"))
        positison = int(input("enter your position :"))
        ll.insert_at_position(data,positison)

    elif choise == 5:
        data=int(input("delete your element :"))
        ll.delete_by_value(data)

    elif choise ==6:
        data=int(input("search your element : "))
        ll.search(data)

    elif choise == 7:        
        ll.display()

    elif choise == 6:
        print("  EXIT  ")
        break
    else:
        print("invalid choice... ")



