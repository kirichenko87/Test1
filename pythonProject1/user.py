class User:
    count = 0

    def __init__(self, name, age):

        if not isinstance(name, str):
            raise TypeError

        if not isinstance(age, int):
            raise TypeError

        if age < 0 or age > 100:
            raise ValueError

        self.name = name
        self.age = age
        User.count += 1

    def get_name(self):


        if len(self.name) == 0:
            raise ValueError
        if self.name.isdigit():
            raise ValueError

        return self.name


    def get_age(self):

        return self.age

    def up_age(self):
        self.age += 1
        return self.age