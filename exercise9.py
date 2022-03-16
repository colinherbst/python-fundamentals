# 8-3 through 8-5
def make_shirt(size='large', message='I love Python'):
    print("\nI will make a " + size + " t-shirt.")
    print('It will say, "' + message + '".')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Exercise 9')


def describe_city(city, country='canada'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)


describe_city('reykjavik', 'iceland')
describe_city('toronto')
describe_city('calgary')


# 8-9 through 8-11
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians


magicians = ['David Blane', 'Dynamo', 'Houdini']
show_magicians(magicians)
print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
print("\nOriginal magicians:")
show_magicians(magicians)


# 9-1 through 9-3
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open."
        print("\n" + msg)


mcdonalds = Restaurant('McDonalds', 'french fries')
mcdonalds.describe_restaurant()

wendys = Restaurant("Wendys", 'lemonade')
wendys.describe_restaurant()

burger_king = Restaurant('Burger King', 'burgers')
burger_king.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, username, email, age):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.age = age

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Age: " + self.age)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")


colin = User('colin', 'herbst', 'cherbst1', 'colinherbst123@gmail.com', '17')
colin.describe_user()
colin.greet_user()

jevon = User('jevon', 'smith', 'jsmith3', 'jevonsmith123@gmail.com', '18')
jevon.describe_user()
jevon.greet_user()


# 9-4 through 9-5
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


restaurant = Restaurant('mcdonalds', 'french fries')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 451
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(2321)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(435)
print("Number served: " + str(restaurant.number_served))


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


colin = User('colin', 'herbst', 'cherbst1', 'colinherbst123@gmail.com', '17')
colin.describe_user()
colin.greet_user()
print("\nMaking 5 login attempts")
colin.increment_login_attempts()
colin.increment_login_attempts()
colin.increment_login_attempts()
colin.increment_login_attempts()
colin.increment_login_attempts()
print("  Login attempts: " + str(colin.login_attempts))
print("Resetting login attempts")
colin.reset_login_attempts()
print("  Login attempts: " + str(colin.login_attempts))
