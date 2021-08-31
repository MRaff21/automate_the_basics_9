# automate_the_boring_stuff_chapter_9
Automate the boring stuff chapter 9

Project: Generating Random Quiz Files - automate_project.py

This project was challenging as it helped firm up ideas of dictionaries as well as loops. As a whole this project was rather challenging but was worth doing. It could be updated to feed it information and questions instead of having to edit the source code. I might use this eventually for Sec+ quiz practice. Comments are in the file

Project: Updated Multi-Clipboard - mcb.py

This program has three inputs it can take. 

python3 mcb.py <option> <keyword>
python3 mcb.py <option>
python3 mcb.py <keyword>
 
  The point of this script is to save items on your clipboard in a database for later use. If I have ("Hello world") on my clipboard and I want it saved for later use I can use this script to save the clipboard to a keyword, then recall that keyword later to make the saved text part of my clipboard again.
  
  Options can only be between list or save, there is a delete but its not been implemented. The list function will list all keywords that have been saved to the database. While the save option will save new data to the database. If using list you CANNOT have a keyword attatched to it, while the save function MUST have a keyword to work correctly. 
  
python3 mcb.py save <keyword>  -> will take what ever keyword you use and place it into a database for later use
python3 mcb.py list -> Will list all keywords currently saved in the database
python3 mcb.py <keyword> -> Will load the data saved to keyword. 
  
  Known bug: When recalling data I can paste the data inside the program but it won't be pasted on your clipboard outside the program. The expections to me was it should be able to recall data and paste it on the clipboard to be used outside of this program. This might be the intention of the project but it was unclear in the instructions. This is something to come back to eventually and see if I can fix it. 
