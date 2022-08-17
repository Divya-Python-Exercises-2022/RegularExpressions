import re

if __name__ == '__main__':
    text = "The rain in Spain."
    match = re.findall(r'.ai.', text)
    print(len(match))
