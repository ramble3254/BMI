height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
height = float(height) / 100
weight = float(weight)
BMI = weight / (height * height)
print('您的BMI值為: ',round(BMI,2))
if BMI < 18.5:
	print('過輕')
elif BMI >= 18.5 and BMI <= 24:
    print('正常')
elif BMI >= 24 and BMI <= 27:
	print('過重')
elif BMI >= 27 and BMI <= 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI <= 35:
	print('中度肥胖')
else:
	print('重度肥胖')