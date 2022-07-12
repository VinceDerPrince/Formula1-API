# Formula 1 API
An API to get the popular quotes from the sport section of the site [bbc.com](https://www.bbc.com/sport/formula1).

## Features
You can get:
* the results to a specific race of the season:
![race results](/images/race_results.gif)
* the results to a specific qualifying of the season:
![qualifying results](/images/qualifying_results.gif)
* the results to a specific practice of the season:
![practice results](/images/practice_results.gif)

## Setup
### Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
Or use any virtual environment you like.

### Uvicorn
To show the UI I used in the Introduction, we use uvicorn.
You do this as such:
```
uvicorn main:app --reload
```
It should know look like this in your terminal and a browser Window with the API UI should show up. To get this better looking interface, as in my preview of the features, append "/docs" at the end of the link in your browser!

![Uvicorn Setup](/images/uvicorn_setup.png)

## Need To Know
This API is not to be used neither is being used for commercial use exists to hurt the [bbc.com](https://www.bbc.com/sport/formula1) site. 
The API was created because I want to practice my API developing and web scraping skills!
