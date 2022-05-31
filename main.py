from faker import Factory



fake = Factory.create('en-IN')


names = []

for _ in range(50):
	names.append(fake.name().replace(' ', '_'))

with open('names.txt', 'a') as file:
	for i in names:
		file.write(i+'\n')
	print("Done...")