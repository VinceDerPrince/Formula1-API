from fastapi import FastAPI
import scraper as _scraper

app = FastAPI()

@app.get("/")
async def route():
    return {"message":"Welcome to this unoffical Formula1 API"}

@app.get("/get_race_results")
async def get_race_results(year: int, grand_prix: str):
    return _scraper.get_all_results(year, grand_prix)