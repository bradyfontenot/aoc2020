import re

def main():
    # password format: 1-3 a: abcde
    
    # number of valid passwords
    valid = 0

    # read file into list line by line 
    with open('input_02.txt') as f: 
        pwords = [line for line in f]

    # parse each policy
    pass_policies = [re.split("[\- :\s]+", line) for line in pwords]
    for policy in pass_policies:
        lo = int(policy[0])-1
        hi = int(policy[1])-1
        char = policy[2]
        password = policy[3]

        if (char == password[lo] or char == password[hi]) and password[lo] != password[hi]:
            valid += 1


    print(f"# of valid passwords: {valid}")

if __name__=="__main__":
    main()