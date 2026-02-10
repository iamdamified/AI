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


#Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color='green', edgecolor='black')
plt.title("Histogram")
plt.show()


#Scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.show()


#Box Plot
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()


#Customizing Plots
#-Title, labels, and legends
#-Colors and styles
#-Gridlines
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Line Graph")
plt.legend()
plt.plot([1, 2, 3], [10, 20, 30], color='purple', linestyle='--', marker='o', label='Line Graph')
plt.grid(True)
plt.show()



#Pie Chart
labels = ['A', 'B', 'C']
sizes = [25, 35, 40]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()


#Heatmap
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title("Heatmap")
plt.colorbar()
plt.show()

#Subplots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(2, 1, 1) # 2 rows, 1 column, first subplot
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")
plt.subplot(2, 1, 2) # 2 rows, 1 column, second subplot
plt.plot(x, y2, color='orange')
plt.title("Cosine Wave")
plt.tight_layout() # Adjust layout to prevent overlap
plt.show()


#Saving Plots
plt.plot(x, y1, color='blue')
plt.savefig("sine_wave.png")
