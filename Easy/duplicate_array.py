
""" 217. Contains Duplicate"""
#SOL 1
def dup(nums):
    hashset= set()
    for n in nums:
        if n in hashset:
            print("Contains Dup")
            return True
        else:
            hashset.add(n)
    return False

#SOL 2
def dup_set(nums):
    setList = set(nums)
    print(f"SETLIST {setList}")
    if len(setList) == len(nums):
            print("No Dup")
            return False
    else:   
            print("Contains Dup")
            return True  

if __name__ == "__main__":
    n = [1,3,4,5,9,1] # Dup value
    n = [1,3,4,5,9]
     
    print(f"calling Length {len(n)}")

   # sum_indx(n,target)
    #print(dup(n))
    print(dup_set(n))