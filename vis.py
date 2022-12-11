import matplotlib.pyplot as plt

# create a scatter plot of the data, with different colors for each cluster
plt.scatter(vectors[:, 0], vectors[:, 1], c=clusters)

# add labels to the axes of the plot
plt.xlabel('x')
plt.ylabel('y')

# show the plot
plt.show()
