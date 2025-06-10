def interview(lst, tot):
	if len(lst) < 8 or tot > 120 or lst[0] > 5 or lst[1] > 5 or lst[2] > 10 or lst[3] > 10 or lst[4] > 15 or lst[5] > 15 or lst[6] > 20 or lst[7] > 20:
		return "disqualified"
	else:
		return "qualified"