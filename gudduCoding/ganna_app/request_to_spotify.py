from cgitb import html
from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://www.spotify.com"

# Step 1 : get the html
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the html
soup = BeautifulSoup(htmlContent ,'html.parser')
# print(soup.prettify)   

# Get the title of HTML page
title = soup.title

# Get all paragraphs from the page :- Just like paragraphs , the anchor tags also find
paras = soup.find_all("p") 
print(paras)