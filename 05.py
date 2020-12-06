stra='FBFBBFFRLR'
stras='BFFFBBFRRR'
str = open('input.txt', 'r').read()

def partone(str):
	row = 0
	for entry in str[:7]:
		if entry=='F':
			row <<= 1
		else:
			row=(row+1)<<1
	row >>= 1
	col = 0
	for entry in str[-3:]:
		if entry == 'L':
			col <<= 1
		else:
			col = (col+1)<<1
	col >>=1
	return (row * 8) + col

seat_ids=[]
for entry in str.splitlines():
	seat_ids.append(partone(entry))

largest = max(seat_ids)
smallest = min(seat_ids)
for id in range(smallest, largest):
    if id not in seat_ids:
        print(id)
        break