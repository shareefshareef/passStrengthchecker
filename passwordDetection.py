import re

class DetectPassword():

    def __init__(self,pattern=r'[a-zA-Z0-9!@#$%^&()_+<>/]+'):
        self.pattern = pattern

    def contains_lower_and_upper(self,password):
        '''checks if password contains both lower and uppercase'''
        lower = any(l.islower() for l in password)
        upper = any(l.isupper() for l in password)
        return lower and upper
    
    def contains_lower(self,password):
        '''checks if password contains lower case '''
        return any(l.islower() for l in password)
    
    def contains_upper(self,password):
        '''checks if password contains upper case'''
        return any(l.isupper() for l in password)

    def contains_digit(self,password):
        '''checks whether if password contains digits'''
        return any(n.isdigit() for n in password)
    
    def contains_special_characters(self,password):
        '''checks whether if password contains special characters'''
        special_characters = set("!@#$%^&*()_+{}[]?<>.,;':=")
        return any(spc in special_characters for spc in password)
    
    def strong_password_detection(self,password):
        '''checks if the password is strong or weak or medium'''
        password_re = re.compile(self.pattern)
        myatch = password_re.search(password)

        if not myatch:
            print('NO PASSWORD DETECTED.')
        else:
            password = myatch.group()
            '''new string with added asterisk'''
            resubbed_password = re.compile(r'\w+.*').sub(f"{password[0]}{'*'*(len(password)-1)}",password)
            
            if len(password) < 8:
                if password == '12345' or password == '1234' or password == 'abcd1234' or password == 'abcd':
                    print(f'PLEASE DO NOT USE THIS KIND OF PASSWORD')
                return f'({resubbed_password}) PASSWORD STATUS: WEAK - must be at least 8 characters long.'
            elif not self.contains_lower(password):
                return f'({resubbed_password}) PASSWORD STATUS: MEDIUM - add lower letters.'
            elif not self.contains_upper(password):
                return f'({resubbed_password}) PASSWORD STATUS: MEDIUM - add upper letters.'
            elif not self.contains_digit(password):
                return f'({resubbed_password}) PASSWORD STATUS: MEDIUM - add at least one digit.'
            elif not self.contains_special_characters(password):
                return f'({resubbed_password}) PASSWORD STATUS: MEDIUM - add at least one special characters.'
            else:
                return f'({resubbed_password}) PASSWORD STATUS: STRONG - VALID PASSWORD'

    def test_password_with_dummytext(self):
        '''checks the strong_password_detection() function with dummy passwords'''
        dummy_passwords = {
                "WEAK": [
                    "abc",           
                    "1234567",       
                    "ABC",           
                    "aB3!",          
                    "xyz123",       
                            ],
                "MEDIUM": [
                    "onlylowercase",    
                    "ONLYUPPERCASE",    
                    "MixCaseOnly",       
                    "Pass1234",          
                    "NoDigits@",        
                    "Test@Case",        
                            ],
                "STRONG": [
                    "Strong@123",
                    "TestPass#456",
                    "Abc@2024!",
                    "My_Pass9$",
                    "Secure#99",
                    "Welcome#1",
                    "Xyz@890Z"
                            ]
                            }
        for k,v in dummy_passwords.items():
            print(f"----{k} PASSWORDS ----")
            for pwd in v:
                print(self.strong_password_detection(pwd))
            print()









