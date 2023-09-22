import random #importing module to generate random numbers or do random operations
import string #importing module that provides various constants and functions related to string manipulation. 

while True:

    def store_password(store): #creating a function to store the randomly generated passwords in a txt file so we can view all the passwords

        with open("password.txt", "a") as f:
            f.write(f"Password: {store}\n")

    def generate_password(min_len, numbers = True, special_char = True):  

        letters = string.ascii_letters  #assigning a variable that stores a string containing all ASCII letters
        digits = string.digits  #assigning a variable that stores a string containing all ASCII digits
        special = string.punctuation  #assigning a variable that stores a string containing all ASCII punctuation characters

        characters = letters #doing this because in our randomly generated password, there is always letters
        
        if numbers:  #if we want to include a number in our randomly generated password, then add numbers to the password 
            characters += digits

        if special_char:  #if we want to include special characters in our randomly generated password
            characters += special

        pwd = ""
        meets_criteria = False
        has_num = False
        has_special  =False

        while not meets_criteria or len(pwd) < min_len:

            new_char = random.choice(characters)  #randomly generating characters from the variable characters
            pwd += new_char # adding that to our empty pwd string

            if new_char in digits:
                has_num = True

            elif new_char in special:
                has_special  = True

            meets_criteria = True

            if numbers:
                meets_criteria = has_num

            if special_char:
                meets_criteria = has_special

        return pwd
    

    minimum = int(input("What would you like the minimum length of the password to be?: "))  #taking user input for the minimum length of password and converting it to int
    num = input("Would you like to include numbers in your password? (y/n): ").lower() == "y"  #asking the user if they want to include a number and if they press "y", it will return a value of True since we assigned it in our function
    spec_char = input("Would you like to include special characters in your password? (y/n): ").lower() == "y"  #asking the user if they want to include special characters and if they press "y", it will return a value of True since we assigned it in our function


    password = generate_password(minimum, num, spec_char)  #calling the generate_password function
    store_password(password)  #calling the store_password function 

