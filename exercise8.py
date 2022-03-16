# 5-8 Hello Admin and 5-9 No Users
usernames = ['colin', 'jevon', 'admin', 'charles', 'josh']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")


# 5-10 Checking Usernames
current_users = ['colin', 'jevon', 'admin', 'charles', 'josh']
new_users = ['COLIN', 'JeVoN', 'brayden', 'tim', 'brock']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken please enter a new username.")
    else:
        print("Yes, the name " + new_user + " is still available.")


# 5-11 Ordinal Numbers
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")


# 6-1 Person
person = {
    'first_name': 'colin',
    'last_name': 'herbst',
    'age': 17,
    'city': 'haysville',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


# 6-7 People
people = []
person = {
    'first_name': 'colin',
    'last_name': 'herbst',
    'age': 17,
    'city': 'haysville',
}
people.append(person)
person = {
    'first_name': 'jevon',
    'last_name': 'smith',
    'age': 18,
    'city': 'wichita',
}
people.append(person)
person = {
    'first_name': 'charles',
    'last_name': 'smith',
    'age': 18,
    'city': 'austin',
}
people.append(person)
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", lives in " + city + ", and is " + age + " years old.")
