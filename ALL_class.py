# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("man","Olsen")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
  

# x = Student("Mike", "Olsen")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#     print(brand)

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#     # print(brand)

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# c1=Car("ford","musteng")
# b1=Boat("ibiza","touring")
# p1=Plane("boeing","45")
# for x in(c1,b1,p1):
#   c1.brand

  


# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(-26)
# print(p1.get_age())

# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.__grade = 0

#   def set_grade(self, grade):
#     if 0 <= grade <= 100:
#       self.__grade = grade
#     else:
#       print("Grade must be between 0 and 100")

#   def get_grade(self):
#     return self.__grade

#   def get_status(self):
#     if self.__grade >= 60:
#       return "Passed"
#     else:
#       return "Failed"

# student = Student("Emil")
# student.set_grade(20)
# print(student.get_grade())
# print(student.get_status())

# class Person:
#   def __init__(self, name, salary):
#     self.name = name
#     self._salary = salary  # Protected property

# p1 = Person("Linus", 50000)
# print(p1.name)
# print(p1._salary)  # Can access, but shouldn't

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age  # Private property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age)  # This will cause an error




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

# p1 = Person("Emil", 30)

# # This is how Python mangles the name:
# print(p1.name)  # Not recommended!
# print(p1.__age)

# class Outer:
#   def __init__(self):
#     self.name = "Outer Class"

#   class Inner:
#     def __init__(self,outer):
#       self.outer = outer

#     def display(self):
#       print(F"This is the inner class name :{self.outer.name}")

# outer = Outer()
# inner= Outer.Inner(outer)
# inner.display()
# # print(outer.name)

# class Outer:
#   def __init__(self):
#     self.name = "Emil"

#   class Inner:
#     def __init__(self, outer):
#       self.outer = outer

#     def display(self):
#       print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#     self.engine = self.Engine()

#   class Engine:
#     def __init__(self):
#       self.status = "Off"

#     def start(self):
#       self.status = "Running"
#       print("Engine started")

#     def stop(self):
#       self.status = "Off"
#       print("Engine stopped")

#   def drive(self):
#     if self.engine.status == "Running":
#       print(f"Driving the {self.brand} {self.model}")
#     else:
#       print("Start the engine first!")

# car = Car("Toyota", "Corolla")
# car.drive()
# car.engine.start()
# car.drive()
# car.engine.stop()
# car.drive()

# class Computer:
#   def __init__(self):
#     self.cpu = self.CPU()
#     self.ram = self.RAM()

#   class CPU:
#     def process(self):
#       print("Processing data...")

#   class RAM:
#     def store(self):
#       print("Storing data...")
# class TransportUser:
#     def __init__(self, name):
#         self.name = name

#     def travel(self):
#         print("User travels by some transport.")

# computer = Computer()
# computer.cpu.process()
# computer.ram.store()




# from abc import ABC, abstractmethod

# class FareCalculator(ABC):
#     @abstractmethod
#     def calculate_fare(self, distance):
#         pass



# class BusFareCalculator(FareCalculator):
#     def calculate_fare(self, distance):
#         return distance * 10   

# class AutoFareCalculator(FareCalculator):
#     def calculate_fare(self, distance):
#         return distance * 15 
# bus_fare_calc = BusFareCalculator()
# auto_fare_calc = AutoFareCalculator()

# distance = 5

# print("Bus fare for student:", bus_fare_calc.calculate_fare(distance))
# print("Auto fare for teacher:", auto_fare_calc.calculate_fare(distance))

############### claculator  ##################

class Claculator:
    def __init__(self,num1=None,num2=None):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1*self.num2
    
    def divde(self):
        if self.num2 == 0:
             return "ERROR : num is not divison by zero"
        return self.num1 / self.num2
    @staticmethod
    def squaer(num):
        return num*num
 # repeating calculation   
while True:
    print("\n Calculator Menu ")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Square")
    print("6 EXIT")
       
    select=input("select 1 TO 6 : ")
    if select in ["1","2","3","4"]:
        num1=float(input("enter a num 1 :"))
        num2=float(input("enter a num 2 :"))
        calu=Claculator(num1,num2)


        if select == "1":
            print("Result",calu.add())
        elif select == "2":
            print("Result :",calu.subtract())
        elif select == "3":
            print("Result :",calu.multiply())
        elif select == "4":
            print("Result :",calu.divde())
# use staticmethod so write class name 
    elif select == "5":
        num= int (input("enter a num for square :"))
        print("square :",Claculator.squaer(num))
    
    elif select == "6":
        print("Thank you !!")
        break

    else:
        print("invalid choise !!!")
#_________________________________________________________________#


# class Transportuser:
#     def __init__(self,name):
#         self.name=name
#     def travel(self):
#         print("User travels by some transport.")
        
# class Student(Transportuser):
#   def __init__(self, name, roll_no:int, grade):
#   # How to intialize a parent class constructor
#       super().__init__(name)
#       self.name = name
#       self.__roll_no = roll_no  
#       self.grade = grade
#   def get_roll_no(self):
#       return self.__roll_no

#   def set_roll_no(self, new_roll_no:int):
#       if not new_roll_no: 
#           print("Error: Roll number cannot be empty!")
#       else:
#           self.__roll_no = new_roll_no
#   # Overriding
#   def travel(self):   
#       print(f"Student {self.name} travels by school bus.")

#   def display_info(self):
#       print(f"Student Name: {self.name}, Roll No: {self.__roll_no}, Grade: {self.grade}")
# class Bus:
#   def __init__(self,bus_no,drive_name):
#       self.bus_no=bus_no
#       self.drive_name=drive_name

#   def display_details(self):
#       print(f"bus no{self.bus_no},drive: {self.drive_name}")  

# tra=Transportuser("man")
# std=Student("man",21,"A")
# std.display_info()
# std.travel()
# std.set_roll_no("2040")

# bus=Bus("21","raj")
# bus.display_details()

# class StudentMarks:
#     def __init__(self, name,a,b):
#         pow()
#         self.name = name
        
#         self.marks = []  
#     def add_mark(self, mark):
#         self.marks.append(mark)

#     def show_marks(self):
#         print(f"{self.name}'s Marks:", self.marks)

#     def total_marks(self):
#         return sum(self.marks)

#     def average_marks(self):
#         if len(self.marks) == 0:
#             return 0
#         return sum(self.marks) / len(self.marks)



# stu = StudentMarks("man")
# stu.add_mark(80)
# stu.add_mark(90)
# stu.add_mark(70)

# stu.show_marks()
# print("Total:", stu.total_marks())
# print("Average:", stu.average_marks())


