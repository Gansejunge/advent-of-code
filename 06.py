import re
from collections import Counter

def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

str = open('input.txt', 'r').read()
whole_text=split_on_empty_lines(str)
ghaa=[entry.splitlines() for entry in whole_text]
#print(ghaa)
def partone():
	counter = 0
	for entry in whole_text:
		counter += len(set(entry.replace("\n", "")))
	print(counter)

def parttwi():
	counter=0
	for entry in ghaa:
		people = [set(p) for p in entry]
		counter+=len(set.intersection(*people))
	print(counter)

if __name__ == '__main__':
	parttwi()
