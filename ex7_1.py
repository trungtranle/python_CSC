animals_list = ['ant','bear','cat','dog','elephant','fish', 'goat','hippo']

print(animals_list)
print('Number of animals: ', len(animals_list))

animal = input ('I want to find: \n')

if animal in animals_list:
    print('There is', animal,'in the list of animals')
else: 
    print(animal, 'is not in the list of animals')