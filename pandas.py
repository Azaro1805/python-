import pandas as pd

df = pd.read_csv('assignment_inspections11.csv')


#-------------------------------------------------df info----------------------------------------#

#print(df.info())
#print(df.shape)
#print(df.columns)
#-----------------------------------------------set df------------------------------------------#

#print(df.set_index('hive_id')) #this do index by hive id but the original df dont change! 
#df.set_index('hive_id', inplace = True) #this do index by hive id and the original df indexing change! 
#print(df)

#df.reset_index(inplace = True) #reset the index to number 

#df.sort_index() #to sort index, it depends on the value of the index string or int - str = alphabetic | ascending optional 


#-----------------------------------------------get values--------------------------------------#

#print(df.iloc[0]) # iloc its by index 
#print(df.iloc[0:2]) # iloc its by indexs (2 rows) 
#print(df.iloc[[0,1], 2]) # display the second col (third start from 0) of the rows: 0,1 

#print(df.loc[[0, 1], 'hive_id']) # same like iloc but can use string


#print(df.hive_id.value_counts()) #how many time each vaule repeat -  object : value

#--------------------------------------------------Prints----------------------------------------#

#pd.set_option('display.max_rows', 5)
#pd.set_option('display.max_columns', 6)

#print(df.head(5))
#print(df.tail(5))

#print(df[['inspection_date', 'hive_id']])

#print(df)