import re

if __name__ == '__main__':
    text = "The rain in Spain."
    match = re.search(r'.*ai.*', text)
    print(match.group(0))
    #print(match.count('ai'))
