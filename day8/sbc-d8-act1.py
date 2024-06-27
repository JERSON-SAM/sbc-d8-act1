''' A Global Dictionary to store user credentials'''
me = {}

def register():
    """Getting username and password. Credentials are saved to login.txt and also stored in 'me' dictionary."""
    username = input("Enter Ang Username: ")
    password = input("Enter Ang Password: ")
    file = open("Login.txt","a")
    file.write (f" {username}, {password}\n" )
    file.close()
    if username in me:
        print("Username already exists.")
    else:
        me[username] = password
        print("User registered successfully.")


def login():
    """Log in an existing user by checking the username and password against the 'me' dictionary."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if the username exists and the password matches
    if username not in me:
        print("Username not found.")
    elif me[username] == password:
        print("Login successful.")
    else:
        print("Incorrect password.")

def change_password():
    """Change the password for an existing user by verifying the old password. The new password is saved to the 'login.txt' file and updated in the 'me' dictionary."""
    username = input("Enter Ang Username: ")
    old_password = input("Enter old password: ")
    new_password = input("Enter new password: ")

    # Check if the username exists and the old password matches
    if username in me and me[username] == old_password:
        # Update the password in the dictionary
        me[username] = new_password
        
        # Write all user credentials to the file (overwrite the file)
        with open("login.txt", "w") as file:
            for user, pwd in me.items():
                file.write(f"{user},{pwd}\n")
        
        print("Password changed successfully.")
    else:
        print("Username not found or incorrect old password.")

def main():
    """Main function to display a menu and handle user input for different operations."""
    while True:
        print("\nPili Ka!:")
        print("1. Register")
        print("2. Log In")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
