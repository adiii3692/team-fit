# importing the required module
import matplotlib.pyplot as plt
# number of entries
logs = int(input("The number of logs you want to make: "))
# x axis values
x = []
# corresponding y axis values
y = []
for i in range(logs):
    lap = int(input("The lap number: "))
    time = float(input("The time taken (in minutes):"))
    x.append(lap)
    y.append(time)
# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Lap number')
# naming the y axis
plt.ylabel('Lap time')

# giving a title to my graph
plt.title('Graph for lap vs lap-time:')

# function to show the plot
plt.show()

