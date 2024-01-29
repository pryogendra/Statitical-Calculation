import mmm
import Binning
import Range_Quartiles
import Normalisation
s1='*'*100
s2=' '*35

print("""\n\n\n
""",s1,'''\n
''',s2+'''NAME       :  YOGENDRA PRASAD\n 
''',s2+'''CLASS       :  SY BSc IT \n
''',s2+'''DIV           :  'B' \n
''',s2+'''ROLL NO.   :  4098\n
''',s2+'''SEM          :  IV\n
''',s2+'''YEAR         :  2023-24\n 
''',s1)

Record_list=[]
print(s2,end=' ')
N=int(input("Enter total no. of data :  "))

print(s2,"Enter data on by one :  ")

for i in range(N):
	Record_list.append(float(input('\t')))

	
while(1):
	print("\n\n\n\n")
	print('''
''',s2,'''****** OPTIONS AVAILABLE ******\n\n
''',s2,'''1. Mean \n
''',s2,'''2. Mode \n
''',s2,'''3. Median \n
''',s2,'''4. Range \n
''',s2,'''5. Quartiles \n
''',s2,'''6. Binning \n
''',s2,'''7. Normalisation \n
''',s2,'''8. Exit \n\n
''',s1,'''\n\n\n''')

	print(s2,end=' ')
	choice=int(input("Enter your Choice :  "))
	
	if choice==1:
		Mean=mmm.Mean(Record_list,N)
		print("\n\n",s2,"Mean of the data is : ",Mean)
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==2:
		Mode=mmm.Mode(Record_list,N)
		print("\n\n",s2,"Mode of the data is : ",Mode)
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==3:
		Median=mmm.Median(Record_list,N)
		print("\n\n",s2,"Median of the data is : ",Median)
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==4:
		Range=Range_Quartiles.Range(Record_list)
		print("\n\n",s2,"Range of the data is : ",Range)
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==5:
		Q1,Q2,Q3=Range_Quartiles.Quartiles(Record_list,N)
		print("\n\n",s2,"Quartiles of the data \n",s2,"Q1 = ",Q1,"\n",s2,"Q2 = ",Q2,"\n",s2,"Q3 = ",Q3,"\n")
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==6:
		P_lst,B_Mean,B_Median,B_Boundary=Binning.Binning(Record_list,N)
		print("\n\n",s2,"Binning of the data \n",s2,"Partition is  = ",P_lst,"\n",s2,"Binning by mean = ",B_Mean,"\n",s2,"Binning by medain = ",B_Median,"\n",s2,"Binning by boundary = ",B_Boundary,"\n")
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice==7:
		New_value=Normalisation.Normalisation(Record_list)
		print("\n\n",s2,"Normalisation of the data is : ",New_value)
		print("\n",s2,input("\tPress enter to continue.............."))
		
	elif choice ==8:
		break
		
	else:
		print(s2,"Invalid Choice..............\n")
		print(s2,input("\tPress enter to continue.............."))
		continue
