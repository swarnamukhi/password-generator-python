from password_core import password_generator
import sys
import string




print("welcome to Password Generator")
def password_length():
    while True:
        
        user_input = input("please enter the length of the password you desire or type 'exit' to quit").strip()
        if user_input.lower() in ("exit","quit","q"):
            print("Good Bye....")
            sys.exit()

        try:    
            length = int(user_input)
            if length > 0:
               return length
            else: 
                print("passowrd must be greater than zero")
        except ValueError:
                print("invalid input please enter valid number")   
                
                
def char_pref():
    while True:
        pool = ""
        chosen_set = []
        upper_case = input("Do you want to include the upper case letter in password type 'yes' or 'No'").strip().lower()
        if upper_case =='yes':
           pool+=string.ascii_uppercase
           chosen_set.append(string.ascii_uppercase)

        lower_case = input("Do you want to include the lower case letter in password type 'yes' or 'No'").strip().lower()
        if lower_case == 'yes':
            pool += string.ascii_lowercase
            chosen_set.append(string.ascii_lowercase)

        user_number = input("Do ypu want to include the numbers from 0-9 type 'yes' or 'No'").strip().lower()
        if user_number == 'yes':
            pool+= string.digits
            chosen_set.append(string.digits)

        spl_char    = input("Do you want to include special charcters @ # $ % )? type 'yes' or 'No'").strip().lower()
        if spl_char == 'yes':
            pool+= string.punctuation
            chosen_set.append(string.punctuation)

        if pool =="":
           print("you did not selected any ...")  
           continue
        else:
            break
    return pool,chosen_set    





if __name__ == "__main__":
    length = password_length()
    pool, chosen_set = char_pref()
    password = password_generator(length, pool, chosen_set)
    print("\n✅ Your generated password:", password)
 


    


                    

               
                
