#留言分析程式, 讀取reviews.txt進行分析

data = []
count = 0
with open('/Users/evan/Desktop/Coding/PythonLab/reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 1000 == 0:
			print(len(data))   #印出目前的進度
print('檔案讀取完成, 總共有',len(data),'筆資料')

print(data[0])

wc = {}                        #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1       #新增一筆

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過！！')
print('感謝使用本查詢功能!!')