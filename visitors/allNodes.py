import ast


# ast visitor template
# https://gist.github.com/jtpio/cb30bca7abeceae0234c9ef43eec28b4
# useful stuff to vectorize
# https://github.com/scriptographers/UnPlag

class Visitor(ast.NodeVisitor):
    tokens = []

    def visit_NamedExpr(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_FormattedValue(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        self.tokens.append(typeToStr(node))
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
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Name(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Load(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Store(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Del(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Starred(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Expr(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_UAdd(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_USub(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Not(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Invert(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BinOp(self, node):
        self.tokens.append(typeToStr(node))
        self.tokens.append(typeToStr(node.op))
        self.generic_visit(node)

    def visit_Add(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Sub(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Mult(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Div(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_FloorDiv(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Mod(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Pow(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_LShift(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_RShift(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BitOr(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BitXor(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BitAnd(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatMult(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_And(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Or(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Compare(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Eq(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_NotEq(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Lt(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_LtE(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Gt(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_GtE(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Is(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_IsNot(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_In(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_NotIn(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Call(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_keyword(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_IfExp(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Attribute(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Slice(self, node):
        self.tokens.append(typeToStr(node))
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
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Print(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Raise(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Delete(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Pass(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Import(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_alias(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_If(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_For(self, node):
        self.tokens.append(typeToStr(node))
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

    def visit_TryFinally(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_TryExcept(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_With(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_withitem(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_Lambda(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_arguments(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_arg(self, node):
        self.tokens.append(typeToStr(node))
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
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.tokens.append(typeToStr(node))
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

    def visit_match_case(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchValue(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchSingleton(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchSequence(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchStar(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchMapping(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchClass(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchAs(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_MatchOr(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)

    def visit_TryStar(self, node):
        self.tokens.append(typeToStr(node))
        self.generic_visit(node)


SOURCE = """
test = 'aa'
match test:
    case 'a':
        print('aahh')
    case 'aa':
        print('aaahhhhhh')

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
    root = ast.parse(SOURCE)
    visitor = Visitor()
    visitor.visit(root)
    print(['var_assign', 'str_literal', 'match', 'var_used', 'str_literal', 'func_call', 'n_args_1', 'var_used',
           'str_literal', 'str_literal', 'func_call', 'n_args_1', 'var_used', 'str_literal', 'var_assign', 'func_call',
           'n_args_2', 'var_used', 'func_call', 'n_args_1', 'var_used', 'str_literal', 'str_literal', 'str_literal',
           'var_assign', 'list', 'for', 'var_used', 'var_assign', 'func_call', 'n_args_0', 'attr_used', 'func_call',
           'n_args_0', 'attr_used', 'var_used', 'func_call', 'n_args_1', 'attr_used', 'var_used', 'var_used',
           'func_call', 'n_args_0', 'attr_used', 'var_used', 'var_assign', 'list', 'for', 'func_call', 'n_args_1',
           'var_used', 'func_call', 'n_args_1', 'var_used', 'var_used', 'var_assign', 'func_call', 'n_args_1',
           'attr_used', 'subscript_constant', 'subscript_name', 'var_used', 'var_used', 'int_literal', 'str_literal',
           'var_assign', 'add', 'mult', 'int_literal', 'func_call', 'n_args_1', 'var_used', 'subscript_constant',
           'var_used', 'int_literal', 'func_call', 'n_args_1', 'var_used', 'subscript_constant', 'var_used',
           'int_literal', 'var_assign', 'func_call', 'n_args_1', 'attr_used', 'subscript_constant', 'subscript_name',
           'var_used', 'var_used', 'int_literal', 'str_literal', 'var_assign', 'add', 'mult', 'int_literal',
           'func_call', 'n_args_1', 'var_used', 'subscript_constant', 'var_used', 'int_literal', 'func_call',
           'n_args_1', 'var_used', 'subscript_constant', 'var_used', 'int_literal', 'for', 'func_call', 'n_args_1',
           'var_used', 'func_call', 'n_args_1', 'var_used', 'var_used', 'var_assign', 'func_call', 'n_args_1',
           'attr_used', 'subscript_constant', 'subscript_name', 'var_used', 'var_used', 'int_literal', 'str_literal',
           'var_assign', 'add', 'mult', 'int_literal', 'func_call', 'n_args_1', 'var_used', 'subscript_constant',
           'var_used', 'int_literal', 'func_call', 'n_args_1', 'var_used', 'subscript_constant', 'var_used',
           'int_literal', 'var_assign', 'func_call', 'n_args_1', 'attr_used', 'subscript_constant', 'subscript_name',
           'var_used', 'var_used', 'int_literal', 'str_literal', 'var_assign', 'add', 'mult', 'int_literal',
           'func_call', 'n_args_1', 'var_used', 'subscript_constant', 'var_used', 'int_literal', 'func_call',
           'n_args_1', 'var_used', 'subscript_constant', 'var_used', 'int_literal', 'if_else', 'and', 'lt', 'var_used',
           'var_used', 'gt', 'var_used', 'var_used', 'gt', 'func_call', 'n_args_1', 'var_used', 'subscript_constant',
           'subscript_name', 'var_used', 'var_used', 'int_literal', 'func_call', 'n_args_1', 'var_used',
           'subscript_constant', 'subscript_name', 'var_used', 'var_used', 'int_literal', 'func_call', 'n_args_1',
           'attr_used', 'var_used', 'var_used', 'for', 'subscript_slice', 'var_used', 'usub', 'int_literal',
           'func_call', 'n_args_1', 'attr_used', 'var_used', 'var_used', 'for', 'var_used', 'func_call', 'n_args_3',
           'var_used', 'subscript_constant', 'var_used', 'int_literal', 'subscript_constant', 'var_used', 'int_literal',
           'subscript_constant', 'var_used', 'int_literal'])
    print(visitor.tokens)
    print(sorted(visitor.tokens))
