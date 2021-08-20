from pathlib import Path
import os

###########################################
#myFiles = ['accounts.txt', 'details.csv', 'invites.docx']
#for filename in myFiles:
#	print(Path(r'/home/manfred/Documents/',filename))
###########################################
	
# this wont show unless your in the interactive shell
# The point of this is to show that you can concatinate these paths with the / instead of with + or .join method out puts will be tabbed forward

#########################################
#Path('spam')/'bacon'/'eggs'
#	PosixPath('spam/bacon/eggs')
#Path('spam')/Path('bacon/eggs')
#	PosixPath('spam/bacon/eggs')
#Path('spam')/Path('bacon','eggs')
#	PosixPath('spam/bacon/eggs')
#########################################

# This section is just showing how you dont really want or need to use the + or .join operator or it can cause unintended errors where you'll get paths looking like this 
# /home/lab//spam
# Im almost positive I had this problem at work with my script...might be worth taking a look at it again. 


# -------------------------------------- # 
#homeFolder = r'/home/manfred/'
#subFolder = 'spam'
#homeFolder + '/' + subFolder
# -------------------------------------- #

# This will check what ever your current working directory is... kinda wish I had this for the last assignment -_-. Regardless note that we can change the dir in the script here and it will apply again ...check to see if it actually moves us in the shell. I dont believe it will -> it did not

# ------------------------- #
#print(Path.cwd())
#os.chdir('/etc/')
#print(Path.cwd())
# ------------------------- #


# Honestly more methods they go through...honestly seems like this is pretty easy stuff to just look up online. Gonna give it two more chapters then go from there.
# --------------------------# 
#p = Path('/home/lab/')
#p.anchor
#'/'
#p.parent
#PosixPath('/home')
#p.name
#'lab'
# p.stem
#'lab'
#p.suffix
#''
#p.drive
#''

# ---------------------- #

# Lets start with some of the questions on and see if I can answer them I think I should be fine...if not just go back through the chapter.

# https://automatetheboringstuff.com/2e/chapter9/






