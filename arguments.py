def multiValue(*args):
    #print(sum(args))
    total = 0
    for num in args:
        total += num
    
    return total
        

print(multiValue(1, 21, 12))

#key arguments
def keyArgs(f_name, l_name, age):
    pText = f"My name is {f_name} {l_name}. I'm {age} years old."
    return pText

print(keyArgs(f_name= "Masum", age= 25, l_name= "Hossain"))

#Arbitary keyword arguments
def arbitaryArgs(**data):
    pText = f"My name is {data["f_name"]} {data["l_name"]}. I'm {data["age"]} years old. I get {data["marks"]} marks in programming. And I leave in {data["address"]}"
    return pText

print(arbitaryArgs(age= 25, f_name = "Masum", address = "Dhaka, Bangladesh", marks = 97, l_name = "Hossain"))