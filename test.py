import requests
from bs4 import BeautifulSoup

# url = "https://statiz.sporki.com/stats/api/batting?year=2025&reg=R&limit=50"
url = "https://statiz.sporki.com/stats/?m=main&m2=batting&m3=default&so=WAR&ob=DESC&year=2025&sy=1994&ey=2024&te=5002&po=&lt=10100&reg=R&pe=&ds=&de=&we=&hr=&ha=&ct=&st=&vp=&bo=&pt=&pp=&ii=&vc=&um=&oo=&rr=&sc=&bc=&ba=&li=&as=&ae=&pl=&gc=&lr=&pr=50&ph=&hs=&us=&na=&ls=&sf1=&sk1=&sv1=&sf2=&sk2=&sv2="

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

if res.ok:
    html = res.text

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html, "html.parser")   

    datas = soup.select("div.table_type01 table tr")


    for data in datas[3:4]:
        items = data.select("td")
        
        for item in items:
            print(item)

            # sor



