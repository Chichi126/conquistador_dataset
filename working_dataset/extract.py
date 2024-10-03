import pandas as pd
from faker import Faker

fake = Faker('yo_NG')  # Set the locale to Nigerian English

# Define the fields you want to generate
fields = [
    'name',
    'address',
    'phone_number',
    'email',
    'state',
    'city',
    'zip_code'
]

# Create a dictionary to store the fake data
data = {field: [] for field in fields}

# Generate fake data for each field
for _ in range(100):  # Generate 100 rows of data
    data['name'].append(fake.name())
    data['address'].append(fake.address())
    data['phone_number'].append(fake.phone_number())
    data['email'].append(fake.email())
    data['state'].append(fake.state())
    data['city'].append(fake.city())
    data['zip_code'].append(fake.zipcode())

# Create a Pandas DataFrame from the fake data
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print(df.head())