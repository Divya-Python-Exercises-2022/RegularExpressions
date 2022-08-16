import re

if __name__ == '__main__':
    text = "Berlin is a world city of culture, politics, media and science."
    match = re.search(r'\s',text)
    print(match)
    print(f'The first white-space character is located at position: {match.start()}')
