import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import rotate_axes

myfile= open("data/art_coverage_by_country_clean.csv")

# print(myfile.read())
num_of_lines = sum(1 for line in myfile)
myfile.seek(0)
sentence = myfile.readline()
mylist= sentence.split(",")
print(mylist[0:3])

# myfile.seek(0)
countries= []
africa= []
South_East_Asia = []
Europe = []
Americas = []
Western_Pacific = []
Eastern_Mediterranean = []

people_on_art=[]
people_on_hiv=[]
myfile= open("data/art_coverage_by_country_clean.csv")

for row in myfile:
    myList = row.split(",")
    if len(myList) >= 3:
        countries.append(myList[0])
        if mylist[10] == "Africa":
            africa.append(myList[0])
        elif mylist[10] == "South-East Asia":
            South_East_Asia.append(myList[0])
        elif mylist[10] == "Europe":
            Europe.append(myList[0])
        elif mylist[10] == "Americas":
            Americas.append(myList[0])
        elif mylist[10] == "Eastern Mediterranean":
            Eastern_Mediterranean.append(myList[0])
        else:
            Western_Pacific.append(myList[0])

        people_on_art.append(myList[1])
        people_on_hiv.append(myList[2])

for index in range(1,len(people_on_art)):
        people_on_art[index] = 0 if people_on_art[index] == "Nodata" else people_on_art[index]

# for item in people_on_hiv:
#     for index in range(len(item)):
#         print(len(item))
#         # if item[index] == "[":
#         #     item = item[0:index]

pwhcopy = []
for item in people_on_hiv:
    if item.__contains__("["):
        index = item.find("[")
        item = item[0:index]
    pwhcopy.append(item)

people_on_hiv = pwhcopy

for index in range(1,len(people_on_hiv)):
    people_on_hiv[index] = 0 if people_on_hiv[index] == "Nodata" else people_on_hiv[index]

for index in range(1,len(people_on_art)):
    people_on_art[index] = int(people_on_art[index])

for index in range(1,len(people_on_hiv)):
    people_on_hiv[index] = int(people_on_hiv[index])

# item.remove(item[index-1])
print(people_on_art)
print(countries)
print(people_on_hiv)

xpoints = np.array(countries[1:])
ypoints = np.array(people_on_art[1:])
ypoints2 = np.array(people_on_hiv[1:])


# plt.plot(xpoints,ypoints, color='red')
# plt.plot(xpoints,ypoints2, color='blue')
# plt.xlabel("Country", color="red")
# plt.ylabel("Population", color="red")
# plt.title("Number of people on ART vs number of people on HIV in 100+ countries", color="red")
# #plt.legend(xpoints)
# plt.xticks(rotation=90)
# plt.show()

w = 1.0
x = np.arange(len(xpoints))

plt.bar(x - w/2,ypoints, w, color='red')
plt.bar(x + w/2,ypoints2, w, color='blue')

plt.xlabel("Country", color="red")
plt.ylabel("Population", color="red")
plt.title("Number of people on ART vs number of people on HIV in 100+ countries", color="red")
plt.xticks(rotation=90)
plt.legend.__init__(xpoints = "red", ypoints = "blue", ypoints2 = "green")
plt.show()