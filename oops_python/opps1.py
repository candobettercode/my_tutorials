# initalizing a class with constructor and displaying its attributes
class employee:
    # Constructor to initialize the employee attributes
    # name, age, and salary
    def __init__(self):
        print("Constructor called.. executing attributes/data")
        self.id=121
        self.salary=50000
        self.designation="Software Engineer"  
        print("Attributes initialized successfully")

    def travel(self,destination):  
        print("Travel method called.. executing travel") 
        print(f"Traveling to {destination}")
    

# create an instance of the employee class 
sam = employee()
# Display the attributes of the employee instance
# print(sam.salary)
# print(sam.travel("New York"))
print(type(sam))