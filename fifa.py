"""
Created on Wed Oct 11 15:45:20 2023

EDA on Fifa data: course and files
https://olympus.mygreatlearning.com/courses/47906/modules/items/1288975

fifa player data set

"""

import pandas as pd
from matplotlib import pyplot as plt
## import seaborn as sns


fifa = pd.read_csv('players_20.csv')
fifa.head()

#print the name of each column in the data set
for col in fifa.columns:
    print(col)

fifa.shape
# 18278 rows (records), 104 columns

fifa['nationality'].value_counts()
#count of players from each country in the data set
#number of records for each country

# distinct_countries = fifa['nationality'].unique()
# print(distinct_countries)
# #print the names of all distinct countries in the data set

# fifa['nationality'].nunique()
# # count the number of distinct countries in the data set
# #162 unique countries in the data set

fifa['nationality'].value_counts()[0:10]
#top 10 countries with most players

# fifa['nationality'].value_counts()[0:5]
# fifa['nationality'].value_counts()[0:5].keys()

 
plt.figure(figsize=(7,7))
plt.bar(
        list(fifa['nationality'].value_counts()[0:5].keys()),
        list(fifa['nationality'].value_counts()[0:5]),
        color='lavender'
        )
plt.show()


#player salaries
player_salary = fifa[['short_name','wage_eur']]

#sort player salaries data frame by wage, using sort method
player_salary = player_salary.sort_values(by='wage_eur',ascending=False)
player_salary.head()

# bar chart for top 5 highest paid players
plt.figure(figsize=(7,7))
plt.bar(
        list(player_salary['short_name'][0:5]),
        list(player_salary['wage_eur'][0:5]),
        color='darkseagreen'
        )
plt.show()

# subset of data only including german players
germany = fifa[fifa['nationality']=='Germany']
germany.shape

germany['sofifa_id'].nunique()
#1216 german players

germany.head(10)

#tallest german players
germany.sort_values(by='height_cm',ascending=False).head()

#german players sorted by highest weight
germany.sort_values(by='weight_kg',ascending=False).head()

#highest paid german player
germany.sort_values(by='wage_eur',ascending=False).head()

#subset of short name and wage
germany[['sofifa_id','short_name','wage_eur']].sort_values(by='wage_eur',
                                                           ascending=False).head()

# fifa players with best shooting skills
shooting = fifa[['sofifa_id','short_name','shooting']]
shooting.sort_values(by='shooting',ascending=False).head()

# best defensive players
defense = fifa[['sofifa_id','short_name','defending','nationality','club']]
defense.sort_values(by='defending',ascending=False).head()

#real madrid players
madrid = fifa[fifa['club']=='Real Madrid']

#highest paid madrid players
madrid.sort_values(by='wage_eur',ascending=False).head()

#best shoters from real madrid club
madrid.sort_values(by='shooting',ascending=False).head()

madrid['nationality'].value_counts()


