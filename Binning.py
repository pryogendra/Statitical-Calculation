def Binning(lst,n,D=3):
	b_lst=[]
	#Partition
	for i in range(int(n/D)+1):
		b_lst.append(list(lst[i*D:i*D+D]))
	#print("Partition = ",b_lst)
	partition_lst=b_lst
	
	b_mean,b_median=[],[]
	b_boundary=[]
	
	#binning by mean
	ind=0
	for i in b_lst:
		s=0
		for j in i:
			s+=j
		v=round(s/D)
		b_mean.append([v,v,v])
		
		#binning by median
		val=b_lst[ind][1]
		b_median.append([val,val,val])
		
		#binning by boundary
		b_boundary.append(b_lst[ind])
		if len(b_boundary[ind])==D:
			b_boundary[ind][1]= (b_lst[ind][2])
		ind+=1
	return b_lst,b_mean,b_median,b_boundary
'''	print("\nBinning by Mean = ",b_mean)
	print("\nBinning by Median = ",b_median)
	print("\nBinning by Boundary = ",b_boundary)
	
lst=[1,1,2,3,4,5,5,5,6,7,8,9,9,11,13,13,33,50]
Binning(lst,len(lst)) '''