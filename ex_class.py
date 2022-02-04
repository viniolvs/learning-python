class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loggin_attempts = 0

    def describe_user(self):
        print("name: " + self.first_name, self.last_name + "\nAge: ", self.age)
    def increment_login_attempts(self):
        self.loggin_attempts += 1
    def reset_login_attempts(self):
        self.loggin_attempts = 0

u = User("vincius","silva",20)
u.describe_user()
u.increment_login_attempts()
print(u.loggin_attempts)

#classe privilegios do admin
class Previleges():
    def __init__(self) -> None:
        self.privileges = ["can add post", "can ban user"]
    def show_privileges(self):
        print("privileges: ")
        for privilege in self.privileges:
            print(privilege)
    
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Previleges()

   
a = Admin("vincius","silva",20)
a.privileges.show_privileges()