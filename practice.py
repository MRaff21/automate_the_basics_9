import random
import subprocess
import json
import pprint

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
testfile="try"
count = 1

for i in range(5):
	subprocess.run(["touch", "/home/manfred/Documents/dumpFolder/hello" + str(count) + ".txt"])
	count = count + 1
f = open("hello.txt", "a")

#print(dict.values())

subprocess.run(["touch", "hello.txt"])


x = pprint.pformat(dict)


print(x)



f.write(x)
f.close()

#subprocess.run(['cat', 'hello.txt'])

#f = open ("hello.txt", "r")
#print(f.read())

