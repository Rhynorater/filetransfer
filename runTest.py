import pip
pip.main(['install', 'requests'])
import requests
x = open("top500Domains.csv")
d = list(map(lambda i: i.split('"')[3], x.readlines()[1:]))
x.close()

for i in d:
    try:
        r = requests.get("https://"+i, timeout=2)
        print(i+":"+str(r))
    except:
        pass
