import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def run_vis(vectors, clusters):
    """Create a scatter plot of the data, with different colors for each cluster"""
    X = PCA(n_components=2).fit_transform(vectors.todense())

    plt.scatter(X[:,0], X[:,1], c=clusters)

    # add labels to the axes of the plot
    plt.xlabel('x')
    plt.ylabel('y')
