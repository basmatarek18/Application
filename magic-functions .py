class Customer:
    
    def __init__(self, name, balance=5):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __repr__(self):
        return f"Customer(name={self.name}, balance={self.balance})"
    
    # Equality check
    def __eq__(self, other):
        return self.balance == other.balance
    
    # Less than comparison
    def __lt__(self, other):
        return self.balance < other.balance
    
    # Less than or equal to comparison
    def __le__(self, other):
        return self.balance <= other.balance
    
    # Greater than comparison
    def __gt__(self, other):
        return self.balance > other.balance
    
    # Greater than or equal to comparison (already provided in the original)
    def __ge__(self, other):
        return self.balance >= other.balance
    
    # Addition of balances between two Customer objects
    def __add__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
    # Subtraction of balances between two Customer objects
    def __sub__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

# Creating Customer instances
customer1 = Customer("Basma", 10)
customer2 = Customer("Sarah", 7)
customer3 = Customer("Ali", 10)


print(str(customer1)) 
print(repr(customer2)) 

print(customer1 == customer2)  
print(customer1 == customer3)  

print(customer2 < customer1) 
print(customer1 < customer3)   

print(customer2 <= customer1)  
print(customer1 <= customer3)  

print(customer1 > customer2)   
print(customer2 > customer3)   

print(customer1 >= customer2) 
print(customer1 >= customer3) 

customer4 = customer1 + customer2 
print(customer4)  

customer5 = customer1 - customer2  
print(customer5)  
