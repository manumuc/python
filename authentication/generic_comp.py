# python3
# idea from https://automatetheboringstuff.com/chapter0/
# compares an input with the content of a file
# usage: 
#   generic_comp
# no command line arguments
# instead of clipboard if there is no agument the clipboard will be used
# 
# Constants
c_pwd_folder = '.'
c_pwd_fn: 'SecretPasswordFile.txt'

o_password_file = open(c_pwd_folder + c_pwd_fn)
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
   print('Access granted')
   if typedPassword == '12345':
   print('That password is one that an idiot puts on their luggage.')
   else:
      print('Access denied')
