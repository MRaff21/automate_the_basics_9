import json
import subprocess
import os
import random


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


def shuffle(dictionary_shuffle):
    for key in dictionary_shuffle:
        lst = dictionary_shuffle.get(key)
        random.shuffle(lst)

    keys = list(dictionary_shuffle.keys())
    random.shuffle(keys)

    shuffled_dict = {}

    for key in keys:
        shuffled_dict.update({key: dictionary_shuffle[key]})

    return shuffled_dict


global count
count = 1


def write_to_file(anythingHere):
    global count

    subprocess.run(["touch", "/home/lab/Documents/dumpFolder/Test_" + str(count) + ".txt"])

    openfile = open("/home/lab/Documents/dumpFolder/Test_" + str(count) + ".txt", "a")
    openfile.write(json.dumps(shuffle(anythingHere)))
    openfile.close()
    count += 1


def populate_list(dict_here):
    for key in dict_here:
        result = []

        result.append((dict_here.get(key))[0])

        for i in range(3):
            pick = random.choice(city_list)
            while True:
                if pick in result:
                    pick = random.choice(city_list)
                else:
                    result.append(pick)
                    break
            else:
                result.append(pick)
        dict_here.update({key: result})
    return dict_here


for i in range(13):
    dict = {}
    dict = prov.copy()
    populate_list(dict)
    write_to_file(dict)
