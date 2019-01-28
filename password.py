password="a123456"

password1 = input("請輸入密碼:")
while True:
	if password1 == password:
		print("登入成功")
		break
	elif password1 != password:
		print("密碼錯誤！還有2次機會")
		password2 = input("請輸入密碼:")
		if password2 == password:
			print("登入成功！")
			break
		elif password2 != password:
			print("密碼錯誤！還有1次機會")
			password3 = input("請輸入密碼:")
			if password3 == password:
				print("登入成功！")
			elif password3 != password:
				print("密碼錯誤！帳號已封鎖")
				break





