from analysis import *
from vis import *

import seaborn as sns
import numpy as np
from sklearn.metrics.pairwise import linear_kernel

# matrix for every student where all the similairies are added together
scm = get_similarity_count_matrix(377)

dir_names = []

for K in range(14, 15):
    for k in range(1, 5):
        num = "0" * (2 - len(str(K))) + str(K)
        dir_name = "data/K" + num + "kodu" + str(k)
        dir_names.append(dir_name)

for dir_name in dir_names:
    # check if directory is valid
    if not os.path.isdir(dir_name):
        continue
    print(dir_name)

    # read in all python files and student codes for all the students that submitted a solution for this homework
    data_contents, student_codes = read_python_files(dir_name)

    # tokenize every python file  example: tokens = [["call", "if", ... , "var_name"], [...], [...]]
    tokens = [result for file in data_contents for result in [ast_to_tokens(file)] if result]

    # TF-IDF
    vectorizer = make_vectorizer(tokens)

    # print(vectorizer.vocabulary_)  # Vocabulary built is inside vectorizer.vocabulary_
    vectors = vectorizer.transform(tokens)

    # make clusters with KMeans
    clusters = get_clusters(vectors, n_clusters=10)

    # plot clusters
    run_vis(vectors, clusters)
    plt.show()
    # plt.savefig("results/clusters_K" + num + "kodu" + str(k) + ".png")

    tfm = linear_kernel(vectors, vectors)

    # # TF-IDF Heatmap
    # thm = sns.heatmap(tfm)
    # fig = thm.get_figure()
    # fig.savefig("results/varnames_K" + num + "kodu" + str(k) + ".png", dpi=150)
    #
    # np.savetxt("results/varnames_K" + num + "kodu" + str(k), tfm, fmt="%.4f", delimiter=',')

    # add up the similarities between every student that submitted a solution and count how many times the 2 students
    # submitted a solution for the same homework
    for i, row in enumerate(tfm):
        # student code 1
        s1 = student_codes[i][:-3]
        for j, student2 in enumerate(row):
            # student code 2
            s2 = int(student_codes[j][1:-3]) - 1
            # +1 so we know that both of these students submitted the homework
            scm[s1][s2][0] += 1
            # add up the similarities for these 2 students
            scm[s1][s2][1] += student2


# Similarity matrix across all submitted homeworks
S = []
S_count = []
student_codes = []
for key, value in scm.items():
    temp = []
    counts = []
    student_codes.append(key)
    for tup in value:
        # these 2 students or one of the students didn't submit anything and were not comparable
        if tup[0] == 0:
            counts.append(0)
            temp.append(0)
        # divide the sum of the homework similarities with the number of times these students could be compared
        else:
            counts.append(tup[0])
            temp.append(tup[1] / tup[0])

    S_count.append(counts)
    S.append(temp)

# TF-IDF Heatmap
thm = sns.heatmap(S)
fig = thm.get_figure()
fig.savefig("results/results_varnames", dpi=150)
np.savetxt("results/results_varnames", S, fmt="%.4f", delimiter=',')

# print highest and lowest similarities between all the students
student_codes = ["S" + "0" * (3 - len(str(i))) + str(i) for i in range(1, 377 + 1)]
most_similar, least_similar = get_similarities(S, S_count, student_codes)

print("Most similar:")
prev = []
k = 0
for i in most_similar:
    if i[0] not in prev and i[3] > 1:
        k += 1
        print(i[0], "- ", i[1], i[2], "   num of hw matches", i[3])
    prev.append(i[0])
    if k>200:
        break

print("Least similar:")
prev = 69
for i in least_similar[:20]:
    if i != prev:
        print(i[0], "- ", i[1], i[2], "   num of hw matches", i[3])
    prev = i[0]
