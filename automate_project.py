import json
import subprocess
import os
import random
import pprint

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

count = 0

city_list = ["Whitehorse", "Yellowknife", "Iqaluit", "Victoria", "Edmonton", "Regina", "Winnipeg", "Ottawa",
             "Quebec City", "Fredericton", "Charlottetown", "Halifax", "Saint John's"]

# ------------------------# Helper Methods

# This method here write to a file but its not correct yet. Its currently writing
# the same file over and over. It should
def write_to_file():
    write_to_file.counter += 1
    subprocess.run(["touch", "/home/manfred/Documents/dumpFolder/Test_" + str(write_to_file.counter) + ".txt"])
    formatted_text = pprint.pformat(prov)
    openfile = open("/home/manfred/Documents/dumpFolder/Test_" + str(write_to_file.counter) + ".txt", "a")
    openfile.write(formatted_text)
    openfile.close()
write_to_file.counter = 0


# This method will populate the lists inside the dictionary...im like 90% sure this can be done
# better considering the I am having to index my way through the dictionary instead of just looping
# through the key value pairs. That is probably why it was not working originally (check later use for example)

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

def file_creation():


    # Inital set of questions
    for k in range(1):
        num_questions = len(prov)

        # picks number between 1-13
        option = random.randint(0, num_questions - 1)

        # subtract 1 from the list so next rotation it will be 1-12
        num_questions = num_questions - 1

        # --------------- # Puts all the keys in an index so we can pick the index from the random number
        x = list(prov)

        d = {}


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

        write_to_file()


file_creation()
