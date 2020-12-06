import re

def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

def stringfunfunfun(list):
	nyaa = {}
	for entry in list:
		nyaa[entry.split(":")[0]]=entry.split(":")[1]
	return nyaa

def is_valid_part1(entry):
	if len(entry)==8:
		return True
	if len(entry)==7 and not "cid" in entry:
		return True
	return False

def is_valid_part2(entry):
	if not {'byr','iyr','eyr','hgt','hcl','ecl','pid'} <= entry.keys():
		return False
	if not 1920<=int(entry['byr'])<=2002:
		return False
	if not 2010<=int(entry['iyr'])<=2020:
		return False
	if not 2020<=int(entry['eyr'])<=2030:
		return False
	if not entry['hgt'][-2:] in ['cm','in']:
		return False
	if 'cm' in entry['hgt']:
		if not 150<=int(entry['hgt'][:-2])<=193:
			return False
	if 'in' in entry['hgt']:
		if not 59<=int(entry['hgt'][:-2])<=76:
			return False
	if not entry['hcl'][:1]=='#':
		print(entry['hcl'])
		return False
	if not re.match("^[a-z0-9]*$",entry['hcl'].split('#')[1]):
		return False
	if not entry['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False
	if not len(entry['pid'])==9 or not entry['pid'].isnumeric():
		return False
	return True

str = open('input.txt', 'r').read()
whole_text=split_on_empty_lines(str)
individual_passports=[entry.split() for entry in whole_text]
individual_passports=[stringfunfunfun(entry) for entry in individual_passports]
counter=0
for entry in individual_passports:
	if is_valid_part2(entry):
		print(entry)
		counter+=1
	print("                                      ")
print(counter)