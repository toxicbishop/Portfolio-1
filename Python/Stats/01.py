import pandas as pd 
#Merge
df1 = pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame({'ID':[1,2,4],'Age':[25,30,22]})
merged_df = pd.merge(df1,df2, on ='ID',how = 'inner')
print(merged_df)


#Join
df1.set_index('ID',inplace=True)
joined_df=df1.join(df2.set_index('ID'),how='inner')
print(joined_df)



#Concate
df3=pd.DataFrame({'ID':[5,6],'Name':['David','Eva']})
concatenated_df=pd.concat([df1.reset_index(),df3],ignore_index=True)
print(concatenated_df)


#compare
df4 = pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
comparison = df1.equals(df4.set_index('ID'))
print(f"Are the data frames equal? {comparison}")

#Reshape
data={'Name':['Alice','Bob','Charlie'],
      'Math':[85,90,95],
      'Science':[80,85,90]}
df = pd.DataFrame(data)
melted_df = pd.melt(df,id_vars=['Name'],value_vars=['Math','Science'],
                   var_name='Subject',value_name='Score')
print(melted_df)



#Pivot
data ={'Name':['Alice','Bob','Alice','Bob'],
       'Subject':['Math','Math','Science','Science'],
       'Score':[85,90,80,85]}
df=pd.DataFrame(data)
pivoted_df=df.pivot(index='Name',columns='Subject',values='Score')
print(pivoted_df)


#pivot table
data ={'Name':['Alice','Bob','Alice','Bob'],
       'Subject':['Math','Math','Science','Science'],
       'Score':[85,90,80,85]}
df=pd.DataFrame(data)
pivoted_df=df.pivot(index='Name',columns='Subject',values='Score')
print(pivoted_df)