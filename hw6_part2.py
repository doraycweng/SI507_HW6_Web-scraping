# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here
html = requests.get('https://www.michigandaily.com/').text 
soup = BeautifulSoup(html, 'html.parser') 

mostRead = soup.find_all(class_='panel-pane pane-mostread')


for li in mostRead[0].find_all('li'):
	print(li.string)
