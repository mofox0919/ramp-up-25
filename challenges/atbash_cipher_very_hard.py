def atbash(txt):
	return ''.join([chr(ord('Z') - (ord(x) - ord('A'))) if x.isupper() else chr(ord('z') - (ord(x) - ord('a'))) if x.islower() else x for x in txt])