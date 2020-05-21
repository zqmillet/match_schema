def instantiate_expression(expression, variables = None):
    assertion = eval(expression)
    if hasattr(assertion, '__globals__'):
        assertion.__globals__.update(variables if variables else dict())
    return assertion
