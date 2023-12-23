# 分支学习

userName = input("请输入用户名:")
passWord = input("请输入密码:")

# 用户名是admin且密码是123456才可以进入

if userName == 'admin' and passWord == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')
