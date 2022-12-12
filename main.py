from analysis import *
from vis import *

import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel

scm = get_similarity_count_matrix(377)

for K in range(1, 16):
    for k in range(1, 5):
        num = "0" * (2 - len(str(K))) + str(K)
        dir_name = "data/K" + num + "kodu" + str(k)

        if not os.path.isdir(dir_name):
            continue

        print(dir_name)

        data_contents, student_codes = read_python_files(dir_name)

        tokens = [ast_to_tokens(file) for file in data_contents]

        vectorizer = make_vectorizer(tokens)

        # print(vectorizer.vocabulary_)  # Vocabulary built is inside vectorizer.vocabulary_
        vectors = vectorizer.transform(tokens)

        clusters = get_clusters(vectors, n_clusters=2)

        run_vis(vectors, clusters)

        # show the plot
        plt.show()
        # plt.savefig("results/clusters_K" + num + "kodu" + str(k) + ".png")

        tfm = linear_kernel(vectors, vectors)

        # TF-IDF Heatmap
        thm = sns.heatmap(tfm)
        fig = thm.get_figure()
        fig.savefig("results/varnames_K" + num + "kodu" + str(k) + ".png", dpi=150)

        np.savetxt("results/varnames_K" + num + "kodu" + str(k), tfm, fmt="%.4f", delimiter=',')

        for i, row in enumerate(tfm):
            s1 = student_codes[i][:-3]
            for j, student2 in enumerate(row):
                s2 = int(student_codes[j][1:-3]) - 1
                scm[s1][s2][0] += 1
                scm[s1][s2][1] += student2

S = []
student_codes = []
for key, value in scm.items():
    temp = []
    student_codes.append(key)
    for tup in value:
        if tup[0] == 0:
            temp.append(0)
        else:
            temp.append(tup[1] / tup[0])
    S.append(temp)

student_codes = ["S" + "0" * (3 - len(str(i))) + str(i) for i in range(1, 377 + 1)]

most_similar, least_similar = get_similarities(S, student_codes)

print("EPIC FINALLLY")
print("Most similar:")
for i in most_similar[:20]:
    print(i[0], "- ", i[1], i[2])

print("Least similar:")
for i in least_similar[:20]:
    print(i[0], "- ", i[1], i[2])