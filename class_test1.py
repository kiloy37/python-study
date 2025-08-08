import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def rename(self, new_name):
        self.name = new_name

person_list = []
person_list.append(Person("Alice", 30))
person_list.append(Person("Bob", 25))

print(person_list[0])  # Alice

print(person_list[1])  # Bob

with open("data.txt", "wb") as f:   # 'wb' : write-binary
    pickle.dump(person_list, f)