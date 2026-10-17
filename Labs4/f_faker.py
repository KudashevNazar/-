from faker import Faker

def fake_person():
    fake = Faker("uk_UA")
    return {"name": fake.name(), "city": fake.city()}