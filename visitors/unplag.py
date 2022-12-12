import ast


# ast visitor template
# https://gist.github.com/jtpio/cb30bca7abeceae0234c9ef43eec28b4
# useful stuff to vectorize
# https://github.com/scriptographers/UnPlag

class Visitor(ast.NodeVisitor):
    tokens = []

    def visit_JoinedStr(self, node):
        self.tokens.append("str_literal")
        self.generic_visit(node)

    def visit_List(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Tuple(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Set(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Constant(self, node):
        self.tokens.append(type(node.value).__name__ + "_literal")
        self.generic_visit(node)

    def visit_Name(self, node):
        if type(node.ctx) == ast.Load:
            self.tokens.append("var_used")
        self.generic_visit(node)

    def visit_Starred(self, node):
        self.tokens.append("var_ref")
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_BinOp(self, node):
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_Compare(self, node):
        for op in node.ops:
            self.tokens.append(typeToStr(op))
        self.generic_visit(node)

    def visit_Call(self, node):
        self.tokens.append("func_call")
        self.tokens.append("n_args_" + str(len(node.args)))
        self.generic_visit(node)

    def visit_IfExp(self, node):
        self.tokens.append("if_else")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if type(node.ctx) == ast.Load:
            self.tokens.append("attr_used")
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.tokens.append("subscript_" + typeToStr(node.slice))
        self.generic_visit(node)

    def visit_ListComp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_SetComp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_DictComp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_comprehension(self, node):
        self.tokens.append("for")
        self.generic_visit(node)

    def visit_Assign(self, node):
        for i in node.targets:
            if type(i) == ast.Name:
                self.tokens.append("var_assign")
            elif type(i) == ast.Tuple:
                self.tokens.append("unpack_assign")
            elif type(i) == ast.Attribute:
                self.tokens.append("attr_assign")
            elif type(i) == ast.Subscript:
                self.tokens.append("subscr_assign")
            else:
                self.tokens.append("assign")
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        # Annotated assign and simple assign are treated the same
        if type(node.target) == ast.Subscript:
            self.tokens.append("subscr_assign")
        elif type(node.target) == ast.Attribute:
            self.tokens.append("attr_assign")
        elif type(node.target) == ast.Name:
            self.tokens.append("var_assign")
        else:
            self.tokens.append("assign")
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        # Assignments of the form (a += 1)
        if type(node.target) == ast.Subscript:
            self.tokens.append("subscr_assign")
        elif type(node.target) == ast.Attribute:
            self.tokens.append("attr_assign")
        elif type(node.target) == ast.Name:
            self.tokens.append("var_assign")
        else:
            self.tokens.append("assign")
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_Raise(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Delete(self, node):
        for i in node.targets:
            if type(i) == ast.Name:
                self.tokens.append("var_delete")
            elif type(i) == ast.Attribute:
                self.tokens.append("attr_delete")
            elif type(i) == ast.Subscript:
                self.tokens.append("subscr_delete")
            else:
                self.tokens.append("delete")
        self.generic_visit(node)

    def visit_Pass(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_If(self, node):
        self.tokens.append("if_else")
        self.generic_visit(node)

    def visit_For(self, node):
        self.tokens.append("for")
        self.generic_visit(node)

    def visit_While(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Break(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Continue(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Try(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_With(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_withitem(self, node):
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        arguments = node.args
        args = arguments.args
        decs = node.decorator_list
        self.tokens.append("func_def_nd_" + str(len(decs)))
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_Lambda(self, node):
        arguments = node.args
        args = arguments.args
        self.tokens.append("lambda")
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_Return(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Yield(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_YieldFrom(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Global(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Nonlocal(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        bases = node.bases
        decs = node.decorator_list
        self.tokens.append("class_def_na_" + str(len(bases)) + "_nd_" + str(len(decs)))
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        arguments = node.args
        args = arguments.args
        decs = node.decorator_list
        self.tokens.append("async_func_def_nd_" + str(len(decs)))
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_Await(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncWith(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Match(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)


SOURCE = """
def järjesta_punktid(p):
    for a in range(len(p)-1):
        for b in range(a+1,len(p)):
            if p[b][1] < p[a][1] or p[b][1] == p[a][1] and p[b][0] < p[a][0]:
                p[a], p[b] = p[b], p[a]
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
