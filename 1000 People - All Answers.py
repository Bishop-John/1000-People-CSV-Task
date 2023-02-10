import csv, datetime
    
print ("Welcome to the 1000 people program. ")

print ("Press 1 to print the first 10 rows. ")# DONE
print ("Press 2 to sort the list alphabetically by first name and show the first 10. ")#DONE
print ("Press 3 to see the first 10 female names. ")#DONE
print ("Press 4 to see the number of female names in the list ")#DONE
print ("Press 5 to see only the first names that appear more than once. ")#DONE
print ("Press 6 to see the number of people in the list who are older than 30. ")#DONE
print ("Press 7 to see the number of people in the list who were born in February or September. ")#DONE
print ("Press 8 to print out “Happy birthday” and the name of anyone who’s birthday is today, and include their age. ")# DONE
print ("Press 9 to see the full name and email of anyone who has an ebay email address (.com or .co.uk)")# DONE

userChoice = input("> ")

if userChoice == "1":
    rowsShown = 0
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            print (row['First Name'], row['Surname'], row['Email Address'], row['Gender'], row['D.O.B'])
            rowsShown = rowsShown + 1
            if rowsShown == 10:
                break

elif userChoice == "2":
    allNames = []
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            allNames.append([row['First Name'], row['Surname']])
        allNames.sort()
        for i in range(10):
            print (allNames[i])

elif userChoice == "3":
    femalesFound = 0
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if row['Gender'] == "Female":
                print (row['First Name'], row['Surname'])
                femalesFound = femalesFound + 1
            if femalesFound == 10:
                break
          
elif userChoice == "4":
    allFemaleNames = []
    allUniqueFemaleNames = []
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if row['Gender'] == "Female":
                allFemaleNames.append(row['First Name'])

    for i in allFemaleNames:
        if i not in allUniqueFemaleNames:
            allUniqueFemaleNames.append(i)

    print (len(allFemaleNames))
    print (len(allUniqueFemaleNames))

elif userChoice == "5":
    allNames = []
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            allNames.append(row['First Name'])
    duplicateNames = set([x for x in allNames if allNames.count(x) > 1])
    print (duplicateNames)
    
elif userChoice == "6":
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if int(row['D.O.B'][-2:]) < 87:
                print (row['First Name'], row['Surname'], "is over 30.")

elif userChoice == "7":
    febDOB = 0
    septDOB = 0
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if row['D.O.B'][3:5] == "02":
                febDOB = febDOB + 1
            if row['D.O.B'][4] == "9":
                septDOB = septDOB + 1

    print (febDOB, "people have their birthdays in February.")             
    print (septDOB, "people have their birthdays in September.")


elif userChoice == "8":
    todaysDate = str(datetime.datetime.now())
    print (todaysDate)
    formattedDate = todaysDate[8:10], "/", todaysDate[5:7]
    formattedDate = "".join(formattedDate)
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if row['D.O.B'][0:5] == formattedDate:
                print ("Happy birthday to ", row['First Name'], row['Surname'])
    
    
elif userChoice == "9":
    with open('1000people.csv') as peopleFile:
        fileReader = csv.DictReader(peopleFile)
        for row in fileReader:
            if "ebay" in row['Email Address']:
                print (row['Email Address'], "belongs to", row['First Name'], row['Surname'])
