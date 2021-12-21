#Email Slicer
email=input('Enter the Email ID')
username=email[0:email.index('@')]
domainname=email[email.index('@')+1:]
print(f'The user name is {username} \nThe domain name is {domainname}')
