#people's list
people = ['John','Jane','Michael']

#checks for given letter in a list
def checkForChar(input_list,letter):
    new_list = []
    for person in people:
        if person[0] == letter:
            #add the person with first letter to the list
            new_list.append(person)
    
    return new_list

result_list = checkForChar(people,'M')
print(result_list)