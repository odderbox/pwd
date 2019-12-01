password = 'a123456'
chance = 3
while True:
	text = input('請輸入密碼：')
	if text == password:
		print('登入成功')
		break
	else:
		chance -= 1
		if chance == 0:
			break
		else:	
			print('密碼錯誤！還有', chance, '次機會')