import os

mockThis = input("What are we mocking today?\n")
uppercase = True
mocked = ""
for letter in mockThis:
    if letter.isalpha():
        if uppercase is False:
             letter = letter.upper()
             uppercase = True
        else:
             letter = letter.lower()
             uppercase = False
    mocked += letter
print(mocked)
os.system("pause")
