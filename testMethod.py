import random


dict = {
	"Ontario" : "Ottawa",
	"BC" : "Victoria",
	"Nova Scotia" : "Halifax",
	"Alberta" : 'Edmonton',
	"Answer" : ['Ottawa']
}






lists = ["Ottawa", "Vic", "Hali", "Edmonton"]
pick = random.choice(list)
check = 0
while check != 3 :
	if pick in dict["Answer"] :
		print("Item was not added because its in the list already")
		pick = random.choice(lists)
	else:
		check = check + 1
		dict["Answer"].append(pick)
		pick = random.choice(lists)

print(dict["Answer"])


prov = { 
	"Yukon" : ["Whitehorse"], 
	"Northwest Territories" : ["Yellowknife"],
	"Nunavut" : ["Iqaluit"], 
	"British Comlumbia" : ["Victoria"], 
	"Alberta" : ["Edmonton"],
	"Saskatchewan" : ["Regina"],
	"Manitoba" : ["Winnipeg"],
	"Ontario" : ["Ottawa"],
	"Quebec" : ["Quebec City"],
	"New Brunswick" : ["Fredericton"],
	"Prince Edward Island" : ["Charlottetown"],
	"Nova Scotia" : ["Halifax"],
	"Newfoundland and Labrador" : ["Saint John's"]
}

keys = list(prov.keys())
random.shuffle(keys)

ShuffledProv = dict()

for key in keys:
	ShuffledProv.update({key: prov[key]})

print("\nDic after shuffling")
print(ShuffledProv)
