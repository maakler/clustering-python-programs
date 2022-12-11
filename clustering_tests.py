from analysis import *
from vis import *
import numpy as np

data_contents, student_codes = read_python_files("data/test2")

tokens = [ast_to_tokens(file) for file in data_contents]

vectorizer = make_vectorizer(tokens)

vectors = vectorizer.transform(tokens)

# K-Means n_clusters=10
clusters = get_clusters(vectors, n_clusters=10)
run_vis(vectors, clusters)
# show the plot
plt.show()
plt.savefig("results/clusters_KMeans-10-2.png")

# K-Means n_clusters=5
clusters = get_clusters(vectors, n_clusters=5)
run_vis(vectors, clusters)
# show the plot
plt.show()
plt.savefig("results/clusters_KMeans-5-2.png")

from sklearn.cluster import DBSCAN
# DBSCAN eps=0.5
clusters = get_clusters(vectors, clustering=DBSCAN)
run_vis(vectors, clusters)
# show the plot
plt.show()
plt.savefig("results/clusters_DBSCAN-0.5-2.png")

# DBSCAN eps=1
clusters = get_clusters(vectors, clustering=DBSCAN, eps=1)
run_vis(vectors, clusters)
# show the plot
plt.show()
plt.savefig("results/clusters_DBSCAN-1.0-2.png")

from sklearn.cluster import SpectralClustering
# SpectralClustering n_clusters=5
clusters = get_clusters(vectors, clustering=SpectralClustering, n_clusters=5)
run_vis(vectors, clusters)
# show the plot
plt.show()
plt.savefig("results/clusters_SpectralClustering-5-2.png")
