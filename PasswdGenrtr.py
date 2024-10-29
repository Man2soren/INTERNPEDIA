import secrets # used to generate strong random numbers 
import string

# function to generate a random password

def make_passwd(length,uppercase=True,lowercase = True,digits=True,symbols=True) :
    # make sure at least one character type is entered
    if not(uppercase or lowercase or digits or symbols) :
        raise ValueError("Select at least one")
    
    passwd = ""
    if uppercase :
        passwd += string.ascii_uppercase
    if lowercase :
        passwd += string.ascii_lowercase
    if digits :
        passwd += string.digits
    if symbols :
        passwd += string.punctuation

    if not passwd :
        raise ValueError("String is empty.")
    
    #generating the password using secrets for randomness
    password = ''.join(secrets.choice(passwd) for _ in range(length))
    return password

# Function for generating multiple passwords
def make_multi_passwd(count,length,uppercase=True,lowercase = True,digits=True,symbols=True) :
    return [make_passwd(length,uppercase,lowercase,digits,symbols) for _ in range(count)]

# take the user input
def user_input() :
    try:
        count = int(input("Numbers of password :"))
        length = int(input("Password Length :"))

        uppercase = input("include uppercase letters ?(y/n) :").strip().lower() == 'y'
        lowercase = input("include lowercase letters ?(y/n) :").strip().lower() == 'y'
        digits = input("include digits ?(y/n) :").strip().lower() == 'y'
        symbols = input("include symbols ?(y/n) :").strip().lower() == 'y'


        passwords = make_multi_passwd(count,length,uppercase,lowercase,digits,symbols)

        #display password
        for i, password in enumerate(passwords,1) :
            print(f"Password {i}: {password}")

    except ValueError as err:
        print(f"error : {err}")
    except Exception as exc:
        print(f"Unexpected error occured :{exc}")

if __name__ == "__main__":
    user_input()
    
