
class User:
    def __init__(self, name: str, email:str):
        self.name = name
        self.email = email

    def show_details(self):
        print(f"Name: {self.name}, Email: {self.email}")

class Admin(User):
    def __init__(self, name:str, email:str, role:str):
        super().__init__(name, email)
        self.role = role

    def show_details(self):
        print(f"Name: {self.name}, Email: {self.email}, Role: {self.role}")

user1 = User("Almaaz", "almaaz@gmail.com")
user2 = Admin("Ahmed", "ahmed@gmail.com", "admin")

user1.show_details()
user2.show_details()