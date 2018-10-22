import random
r = random.randint(1, 100)
while True:
	num = input('請輸入1~100的一個數字：')
	num = int(num)
	if num < r:
		print('再大一點')
	elif num >r:
		print('再小一點')
	else:
		print('恭喜你答對了！')
		break
