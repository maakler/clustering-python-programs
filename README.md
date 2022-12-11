# Clustering Python Programs
by Yehor Atell Krasnopolskyi and Oliver Vainikko.

In this project, we have implemented a tool that you can use to cluster different python programs. We used Python 3, as well as some data analysis packages (like `sklearn`).

## Files
Files `analysis.py` and `vis.py` have all the working routines defined in them, while `main.py` and `clustering_tests.py` are python executable files with usage examples. `main.py` allows you to use the basic functionality of our program (for instance to find the closest program for each program in the data set). `clustering_tests.py` shows how one can test and visualise all sorts of clustering algorithms.

## Data
We used a data set collected at the University of Tartu by Reimo Palm. The data set consists of submissions for Python programming course assignments by different students. In the `data` directory, there are two other subfolders: `test1` and `test2` that illustrate how the data is prepared to be used. They contain multiple Python source code files that should in theory produce identical or similar results. The process of extracting the files from the data set has been automated in the `get.py` file. We do not provide the entire data set in this repository.

## Approach
Our approach can be described as the following:
1. Load all the data files with Python source codes from the given folder.
2. Use Python's abstract syntax trees (ASTs) and `visitors` to produce a sequence of tokens for every program, while preserving the program's structure.
3. Feed the sequences of tokens to a vectoriser.
4. Perform clusterisation on the resulting vectors.
We also use PCA for dimensionality reduction when plotting.
