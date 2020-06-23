#Python Dictionaries
#Objective 1 is Creating a dictionary

print ("Creating a Dictionary")

#Creating a variable that holds a dictionary
f = {1: "Godfrey", 2 : "Lynda", 3 : "Ikran", 4 : "John", 5 : "David"}

#Converting Dictionaries to strings
print ("\nOur Dictinary contains of the following" + str(f))


#method two for creating a dictionary

d = dict({"Godfrey" : "Esther", "John" : "Mary", "Joel" : "Alivista"})


print ("\nDictionary Values are " + str(d))

#Nsted Dictionaries
#A representation of a dictionary inside a dictionary

h = {1:{"S": "Data Comm",
        "S": "Programming"}, 
     2: {"J": "Ethics",
         "J" : "Multimedia"},
     3: {"M" : "Database",
         "M" : "N/A"}, 
     4 : {"SOL" : "Computer Systems"}}

print (h)

#An empty string
j = dict()

#Adding values to the empty string
j['Name'] = 'Godfrey'

j['Age'] = '21'

j['School'] = 'Zetech'


print(j)

#Accessing elemets in a dictionary

print(h[1])


#Deleting a dictionary



print(j.popitem())

#you can use clear also

j.clear()

print(j)

