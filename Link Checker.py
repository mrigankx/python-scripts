import os,requests,bs4
c=0
s=0
n=0
inp=input("website address(without https): ")
url="https://"+inp
res=requests.get(url)
stcode=res.status_code
if(stcode==200):
    print("It's a valid URL....\nPlease Wait........")
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    links=soup.select("a")
    for i in range(len(links)):
        ulink=links[i].get("href")
        klink=str(ulink)
        if(klink.startswith("http:")):
            res=requests.get(klink)
        else:
            n=n+1
        sc=res.status_code
        if(sc==200):
            s=s+1
        else:
            c=c+1
    print("Healthy Links: "+str(s)+"\nBroken Links: "+str(c)+"\nNot a link: "+str(n))           
else:
    print("failed")


