
import random

from numba.cuda import popc

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


dict = {
	"Ontario" : "Ottawa",
	"BC" : "Victoria",
	"Nova Scotia" : "Halifax",
	"Alberta" : 'Edmonton',
	"Answer" : ['Ottawa']
}

#lists = ["Ottawa", "Vic", "Hali", "Edmonton"]
#pick = random.choice((4))
#check = 0
#while check != 3 :#
	#if pick in dict["Answer"] :
#		print("Item was not added because its in the list already")
#		pick = random.choice(lists)
#	else:
#		check = check + 1
#		dict["Answer"].append(pick)
#		pick = random.choice(lists)

#print(dict["Answer"])



#keys = list(prov.keys())
#andom.shuffle(keys)

#ShuffledProv = dict()

#for key in keys:
#	ShuffledProv.update({key: prov[key]})

#print("\nDic after shuffling")
#print(ShuffledProv)
city_list = ["Whitehorse", "Yellowknife", "Iqaluit", "Victoria", "Edmonton", "Regina", "Winnipeg", "Ottawa",
             "Quebec City", "Fredericton", "Charlottetown", "Halifax", "Saint John's"]

d = prov.copy()

# this method works but wont filter duplicates so figure that out and we can use this method to fix the problem
def populate_list(dict_here):

	for key in dict_here:
		result = []
	# puts the first value of the key into a list called result
		result.append((dict_here.get(key))[0])

		for i in range(3):
			pick = random.choice(city_list)
			for j in range(len(result)):
				if (pick == result[j]):
					pick = random.choice(city_list)
					print("here btw")
				else :
					result.append(pick)
					break
			else:
				result.append(pick)
		dict_here.update({key: result})
	return dict_here

populate_list(d)

print(prov)
print(d)