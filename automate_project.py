import subprocess
import os
import random

#

prov = {
    "Yukon": ["Whitehorse"],
    "Northwest Territories": ["Yellowknife"],
    "Nunavut": ["Iqaluit"],
    "British Comlumbia": ["Victoria"],
    "Alberta": ["Edmonton"],
    "Saskatchewan": ["Regina"],
    "Manitoba": ["Winnipeg"],
    "Ontario": ["Ottawa"],
    "Quebec": ["Quebec City"],
    "New Brunswick": ["Fredericton"],
    "Prince Edward Island": ["Charlottetown"],
    "Nova Scotia": ["Halifax"],
    "Newfoundland and Labrador": ["Saint John's"]
}

city_list = ["Whitehorse", "Yellowknife", "Iqaluit", "Victoria", "Edmonton", "Regina", "Winnipeg", "Ottawa",
             "Quebec City", "Fredericton", "Charlottetown", "Halifax", "Saint John's"]

# inital set of questions
num_questions = len(prov)

# picks number between 1-13
option = random.randint(0, num_questions - 1)

# subtract 1 from the list so next rotation it will be 1-12
num_questions = num_questions - 1

# --------------- # Puts all the keys in an index so we can pick the index from the random number
x = list(prov)

d = {}


def populate_list(dictionary, listOfCity, indexOfOption, CityinIndex):
    pick = random.choice(listOfCity)
    check = 0
    while check != 3:
        if pick in dictionary.get(indexOfOption[CityinIndex]):
            print("Item was not added because its in the list already")
            pick = random.choice(city_list)
        else:
            check = check + 1
            dictionary.get(indexOfOption[CityinIndex]).append(pick)
            pick = random.choice(listOfCity)

# loops 13 times 
for i in range(13):

    # This will update the dict -> x is a list and option is the index of that list

    d.update({x[option]: prov.get(x[option])})
    d.update({x[option]: populate_list(d, city_list, x, option)})
# We remove the index that has been put into the list so we never get a duplicate.
    x.pop(option)

    # This is for the final loop as it will do one last loop after the list is empty and will exit out of the loop
	# before we hit an error (probably changet his to while loop before submitting)
    if (len(x)) == 0:
        break
    else:
        # This will update the index and pick another random number between 0 and the lenth of the current list
        option = random.randint(0, len(x) - 1)

x = prov.values()

for key in prov:
    x = prov.get(key)
    random.shuffle(x)

# ------------- # This will shuffle the dirtionary around list is not done here
keys = list(prov.keys())
random.shuffle(keys)

newDir = dict()
for key in keys:
    newDir.update({key: prov[key]})

print(newDir)
