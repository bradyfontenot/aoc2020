def main():
    with open('input.txt') as f: 
        nums = [int(line) for line in f]
    
    product = find_3_addends_prod(nums)
    print(f"{product}")

# got lazy.... O(n^3) 
def find_3_addends_prod(nums):
    prod = 0
    for i in range(len(nums)-2):
        for j in range(1,len(nums)):
            for k in range(2, len(nums)-1):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 2020:
                     prod = nums[i] * nums[j] * nums[k]
    return prod


if __name__=="__main__":
    main()