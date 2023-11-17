import requests
import bs4
"""
quest=requests.get("https://www.google.com/maps/place?q=台北商業大學",
                    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
                                          
data=bs4.BeautifulSoup(quest.text,"html.parser")
find=data.find("meta",{'itemprop':'image'})['content']
lat_long=find[50:72].split("%2C")
lat=float(lat_long[0])
long_=float(lat_long[1])+0.0002
print(lat,long_)
"""

def get_addr_to_coodinate(addr):
    quest=requests.get("https://www.google.com/maps/place?q="+addr,
                    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
                                          
    data=bs4.BeautifulSoup(quest.text,"html.parser")
    find=data.find("meta",{'itemprop':'image'})['content']
    lat_long=find[50:72].split("%2C")
    lat=float(lat_long[0])
    long_=float(lat_long[1])+0.0002
    return(str(lat)+" "+str(long_))


get_addr_to_coodinate("台北商業大學")


  




