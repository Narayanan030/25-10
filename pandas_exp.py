#pandas

#load csv & print 5 rows
import pandas as pd
data=pd.read_csv("iris.csv")
data.head()

#rename
import pandas as pd
df = pd.read_csv("iris.csv")
df.rename(columns={"petal.length": "length", "petal.width": "width"}, inplace=True)
print(df)

#drop
import pandas as pd
df = pd.read_csv('iris.csv')
newdf = df.dropna()
print(newdf.to_string())

#filter
data=pd.read_csv("iris.csv")
filter_row=df[df["petal.width"]<1]
print(filter_row)

#filter by 2 conditions
data=pd.read_csv("iris.csv")
filter_row=df[(df["petal.width"]<1) & (df["petal.length"]<2)]
print(filter_row)

#DataFrame by a column and calculate the sum of another column.
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','55days','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
                })
df = pd.DataFrame(technologies, columns=['Courses','Fee','Duration','Discount'])
print("Create DataFrame:\n", df)

df2 = df.groupby('Courses').sum()
print("Get sum of the grouped data:\n", df2)

#Add a new column to a DataFrame with computed values from other columns.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df.apply(lambda row: row['A'] * row['B'], axis=1)
print(df)

#merge
import pandas as pd
df1 = pd.DataFrame({'Name':['Raja', 'Rani', 'bishop', 'rook', 'pawn'],
					'Marks':[80, 90, 75, 88, 59]})
df2 = pd.DataFrame({'Name':['Raja', 'Divya', 'bishop', 'rook'],
					'Grade':['A', 'A', 'B', 'A'],
					'Rank':[3, 1, 4, 2 ],
					'Gender':['Male', 'Female', 'Female', 'Female']})
display(df1)
display(df2)
df_merged = df1.merge(df2[['Name', 'Grade', 'Rank']])
print(df_merged)

#fill null values
import numpy as np
import pandas as pd
df = pd.DataFrame({'rating': [np.nan, 85, np.nan, 88, 94, 90, 76, 75, 87, 86],
                   'points': [25, np.nan, 14, 16, 27, 20, 12, 15, 14, 19],
                   'assists': [5, 7, 7, np.nan, 5, 7, 6, 9, 9, 5],
                   'rebounds': [11, 8, 10, 6, 6, 9, 6, 10, 10, 7]})
print(df)
df = df.fillna(df.median())
print(df)

#Export the DataFrame to a CSV file without the index.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
df.to_csv('data.csv', index=False)
