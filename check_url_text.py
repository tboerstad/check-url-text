from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from config import YO_API_TOKEN, URLS, DIVCLASS_STRING

payload = {'api_token': YO_API_TOKEN}
params  = urlencode(payload).encode('utf-8')

template_match = False
for u in URLS:
    response = urlopen(u).read()
    soup = BeautifulSoup(response, 'html.parser')

    for (div_class, string) in DIVCLASS_STRING:
        divs = soup.findAll("div", { "class" : div_class })
        for e in divs:
            template_match = True
            if e.string != string:
                urlopen("http://api.justyo.co/yoall/",params)

if not template_match:
    raise SystemExit("None of the supplied templates matched the URLs")


