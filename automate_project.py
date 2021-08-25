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

shuffled_dict = {}

def shuffle():
    for key in dict:
        lst = dict.get(key)
        random.shuffle(lst)

    keys = list(dict.keys())
    random.shuffle(keys)
    for key in keys:
        shuffled_dict.update({key: dict[key]})



global count
count = 1


def write_to_file(dictionary_here):
    global count
    subprocess.run(["touch", "/home/lab/Documents/dumpFolder/capitalsquiz" + str(count) + ".txt"])
    subprocess.run(["touch", "/home/lab/Documents/dumpFolder/capitalsquiz_answers" + str(count) + ".txt"])

    quizFile = open(f'/home/lab/Documents/dumpFolder/capitalsquiz{count}.txt', 'w')
    answerKeyFile = open(f'captialsquiz_answers{count}.txt', 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20) + f'Province Capitals Quiz(Form{count})')
    quizFile.write('\n\n')


    shuffle()
    for question_num in range(3):
        key, value = list(shuffled_dict.items())[question_num]
        quizFile.write(f'\n{question_num + 1}: What is the capital of {key}?\n\n')
        quizFile.write(f'\tA: {value[0]}\n\n\tB: {value[1]}\n\n\tC: {value[2]}\n\n\tD: {value[3]}\n')

    quizFile.close()
    #openfile = open("/home/lab/Documents/dumpFolder/Test_" + str(count) + ".txt", "a")
    #openfile.write(json.dumps(shuffle(anythingHere)))
    #openfile.close()
    count += 1
# --- Helper method use this to finish off the task

def findAnswer():

	for i in range(13):

		key, value = list(dict.items())[i]

		for j in range(13):
			skey, svalue = list(prov.items())[j]

			if key == skey:

				for k in range(4):
					if svalue[0] == value[k]:
						print("confirm")
						index = k
						answer_key[skey] = index
						break

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


for i in range(3):
    dict = {}
    dict = prov.copy()
    populate_list(dict)
    write_to_file(dict)
