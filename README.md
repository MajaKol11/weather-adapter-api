# Weather Adapter API

A minimal FastAPI adapter that accepts `?query=City,CountryCode`, fetches OpenWeather server-side, and returns a small, stable JSON payload for my own projects.

## Setup (quick)
- Python 3.10+ recommended
- Create a virtual environment
- Install deps
- Add `.env` with `OWM_API_KEY=...`
- Run with `uvicorn main:app --reload`
