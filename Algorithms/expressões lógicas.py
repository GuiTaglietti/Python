'''
 
    Criar um programa que analise se um argumento é válido ou não.
 
    ### Assumptions
        - Input vai conter as operações com os seguintes caracteres 
            -   not
            -   and
            -   or
            -   () (parenteses)
            -   p,q,r (variáveis de apenas um caracter)
 
        - Input vai conter um espaço entre as operações e as variáveis
            - "notp" é inválido
            - "not p" é válido
            - "(p and q)" é válido
        
        - Multiplos parenteses também sao validos
            
    ### Precedência
        - ()
        - not
        - and
        - or
 
    ### Ideias
        - Separar os termos da expressão
        - Substituir variáveis pelos valores
        - Resolver as expressões
 
'''
 
VALID_OPERATIONS = [
    'not',
    'and',
    'or',
    '(',
    ')'
]
 
def is_variable(expr: str) -> bool:
    return expr not in VALID_OPERATIONS
    
def precedence(operation: str) -> int:
    if operation == 'not':
        return 3
    if operation == 'and':
        return 2
    if operation == 'or':
        return 1
    return 0
    
def parse_expression(expression: str) -> list[str]:
    splitted = expression.split()
    parsed = []
    for expr in splitted:
       
        while '(' in expr:
            parsed.append('(')
            expr = expr[1:]
 
        if expr in VALID_OPERATIONS:
            parsed.append(expr)
            continue
 
        parsed.append(expr[0])
        
        while ')' in expr:
            parsed.append(')')
            expr = expr[1:]
    return parsed
 
def resolve_variables(statements: list[str]) -> list[str]:
    variables = [expr for expr in statements if is_variable(expr)]
    variables = list(set(variables)) 
    return variables
 
def prompt_variables(variables: list[str]) -> dict[str, bool]:
    mapping = {}
    for variable in variables:
        logical_value = input(f'Valor lógico de: {variable} - (digite V ou F): ').upper()
        if logical_value not in ['V', 'F']:
            raise ValueError('Valor lógico só pode ser V ou F!')
 
        mapping[variable] = (True if logical_value == 'V' else False)
    return mapping
 
def resolve_statements(statements: list[str], variables_map: dict[str, str]) -> list[object]:
    resolved_statements = statements.copy()
    for i, expr in enumerate(statements):
        if is_variable(expr):
            resolved_statements[i] = variables_map[expr]
    return resolved_statements
 
def solve_multiple_operation(var1: bool, var2: bool, operation: str) -> bool:
    if operation == 'and':
        return var1 and var2
    elif operation == 'or':
        return var1 or var2
    else:
        raise ValueError(f"Operação inexistente: {operation}")
 
def resolve_operation(operation: str, values: list[str]) -> list[str]:
    if operation == 'not':
        val = values.pop()
        values.append(not val)
    else:
        val1 = values.pop()
        val2 = values.pop()
        oper_result = solve_multiple_operation(val1, val2, operation)
        values.append(oper_result)
    return values
 
def solve_parenthesis(values: list[object], operations: list[object]) -> (list[object], list[object]):
    while operations and operations[-1] != '(':
        values = resolve_operation(operations.pop(), values)
    if operations:
        operations.pop()
    return (values, operations)
 
def solve_operation(values: list[bool], operations: list[str], expr: str) -> (list[object], list[object]):
    
    while operations and precedence(operations[-1]) >= precedence(expr):
        values = resolve_operation(operations.pop(), values)
    operations.append(expr)
    return (values, operations)
 
def solve_remaining(values: list[bool], operations: list[str]) -> bool:
    while operations:
        values = resolve_operation(operations.pop(), values)
    return values
 
def solve_statements(statements: list[str]) -> bool:
    values_stack = []
    operations_stack = []
    for expr in statements:
        if expr == '(':
            operations_stack.append(expr)
        elif expr in [True, False]:
            values_stack.append(expr)
        elif expr == ')':
            values_stack, operations_stack = solve_parenthesis(values_stack, operations_stack)
        else:
            values_stack, operations_stack = solve_operation(values_stack, operations_stack, expr)
 
    result = solve_remaining(values_stack, operations_stack)
 
    return result.pop()
 
 
 
def solve_expression(expression: str, variables_map=None) -> bool:
    statements = parse_expression(expression)
    variables = resolve_variables(statements)
    if variables_map is None:
        variables_map = prompt_variables(variables)
    resolved_statements = resolve_statements(statements, variables_map)
    answer = solve_statements(resolved_statements)
    return answer
 
 
test_expression_1 = 'not p or q and (p or r)'
test_vars_1 = { 'p': True, 'q': False, 'r': True }
result_1 = solve_expression(test_expression_1, test_vars_1)
assert result_1 == False
 
test_expression_2 = '(p or q) and (not p or r)'
test_vars_2 = { 'p': True, 'q': True, 'r': False }
result_2 = solve_expression(test_expression_2, test_vars_2)
assert result_2 == False
 
test_expression_3 = '((p and q) or (r) and (q and (q or r)))'
test_vars_3 = { 'p': True, 'q': False, 'r': True }
result_3 = solve_expression(test_expression_3, test_vars_3)
assert result_3 == False
 
test_expression_4 = '((a and (b or c)) and (d or not e))'
test_vars_4 = { 'a': True, 'b': True, 'c': False, 'd': False, 'e': False }
result_4 = solve_expression(test_expression_4, test_vars_4)
assert result_4 == True
 
test_expression_5 = '((p and q) or (not p) and (q or (q or (p and q))))'
test_vars_5 = { 'p': True, 'q': False }
result_5 = solve_expression(test_expression_5, test_vars_5)
assert result_5 == False
 
print("Todos testes OK!")

print("Os operadores devem ser digitados em inglês! Pois o python os lê dessa forma!")
print("Operadores: ou = or / e = and / não = not")
print("Exemplo de expressão: not p and q or (not r and s)")
 
expression = input("Insira a expressão lógica: ")
print("Resultado:", solve_expression(expression))
