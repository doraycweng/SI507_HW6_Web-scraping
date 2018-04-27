# 507/206 Homework 6 Part 1
import requests
import sys
from bs4 import BeautifulSoup

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here
url = sys.argv[1]
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

all_img_tag=soup.find_all('img')
for image in all_img_tag:
	if image.has_attr('alt') == True:
		print(image['alt'])
	else:
		print('No alternative text provided!!')

