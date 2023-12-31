# 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3

# Read a token.
# If the token is a number, then add it to the output queue.
# If the token is a function token, then push it onto the stack.
# If the token is a function argument separator (e.g., a comma):
# Until the token at the top of the stack is a left parenthesis, pop operators off the stack onto the output queue. If no left parentheses are encountered, either the separator was misplaced or parentheses were mismatched.
# If the token is an operator, o1, then:
# while there is an operator token o2, at the top of the operator stack and either
# o1 is left-associative and its precedence is less than or equal to that of o2, or
# o1 is right associative, and has precedence less than that of o2,
# pop o2 off the operator stack, onto the output queue;
# at the end of iteration push o1 onto the operator stack.
# If the token is a left parenthesis (i.e. "("), then push it onto the stack.
# If the token is a right parenthesis (i.e. ")"):
# Until the token at the top of the stack is a left parenthesis, pop operators off the stack onto the output queue.
# Pop the left parenthesis from the stack, but not onto the output queue.
# If the token at the top of the stack is a function token, pop it onto the output queue.
# If the stack runs out without finding a left parenthesis, then there are mismatched parentheses.
# When there are no more tokens to read:
# While there are still operator tokens in the stack:
# If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
# Pop the operator onto the output queue.
# Exit.


def shunting(tokens):

    # operator	precedence	associativity
    # ^	4	Right
    # *	3	Left
    # /	3	Left
    # +	2	Left
    # −	2	Left

    nums

    ops_prec = {'+': 4,
                '*': 3,
                '/': 3,
                '+': 2,
                '-': 2}

    op_assoc = {'+': 'r',
                '*': 'l',
                '/': 'l',
                '+': 'l',
                '-': 'l'}
    for t in tokens:


    return postfix_stack

if __name__ == '__main__':

    truth_expr = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
