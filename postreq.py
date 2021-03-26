import requests
from html.parser import HTMLParser
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET

r = requests.post("http://www.arrailgroup.com/index.php?s=/Home/Index/getaddresslist.html", data={"yewu": 2})
print(r.content)
cityhtml = ET.fromstring("<xml>"+r.content.decode("utf-8")+"</xml>")

citylist = []
city=[]

for e in cityhtml.findall("li"):
    citylist.append(e.attrib["data-id"])
    city.append(e.find("i").text)

idx = 0
for cid in citylist:

    r = requests.post("http://www.arrailgroup.com/index.php?s=/Home/Index/getlist.html", data={"diqu": int(cid)})
    if len(r.content) < 20:
        continue
    try:
        addhtml = ET.fromstring("<xml>"+r.content.decode("utf-8")+"</xml>")
    except:
        print(city[idx])
        idx+=1
        continue

    address = []
    licens=[]
    names =[]

    for e in addhtml.findall("li/div/div"):
        names.append(e.find("span").text)
        ps = e.findall("p")
        licens.append(ps[0].text)
        address.append(ps[1].text)

        print("{}\t{}\t{}\t{}".format(city[idx], e.find("span").text, ps[0].text, ps[1].text))

    idx +=1


