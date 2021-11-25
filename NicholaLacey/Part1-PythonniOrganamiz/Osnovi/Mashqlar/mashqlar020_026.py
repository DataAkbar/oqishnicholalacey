# 020

person = str(input("Iltimos ismingizni kiriting: "))
print(len(person), "--- Eee, Yashshang - Suvga kalla tashang :)")

# 021 

name = str(input("Boshda ismingizni kiriting: "))
lastname = str(input("Endi familiyangizni kiriting: "))

fullname = name + " " + lastname
print(fullname.title())

# 022 

name1 = str(input("Iltimos ismingizni kichik harf bn yozing: "))
lastname1 = str(input("Endi shunday tartibda familiyangizni yozing: "))

fullname1 = name1 + " " + lastname1 
print ( fullname1.title() )

# 023 

phrase = input("Enter the first line of a nursery rhyme: ")
length = len(phrase)
print("This has ", length, " letters in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
part = (phrase[start:end])
print(part)

# 024 

name = str(input("Ismingizni kiriting: "))
upper = name.upper()

print(upper)

# 025

name = str(input("Ismingizni kiriting: "))

if len(name) < 5:
    taklif = str(input("Familiyangizni kiriting: "))
    name22 = name + taklif
    print(taklif.upper())
else:
    print(name.lower())

# 026 

word = input("Iltimos oz ishingizni yozing: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + 'ay'
else:
    newword = word + "way"
print(newword.lower())

