string=input("enter a string")
vowels=0
consonants=0
for i in string:
    if i. isalpha():
        if i in "aeiouAEIOU":
            vowels=vowels+1
        else:
            consonants=consonants+1
print("number of vowels",vowels)
print("number of consonants",consonants)                