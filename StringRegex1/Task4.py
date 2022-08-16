import re

if __name__ == '__main__':
    text = "Berlin is a city of culture."
    match = re.search(r'in', text)
    print(match)
