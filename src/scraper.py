import chunk
from typing import Dict,List
import requests as _requests
import bs4 as _bs4

#generate the url which is about to be scraped, depending on the following information
def _generate_url(year: int, place: str, race_type: str) -> str:
    place = place.replace(" ", "-")
    url = f"https://www.bbc.com/sport/formula1/{year}/{place}-grand-prix/results/{race_type}"
    return url

#creates the beautifulsoup object of the page
def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

#gets the race results of the grand price place and the year it was in
def get_race_results(year: int, place: str) -> Dict:
    #return results of a specific race
    url = _generate_url(year, place, "race")
    page = _get_page(url)
    raw_placements = page.find_all(class_ = "gs-u-vh")
    placements = [placement.text for placement in raw_placements]
    placements = placements[4:]
    chunks = [placements[x:x+8] for x in range(0, len(placements), 8)]
    final = dict()
    for i in range(len(chunks)):
        final[i+1] = {
            "driver": chunks[i][1],
            "number": chunks[i][2],
            "grid": chunks[i][3],
            "pits": chunks[i][4],
            "fastest-lap": chunks[i][5],
            "race-time": chunks[i][6],
            "points": chunks[i][7]
        }
    
    return final

#gets the qualifying results of the grand price place and the year it was in
def get_qualifying_results(year: int, place: str) -> Dict:
    #return results of a specific race
    url = _generate_url(year, place, "qualifying")
    page = _get_page(url)
    raw_placements = page.find_all(class_ = "gs-u-vh")
    placements = [placement.text for placement in raw_placements]
    placements = placements[6:]
    chunks = [placements[x:x+7] for x in range(0, len(placements), 7)]
    final = dict()
    for i in range(len(chunks)):
        final[i+1] = {
            "driver": chunks[i][1],
            "number": chunks[i][2],
            "q1": chunks[i][3],
            "q2": chunks[i][4],
            "q3": chunks[i][5],
        }
    
    return final

#gets the practice results of the grand price place and the year it was in
def get_practice_results(year: int, place: str) -> Dict:
    #return results of a specific race
    url = _generate_url(year, place, "practice")
    page = _get_page(url)
    raw_placements = page.find_all(class_ = "gs-u-vh")
    unwanted = ["Qualifying", "Rank", "BBC"]
    placements = [placement.text for placement in raw_placements if placement.text not in unwanted]
    chunks = [placements[x:x+5] for x in range(0, len(placements), 5)]
    split = [chunks[:20], chunks[20:40], chunks[40:60]]
    waba = dict()
    for j in reversed(range(3)):
        final = dict()
        for i in range(20):
            final[i+1] = {
                "driver": split[j][i][1],
                "number": split[j][i][2],
                "fastest-lap": split[j][i][3],
                "laps": split[j][i][4]
            }
        waba[f"{3-j}. training"] = final
    
    return waba