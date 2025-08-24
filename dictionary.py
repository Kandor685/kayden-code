thisdict = { 
            'Brand' : 'Ford',
            'Model' : "Mustang",
            "Year" : 1964
}

print ("thisdict")
print (thisdict)

#copy dictionary
print ("###################################################")
thisdict=thisdict.copy()
print("thisdict")
print(thisdict)

print ("###################################################")
#another way to copy a dictionary 
thisdict2 = dict(thisdict)
print("thisdict2")
print(thisdict2)