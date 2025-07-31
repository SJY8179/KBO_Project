
import requests
from bs4 import BeautifulSoup
from libs.requests import get_request_header
import json

def get_hitter():
    header= get_request_header()

    res = requests.get("https://www.welcometopranking.com/baseball/?p=chart&searchType=DAILY&searchDate=2025-07-20&position=T&team=2002&page=1&orderBy=&orderSort=", headers=header);

    if res.ok:

        html = res.text

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, "html.parser") 

        trs = soup.select("table.type01 > tbody > tr")
        all_players = []

        for tr in trs:
            tds = tr.select("td")
            texts = [td.get_text(strip=True) for td in tds]
            # 선수 1명당 14개 항목, 몇 명인지 계산
            num_players = len(texts) // 14

        for i in range(num_players):
            chunk = texts[i * 14:(i + 1) * 14]

            player = {
                "rank": chunk[0],
                "name": chunk[1],
                "team": chunk[2],
                "top_rank_point": chunk[3],
                "base_point": chunk[4],
                "win_point": chunk[5],
                "hit_ratio": chunk[6],
                "hit": chunk[7],
                "homerun": chunk[8],
                "hit_score": chunk[9],
                "walk": chunk[10],
                "go_ratio": chunk[11],
                "on_base": chunk[12],
                "ops": chunk[13]
            }

            all_players.append(player)

            # JSON 저장
            with open("hitters.json", "w", encoding="utf-8") as f:
                json.dump(all_players, f, ensure_ascii=False, indent=4)

            print("hitters.json 저장 완료")


get_hitter()

