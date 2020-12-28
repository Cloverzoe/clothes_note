import os

clothes = []

if os.path.isfile('clothes.csv'):
	print('已找到檔案。')
	with open('clothes.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			clothes.append([name, price])
	print(clothes)

else:
	print('找不到檔案......')



while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	clothes.append([name, price])

for c in clothes:
	print(c[0], '的價格是', c[1])

with open('clothes.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for c in clothes:
		f.write(c[0] + ',' + str(c[1] + '\n'))


