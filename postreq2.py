import requests
from html.parser import HTMLParser
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
import json
import bs4

ws = [1,2,3,4,5,6,7]

for w in ws:
    r = requests.post("http://www.5iarraildental.com/index.php?s=/Home/Index/getClinicListByArea.html", data={"w1": w})
    j = json.loads(r.content)
    h = bs4.BeautifulSoup(j["html"], features="html.parser")
    print(h)
    cityhtml = ET.fromstring("<xml>"+str(h.contents[0])+"</xml>")
    for e in cityhtml.findall("li/div/div/div"):
        ss = e.findall("span")
        print("{}\t{}\t{}\t{}".format(e.find("a").text, ss[0].text, ss[1].text,ss[2].text))

    break
