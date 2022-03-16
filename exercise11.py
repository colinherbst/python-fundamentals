# 9-6
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open."
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nThe flavors we have are:")
        for flavor in self.flavors:
            print(flavor.title())


two_four_seven_icecream = IceCreamStand('24/7 Ice Cream')
two_four_seven_icecream.flavors = ['vanilla', 'chocolate', 'strawberry']

two_four_seven_icecream.describe_restaurant()
two_four_seven_icecream.show_flavors()


# 9-7 and 9-8
class User:

    def __init__(self, first_name, last_name, username, email, age):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.age = age.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Age: " + self.age)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username, email, age):
        super().__init__(first_name, last_name, username, email, age)
        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(" " + privilege)
        else:
            print(" This user has no privileges.")


colin = Admin('colin', 'herbst', 'cherbst1', 'colinherbst123@gmail.com', '17')
colin.describe_user()

colin.privileges.show_privileges()

print("\nNew Privileges")
colin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
colin.privileges.privileges = colin_privileges
colin.privileges.show_privileges()
