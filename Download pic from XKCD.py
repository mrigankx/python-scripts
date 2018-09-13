import requests,bs4,os
url="https://xkcd.com"
os.makedirs("xkcd")
print("Processing....")
while not url.endswith("#"):
    res=requests.get(url)
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    elem=soup.select("#comic img")
    if elem==[]:
        print("Image not found....")
    else:
        cmurl=elem[0].get("src")
        res=requests.get("https:"+cmurl)
        print("Downloading image: %s"%(cmurl))
        imageFile=open(os.path.join("xkcd",os.path.basename(cmurl)),"wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prev=soup.select("a[rel='prev']")[0]
    url="https://xkcd.com"+prev.get("href")
print("Downloaded.....")
    
