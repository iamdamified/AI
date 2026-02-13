"""1. Create a histogram with multiple datasets overload"""
import matplotlib.pyplot as plt
import seaborn as sns
# Load the example tips dataset
tips = sns.load_dataset("tips")
# Create a histogram with multiple datasets overload
sns.histplot(data=tips, x="total_bill", hue="day", multiple="stack")
# Show the plot plt.show()
plt.show()


"""2. Use seaborn to create a violin plot and box plot for visualizing distributions"""
sns.violinplot(data=tips, x="day", y="total_bill")
plt.show()
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

"""3. Combine multiple plots in a single figure using Matplotlib's subplot"""
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.violinplot(data=tips, x="day", y="total_bill", ax=axes[0])
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[1])
axes[0].set_title("Violin Plot")
axes[1].set_title("Box Plot")
plt.tight_layout()
plt.show()