import re

if __name__ == '__main__':
    text = "Berlin is a city of culture."
    match = re.sub(r'\s', '-', text)
    print(match)