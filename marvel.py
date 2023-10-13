# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:38:10 2023

EDA on Marvel Superheroes data
https://olympus.mygreatlearning.com/courses/47906/modules/items/1288976

data set:
https://www.kaggle.com/datasets/dannielr/marvel-superheroes?select=charcters_stats.csv

@author: caraguir1
"""

import pandas as pd
from matplotlib import pyplot as plt

marvel = pd.read_csv('characters_stats.csv')
marvel.head()
marvel.columns #column names
marvel.shape

#how many characters are good, bad or neutral
#frequency of the categories
marvel['Alignment'].value_counts()

#new data frame with only good super heroes
good=marvel[marvel['Alignment']=='good']
good.head()

#fastest 'good' super heroes
good.sort_values(by='Speed',ascending=False).head(10)

# good heroes with a speed of 100
maxspeed = good[good['Speed']==100]
maxspeed.shape

#good heroes with speed equal to 1
minspeed = good[good['Speed']==1]
minspeed.head()

# data set of all heroes (good, bad or neutral) with the least speed
# minspeed = marvel[marvel['Speed'] == marvel['Speed'].min()]

#MOST POWERFUL SUPERHEROES

good.sort_values(by='Power',ascending=False).head()

# all good heroes with power of a 100
power = good[good['Power']==100]
power.shape
#33 rows, 9 columns. 33 superheroes with power of 100

#show just name and power, sorted
power[['Name','Power']].sort_values(by=['Power','Name'],ascending=[False,True])


# bar chart of most powerful overall (good) heroes (top 5)
plt.figure(figsize=(7,7))
plt.bar(list(power['Name'])[0:5],list(power['Total'])[0:5],color='slateblue')
plt.show()


# bad superheroes ('villains')

bad = marvel[marvel['Alignment']=='bad']
bad.head()

#fastest villains
bad.sort_values(by='Speed',ascending=False).head()

#most powerful villains
bad.sort_values(by='Total',ascending=False)

#top 5 super villains:
#sort the villains by total first, largest to smallest, and save as a new df
maxbad = bad.sort_values(by='Total',ascending=False)

plt.figure(figsize=(7,7))

plt.bar(
        list(maxbad['Name'])[0:5],
        list(maxbad['Total'])[0:5],
        color='palegreen'
        )

plt.show()


#histogram of the fastest super heroes (good)
plt.figure(figsize=(7,7))
plt.hist(good['Speed'])
plt.xlabel('Speed')
plt.ylabel('Ocurrences (superheroes)')
plt.title('Speed distribution')
plt.show()

# combat histogram for good heroes
plt.figure(figsize=(7,7))
plt.hist(good['Combat'],color='darksalmon')
plt.xlabel('Combat')
plt.ylabel('Ocurrences (superheroes)')
plt.title('Combat distribution')
plt.show()


# combat histogram for villains
plt.figure(figsize=(7,7))
plt.hist(bad['Combat'],color='silver')
plt.xlabel('Combat')
plt.ylabel('Ocurrences (villains)')
plt.title('Combat distribution')
plt.show()