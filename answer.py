#creating a function that checks whatever string entered sets all letters to lower case for the purpose of comparing
#and replaces all white spaces with non so it doesnt confuse blanks as unique characters being repeated

def Check(string):
    string=string.replace(" ","").lower()

    x=0

#for loop that checks each character in the string
    #count is telling it to search for the substring i
    #if i exist return the int for how many times it does
    for i in string:
        count = string.count(i)
        if count >1:
            x += count

 #if it does return any matches
    if x >0:
        print ("Not all unique characters")
   #if it doesn't
    else:
        print ("All unique characters")


Check("ljikhnb   ")