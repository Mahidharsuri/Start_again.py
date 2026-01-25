username = input("Enter a username :")


while True:
    if len(username) > 12:
        print("You're username can't be more than 12 characters ")

    elif not username.find(" ") == -1:  
        print("You're username can't contain spaces")

    elif not username.isalpha():
        print("You're username can't contain numbers ")

    else:

        print(f" Welcome {username}")
        break
