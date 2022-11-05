#Seatwork in DSA

#Write a python program that do the following:

#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array

#Note: 
#- The program has an array variable containing 10 random numbers
#- You may add other options and features
#- Your program should be uploaded to github before 1:30pm
#- Record a demo presenting your program
#- Send the demo directly to my messenger

#Example Output:

#Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
#Menu:
# 1 -> Add an element
# 2 -> Insert an element
# 3 -> Modify an element
# 4 -> Delete an element
# 5 -> Arrange in ascending order
# 6 -> Arrange in descending order
#What do you want to do? (1-6): 4
#Enter the index you want to delete: 3
#The element has been deleted
#This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

#1st step: Create and display an array
array = [4, 12, 16, 1, 9, 10, 23, 30, 51, 6]
print (array)
#2nd step: Display the options for the user
print ("\nMENU:")
print ("\n1 -> Add an Element")
print ("2 -> Insert an Element")
print ("3 -> Modify an Element")
print ("4 -> Delete an Element")
print ("5 -> Arrange in Ascending order")
print ("6 -> Arrange in Descending order")
print ("7 -> Get the sum of the list")

inputFunction = input ("\nWhat do you want to do? [Enter the corresponding number (1-7) from the MENU.]: ")

#3rd step: Create the conditions for each option
    #First Option
if int(inputFunction) == 1:
    addNumber = int(input("\nWhat number do you wish to add? "))
    array.append (addNumber)
    #Second Option
elif int(inputFunction) == 2:
    insertNumber = int(input("\nWhat number do you want to insert? "))
    insertNumberIndex = int(input (f"\nYou entered number {insertNumber}\n\nEnter the index you wish to insert this number: "))
    array.insert (insertNumberIndex, insertNumber)
    #Third Option
elif int(inputFunction) == 3:
    modifyIndex = int(input("\nEnter the index you want to modify: "))
    modifyNumber = int(input("\nWhat number do you want to see in this index? "))
    array[modifyIndex] = modifyNumber
    #Fourth Option
elif int(inputFunction) == 4:
    deleteIndex = int(input("\nEnter the index you want to delete "))
    array.pop(deleteIndex)
    #Fifth Option
    #Sixth Option
    #Seventh Option

#4th step: Display the new Array
print(f"\nYour new list is {array}\n")

