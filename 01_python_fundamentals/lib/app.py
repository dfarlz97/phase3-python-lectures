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

print(say_hello())

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

def pet_greeting(pet_name="Piper"):
    return(f"{pet_name} says hello!")
print(pet_greeting('Dennis'))
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
print(pet_birthday("10"))

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


