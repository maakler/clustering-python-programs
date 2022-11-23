import os
import ast

import numpy as np
import seaborn as sns

import visitors.cyclomatic as cyclomatic
import visitors.allNodes as allnodes
import visitors.unplag as unplag
import visitors.vars as v
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

filepath = os.path.join(os.path.dirname(__file__), "input.py")
with open(filepath, 'r') as f:
    pyfile = f.read()

root = ast.parse(pyfile)

# visitor for cyclomatic complexity
cycvisitor = cyclomatic.Visitor()
cycvisitor.visit(root)

# visitor with UnPlag metrics https://github.com/scriptographers/UnPlag
# not working correctly
unpvisitor = unplag.Visitor()
unpvisitor.visit(root)

# collects all nodes from ast tree (a bit unbalanced)
allvisitor = allnodes.Visitor()
allvisitor.visit(root)

varnames = v.getVarNames(filepath)

print('expressions and statements:')
print(cycvisitor.tokens)
print(allvisitor.tokens)
print(unpvisitor.tokens)
print('expressions and statements sorted:')
print(sorted(cycvisitor.tokens))
print(sorted(allvisitor.tokens))
print(sorted(unpvisitor.tokens))
print('names of functions variable etc:')
print(varnames)


def identityFunction(file):
    return file


vectorizer = TfidfVectorizer(
    analyzer="word",
    tokenizer=identityFunction,
    preprocessor=identityFunction,
    # Consider unigrams, bigrams and trigrams, including trigrams works better for python files
    ngram_range=(1, 3),
    sublinear_tf=True,  # (1+log(tf)) instead of just tf
    max_features=5000,
    encoding="utf-8",
    decode_error="ignore",
    stop_words=None,
    lowercase=False,
    norm="l2"  # Each row will be unit normalized
)


files = [cycvisitor.tokens]

S = vectorizer.fit_transform(files)  # Vocabulary built is inside vectorizer.vocabulary_
print(vectorizer.vocabulary_)

tfm = linear_kernel(S, S)

# TF-IDF Heatmap
thm = sns.heatmap(tfm)
fig = thm.get_figure()
fig.savefig("results/tfidf_heatmap.png", dpi=150)

np.savetxt("results/tfidf", tfm, fmt="%.4f", delimiter=',')
