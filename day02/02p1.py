import re

def main():
    # password format: 1-3 a: abcde
    
    # number of valid passwords
    valid = 0

    # read file into list line by line 
    with open('input_02.txt') as f: 
        pwords = [line for line in f]

    pass_policies = [re.split("[\- :\s]+", line) for line in pwords]

    for policy in pass_policies:
        lo = int(policy[0])
        hi = int(policy[1])
        char = policy[2]
        password = policy[3]

        char_count = password.count(char)
        if char_count <= hi and char_count >= lo:
            valid += 1

    print(valid)

if __name__=="__main__":
    main()