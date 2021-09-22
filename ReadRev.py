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