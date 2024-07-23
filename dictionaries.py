my_dict = {'name': 'John', 'age': 26, 'city': 'New York'}
#print(my_dict['name']) 

#my_dict['age'] = 26

#my_dict['occupation'] = 'Engineer'
#print(my_dict)

#del my_dict['city']  # Removing a key-value pair
#print(my_dict)

#if 'age' in my_dict:
#   print('Age is present in the dictionary')
#else:
#    print('not present')  
for key, value in my_dict.items():
    print(key, value)  