import re

if __name__ == '__main__':
    text = "Berlin is a city of culture."
    print((re.search(r'\bB\w+', text)).span())