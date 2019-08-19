import requests
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plot
import pandas as pd
import sys
import matplotlib



response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in_7")
soup = BeautifulSoup(response.text,"html.parser")

divTags = soup.find_all('td',class_ ="titleColumn" )
movies = []
movies1 = []
for tag in divTags:
    movies.append(tag.text.strip())
#    print("================================")
for movie in movies:
    start = movie.find('(') + 1
    end = movie.find(')')
    movies1.append(movie[start:end].strip())
movies2 = sorted(movies1)


rating = []

tdTags = soup.find_all('td',class_ = "ratingColumn")
for tag in tdTags:    
    if tag.find("strong") is not None:
        rating.append(tag.find("strong").text)
#print(movies1)
#print(rating)

dataSet = list(zip(movies1,rating))
#print(dataSet)
dataSet1 = sorted(dataSet, key = lambda x: x[0])
# print(dataSet1)
df = pd.DataFrame(data=dataSet1,columns=["year","rating"])
#print(df)
df.to_csv("rating123.csv",index=False,header=None)
#print("DataFrame written to File")

df1 = pd.read_csv("rating123.csv",header=None,names=["year","ratings"])

year_column = df1.year
x = list(year_column)
rating_column = df1.ratings
y = list(rating_column)

plot.plot(x,y)

#Add titles
plot.title("Points")
plot.xlabel("Year")
plot.ylabel("Rating")
plot.grid(True)
plot.show()


    

        