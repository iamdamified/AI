"""Matplotlib is for static, interactive, and animated visualizations(plots) in Python."""
#Basic syntax of Matplotlib
import matplotlib.pyplot as plt
# Basic plotting a line graph
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show() # Display the plot


#Typical Line plot with labels and title
plt.plot([1, 2, 3], [10, 20, 30], label='Line Graph')
plt.title("Line Graph")# not necessary but it is good to have a title for the graph
plt.xlabel("X-axis")# not necessary but it is good to have
plt.ylabel("Y-axis")# not necessary but it is good to have
plt.legend()
plt.show()


#Barchart
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values, color=['blue'])
plt.title("Bar Chart")
plt.show()


