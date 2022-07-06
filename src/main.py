from fastapi import FastAPI
import scraper as _scraper

app = FastAPI()

@app.get("/")
async def route():
    return {"message":"Welcome to this unoffical Formula1 API"}

@app.get("/get_race_results")
async def get_race_results(year: int, track: str):
    return _scraper.get_race_results(year, track)

@app.get("/get_quali_results")
async def get_quali_results(year: int, track: str):
    return _scraper.get_qualifying_results(year, track)
