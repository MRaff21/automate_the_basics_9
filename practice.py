import random


dict = {
	"Ontario" : ["Ottawa", "more", "here", "fun"],
	"BC" : ["Ottawa", "more", "here", "fun"],
	"Nova Scotia" : ["Halifax", "more", "here", "fun"],
	"Alberta" : ["asdf", "more", "here", "fun"],
	"Yukon" : ["Place", "more", "here", "fun"]
}

x = dict.values()



#random.shuffle(dict["Answer"])


for key in dict:
	x = dict.get(key)
	
	random.shuffle(x)
#	print(x)

print(dict.values())
