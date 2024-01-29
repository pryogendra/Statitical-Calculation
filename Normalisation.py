import mmm

def Normalisation(lst):
	N_lst=[]   #x-mean
	mean=mmm.Mean(lst,len(lst))
	
	for data in lst:
		N_lst.append(data-mean)
	N_lst2=[]
	sum_N_lst2=0  #£(x-mean)²
	
	for data in N_lst:
		N_lst2.append(data*data)
		sum_N_lst2+=data*data
	
	SD=(sum_N_lst2/len(lst))**0.5
	new_lst=[]
	print("£(x-mean)² = ",sum_N_lst2)
	print("SD = ",SD)
	
	for i in N_lst:
		new_lst.append(i/SD)
	return new_lst
	
'''	print("Normslisation new value = ",new_lst)
	
lst=[1,2,4,4,5,6,7,7,8,8,9]
Normalisation(lst) '''