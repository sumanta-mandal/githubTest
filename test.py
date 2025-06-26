class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

# Create a user object
user1 = User("Alice", 30, "alice@example.com")

# Print user data
user1.display_info()
