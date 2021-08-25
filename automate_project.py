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

# this entire method makes much of the rest of the code redundent. Implement this into the main branch and then shuffle everything.
def populate_list(dict_here):
    for key in dict_here:
        result = []

        result.append((dict_here.get(key))[0])

        for i in range(3):
            pick = random.choice(city_list)
            while True:
                if pick in result:
                    pick = random.choice(city_list)
                    print("here btw")
                else:
                    result.append(pick)
                    break
            else:
                result.append(pick)
        dict_here.update({key: result})
    return dict_here

dict = prov.copy()


populate_list(dict)
print(prov)
print(dict)
