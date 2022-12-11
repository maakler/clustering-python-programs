import os
import ast
import numpy as np

import visitors.cyclomatic as cyclomatic
import visitors.allNodes as allnodes
import visitors.unplag as unplag
# import visitors.vars as v

# from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def read_python_files(data_path):
    """Reads `.py` files from the given folder `data_path`"""
    pyfiles = []
    _true_filenames = []
    filenames = os.listdir(data_path)
    for filename in filenames:
        if filename[-3:] == ".py":
            _true_filenames.append(filename)
            full = os.path.join(data_path, filename)
            if os.path.isfile(full):
                with open(full, 'r', encoding='utf-8') as f:
                    pyfiles.append(f.read())
    return pyfiles, _true_filenames


def ast_to_tokens(pyfile_content: str, visitor=unplag.Visitor()) -> list:
    """Returns tokens from the `visitor` after it visits `pyfile_content`. `visitor` defaults to `cyclomatic.Visitor()`"""
    try:
        root = ast.parse(pyfile_content)
        visitor.visit(root)
        names = [node.id for node in ast.walk(root) if isinstance(node, ast.Name)]
        return visitor.tokens + names
    except Exception:
        return ["ERROR"]


def make_vectorizer(tokens: list):
    """Trains and returns the vectorizer. `tokens` should be a list of collections of tokens, e.g. `[['token1', 'token2'], ['token1']]`"""
    I = lambda x: x
    vectorizer = TfidfVectorizer(
        analyzer="word",
        tokenizer=I,
        preprocessor=I,
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
    vectorizer.fit(tokens)
    return vectorizer


def get_clusters(vectors, clustering=KMeans, **kwargs):
    """Get cluster labels."""
    # create an instance of the clustering algorithm
    model = clustering(**kwargs)

    # predict the cluster assignments for each sentence
    return model.fit_predict(vectors)


def get_similarities(vectors, student_codes):
    max_values = []
    for i, row in enumerate(vectors):
        row[i] = 0
        max_index = np.argmax(row)
        max_values.append((row[max_index], student_codes[i], student_codes[max_index]))

    most_similar = sorted(max_values, key=lambda x: x[0])
    most_similar.reverse()
    least_similar = sorted(max_values, key=lambda x: x[0])
    return most_similar, least_similar
