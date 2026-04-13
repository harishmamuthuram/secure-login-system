import hashlib
import os

# --- REGISTER ---
def register():
    username=input("Please enter your username: ")
    
    # check if username already exists in users.txt
    try:
        with open("users.txt","r") as f:
            for line in f:
                stored=line.strip().split(":")
                if stored[0]==username:
                    print("Username already taken. Try again.")
                    return
    except FileNotFoundError:
        pass
    
    password=input("Please enter your password: ")
    
    #generate salt + hash
    salt=os.urandom(16).hex()
    hashed=hashlib.sha256((password+salt).encode()).hexdigest()
    
    #save to users.txt
    with open("users.txt","a") as f:
        f.write(f"{username}:{salt}:{hashed}\n")
        
    print(f"Account created for {username}!")
    

# --- LOGIN ---
def login():
    username=input("Username: ")
    attempts=0
    while attempts<3:
        password=input("Password: ")
        found=False
        try:
            with open("users.txt","r") as f:
                for line in f:
                    stored=line.strip().split(":")
                    stored_username=stored[0]
                    stored_salt=stored[1]
                    stored_hash=stored[2]
                    
                    if stored_username==username:
                        found = True
                        attempt_hash = hashlib.sha256((password + stored_salt).encode()).hexdigest()
                         
                        if attempt_hash==stored_hash:
                             print("Login Successful!")
                             return
                        else:
                            attempts+=1
                            remaining=3-attempts
                            if remaining>0:
                                print(f"wrong password. {remaining} attmept(s) left")
                            break
        except FileNotFoundError:
            print("No users registered yet.")
            return
        if not found:
            print("Username not found.")
            return
    print("Account locked. Too many failed attempts.")
    
    
# --- MAIN MENU ---
def main():
    print("=== Secure Login System ===")
    choice = input("Type 'register' or 'login': ").strip().lower()
    
    if choice=="register":
        register()
    elif choice=="login":
        login()
    else:
        print("Invalid choice.")
        
main()
