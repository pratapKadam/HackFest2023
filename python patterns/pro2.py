i=0
ls=[]
num=1
while i<6:
	ls.append([])
	ls[i].append([])
	ls[i].append([])
	k=i%2+2
	sum=0
	while k:
		ls[i][0].append(num)
		sum+=num
		num+=1
		k-=1
	ls[i][1].append(sum)
	i+=1
print(ls)