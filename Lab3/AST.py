class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)
    # pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


#  zmienna np. "A"
class Variable(Node):
    def __init__(self, name):
        self.name = name


#  Operatory typu +, -, M_ADD itd. gdzie left to lewa strona przed operatorem, right to prawa strona po operatorze
class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


# ...
# fill out missing classes
# ...


class String(Node):
    def __init__(self, value):
        self.value = value


#  Operator relacji, np. k<5, gdzie "k" - left, "<" - op, "5" - right
class RelExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


#  Do użycia w transpose
class Transpose(Node):
    def __init__(self, name):
        self.name = name


#  Do użycia w funkcji uminus
class UMinus(Node):
    def __init__(self, name):
        self.name = name


#  Czyli lista (w przykładzie ma wypisywanie jako "VECTOR" więc tak nazwałem klase)
#  Elements to elementy listy
class Vector(Node):
    def __init__(self, elements):
        self.elements = elements


#  Użyta do zeros, ones, eye np. zeros(5)
#  gdzie func to "zeros", args to "5"
class MatrixFunc(Node):
    def __init__(self, func, args):
        self.func = func
        self.args = args


#  Do fora np. for i = 1:N {
#  czyli range by był left - "1", right - "N"
class Range(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


#  Czyli zwykłe równa się np. A = zeros(5);
#  gdzie "A" to left, "=" to op, "zeros(5)" to right
class Assign(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


#  Przypisanie referencji to miejsca w tablicy np. A[1,3] = 0;
#  gdzie name to A, args to 1,3
class Ref(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args


class For(Node):
    def __init__(self, variable, range, instruction):
        self.variable = variable
        self.range = range
        self.instruction = instruction


class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction


class If(Node):
    def __init__(self, condition, if_expression, else_expression=None):
        self.condition = condition
        self.if_expression = if_expression
        self.else_expression = else_expression


class Error(Node):
    def __init__(self):
        pass


class Break(Node):
    def __init__(self):
        self.name = 'BREAK'


class Continue(Node):
    def __init__(self):
        self.name = 'CONTINUE'


#  Print zawiera content
class Print(Node):
    def __init__(self, content):
        self.content = content


#  Return - może zawierać content
class Return(Node):
    def __init__(self, content=None):
        self.content = content


#  Argument - lista argumentów (użyta chyba będzie w princie jako to
#       co się printuje)
class Args(Node):
    def __init__(self, list):
        self.list = list

    def addArg(self, arg):
        self.list.append(arg)


#  Instrukcje - lista instrukcji
class Instructions(Node):
    def __init__(self, list):
        self.list = list

    def addInstruction(self, value):
        self.list.append(value)

    def accept(self, visitor):
        visitor.visit(self)


#  Cały program - zawiera zero lub więcej instrukcji
class Program(Node):
    def __init__(self, instructions=None):
        self.instructions = instructions

    def accept(self, visitor):
        visitor.visit(self)
