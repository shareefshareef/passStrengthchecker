import random,string,re,os
from passwordDetection2 import DetectPassword
from getpass import getpass
import hashlib

class L1():

    existing_usernames = set()
    '''function that return unique usernames'''
    def generate_unique_username(self,first, last, middle=''):
        if middle:
            first = first.strip()
            last = last.strip()
            middle = middle.strip()
            while True:
                patterns = [
                    f"{first}{random.randint(10,99)}",
                    f"{first[0]}{last}{random.randint(100,999)}",
                    f"{first}{middle[0]}{last}",
                    f"{first}_{last}",
                    f"{last}{random.choice(string.ascii_letters)}{random.randint(10,99)}",
                    f"{first[:3]}{last[:3]}{random.randint(1000,9999)}"
                        ]
                username = random.choice(patterns).lower()
            
                if username not in self.existing_usernames:
                    self.existing_usernames.add(username)
                    return username
        else:
            first = first.strip()
            last = last.strip()
            while True:
                patterns = [
                    f"{first}{random.randint(10,99)}",
                    f"{first[0]}{last}{random.randint(100,999)}",
                    f"{first}_{last}",
                    f"{last}{random.choice(string.ascii_letters)}{random.randint(10,99)}",
                    f"{first[:3]}{last[:3]}{random.randint(1000,9999)}"
                        ]
                username = random.choice(patterns).lower()
            
                if username not in self.existing_usernames:
                    self.existing_usernames.add(username)
                    return username

    '''create usernames'''
    def generate_username(self,first, last,middle=''):
        if middle:
            patterns = [
            f"{first}{random.randint(10,99)}",
            f"{first[0]}{last}{random.randint(100,999)}",
            f"{first}{middle[0]}{last}",
            f"{first}_{last}",
            f"{last}{random.choice(string.ascii_letters)}{random.randint(10,99)}",
            f"{first[:3]}{last[:3]}{random.randint(1000,9999)}"
            ]
            return random.choice(patterns).lower()
        else:
            patterns = [
            f"{first}{random.randint(10,99)}",
            f"{first[0]}{last}{random.randint(100,999)}",
            f"{first}_{last}",
            f"{last}{random.choice(string.ascii_letters)}{random.randint(10,99)}",
            f"{first[:3]}{last[:3]}{random.randint(1000,9999)}"
            ]
            return random.choice(patterns).lower()
        
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
           
    def check_password_mistmatch(self,password,re_password):
        password = password.strip()
        re_password = re_password.strip()

        if password != re_password:
            print("password mismatch!".upper())
            while True:
                password = getpass("enter the password: ".upper()) #input("enter the password: ".upper())
                re_password = getpass("re-enter the password: ".upper()) #input("re-enter the password: ".upper())

                if password != re_password:
                    print("password mismatch!".upper())
                if password == re_password:
                    return password
        elif password == re_password:
            return password
                
    def password_re_setting_with_eligible_criteria(self):
        prompt = '''
        - password must be at least 8 characters long.
        - add at least one lower and upper letters.
        - add at least one digit.
        - add at least one special characters.  
                '''
        prompt += '\n'
        print(prompt)
        password = getpass("enter the password: ".upper())#input("enter the password: ".upper())
        return password
    
    def check_password_criteria(self,password):
        password_object = DetectPassword()
        password_object.strong_password_detection(password)
        if password_object:
            return True
        else:
            return False
        
    def check_email(self,email):
        email = email.strip()
        email_regex = DetectPassword().email_re
        try:
            pattern = re.compile(email_regex).search(email).group()
            return True
        except:
            return None
    def re_enter_email(self):
        prompt = '''enter a valid email'''.upper()
        prompt += '\n'
        print(prompt)
        email = input("enter your email: ".upper())
        return email
    
    def create_account(self,username,password,email,fullname):
        os.makedirs('Accounts',exist_ok=True)
        filepath = os.path.join(f'Accounts',f"{username}.txt")
        heading = fullname.center((len(fullname)*4),"=")
        with open(filepath,'w') as file:
            file.write(heading)
            file.write("\nusername: "+username)
            file.write("\npassword: "+self.hash_password(password)+'\n')
            file.write("email: "+email+'\n')
        print(f"Account created with the username({username}) password({password}).")
    
    def email_exists(self,email=''):
        username_regex = r'username:\s*([a-zA-Z0-9_]+)'
        email_regex = DetectPassword().email_re
        for user in os.listdir('Accounts'):
            with open(f"Accounts\{user}") as file:
                file_content = file.read()
                try:
                    femail = re.compile(email_regex).search(file_content).group()
                    username = re.compile(username_regex).search(file_content).group(1)
                    if email == femail:
                        user_data = {
                            'username':username,
                            'email':email,
                            'status':True
                        }
                        return user_data
                except Exception as e:
                    return False

    def proceed_to_create_account_or_not(self,prompt,first_name,last_name,email,password,middle_name=''):
        '''this ask whether to create account or not'''
        if prompt.lower() == 'y':
            if middle_name:
                full_name = first_name + ' ' + middle_name + ' ' + last_name
                username = self.generate_unique_username(first=first_name,last=last_name,middle=middle_name)

                result = self.email_exists(email=email)
                if not result:
                    self.create_account(username=username,password=password,email=email,fullname=full_name)
                else:
                    print(f"email already exists with the username({result['username']})")
            else:
                full_name = first_name + ' ' + last_name
                username = self.generate_unique_username(first=first_name,last=last_name)
                
                result = self.email_exists(email=email)
                if not result:
                    self.create_account(username=username,password=password,email=email,fullname=full_name)
                else:
                    print(f"email already exists with username({result['username']})")     
        else:
            print("No account created.")
                  
    def Register(self):
        # print("ACCOUNT REGISTRATION".center(40, '='))
        first_name = input("enter your first_name: ".upper())
        last_name = input('enter your last_name: '.upper())
        middle_name = input("enter your middle name(optional): ".upper())
        email = input("Enter your email: ".upper())

        '''this conditions check whether the emails is valid or not'''
        if self.check_email(email=email):
            pass
        else:
            while True:
                re_check_email = self.re_enter_email()
                if self.check_email(re_check_email):
                    break


        password = getpass("enter your password: ".upper())  
        #input("Enter your password: ".upper())
        re_password = getpass("re-enter your password: ".upper()) #input("re-enter your password: ".upper())

        '''this conditions check the passwords'''
        password = self.check_password_mistmatch(password,re_password)

        if not self.check_password_criteria(password):
            while True:
                password = self.password_re_setting_with_eligible_criteria()
                if self.check_password_criteria(password):
                    break


        prompt = input("Register this details[y|n]: ").upper()

        self.proceed_to_create_account_or_not(prompt=prompt,first_name=first_name,last_name=last_name,email=email,password=password,middle_name=middle_name)

        # print("END OF REGISTRATION".center(40, '='))

    def username_exists(self,username):
        if username in os.listdir("Accounts"):
            return True
        else:
            return False

    def authenticate_user(self,username,password):
        '''function authenticate user '''
        password = self.hash_password(password.strip())
        password_regex = r'password:\s*([a-zA-Z0-9@#$.!+-_=*<>,]+)'
        if self.username_exists(username=username+'.txt'):
            with open(f"Accounts\{username}.txt") as file:
                file_content = file.read()
                password_pattern = re.compile(password_regex).search(file_content).group(1)
                if password_pattern == password:
                    user_status = {
                        'username':username,
                        'password':password,
                        'status':True
                    }
                    return user_status
                else:
                    return False
                
    def re_try_password(self,username,password):
        wpassword = password.strip()
        prompt = 'password didnt match try again.'
        password_regex = r'password:\s*([a-zA-Z0-9@#$.!+-_=*<>,]+)'
        if self.username_exists(username=username+'.txt'):
            with open(f"Accounts\{username}.txt") as file:
                file_content = file.read()
                password_pattern = re.compile(password_regex).search(file_content).group(1)
                stored_password = password_pattern
                count = 3
                while True:
                    print(f"chances left {count}")
                    prompt+='\n'
                    
                    password = getpass("password: ".upper())
                    if password == stored_password:
                        print("Login successfull")
                        return True
                    if count == 1:
                        resforgot = input("forgot password?:[y|n] ".upper())
                        if resforgot.lower() == 'y':
                            self.forgot_password()
                            break
                        else:
                            print("TRY again later".upper())
                            break                        
                    count -= 1
                    print(prompt)
        else:
            return False       

                
    def login(self):
        username = input("username: ".upper())
        password = getpass("password: ".upper())

        result = self.authenticate_user(username=username,password=password)
        if result:
            print("login successfull.")
        else:
            print("WARNING: (password didnt match) ")
            self.re_try_password(username=username,password=password)

    def forgot_password(self):
        '''reset the password '''
        username = input("ENTER YOUR USERNAME: ").strip()
        filename = os.path.join("Accounts", username + '.txt')

        if self.username_exists(username=username + '.txt'):
            password = input("RESET PASSWORD: ").strip()
            re_enter_password = input("RE-ENTER PASSWORD: ").strip()

            if password == re_enter_password:
                # Read all lines
                with open(filename, "r") as file:
                    file_contents = file.readlines()

                # Write back, updating only the password line
                with open(filename, 'w') as file:
                    for line in file_contents:
                        if line.startswith("password:"):
                            file.write(f"password: {self.hash_password(password)}\n")
                        else:
                            file.write(line)

                print(" PASSWORD RESET SUCCESSFULLY")
            else:
                print(" PASSWORDS DIDN'T MATCH.")
        else:
            print(" USERNAME NOT FOUND.")


    def delete_account(self):
        while True:
            asking_user = input("do you want to delete your account[y|n]: ".title())
            if asking_user.lower() == 'y':
                pass
            elif asking_user.lower() == 'n':
                print("process terminated.".title())
            elif asking_user.lower() == 'q':
                break
            else:
                print("invalid input.".upper())
            ask_username = input('enter your username: '.title())

            confirmation = input(f"confirm want to delete the {ask_username} account[y\n]: ".upper())
            if confirmation.lower() == 'y':
                ask_username = ask_username.strip()
                if self.username_exists(username=ask_username+'.txt'):
                    print("To delete your account authenticate your password.")
                    password = input("password: ".upper())
                    res = self.authenticate_user(username=ask_username,password=password)
                    if res['status'] == True:
                        os.remove(f'Accounts\{ask_username.strip()}.txt')
                        print("Account Deleted.")
                        break
                else:
                    print("unable to delete this account")
                    break
            elif confirmation.lower() == 'n':
                print("process terminated.".title())
            elif asking_user.lower() == 'q':
                break
            else:
                print("process terminated.".title())





obj = L1()


obj.login()
"""
create accounts folder , 
in the folder username txt file with password 
when loogin search the username in the accounts folder then check password from it ,

add feature when register check the database if already email or username is found or not. 

before that first perfect the registration forum first 
"""

        