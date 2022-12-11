from analysis import *
import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel

data_contents = read_python_files("data/test2")

tokens = [ast_to_tokens(file) for file in data_contents]

vectorizer = make_vectorizer(tokens)

S = vectorizer.transform(tokens)
print(vectorizer.vocabulary_) # Vocabulary built is inside vectorizer.vocabulary_

tfm = linear_kernel(S, S)

# TF-IDF Heatmap
thm = sns.heatmap(tfm)
fig = thm.get_figure()
fig.savefig("results/tfidf_heatmap2.png", dpi=150)

np.savetxt("results/tfidf", tfm, fmt="%.4f", delimiter=',')
