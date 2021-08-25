import random
import subprocess

dict = {
	"Northwest Territories" : ["Whitehorse", "Fredericton", "Iqaluit", "Yellowknife"],
	"Nunavut" : ["Yellowknife", "Fredericton", "Iqaluit", "Victoria"],
	"Yukon" : ["Whitehorse", "Yellowknife", "Iqaluit", "Victoria"],
    "Manitoba": ["Winnipeg", "Yellowknife", "Iqaluit", "Victoria"],
    "Ontario": ["Yellowknife", "Iqaluit", "Victoria", "Ottawa"],
    "Quebec": ["Yellowknife", "Quebec City", "Iqaluit", "Victoria"],
    "New Brunswick": ["Fredericton", "Yellowknife", "Iqaluit", "Victoria"],
    "Prince Edward Island": ["Yellowknife", "Iqaluit", "Charlottetown","Victoria"],
	"Saskatchewan": ["Yellowknife", "Iqaluit", "Victoria" ,"Regina",],
	"Nova Scotia": ["Halifax", "Yellowknife", "Iqaluit", "Victoria"],
    "Newfoundland and Labrador": ["Saint John's", "Yellowknife", "Iqaluit", "Victoria"],
	"Alberta": ["Edmonton", "Yellowknife", "Iqaluit", "Victoria"],
	"British Comlumbia": ["Victoria", "Yellowknife", "Iqaluit", "Victoria"]

}






#lists = ["Ottawa", "Vic", "Hali", "Edmonton"]
#pick = random.choice(list)
#check = 0
#while check != 3 :
#	if pick in dict["Answer"] :
#		print("Item was not added because its in the list already")
#		pick = random.choice(lists)
##		check = check + 1
#		dict["Answer"].append(pick)
#		pick = random.choice(lists)

#print(dict["Answer"])


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

keys = list(prov.keys())
random.shuffle(keys)

#ShuffledProv = dict()

#for key in keys:
	#ShuffledProv.update({key: prov[key]})

#print("\nDic after shuffling")
#print(ShuffledProv)
#key, value = list(prov.items())[1]
#print(key)
#print(value[1])
#subprocess.run("ls" "/home/")

answer_key = {}

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

	print(answer_key)





findAnswer()