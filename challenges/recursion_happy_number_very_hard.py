def is_happy(n):
	if n == 1:
		return True
	if n == 4:
		return False
	num = 0
	while n > 0:
		num += (n%10)**2
		n -= n%10
		n /= 10
	return is_happy(num)