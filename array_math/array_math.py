############################### core functions #################################
""" Perform array math with only native python. All inputs and outputs
are native python types (list, int, float)
"""

def scalar_op(arr, c, operator='+'):
    """ Perform a scalar operation on an array. Operators [+, -, *, /, **]
    """
    if operator == '+':
        return [x + c for x in arr]
    elif operator == '-':
        return [x - c for x in arr]
    elif operator == '*':
        return [x * c for x in arr]
    elif operator == '/':
        return [x / c for x in arr]
    elif operator == '**':
        return [x ** c for x in arr]

def dot_product(arr1, arr2):
    return sum([x * y for x, y in zip(arr1, arr2)])

def elementwise_op(arr1, arr2, operator='+'):
    """ Perform element-wise operations on two arrays with matching dimensions.
    Operators [+, -, *, /]
    """
    if operator == '+':
        return [x + y for x, y in zip(arr1, arr2)]
    if operator == '-':
        return [x - y for x, y in zip(arr1, arr2)]
    if operator == '*':
        return [x * y for x, y in zip(arr1, arr2)]
    if operator == '/':
        return [x / y for x, y in zip(arr1, arr2)]

############################# 2nd order functions ##############################

def quadratic_weights(n):
    """ Native python only: Generate quadratic weights of length n that sum to 1.
    Weights increase from 0 to n (i.e. taken from y = -(x-n)^2 scaled so f(0) = 0)

    numpy:
        x = np.linspace(1, n, n)
        y = -1 * (x-n)**2 + max(x)*n
        return y / np.sum(y)

    param:
    n       positive integer > 0
    """
    x = range(1, n+1)
    a = scalar_op(x, n, operator='-')
    b = scalar_op(a, 2, operator='**')
    c = scalar_op(b, -1, operator='*')
    y = scalar_op(c, (max(x) * n), operator='+')

    return scalar_op(y, sum(y), operator='/')

def weighed_average(arr, w):
    return dot_product(arr, w)
