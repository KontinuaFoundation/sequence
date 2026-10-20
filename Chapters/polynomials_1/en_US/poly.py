def evaluate_polynomial(pn, x):
    sum = 0.0  
    for degree in range(len(pn)):
        coefficient = pn[degree]
        sum = sum + coefficient * x ** degree
    return sum

def polynomial_to_string(pn):
    
    # Make a list of the monomial strings
    monomial_strings = []

    # For standard form we start at the largest degree
    degree = len(pn) - 1

    # Go through the list backwards stop before constant term
    while degree >= 0:
        coefficient = pn[degree]
        if coefficient != 0.0:

            # Describe the monomial
            if degree == 0:
                monomial_string = "{}".format(coefficient)
            elif degree == 1:
                monomial_string = "{}x".format(coefficient)
            else:
                monomial_string = "{}x^{}".format(coefficient, degree)
                
            # Add it to the list
            monomial_strings.append(monomial_string)
        
        # Move to the previous term
        degree = degree - 1

    # Deal with the zero polynomial
    if len(monomial_strings) == 0:
        monomial_strings.append("0.0")
    
    # Separate the terms with a plus sign
    return " + ".join(monomial_strings)

def add_polynomials(a, b):
    result_length = max(len(a), len(b))
    result = []
    for i in range(result_length):
        if i < len(a):
            coefficient_a = a[i]
        else:
            coefficient_a = 0.0

        if i < len(b):
            coefficient_b = b[i]
        else:
            coefficient_b = 0.0
        result.append(coefficient_a + coefficient_b)
    return result

def scalar_polynomial_multiply(s, pn):
    result = []
    for coefficient in pn:
        result.append(s * coefficient)
    return result

def subtract_polynomial(a, b):
    neg_b = scalar_polynomial_multiply(-1.0, b)
    return add_polynomials(a, neg_b)

def multiply_polynomials(a, b):
    # What is the degree of the resulting polynomial?
    result_degree = (len(a) - 1) + (len(b) - 1)

    # Make a list of zeros to hold the coefficients
    result = [0.0] * (result_degree + 1)

    # Iterate over the indices and values of a
    for a_degree, a_coefficient in enumerate(a):

        # Iterate over the indices and values of b
        for b_degree, b_coefficient in enumerate(b):

            # Calculate the resulting monomial
            coefficient = a_coefficient * b_coefficient
            degree = a_degree + b_degree
            
            # Add it to the right bucket
            result[degree] = result[degree] + coefficient
            
    return result

def derivative_of_polynomial(pn):

    # What is the degree of the resulting polynomial?
    original_degree = len(pn) - 1
    if original_degree > 0:
        degree_of_derivative = original_degree - 1
    else:
        degree_of_derivative = 0

    # We can ignore the constant term (skip the first coefficient)
    current_degree = 1
    result = []

    # Differentiate each monomial
    while current_degree < len(pn):
        coefficient = pn[current_degree]
        result.append(coefficient * current_degree)
        current_degree = current_degree + 1

    # No terms? Make it the zero polynomial
    if len(result) == 0:
        result.append(0.0)

    return result
    

