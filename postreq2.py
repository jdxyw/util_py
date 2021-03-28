import requests
from html.parser import HTMLParser
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
import json
import bs4

ws = [1,2,3,4,5,6,7]

for w in ws:
    for pg in range(1,4):
        r = requests.post("http://www.5iarraildental.com/index.php?s=/Home/Index/getClinicListByArea.html", data={"w1": w, "page":pg})
        j = json.loads(r.content)
        h = bs4.BeautifulSoup(j["html"], features="html.parser")
        s = str(h)
        cityhtml = ET.fromstring("<xml>"+str(s)+"</xml>")
        # print(cityhtml.getchildren())
        for e in cityhtml.findall("li/div/div"):
            d = e.getchildren()
            p = d[1].find("a").find("p")
            ss = d[1].findall("p/span")
            print("{}\t{}\t{}\t{}".format(p.text, ss[0].text, ss[1].text,ss[2].text))
