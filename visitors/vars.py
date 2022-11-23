import ast


def getVarNames(path):
    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
        src = f.read()

    root = ast.parse(src)
    names = sorted({node.id for node in ast.walk(root) if isinstance(node, ast.Name)})
    return names
