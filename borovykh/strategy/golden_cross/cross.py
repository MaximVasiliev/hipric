from pandas import DataFrame
import pandas as pd
import numpy as np
import csv, time, os
from math import *
import numpy as np
from tqdm import tqdm
import time

def crosme(crs,index,i):
	val=[]
	some=[]
	
	op = crs['Open'].ix[index+1]
	crs['Return'] = (crs['Close']/crs['Open'].ix[index+1])-1
	min_elem = crs['Low'].ix[index+1]
	ixz = 1
			
	for j, r in crs[1:].iterrows():
		if r['Low'] < min_elem:
			min_elem = r['Low']
		if (min_elem/op)-1 <= -0.02:
			crs['Return'].ix[j] = -0.02
		some.append(crs['Return'].ix[j])
		
		ixz+=1
	val.append(some)
	return val[0]
	

def sharp(x,crosses):
	result = x.transpose()
	result['STD']= np.std(result,axis=1,ddof=1)
	result['AVG']=result.ix[:,result.columns < crosses].mean(axis=1)
	result['Sharp']=1.
	j=0
	for i,row in result.iterrows():
		result['Sharp'].ix[i]=result['AVG'].ix[i]/result['STD'].ix[i]*sqrt(252/(j+1))
		j+=1
	
	return result

