from faker import Faker

class Anonymizer():
    def __init__(self):
        self.faker = Faker()

    def first_name(self):
        return self.faker.first_name()


    def last_name(self):
        return self.faker.last_name()


    def address(self):
        return self.faker.address().replace('\n', ' ')
