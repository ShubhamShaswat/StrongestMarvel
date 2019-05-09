import pandas as pd
import urllib.request
from bs4 import BeautifulSoup



characters=pd.read_csv('c:/users/shubham/downloads/characters.csv',usecols=['name'])


for chr in charactesr['name']:
    chr

html = urllib.request.urlopen('https://wallpaper.mob.org/gallery/tag={}/'.fromat())
soup = BeautifulSoup(html, 'lxml')

img_links=soup.find_all('img')

src=[]
for link in img_links:
    src.append(link.get('src'))
    
#download image

index = len(src)/2
    
urllib.request.urlretrieve(('https:'+src[index]),'pics/{}.jpg'.format())
    
    
        
        
