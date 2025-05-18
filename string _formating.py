userName = input('What is your name?')
userAge = input('and How much your age?')
txt1 = 'Hello Mr. {}, \n Your age is {}.'.format(userName, userAge)
#another procedure
txt2 = 'Hello Mr. {userName}, \n Your age is {userAge}.'.format(userName = userName, userAge = userAge)
#another procedure
txt3 = f'Hello Mr. {userName},\n Your age is {userAge}.'

print(txt1)
print(txt2)
print(txt3)