import re
if __name__ == '__main__':
    in_str = input('Enter the string')

    val = re.match(r'(\d+ )+([+*/%-])+( \d+)', in_str)
    if val:
        print('true')
    else:
        print('false')
