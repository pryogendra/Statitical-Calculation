def Mean(lst,n):
	sum=0
	for data in lst:
		sum+=data
		Record_mean=sum/n
	return Record_mean

def Mode(lst,n):
	c=0
	for data in lst:
		c1=lst.count(data)
		if c1>c:
			c=c1
			Record_mode=data
	return Record_mode

def Median(lst,n):
	if n%2!=0:
		m=int((n+1)/2)
		Record_median=lst[m-1]
	else:
		m=lst[int(n/2)]+lst[int(n/2+1)]
		Record_median=m/2
	return Record_median