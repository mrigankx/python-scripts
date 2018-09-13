#this can be used to search for mobiles and laptops etc
import requests,bs4
nm=[]
pc=[]
#taking input
ur=input("FLIPKART search: ")
print("Processing....")
#getting the site
urll="https://www.flipkart.com/search?q="+ur
res=requests.get(urll)
soup=bs4.BeautifulSoup(res.text,"html.parser")
#selecting the page no.s
links=soup.select("._1ypTlJ a")
#minimum 3 pages of search
numopen=min(3,len(links))
#iterate through the pages
for i in range(numopen):
    url2="https://flipkart.com"+links[i].get("href")
    res2=requests.get(url2)
    soup2=bs4.BeautifulSoup(res2.text,"html.parser")
    names=soup2.select("._3wU53n")
    prices=soup2.select("._2rQ-NK")
    l=len(names)
    #adding the names and prices in lists
    for i in range(l):
        n=names[i].text.strip()
        nm.append(n)
        p=prices[i].text.strip()
        pc.append(p)
    for i in range(l):
        print("Model Name: "+nm[i]+"\t\t\tPrice: "+pc[i])
print("Finished....")