import os #把os載入

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	return products

def main():
	filename = 'products.csv'
	if os.path.isfile(filename) : #check file is exited or not
		products = read_file(filename)
	else:
		print('找不到檔案')

main()
