#machine learning is making the computer learn from studying data and statistics
#This is a step into artificial intelligence
#It allows us to be able to predict from studying data

# Example of dataset:
egg = [56,78,78, 34,12,546,324, 67, 123,5, 78, 546]

#using plain python
answer = min(egg)
print("minimum is", answer)

#using plain python
answer = max(egg)
print("maximum is", answer)

#Find range
answer = max(egg) - min(egg)
print(answer)

#find mean
    #Way 1- No indexes used
sum = 0
for value in egg:
    sum += value
answer = sum / len(egg)
print(answer, "or", round(answer, 2))

    # Way 2- using indexes
sum = 0
index = 0
while index < len(egg):
    sum += egg[index]
    index += 1
answer = sum / len(egg)
print(answer, "or", round(answer, 2))

# Finding the mode
    #Step 1- sort the list
    #Method 1- easy
# egg.sort()
# print(egg)

# Method 2- bubble sort

n= len(egg)
for index in range(n-1):
    for j in range(n - index - 1):
        if egg[j] > egg[j + 1]:
            egg[j], egg[j + 1] = egg[j + 1], egg[j]
print(egg)
egg =[-1, 1,1,4,8,8,8,12,12,13,13,13,13,13,16]
#mode algorithm
mode = None# number that repeat most
most_times = 0 #how many times that mode has been found
counter = 0 # counts how many of each number exists
current_num = egg[0] #current number we are dealing with - resets when number changes

for num in egg:
    if num == current_num:
        counter += 1
    elif num != current_num:
        counter = 1
        current_num = num
    if counter > most_times:
        most_times = counter
        mode = num
print(mode, most_times, counter, current_num,sep="\n")

# Types of data
