# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:20:20 2023

EDA on IPL data: course and files
https://olympus.mygreatlearning.com/courses/47906/pages/eda-on-ipl-data?module_item_id=1288974


full data set: https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020

@author: caraguir1
"""

import pandas as pd
from matplotlib import pyplot as plt
##import seaborn as sns


ipl = pd.read_csv('matches.csv')

#first five (5) rows of data
ipl.head()

# descriptive statistics about the data set
ipl.describe()

# number of rows and columns
ipl.shape

# frequency of player_of_match // count of players with most matches 
ipl['player_of_match'].value_counts()

#subset of the previous result, just with the top 10 players
ipl['player_of_match'].value_counts()[0:10] # 10 top players

ipl['player_of_match'].value_counts()[0:5] #top 5 players



#matplotlib bar chart:
#the keys (names) and values are converted to lists, and then passed as the
# x-axis values and y-axis values , respectively
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), 
        list(ipl['player_of_match'].value_counts()[0:5]),
        color="g")
plt.show()

#frequency of the different categories of the result column:
ipl['result'].value_counts()

# teams that have won the most tosses:
ipl['toss_winner'].value_counts()

# subset of records from the data set where the team 
# batting first has won the match:
batting_first =  ipl[ipl['win_by_runs']!=0]   
batting_first.head() 

#distribution of all the teams winning by batting first:
plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.title('Distribution of Runs')
plt.xlabel('Runs')
plt.show()  
# x-axis is the number of runs by which the teams has won,
#y axis is the number of instances this has happened

# number of wins for each team that has won by batting first
batting_first['winner'].value_counts()

# bar chart for top 3 teams
plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()), 
        list(batting_first['winner'].value_counts()[0:3]),
        color=['blue','yellow','orange'])
plt.show()

#represent the values as a pie chart
#for pie charts, the first parameter is the numerical values
#the second parameter is the categorical values (labels)
#the autopct parameter is used to format and display 
#the percentages on the chart:
plt.figure(figsize=(7,7))
plt.pie(
        list(batting_first['winner'].value_counts()),
        labels=list(batting_first['winner'].value_counts().keys()),
        autopct='%0.1f%%'
        )
plt.show()   


#teams that have won by batting second:
batting_second =  ipl[ipl['win_by_wickets']!=0]
batting_second.head()
     
#histogram to see the distribution for teams that won, batting second
plt.figure(figsize=(7,7))
plt.hist(
        batting_second['win_by_wickets'],bins=30
        )
plt.title('Distribution of Wins by Wickets')
plt.xlabel('Points Scored')
plt.ylabel('Number of Games')
plt.show()


batting_second['winner'].value_counts() # wins for each team
#count of wins per team

#bar chart of top 3 winners batting second

plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), 
        list(batting_second['winner'].value_counts()[0:3]),
        color=['blue','yellow','red'])
plt.ylabel('Number of Games Won')
plt.show()



plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), 
        list(batting_second['winner'].value_counts()[0:3]),
        color=(1,0.46,0.46)) # rgb 255,118,118 
plt.ylabel('Number of Games Won')
plt.show()

#same plot, rgb colors:

# rgb(8, 2, 163)  -- 255= 1 (max) , 0 is min
# rgb(255, 75, 145) -- 255= 1 (max) , 0 is min
# rgb(255, 118, 118) -- 255= 1 (max) , 0 is min
# rgb(255, 205, 75) -- 255= 1 (max) , 0 is min
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), 
        list(batting_second['winner'].value_counts()[0:3]),
        color=[(1,0.46,0.46),(1,0.80,0.29),(0.03,0.0,0.64)])  
plt.ylabel('Number of Games Won')
plt.show()

#same plot using css color names
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), 
        list(batting_second['winner'].value_counts()[0:3]),
        color=['thistle','orchid','indigo'])  
plt.ylabel('Number of Games Won')
plt.show()

#pie chart for winners batting second
#represent the values as a pie chart
#for pie charts, the first parameter is the numerical values
#the second parameter is the categorical values (labels)
#the autopct parameter is used to format and display 
#the percentages on the chart:
plt.figure(figsize=(7,7))
plt.pie(
        list(batting_second['winner'].value_counts()),
        labels=list(batting_second['winner'].value_counts().keys()),
        autopct='%0.1f%%'
        )
plt.show() 


#number of matches per season
ipl['season'].value_counts()

#number of matches played in each city
ipl['city'].value_counts()


#number of times a team has won the coin toss and the match
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])
# 393 out of 756 , or 52%


