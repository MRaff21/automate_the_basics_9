#!python3
#mcb.pyw

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to option.
#        py.exe mcb.pyw <keyword> - Loads option to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, clipboard
# https://python.plainenglish.io/shelve-saving-the-state-of-objects-in-python-bc96e2633226
# and this https://pymotw.com/2/shelve/
# look at this link here to help figure this out gonna figure out the sys and pyperclip first
# --- use this object to save output
#mcbShelf = shelve.open('/home/lab/Manfred/dumpFolder/mcb')
mcbShelf = shelve.open('/home/lab/Documents/dumpFolder/mcb')

# --- this combination will create a var that stores the current item ready on the clipboard

currentPaste = clipboard.paste()
print(currentPaste)

# --- this line would copy that same item back. So If you copy something else you can call spam and it will bring it
# back to the front of the clipboard (useful for later im sure)
#pyperclip.copy(spam)
test_dict = {}


#print('Number of arguments:', len(sys.argv), 'arguments')
print('Argument list:', str(sys.argv))
option = sys.argv[1]


if len(sys.argv) > 3:
    print('script failed cannot exceed 3 arguments')
else:

    if option == "save":
        keyword = sys.argv[2]
        print("Item will be saved")

        print("Keyword", keyword, "was saved for the key ")
        mcbShelf[keyword] = currentPaste
        print("Item that would have been saved is: " + currentPaste)
        #test_dict[keyword] = currentPaste

    elif option == "list":
        print("List all saved keys")
        for key in mcbShelf:
            print(key)

    else:
        print("loading")
        if sys.argv[1] in mcbShelf:
            print("Loading value to clipboard")
            pyperclip.copy(mcbShelf[sys.argv[1]])
            print(pyperclip.paste())

    mcbShelf.close()



#TODO: Save clipboard content.
#TODO: List keywords and load content
