import ast


# ast visitor template
# https://gist.github.com/jtpio/cb30bca7abeceae0234c9ef43eec28b4
# useful stuff to vectorize
# https://github.com/scriptographers/UnPlag

class Visitor(ast.NodeVisitor):
    tokens = []
    complexity = 0

    def visit_Try(self, node):
        self.complexity += len(node.handlers) + bool(node.orelse)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complexity += len(node.values) - 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_If(self, node):
        self.complexity += 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_IfExp(self, node):
        self.complexity += 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += bool(node.orelse) + 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += bool(node.orelse) + 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        self.complexity += bool(node.orelse) + 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_comprehension(self, node):
        self.complexity += bool(node.orelse) + 1
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.complexity += not self.no_assert
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)


SOURCE = """
fail = open(input("Sisesta failinimi: "), "r", encoding="utf-8")
plaan = []

for rida in fail:
    rida = rida.strip().split()
    plaan.append(rida)

fail.close()

halb = []
for aeg in range(len(plaan)):
    valja = plaan[aeg][0].split(":")
    valja = 100*int(valja[0])+int(valja[1])
    saabumine = plaan[aeg][1].split(":")
    saabumine = 100*int(saabumine[0])+int(saabumine[1])
    for aeg2 in range(len(plaan)):
        valja2 = plaan[aeg2][0].split(":")
        valja2 = 100*int(valja2[0])+int(valja2[1])
        saabumine2 = plaan[aeg2][1].split(":")
        saabumine2 = 100*int(saabumine2[0])+int(saabumine2[1])
        if valja < valja2 and saabumine > saabumine2 and int(plaan[aeg][2]) > int(plaan[aeg2][2]):
            halb.append(aeg)

for el in halb[::-1]:
    plaan.pop(el)

for sobib in plaan:
    print(sobib[0], sobib[1], sobib[2])
"""


# Given an operator, convert to its string representation
def typeToStr(t):
    return type(t).__name__.lower()


if __name__ == "__main__":
    tokens = []
    root = ast.parse(SOURCE)
    visitor = Visitor()
    visitor.visit(root)
    print(visitor.tokens)
    print(sorted(visitor.tokens))
