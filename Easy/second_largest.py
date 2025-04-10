#find the second largest element in an array 
def second_largest(a):
    if len(a) < 2:
        return None  # Not enough elements for second largest
    first, second = float('-inf'), float('-inf')
    for num in a:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
            

if __name__ == "__main__":
    a_lst = [3,5,7,12,3,1]
    second_largest(a_lst)