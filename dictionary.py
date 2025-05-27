data = {
    "Name" : "Masum Hossain",
    "ID" : 20245203028,
    "Intake" : 46,
    "Section" : 1,
    "Department" : "Computer Science and Engineering"
    }

for i in data.values():
    print(i)

print("----------------------")

for key, values in data.items():
    print(f"{key} is: {values}")