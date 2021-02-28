from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')
#print(plt.style.available) # show possible colours
# plt.xkcd() # method to make your graph look funny
ages_x = list(range(25, 36))
dev_y = list(range(40, 51))
pydev_y = list(range(50, 61))
js_y = list(range(20, 31))
plt.plot(ages_x, dev_y, color="#444444", linestyle="--", linewidth="2", marker=".", label="all devs")
plt.plot(ages_x, pydev_y, color="b", marker="o", linewidth="3", label="py devs")
plt.plot(ages_x,js_y, color="#5a7d9a", linestyle="-", linewidth="5", marker=",", label="js")
plt.xlabel("Age") #label for x axis
plt.ylabel("Salary in USD")
plt.title("Dev salary by age in USD") # title of the figure
plt.legend() #put a legend (explicitly set labels in plt.plot) on a figure
plt.grid() #put a grid on a figure
plt.tight_layout() #compact view of the figure
plt.savefig('plot.png') #save figure as plot.png in the current directory
plt.show() 
