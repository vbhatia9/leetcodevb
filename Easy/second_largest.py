#find the second largest element in an array 
# TODO
def large(a):
    largest = 0
    for i in a:
        
        if largest < i:
            largest = i
            
            print(f"largest {largest} a[i] { a[i]} a[i+1] {a[i+1]}")
        
            

if __name__ == "__main__":
    a_lst = [3,5,7,12,3,1]
    large(a_lst)