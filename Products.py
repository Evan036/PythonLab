import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open('/Users/evan/Desktop/Coding/PythonLab/'+filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')  #先清掉換行符號再進行切割
			products.append([name, price])
	return products

#請使用者輸入新資料
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有商品價格資訊
def print_products(products):
	for product in products:
		print(product)

#把資料寫入檔案中
def write_file(filename, products):
	with open('/Users/evan/Desktop/Coding/PythonLab/'+filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


#主程式區塊
def main():
	if os.path.isfile('/Users/evan/Desktop/Coding/PythonLab/products.csv'):
		print('已經有存檔! 讀取中....')
		products = read_file('products.csv')
	else:
		print('找不到檔案!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
