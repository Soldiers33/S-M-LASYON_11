import requests
import datetime
now = datetime.datetime.now(datetime.timezone.utc)
start_time = now.strftime('%Y-%m-%d')
stop_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

params = {
    "format": "text",
    "COMMAND": "'301'",
    "OBJ_DATA": "'YES'",
    "MAKE_EPHEM": "'YES'",
    "EPHEM_TYPE": "'OBSERVER'",
    "CENTER": "'500@399'",
    "START_TIME": f"'{start_time}'",
    "STOP_TIME": f"'{stop_time}'",
    "STEP_SIZE": "'1 d'",
    "QUANTITIES": "'19,20'",
    "CSV_FORMAT": "'YES'"
}

response = requests.get("https://ssd.jpl.nasa.gov/api/horizons.api", params=params, timeout=10)
print(response.text)
