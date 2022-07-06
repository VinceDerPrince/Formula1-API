from typing import Dict,List
import requests as _requests
import bs4 as _bs4

def _generate_url(year: int, place:str) -> str:
    place = place.replace(" ", "-")
    url = f"https://www.bbc.com/sport/formula1/{year}/{place}-grand-prix/results"
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def get_all_results(year: int, place: str) -> Dict:
    #return results of a specific race
    url = _generate_url(year, place)
    page = _get_page(url)
    raw_placements = page.find_all(class_ = "gs-u-vh")
    placements = [placement.text for placement in raw_placements]
    placements = placements[4:]
    chunks = [placements[x:x+8] for x in range(0, len(placements), 8)]
    final = dict()
    for i in range(len(chunks)):
        final[i+1] = {
            "driver": chunks[i][0],
            "number": chunks[i][1],
            "grid": chunks[i][2],
            "pits": chunks[i][3],
            "fastest-lap": chunks[i][4],
            "race-time": chunks[i][5],
            "points": chunks[i][6]
        }
    
    return final

print(get_all_results(2022,"british"))
