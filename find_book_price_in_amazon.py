import requests,bs4
name=[]
price=[]
res=requests.get("https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Delectronics&field-keywords=lenovo+k8+note+mobile+phones")
soup=bs4.BeautifulSoup(res.text,"html.parser")
p=soup.select(".a-size-base.a-color-price.s-price.a-text-bold")
n=soup.select("h2.a-size-base.s-inline.s-access-title.a-text-normal")
for i in range(len(p)):
    x=p[i].text.strip()
    price.append(x)
    y=n[i].text.strip()
    name.append(y)   
for i in price:
    for j in name:
        print(j+"\t"+i)
print("No more items")
print(len(name))
