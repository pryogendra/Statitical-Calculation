def Range(lst):
	return (max(lst)-min(lst))/2
	
def Quartiles(lst,n):
	q1=1/4*(n+1)
	Q1=lst[int(q1)-1]+(q1-int(q1))*(lst[int(q1)]-lst[int(q1)-1])
	
	
	q2=2/4*(n+1)
	Q2=lst[int(q2)-1]+(q2-int(q2))*(lst[int(q2)]-lst[int(q2)-1])
	
	q3=(3/4)*(n+1)
	Q3=lst[int(q3)-1]+(q3-int(q3))*(lst[int(q3)]-lst[int(q3)-1]) 
	return Q1,Q2,Q3
	
lst=[1,3,5,7,8]
#print("  ",Range(lst))
#print("  ",Quartiles(lst,len(lst)))