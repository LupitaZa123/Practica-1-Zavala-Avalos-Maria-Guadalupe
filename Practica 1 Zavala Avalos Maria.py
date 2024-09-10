def infix_to_postfix(expression):
    """
    Convierte una expresión infija a notación polaca inversa.

    Args:
        expression: La expresión infija a convertir.

    Returns:
        Una lista con la expresión en notación polaca inversa.
    """

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append('(')
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

# Ejemplo de uso:
infix_expression = "2+3*(4-5)"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # Imprime: ['2', '3', '4', '5', '-', '*', '+']
