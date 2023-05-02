#!/usr/bin/env python3

# 📚 Review With Students:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
# import ipdb

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.
pet_mood = "Hungry!"
pet_name = "Rose"
pet_age = 10
has_eaten = True #True/False starts with a capital 


def pet_status (pet_mood, pet_name):
    if pet_mood == "hungry":
        return (f"{pet_name} needs to be fed and given water.")
    elif pet_mood == "Rowdy!": 
        return (f"{pet_name} needs a walk.")
    else : 
        return (f"{pet_name} is all good.")

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"


def say_hello(): 
    return "Hello, world!"


# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

def pet_greeting(pet_name="Piper"):
    return(f"{pet_name} says hello!")

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html


def pet_birthday(pet_age=10):
    if type(pet_age) == int:
        pet_age += 1
        return (f"Happy Birthday! Your pet is now {pet_age}")
    else : 
        return ("Type Error Occurred")

# def pet_birthday(age):gi
#     try: 
#         age += 1
#         print(f"Happy Birthday! Your pet is now {age}")
#     except TypeError:
#         if(isinstance(age,str)): 
#             print("The type of the argument is a string")
#         else: 
#             print("Unkown varible type")
#     except UnboundLocalError: 
#         print("I have no idea what you entered")





# 🚨 To create an ipdb breakpoint, comment / uncomment line below:

# ipdb.set_trace()


 

# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose','Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Rose' 'Paul',]

# Reading Information From Lists
#2. ✅ Return the first pet name 


#3. ✅ Return all pet names beginning from the 3rd index


#4. ✅ Return all pet names before the 3rd index


#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th


#6. ✅ Find the index of a given element


#7. ✅ Reverse the original list

pet_names.reverse


#8. ✅ Return the frequency of a given element 

pet_names.count('Rose')
    #=> 1

# Updating Lists
#9. ✅ Change the first element to all uppercase 

pet_names[0].upper()
    #=> "ROSE"
#10. ✅ Append a new name to the list

pet_names.append("Bodhi")


#11. ✅ Add a new name at a specific index

pet_names.insert(0, "Piper")


#12. ✅ Add two lists together 

pet_names = pet_names + ['Luna', 'Milo', 'Pumpkin']

#13. ✅ Remove the final element from the list

pet_names.pop()

#14. ✅ Remove element by specific index

del pet_names[1]

#15. ✅ Remove a specific element 

pet_names.remove('Luke')

#16. ✅ Remove all pet names from the list

                    # pet_names.clear()

#Tuple 
# 📚 Review With Students:
    # Immutable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 

pet_ages = (12, 14, 2, 6, 9, 17, 3, 5, 8, 12)
    #tuple is a list that is immutable and defined using parens () instead of []

#18. ✅ Print the first pet age

# print(pet_ages[0])

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)



#20. ✅ Attempt to change the first element (should error)


# Tuple Methods
#21. ✅ Return the frequency of a given element

pet_ages.count(12)

#22. ✅ Return the index of a given element 

print(pet_ages.index(12))
    #  => 4
#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops

some_range = range(10)
print(some_range)

for num in range(3,7):
    print(pet_names[num])

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods

pets = {"Rose", "Rose", "Rose", "Milo", "Beans"}
pets2 = {"Rose", "Spot", "Tom", "Mini"}

pet_list = pets.union(pets2)
print(pet_list)

pets_diff = pets.difference(pets2)
print(pets_diff)
# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"

pet_info_rose = {'name':'rose',
                 'age':11,
                 'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"

pet_info_spot = dict(name='Spot', age=25, breed='boxer')


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 

print(f"{pet_info_rose['name']} is {pet_info_rose['age']} and a {pet_info_rose['breed']}")


#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error

print(pet_info_rose.get('location'))
    #  ==> "None"

# Updating 
#29. ✅ Update the pets age to 12

pet_info_rose['age'] = 12
print(pet_info_rose)

#30. ✅ Update the other pets age to 26

pet_info_spot['age'] = 26
print(pet_info_spot)

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 

del pet_info_rose['age']
print(pet_info_rose)

#31. ✅ Delete the other pets age using ".pop"

pet_info_spot.pop('age')
print(pet_info_spot)

#32. ✅ Delete the last item in the pet dictionary using "popitem()"

pet_info_spot.popitem()
print(pet_info_spot)

# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range


for num in range(10):
    print(num)


#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number

for num in range(50,60,2): 
    print(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 

def loop(pet_info):
    for pet in pet_info:
        print(pet)
loop(pet_info)

#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument

def print_name(list):
    for name in list:
        print(name)

print_name(pet_names)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

def print_names(list):
    counter = 0
    while counter <= len(list):
        print(f'counting: {counter}')
        counter += 1
   
print_names(pet_names)

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'


def update_age(list, name, age):
    index = 0
    while index < len(list):
        if(list[index]['name'] == name):
            list[index]['age'] == age
            return list[index]
        index += 1
    return "404: PET NOT FOUND"

print(update_age(pet_info, "rose", 8))


# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

pet_with_upper_case_names = [pet.upper() for pet in pet_names]
print(pet_with_upper_case_names)

# find like
#40. ✅ Use list comprehension to find a pet named spot

spot = [pet for pet in pet_names if pet == 'Spot']
print(spot)

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old

young_pets = [pet for pet in pet_info if pet['age'] < 3]
print(young_pets)
#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

