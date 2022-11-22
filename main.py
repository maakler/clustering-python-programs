import os
from cyclomatic.astvisitor import *
from cyclomatic.vars import *


BASE_PATH = 'C:\\Users\\'
FILE = 'kodu3.py'

filepath = os.path.join(BASE_PATH, FILE)
files = []

root = ast.parse(SOURCE)
visitor = Visitor()
visitor.visit(root)
varnames = getVarNames(filepath)

print('different function types used:')
print(visitor.tokens)
print(sorted(visitor.tokens))
print('names of functions variable etc')
print(varnames)
