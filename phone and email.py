#!python3
import re
#create a regex for phone
phone=re.compile(r"""
  (((\d\d\d)|(\(\d\d\d\))) ? #area code
   (\s|-)                            #first separator
    \d\d\d                        #first 3 digits
    - #separator
      \d\d\d\d  #last 4 digits
    (((ext(\.)?\s)|x)
    (\d(2,5)))? )    #extensions
""",re.VERBOSE)
email=re.compile(r"""
[a-zA-Z0-9_.+]+     #NAME PART
@     #@SYMBOL
  [a-zA-Z0-9_.+]+   #DOMAIN NAME PART
""",re.VERBOSE)
rname="readit.txt"
rfile=open(rname,mode="r")
text=rfile.read()
rfile.close()
extphone=phone.findall(text)
extemail=email.findall(text)
allphonenumber=[]
for phonenumber in extphone:
    allphonenumber.append(phonenumber[0])
results="\n".join(allphonenumber)+"\n"+"\n".join(extemail)
fileName="emailphone.txt"
file=open(fileName,mode="w")
file.write(str(results))
file.close()
print("printed successfully")
