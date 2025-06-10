def cartesian_product(n):
	if len(n) == 1:
		return [[i] for i in n[0]]
	combos = []
	for i in n[0]:
		for x in cartesian_product(n[1:]):
			combos.append([i] + x)
	return combos
		
def keys(n):
	if n == 0:
		return [0, 8]
	if n == 1:
		return [1, 2, 4]
	elif n == 2:
		return [1, 2, 3, 5]
	elif n == 3:
		return [2, 3, 6]
	elif n == 4:
		return [1, 4, 5, 7]
	elif n == 5:
		return [2, 4, 5, 6, 8]
	elif n == 6:
		return [3, 5, 6, 9]
	elif n == 7:
		return [4, 7, 8]
	elif n == 8:
		return [0, 5, 7, 8, 9]
	elif n == 9:
		return [6, 8, 9]

def crack_pincode(pincode):
	if len(str(pincode)) == 1:
		return [str(i) for i in keys(int(pincode))]
	nums = cartesian_product([keys(int(i)) for i in str(pincode)])
	string_nums = [''.join([str(i) for i in code]) for code in nums]
	return string_nums
def main():
	print(crack_pincode(12))
	
if __name__ == "__main__":
    main()