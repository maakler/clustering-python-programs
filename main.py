from analysis import *
from vis import *

import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel


data_contents, student_codes = read_python_files("data/test1")

tokens = [ast_to_tokens(file) for file in data_contents]

vectorizer = make_vectorizer(tokens)

# print(vectorizer.vocabulary_)  # Vocabulary built is inside vectorizer.vocabulary_
vectors = vectorizer.transform(tokens)

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

most_similar, least_similar = get_similarities(tfm, student_codes)

print("Most similar:")
for i in most_similar[:20]:
    print(i[0], "- ", i[1], i[2])

print("Least similar:")
for i in least_similar[:20]:
    print(i[0], "- ", i[1], i[2])
