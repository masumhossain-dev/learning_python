a = 10
print(type(a))

uni = 'Bangladesh University of Business and Technology'
print(len(uni))


#String indexing

#print last index on a string(long method)
print(uni[len(uni)-1])

#print last index on a string(short method)
print(uni[-1]) #it also called minus(-) indexing. if i pass -2 as a index number, it will print second last number of the string.

#string methods
name = 'masum hossian'
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.center(20))
print(name.count('h')) #and so on...