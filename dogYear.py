#Intent of this script is to learn IF and ELIF conditions
#Wrote on Python 2.7.5

'''It's a generally accepted belief, to assume that one year in the life of a dog corresponds to seven years 
in the life of a human being. But apparently there are other more subtle methods to calculate this haunting 
problem, haunting at least for some dog owners. 

Another subtler - and some think a preciser method - works like this:

A one year old dog roughly corresponds to a fourteen year old child
A dog who is two years old corresponds to a 22 year old human
Every further dog year corresponds to five human years'''

age = int(input("Age of the dog: "))
print " "
if age < 1:
	print("This can hardly be true!")
elif age == 1:
	print("about 14 human years")
elif age == 2:
	print("about 22 human years")
elif age > 2:
	human = 22 + (age -2)*5
	print "Human years: ",human

###
raw_input('press Return>')

#Comments Added
