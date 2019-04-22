import requests
from bs4 import BeautifulSoup
req = requests.get('http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html')
soup = BeautifulSoup(req.text)
baseurl = "http://cvlab.hanyang.ac.kr/tracker_benchmark/"
dataset_url_list = []
for a in soup.find_all('a', href=True):
    if "seq" in a['href']:
        print (str(baseurl+a['href']))
        dataset_url_list.append(str(baseurl+a['href']))
        
