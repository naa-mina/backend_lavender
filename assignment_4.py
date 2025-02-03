#Ask user for personal details
user_name = input("What is your name? : ")
user_age = input("How old are you? : ")
user_colour = input("What is your favorite color? : ")
friends_name = input("What are the names of your friends? : ")

#put user details in a dictionary
user = {"name":user_name, "age":user_age, "favorite color": user_colour}

#store users friends in a list
friends_name = friends_name.split(",")

#using empty print to create a new empty line
print()
#print of details so user can verify
print(f"user details : {user}")

print()
#This would allow user to determine if they want to update their details
print("To update details type : Yes")
update_details = input("Do you want to update your details ? : ").capitalize()

#Doing this so user can update their details
if update_details == "Yes": 
    new_age = input("What is your new age? : ")
    new_colour = input("What is your new favorite colour? : ")

    user["age"] = new_age
    user["favorite color"] = new_colour
    print()
    print(f"updated_user_details: {user}")
    print(f"list of friends : {friends_name}")

else :
    print(f"list of friends : {friends_name}")

#Allow user to remove a friend from the list
print()
print("To remove a friend from the list, type the person's name")
remove_friend = input("Which friend do you want to remove from the list? : ")

#adding a try clause incase user enters name not on list
try:
    friends_name.remove(remove_friend)
except ValueError:
    print("Sorry the name entered is not on list")
print()
print(f"updated friend's list : {friends_name}")
print(f"updated user details: {user} ")
