#String Polindrom
txt = "drefrd"
if txt == txt[::-1]:
    print("Yes it is polindrom!!")
else:
    print("It is not polindrom!!")

#Count how many times a character appears in a string.
txt = "dreammm"
print(txt.count("m"))
#Replace one word with another.
txt = txt.replace("mmm","tttt")
print(txt)
#Reverse a string.
txt = txt[::-1]
print(txt)
#count Uppercase letters 
