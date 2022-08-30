from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        user_name=faker_en.user_name(),
        email=faker_en.email(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
    )







