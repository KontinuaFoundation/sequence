def recursive_determinant(matrix):
    """
    Compute the determinant of a square matrix recursively.
    matrix: list of lists, forming a matrix of size n by n
    """
    n = len(matrix)
    
    # base case 1x1:
    if n == 1:
        return matrix[0][0]
    # base case 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    
    for col in range(n):
        # build a minor matrix:
        minor = []
        # for every row in the matrix
        for row in matrix[1:]:
            # remove column col and store as new_row
            new_row = row[:col]+row[col+1:]
            # apprend new row to the minor matrix
            minor.append(new_row)
    
        sign = (-1) ** col #exponential for alternating sign
        det += sign * matrix[0][col] * recursive_determinant(minor)
    return det
            
A = [
    [1, 2, 3],
    [2, 4,6],
    [3, 6,9]
]
print(recursive_determinant(A))
    