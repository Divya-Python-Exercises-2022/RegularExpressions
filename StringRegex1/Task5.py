import re

if __name__ == '__main__':
    text = "Berlin is a city of culture."
    #match = re.match(r'\w(.*[A-Z]*)', text) # o/p <re.Match object; span=(0, 28), match='Berlin is a city of culture.'>
    match = re.match(r'[A-Za-z]*',text)
    print(f'({match.start()}, {match.end()})')
    