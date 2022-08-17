import re

if __name__ == '__main__':
    in_str = input('enter the string')
    result = re.sub(r'[:8x;]\(', ')', in_str)
    print(result)