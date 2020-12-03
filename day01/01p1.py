def main():
    with open('input.txt') as f: 
        nums = [int(line) for line in f]
    
    product = find_addends_prod(nums)
    print(f"{product}")


def find_addends_prod(nums):
    nums.sort()
    hi = len(nums)-1
    lo = 0

    while(lo < hi):
        diff = 2020 - nums[hi]
        if diff == nums[lo]:
            return nums[lo] * nums[hi]
        
        if diff > nums[lo]:
            lo += 1
        else:
            hi -= 1
    
    return 0
    

if __name__=="__main__":
    main()