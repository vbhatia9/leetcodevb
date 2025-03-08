def rotate(matrix):
    """
    Rotates the given n x n 2D matrix representing an image by 90 degrees clockwise.

    :param matrix: List[List[int]]
    :return: None, modifies matrix in-place
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
print(matrix)
# Output should be:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]