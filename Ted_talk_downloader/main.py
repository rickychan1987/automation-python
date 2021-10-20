import requests     #getting content of the TED Talk page
from bs4 import BeautifulSoup   #web scraping
import re   #Regular Expression pattern matching
#from urllib.request import urlretrieve #downloading mp4
import sys  #for argument parsing

#Exception handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: please enter the RED Talk URL")

#url = "https://www.ted.com/talks/isha_datar_how_we_could_eat_real_meat_without_harming_animals"
#url = "https://www.ted.com/talks/nabiha_saklayen_could_you_recover_from_illness_using_your_own_stem_cells"

r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("scripts"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]

print("Downloading video from ...... " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ..... " + file_name)

r = requests.get(mp4_url)
with open(file_name, 'wb') as f:
    f.write(r.content)

#Alternate method
#urlretrieve(mp4 url, file_name)
print("Donwload Process finished")