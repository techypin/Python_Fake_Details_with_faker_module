from faker import Factory
import json



fake = Factory.create('en-IN')


names = []

for _ in range(50):
	temp = {}
	temp['name'] = fake.name()
	temp['address'] = fake.address()
	temp['city'] = fake.city_name()
	temp['country'] = fake.country()
	temp['pincode'] = fake.postcode()

	names.append(temp)

with open('data.json', 'w') as file:
	json.dump(names, file, indent=3)