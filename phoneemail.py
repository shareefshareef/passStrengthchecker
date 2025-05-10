import pyperclip,re

'''
This Python script is designed to extract phone numbers and email addresses from the clipboard text. It uses regular expressions to match the phone numbers and emails and formats them accordingly. Once found, the extracted data is copied back to the clipboard and printed on the console
'''
# phone regex
phone_re = re.compile(r'''(
        (\d{3}|\(\d{3}\))? #area code
        (\s|-|\.) #seprator
        (\d{3})   #first three digits
        (\s|-|\.) #separotor
        (\d{4})   #last four digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))? #extension
        )''',re.VERBOSE)

#email regex
email_re = re.compile(r'''(
            [a-zA-Z0-9._%+-]+ #username
            @ # @symbol
            [a-zA-Z0-9.-]+ #domain name
            (\.[a-zA-Z]{2,4}) #dot-something           
            )''',re.VERBOSE)


text = str(pyperclip.paste())

matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num) 
for groups in email_re.findall(text):
    matches.append(groups[0]) 

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("copied to clipboard")
    print("\n".join(matches))
else:
    print('no phone number or email address found.')
