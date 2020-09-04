email = input ("Please enter your E-Mail : ").strip()

#For username of the email

user_name = email[:email.index("@")]

#For domain of the email such as : yahoo.com,email.com,etc..

domain_user = email[email.index("@")+1:]

#Putting the value of user_name and domain_user
output = ("Your username is '{}' and your domain name is '{}'").format(user_name,domain_user)

print (output)