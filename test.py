import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Zomato-data-.csv")
print (df.head())

def handleRate(value):
	value = str(value).split('/')
	value = value[0]
	return float(value)

df['rate']=df['rate'].apply(handleRate)
print(df.head())

df.info()

sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.show()

grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant', c='red', size=20)
plt.ylabel('Votes', c='red', size=20)
plt.show()

max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)

sns.countplot(x=df['online_order'])
plt.show()

plt.hist(df['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()


couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = df)
plt.show()


pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()