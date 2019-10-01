import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = data('iris')
df = pd.DataFrame(iris)
df = df.rename(columns=lambda x: x.replace('.','_'))
df.head(3)

#1.1 What does the distribution of petal length look like
sns.distplot(df.Petal_Length)

#1.2

sns.relplot(x='Petal_Length',y='Petal_Width',data=df)

#1.3 Would it be reasonable to predict species based on sepal width and sepal length?
#1.4
#Petal width and length are better for predicting

sns.relplot(x='Petal_Length',y='Petal_Width',hue='Species',data=df)

sns.boxplot(data=df,y='Petal_Width',x='Species')

sns.boxplot(data=df,y='Petal_Length',x='Species')

#1.1 import anscombe and plot x,y
anscombe = sns.load_dataset('anscombe')

sns.relplot(x='x',y='y',data=anscombe)


#2. load InsectSpratys and read documentation. Create boxplot that shows the effectiveness of different insect sprays

insect_sprays = data('InsectSprays')
data('InsectSprays',show_doc=True)
insect_sprays
# Visualize effectiveness of each spary
sns.boxplot(data=insect_sprays,y='count',x='spray')


#3.a Load swiss dataset. Create viz for is_catholic

swiss['is_catholic'] = swiss['Catholic'] > 80

#3.b Does being Catholic or not influence fertility

sns.boxplot(data=swiss,y='Fertility',x='is_catholic')

#3.c Education, examination, and Catholic
swiss.corr().Fertility.sort_values()


#4 bar chart showing chipotle most popular items and count of items

chipotle.groupby('item_name')['quantity'].count().sort_values(ascending=False).head().plot.bar()

# charting revenue of top 5 items.

chipotle.groupby('item_name')['revenue'].agg('sum').sort_values(ascending=False).head().plot.bar()


#5 sleepstudy line chart of average change in reaction time

sns.lineplot(x='Days',y='Reaction',data=sleepstudy)
