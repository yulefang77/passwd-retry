i = 3
password = 'qwe123'

while True:
	check = input('請輸入密碼: ')
	if check == password:
		print('成功登入')
		break
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤！你還有', i, ' 次機會')
		else:
			print('密碼錯誤！你的帳號已被鎖住，請連絡管理員。')
			break