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

import time
#1st step: Create and display an array
print ("\nTHIS PROGRAM IS ABOUT LISTING METHODS\n")
name = input ("What is your name? ")
print (f"\nHello \033[36m{name}!\033[0m This is the list for today:\n")
array = [4, 12, 16, 1, 9, 10, 23, 30, 51, 6]
print (array)
time.sleep (1)
#2nd step: Display the options for the user
print ("\n\033[93mMENU:\033[0m")
print ("\n\033[92m1\033[0m -> Add an Element")
print ("\033[92m2\033[0m -> Insert an Element")
print ("\033[92m3\033[0m -> Modify an Element")
print ("\033[92m4\033[0m -> Delete an Element")
print ("\033[92m5\033[0m -> Arrange in Ascending order")
print ("\033[92m6\033[0m -> Arrange in Descending order")
print ("\033[92m7\033[0m -> Get the sum of the list")
print ("\033[92m8\033[0m -> Get the length of the list")

def menuInput():
    while True:
        try:
            inputFunction = int(input ("\nWhat do you want to do? [Enter the corresponding number \033[92m(1-8)\033[0m from the MENU]: "))
            if inputFunction not in range (1, 9):
                print ("\n\033[91mSorry, you have entered an invalid input.\033[0m\nPlease enter 1 to 8 only.")
                continue
        except ValueError:
            print("\n\033[91mSorry, you have entered an invalid input.\033[0m\nPlease enter a number only.") 
            continue     
        else:       
#3rd step: Create the conditions for each option
            #First Option
            if int(inputFunction) == 1:
                print ("Chosen Function: Add an Element")
                addNumber = int(input("\nWhat number do you wish to add? "))
                array.append (addNumber)
                print(f"\nYour new list is \033[92m{array}\033[0m\n")
    #Second Option
            elif int(inputFunction) == 2:
                print ("Chosen Function: Insert an Element")
                insertNumber = int(input("\nWhat number do you want to insert? "))
                insertNumberIndex = int(input (f"\nYou have entered number {insertNumber}\n\nEnter the index you wish to insert this number: "))
                array.insert (insertNumberIndex, insertNumber)
                print(f"\nYour new list is \033[92m{array}\033[0m\n")
    #Third Option
            elif int(inputFunction) == 3:
                print ("Chosen Function: Modify an Element")
                modifyIndex = int(input("\nEnter the index you want to modify: "))
                modifyNumber = int(input("\nWhat number do you want to see in this index? "))
                array[modifyIndex] = modifyNumber
                print(f"\nYour new list is \033[92m{array}\033[0m\n")
    #Fourth Option
            elif int(inputFunction) == 4:
                print ("Chosen Function: Delete an Element")
                deleteIndex = int(input("\nEnter the index you want to delete: "))
                array.pop(deleteIndex)
                print(f"\nYour new list is \033[92m{array}\033[0m\n")
    #Fifth Option
            elif int(inputFunction) == 5:
                print ("Chosen Function: Arrange the list in Ascending order")
                array.sort()
                print(f"\nYour updated list is \033[92m{array}\033[0m\n")
    #Sixth Option
            elif int(inputFunction) == 6:
                print("Chosen Function: Arrange the list in Descending order")
                array.sort(reverse = True)
                print(f"\nYour updated list is \033[92m{array}\033[0m\n")
    #Seventh Option
            elif int(inputFunction) == 7:
                print("Chosen Function: Get the sum of the list")
                sumList = sum (array)
                print(f"\nThe sum of the list: {array} is \033[92m{sumList}\033[0m\n")
    #Eighth
            elif int (inputFunction) == 8:
                print("Chosen Function: Get the length of the list")
                length = len(array)
                print(f"\nThe length of the list: {array} is \033[92m{length}\033[0m\n")
        break

    print ("\033[94mThank you for using this program!\033[0m\n")

menuInput()