def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

print(greet.__annotations__)

class Person:
    name: str
    age: int

print(Person.__annotations__)
