from analysis import *
from vis import *

import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
#from sklearn.cluster import DBSCAN

data_contents, student_codes = read_python_files("data/test2")

tokens = [ast_to_tokens(file) for file in data_contents]

vectorizer = make_vectorizer(tokens)

vectors = vectorizer.transform(tokens)
#print(vectorizer.vocabulary_) # Vocabulary built is inside vectorizer.vocabulary_

clusters = get_clusters(vectors, n_clusters=10)

run_vis(vectors, clusters)

# show the plot
plt.show()
plt.savefig("results/clusters2.png")

tfm = linear_kernel(vectors, vectors)

# TF-IDF Heatmap
thm = sns.heatmap(tfm)
fig = thm.get_figure()
fig.savefig("results/tfidf_heatmap2.png", dpi=150)

np.savetxt("results/tfidf", tfm, fmt="%.4f", delimiter=',')