def piska(ticker):
	dayz = pd.DataFrame(np.nan, index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'], columns=['scenario0','scenario1','scenario2','scenario3','scenario4','scenario5','scenario6','scenario7','scenario8','scenario9'])
	dayx = pd.DataFrame(np.nan, index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'], columns=['scenario0','scenario1','scenario2','scenario3','scenario4','scenario5','scenario6','scenario7','scenario8','scenario9'])
	df= pd.read_csv('../../sp500/csv/'+ticker+'.csv')
	if len(df) < 250:
		df_ = pd.DataFrame()
		return df_	
	# df = df.iloc[::-1]
	df['MA50_t1'] = pd.rolling_mean(df['Close'], window = 50)
	df['MA200_t1'] = pd.rolling_mean(df['Close'], window = 200)
	df['MA50_t0'] = (df['MA50_t1'].shift(1))
	df['MA200_t0'] = (df['MA200_t1'].shift(1))
	#print df[240:252]
	df['GoldenCross'] = 'No cross'
	df['GoldenCross'][(df.MA50_t1>df.MA200_t1) & (df.MA50_t0<df.MA200_t0)] = 'Cross'
	data=[0,0,0,0,0,0,0,0,0,0]
	val = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val1 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val2 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val3 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val4 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val5 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val6 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val7 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val8 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	val9 = pd.DataFrame(np.nan,index=[], columns=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
	crosses = 0
	crosses1 = 0
	crosses2 = 0
	crosses3 = 0
	crosses4 = 0
	crosses5 = 0
	crosses6 = 0
	crosses7 = 0
	crosses8 = 0
	crosses9 = 0
	for index, row in df.iterrows():
		if index+11==len(df):
				break
		if row['GoldenCross']=='Cross':
			crosses +=1
			some=[]
			i = index + 11
			''' to function'''
			crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
			myl = crosme(crs,index,i)
			y = pd.DataFrame(myl,index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
			val = val.append(y.transpose(),ignore_index=True)
			if row['Scenario'] == 1:
				crosses1 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val1 = val1.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 2:
				crosses2 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val2 = val2.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 3:
				crosses3 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val3 = val3.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 4:
				crosses4 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val4 = val4.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 5:
				crosses5 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val5 = val5.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 6:
				crosses6 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val6 = val6.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 7:
				crosses7 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val7 = val7.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 8:
				crosses8 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val8 = val8.append(y.transpose(),ignore_index=True)
			elif row['Scenario'] == 9:
				crosses9 +=1
				some=[]
				i = index + 11
				''' to function'''
				crs = df[index:i][['Date','Close', 'Open', 'Low', 'Scenario','RSI','ADX']]
				y = pd.DataFrame(crosme(crs,index,i),index=['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10'])
				val9 = val9.append(y.transpose(),ignore_index=True)
			
					
	''' my sharp ratio '''
	sh1= sharp(val1,crosses1)
	dayz['scenario1'] = sh1['Sharp']
	dayx['scenario1'] = sh1['AVG']
	
	sh2 = sharp(val2,crosses2)
	dayz['scenario2'] = sh2['Sharp']
	dayx['scenario2'] = sh2['AVG']
	
	sh3 = sharp(val3,crosses3)
	dayz['scenario3'] = sh3['Sharp']
	dayx['scenario3'] = sh3['AVG']
	
	sh4 = sharp(val4,crosses4)
	dayz['scenario4'] = sh4['Sharp']
	dayx['scenario4'] = sh4['AVG']
	
	sh5= sharp(val5,crosses5)
	dayz['scenario5'] = sh5['Sharp']
	dayx['scenario5'] = sh5['AVG']
	
	sh6 = sharp(val6,crosses6)
	dayz['scenario6'] = sh6['Sharp']
	dayx['scenario6'] = sh6['AVG']
	
	sh7 = sharp(val7,crosses7)
	dayz['scenario7'] = sh7['Sharp']
	dayx['scenario7'] = sh7['AVG']
	
	sh8 = sharp(val8,crosses8)
	dayz['scenario8'] = sh8['Sharp']
	dayx['scenario8'] = sh8['AVG']
	
	sh9 = sharp(val9,crosses9)
	dayz['scenario9'] = sh9['Sharp']
	dayx['scenario9'] = sh9['AVG']
	
	sh = sharp(val,crosses)
	dayz['scenario0'] = sh['Sharp']
	dayx['scenario0'] = sh['AVG']
	
	myBigList=[]
	move = False
	dayz = dayz.dropna(axis=1,how='all')
	for col in dayz:
		step = -1
		myprev=0
		for row in dayz[col]:
			if step == -1 and abs(row) < -0.02:
				step+=1
				break
			if step != 0 and (row-myprev) < 0:
				step+=1
				break
			step+=1
			myprev=row
		
		pointer = int(col[8:])
		c = 0
		S = sh
		avgSharp=pd.DataFrame()
		if pointer == 0:
			S = sh
			c = crosses
		elif pointer == 1:
			S = sh1
			c =crosses1
		elif pointer == 2:
			S = sh2
			c =crosses2
		elif pointer == 3:
			S = sh3
			c =crosses3
		elif pointer == 4:
			S = sh4
			c =crosses4
		elif pointer == 5:
			S = sh5
			c =crosses5
		elif pointer == 6:
			S = sh6
			c =crosses6
		elif pointer == 7:
			S = sh7
			c =crosses7
		elif pointer == 8:
			S = sh8
			c =crosses8
		elif pointer == 9:
			S = sh9
			c =crosses9
		
		
		myList=[]
		myList.append(ticker)
		myList.append(col)
		myList.append('GoldenCross_2stop')
		myList.append(step)
		myList.append(c)
		myList.append(S['AVG'].ix[step-1])
		myList.append(S['Sharp'].ix[step-1])
		
		myBigList.append(myList)
		
	if len(myBigList) == 0:
		df_ = pd.DataFrame()
		return df_	
	
	last = pd.DataFrame(myBigList,columns=['Ticker','Scenario','Strategy','End date','Signals','Return','Sharp'])

	return last	
		

my_time=time.time()
print 'Collecting golden crosses'
print 'Please wait...'
with open('../../sp500.txt','r') as w:
	os.system('rm result.csv')
	os.system('touch result.csv')
	symbol=w.readline()
	string_name = symbol[:-1]
	string_name = string_name.replace(".","-")
	myCurrentData = piska(string_name)
	myCurrentData.to_csv('result.csv',index=False,index_label=False)	
	for symbol in tqdm(w.readlines()):
		try:		
			string_name = symbol[:-1]
			string_name = string_name.replace(".","-")
			myCurrentData = piska(string_name)
			if myCurrentData.empty:
				continue 
		
			myStoredData = pd.read_csv('result.csv', index_col=False)
			myStoredData = myStoredData.append(myCurrentData,ignore_index=True)
		
		
			myStoredData.to_csv('result.csv',index=False,index_label=False)
		except IOError:
			continue
		
print
print
print
print 'It takes %f minutes'%((time.time()-my_time)/60)

