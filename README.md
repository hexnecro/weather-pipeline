# Weather Pipeline

A small Python data pipeline that fetches live weather for 5 South African cities from the Open-Meteo API (no API key needed).
It extracts the data, shapes it into a pandas DataFrame, and appends it to `weather.csv`, so every run adds to the history.
Run it with `pip install requests pandas` then `python pipeline.py`.
The CSV has 5 columns: `city`, `temperature`, `windspeed`, `observed_at` (time from the API) and `fetched_at` (time the script ran).
Every request has a timeout, and a failed city is reported and skipped while the others still save.
If every city fails, nothing is written to the file, so a bad run can never corrupt the data.
