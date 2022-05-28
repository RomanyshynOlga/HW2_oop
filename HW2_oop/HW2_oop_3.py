class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def _transformation(self):
        return list(self.__dict__.values())


person = Profile('Olga', 'Fox', '0985706636', 'Lviv', 'zt@gmail.com', ' Fabrury 12, 1985', '38', 'woman')
print(person._transformation())
