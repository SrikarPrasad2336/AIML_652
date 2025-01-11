#Strings

#Find if the length of the string is even print as even
string="do what i say to the world"
for word in string.split():
    if len(word) %2==0:
        print(word)

# Find the length of the string if the length of the string is
# more than 3 print the first letter of the word output: w
print()
string="do what i say to the world"
for word in string.split():
    if len(word) >3 :
        print(word[0])
print()

#convert string into list
string="do what i say to the world"
"""for word in string.split():
    if len(word) %2==0:
        print(word)
    if len(word) >3 :
        print(word[0])"""
a=list(string.split())
print(a)
print()

##convert string into list in such a way that only 5 letter 
#words should be there in the code
#['going','start]
str="session is going to start"
res=[i for i in str.split() if len(i)==5]
print(res)
print()

#Reverse of a strings
print(string[::-1])
print()

#Find a code to print string in reverse by using negative indexing
#Using for loop to print multiple of 3 it has to print "bizz"
#multiples of 5 it has to print "bigg" and if it is multiple of 3 and multiple of 5
#we should get the output as "bigg buzz"

for i in range(20):
    if i%3==0:
        print(i,"bizz")
    elif i%5==0:
        print(i,"bigg")
    elif i%3==0 and i%5==0:
        print(i,"bigg buzz")
    
print()

string="Life is beautiful"
res=string[::-1]
print(res)
string[5].upper()    

print()


string="Life is beautiful"
res=string[::-1]
print(res)
string[9].lower()