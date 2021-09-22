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

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('每筆留言的平均長度為:',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d) #塞選長度小於100的留言清單
print('一共有', len(new),'筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆留言提到good')