import faker

def get_sign_up_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name, email, password

def get_incorrect_password():
    fakes = faker.Faker()
    name = fakes.name()
    email = fakes.email()
    return name, email
