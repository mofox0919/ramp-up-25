def snakefill(n):
	eat = 0
	while True:
		if 2**eat > n*n:
			break
		eat += 1
	return eat - 1