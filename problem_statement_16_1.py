import math

print("Enter the number of inputs")
n = int(input())

print("Enter the input values")
li = list()

for x in range(n):
    li.append(int(input()))

# step 1: calculate mean of the given data

mean = float(sum(li)/n)

# step 2: for each point, find the sum of the squares of its distance to the mean

sum_of_squared_distances = 0

for point in li:
    dist = (point - mean)
    dist = dist*dist
    sum_of_squared_distances += dist

# step 3: divide the sum of squared distances by the count of points

sum_of_squared_distances = float(sum_of_squared_distances/n)

# step 4: calculate the square root

standard_deviation = math.sqrt(sum_of_squared_distances)

# step 5: output the calculated standard deviation

print("Standard deviation is " + str(standard_deviation))
