from analysis import *
from vis import *

import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
#from sklearn.cluster import DBSCAN


data_contents = read_python_files("data/test1")

data_contents, student_codes = read_python_files("data/test2")

tokens = [ast_to_tokens(file) for file in data_contents]


vectorizer = make_vectorizer(tokens)

S = vectorizer.transform(tokens)

print(vectorizer.vocabulary_) # Vocabulary built is inside vectorizer.vocabulary_
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

max_values = []
for i, row in enumerate(tfm):
    row[i] = 0
    max_value = max(row)
    max_values.append(("student " + str(student_codes[i]), max_value, row))

most_similar = sorted(max_values, key=lambda x: x[1])
most_similar.reverse()
least_similar = sorted(max_values, key=lambda x: x[1])

print("Most similar:")
for i in most_similar[:20]:
    print(i[0], i[1])

print("Least similar:")
for i in least_similar[:20]:
    print(i[0], i[1])
