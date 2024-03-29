# Implements a function that takes as input an iterable L of nonnegative integers and an integer N,
# and displays all ways of inserting negations and parentheses in L, resulting in an expression
# that evaluates to N.
#
# Written by Eric Martin for COMP9021


def subtractions(L, N):
    for expression in possible_subtractions(L):
        if eval(expression) == N:
            print(expression[1: -1])

def possible_subtractions(L):
    if len(L) == 1:
        return (str(L[0]),)
    for i in range(1, len(L)):
        for expression_1 in possible_subtractions(L[: i]):
            for expression_2 in possible_subtractions(L[i: ]):
                A = ''.join(['(', expression_1, ' - ', expression_2, ')'])
                return A
##    return (''.join(['(', expression_1, ' - ', expression_2, ')'])
##            for i in range(1, len(L))
##                for expression_1 in possible_subtractions(L[: i])
##                    for expression_2 in possible_subtractions(L[i: ]))
