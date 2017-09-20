class Person:
    def __init__(self, name, email, phone, friends=[]]):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people_greeted = []
    def greet(self, other_person):
        print ('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.unique_people_greeted:
            self.unique_people_greeted.append(other_person)
    def num_unique_people_greeted(self):
        print (len(self.unique_people_greeted))
    def print_contact_info(self):
        print(self.name +"'s email:", self.email, ",",self.name + "'s phone number: ", self.phone)
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(sonny.name, sonny.email, sonny.phone)
# print(jordan.name, jordan.email, jordan.phone)

# sonny.print_contact_info()

# jordan.friends.append(sonny)
# print(len(jordan.friends))

# sonny.add_friend(jordan)
# print(len(sonny.friends))
# sonny.num_friends()

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

# print(jordan)

sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
dee_ann = Person('Dee Ann', 'dee@gmail.com', '123-123-1233')
sonny.greet(dee_ann)
sonny.num_unique_people_greeted()


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        print('BEEP BEEP!')
    def print_info(self):
        print(self.year, self.make, self.model)
