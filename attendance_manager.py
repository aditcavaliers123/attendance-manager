import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('attendance.xlsx') #this reads the excel file named attendance

df.fillna(0,inplace=True)#fills the places with values nan as 0
name_list=['b','c','d','e']
df.reset_index#restores index of rows to 0,1,2....
"""
print(df.loc[0,'present'])
"""
i=0 #count variable for selecting location in rows 

for name in df['name']:
	
	a=input('attendance for '+ name + ' : ')

	if int(a)==1:
		df.loc[i,'present']=df.loc[i,'present']+1# i is th row and starts with 0 and present is the column
		
		i=i+1
	elif int(a)==0:
		df.loc[i,'absent']=df.loc[i,'absent']+1
		i=i+1
		
	else:
		while a!=0 or 1:#while loop to continuously ask value of a till 0 or 1 is given as input
			print(" input only 1 for present and 0 for absent")
			a=input('attendance for '+ name + ' : ')
			if a==0 or 1: 
				break
				
	
df['percentage']=(df['present'])/(df['present']+df['absent'])*100


	

print(df)


q=input('do you wish to see visual representation  [y/n] : ')

if q=='y':
	# Data to plot
	t=input('name of student : ')
	labels =['present','absent']
	sizes = [df.loc[name_list.index(t),'present'],df.loc[name_list.index(t),'absent']]
	colors = ['gold','lightskyblue']
	explode = (0.1, 0)  # explode 1st slice
 
	# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        
 
	plt.axis('equal')
	plt.show()


else:
	print('the information has been saved ')


df.to_excel('attendance.xlsx')#saves the whole dataframe in the original excel file


