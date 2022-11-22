import ast

# ast visitor template
# https://gist.github.com/jtpio/cb30bca7abeceae0234c9ef43eec28b4
# useful stuff to vectorize
# https://github.com/scriptographers/UnPlag

class Visitor(ast.NodeVisitor):
    
    tokens = []

    def visit_FormattedValue(self, node):
        print(node)
        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        print(node)
        self.tokens.append("str_literal")
        self.generic_visit(node)

    def visit_List(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Tuple(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Set(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Dict(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Constant(self, node):
        print(node)
        self.tokens.append(type(node.value).__name__ + "_literal")
        self.generic_visit(node)

    def visit_Name(self, node):
        print(node)
        if type(node.ctx) == ast.Load:
            self.tokens.append("var_used")
        self.generic_visit(node)

    def visit_Load(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Store(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Del(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Starred(self, node):
        print(node)
        self.tokens.append("var_ref")
        self.generic_visit(node)

    def visit_Expr(self, node):
        print(node)
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        print(node)
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_UAdd(self, node):
        print(node)
        self.generic_visit(node)

    def visit_USub(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Not(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Invert(self, node):
        print(node)
        self.generic_visit(node)

    def visit_BinOp(self, node):
        print(node)
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_Add(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Sub(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Mult(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Div(self, node):
        print(node)
        self.generic_visit(node)

    def visit_FloorDiv(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Mod(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Pow(self, node):
        print(node)
        self.generic_visit(node)

    def visit_LShift(self, node):
        print(node)
        self.generic_visit(node)

    def visit_RShift(self, node):
        print(node)
        self.generic_visit(node)

    def visit_BitOr(self, node):
        print(node)
        self.generic_visit(node)

    def visit_BitXor(self, node):
        print(node)
        self.generic_visit(node)

    def visit_BitAnd(self, node):
        print(node)
        self.generic_visit(node)

    def visit_MatMult(self, node):
        print(node)
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        print(node)
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_And(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Or(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Compare(self, node):
        print(node)
        for op in node.ops:
            self.tokens.append(typeToStr(op))
        self.generic_visit(node)

    def visit_Eq(self, node):
        print(node)
        self.generic_visit(node)

    def visit_NotEq(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Lt(self, node):
        print(node)
        self.generic_visit(node)

    def visit_LtE(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Gt(self, node):
        print(node)
        self.generic_visit(node)

    def visit_GtE(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Is(self, node):
        print(node)
        self.generic_visit(node)

    def visit_IsNot(self, node):
        print(node)
        self.generic_visit(node)

    def visit_In(self, node):
        print(node)
        self.generic_visit(node)

    def visit_NotIn(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Call(self, node):
        print(node)
        self.tokens.append("func_call")
        self.tokens.append("n_args_" + str(len(node.args)))
        self.generic_visit(node)

    def visit_keyword(self, node):
        print(node)
        self.generic_visit(node)

    def visit_IfExp(self, node):
        print(node)
        self.tokens.append("if_else")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        print(node)
        if type(node.ctx) == ast.Load:
            self.tokens.append("attr_used")
        self.generic_visit(node)

    def visit_Subscript(self, node):
        print(node)
        self.tokens.append("subscript_" + typeToStr(node.slice))
        self.generic_visit(node)

    def visit_Slice(self, node):
        print(node)
        self.generic_visit(node)

    def visit_ListComp(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_SetComp(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_DictComp(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_comprehension(self, node):
        print(node)
        self.tokens.append("for")
        self.generic_visit(node)

    def visit_Assign(self, node):
        print(node)
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
        print(node)
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
        print(node)
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

    def visit_Print(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Raise(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Assert(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Delete(self, node):
        print(node)
        for i in node.targets:
            if type(i) == ast.Name:
                self.tokens.append("var_delete")
            elif type(i) == ast.Attribute:
                self.tokens.append("attr_delete")
            elif type(i) == ast.Subscript:
                self.tokens.append("subscr_delete")
            else:
                self.tokens.append("delete")

    def visit_Pass(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Import(self, node):
        print(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        print(node)
        self.generic_visit(node)

    def visit_alias(self, node):
        print(node)
        self.generic_visit(node)

    def visit_If(self, node):
        print(node)
        self.tokens.append("if_else")
        self.generic_visit(node)

    def visit_For(self, node):
        print(node)
        self.tokens.append("for")
        self.generic_visit(node)

    def visit_While(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Break(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Continue(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Try(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_TryFinally(self, node):
        print(node)
        self.generic_visit(node)

    def visit_TryExcept(self, node):
        print(node)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        print(node)
        self.generic_visit(node)

    def visit_With(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_withitem(self, node):
        print(node)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        print(node)
        arguments = node.args
        args = arguments.args
        decs = node.decorator_list
        self.tokens.append("func_def_nd_" + str(len(decs)))
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_Lambda(self, node):
        print(node)
        arguments = node.args
        args = arguments.args
        self.tokens.append("lambda")
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_arguments(self, node):
        print(node)
        self.generic_visit(node)

    def visit_arg(self, node):
        print(node)
        self.generic_visit(node)

    def visit_Return(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Yield(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_YieldFrom(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Global(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Nonlocal(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(node)
        bases = node.bases
        decs = node.decorator_list
        self.tokens.append("class_def_na_" + str(len(bases)) + "_nd_" + str(len(decs)))
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        print(node)
        arguments = node.args
        args = arguments.args
        decs = node.decorator_list
        self.tokens.append("async_func_def_nd_" + str(len(decs)))
        for _ in range(len(args)):
            self.tokens.append("arg")
        self.generic_visit(node)

    def visit_Await(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncWith(self, node):
        print(node)
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Match(self, node):
        print(node)
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
    print(tokens)
    print(sorted(tokens))
