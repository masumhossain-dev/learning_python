userName = input('What is your name?')
userAge = input('and How much your age?')
txt1 = 'Hello Mr. {}, \b Your age is {}.'.format(userName, userAge)
#another procedure
txt2 = 'Hello Mr. {userName}, \b Your age is {userAge}.'.format(userName = userName, userAge = userAge)

print(txt1)
print(txt2)