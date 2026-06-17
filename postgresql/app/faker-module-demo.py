from faker import Faker

### The faker module generates a fake data for quick use and demo
fake = Faker()

### One fake job
job = {
    "title": fake.job(),
    "company": fake.company(),
    "location": fake.city(),
    "salary": fake.random_int(min=50000, max=200000),
    "description": fake.text(max_nb_chars=300),
}

print(job)