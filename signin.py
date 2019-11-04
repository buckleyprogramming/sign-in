from datetime import date


d = date.today()

people = []
name = ""
while(name != "overpass"):
    name = raw_input("Enter your name: ")
    people.append(name)

print("attendence has been taken")
people.remove("overpass")
print(people)

f = open(str(d) + ".txt","w+")

for i in people:
     f.write(i + "\n")