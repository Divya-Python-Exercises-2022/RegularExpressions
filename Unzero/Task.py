import re
if __name__ == '__main__':
    in_str = input('Enter the string')

    new_res = re.sub(r'[(^0*)]+[(0*$)]', '', in_str)
    print(new_res)

