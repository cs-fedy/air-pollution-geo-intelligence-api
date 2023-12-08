from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def geo_location_data():
    country = request.args.get("country")
    city = request.args.get("city")
    data_type = request.args.get("type")

    if data_type != "ozone" and data_type != "carbon":
        data_type = "all"

    with open("formatted_data.json", "r") as file:
        raw_data = file.read()
        data = json.loads(raw_data)

    filtered_data = data
    if country:
        filtered_data = [row for row in data if row["country"] == country]

    if city:
        filtered_data = [row for row in data if row["city"] == city]

    if data_type == "ozone":
        filtered_data = [
            {
                "country": row["country"],
                "city": row["city"],
                "coordinates": row["coordinates"],
                "ozone_aqi_value": row["ozone_aqi_value"],
                "ozone_aqi_category": row["ozone_aqi_category"]
            }
            for row in data
        ]

    if data_type == "carbon":
        filtered_data = [
            {
                "country": row["country"],
                "city": row["city"],
                "coordinates": row["coordinates"],
                "aqi_value": row["aqi_value"],
                "aqi_category": row["aqi_category"]
            }
            for row in data
        ]

    return {"data": filtered_data, "data_type": data_type}


@app.route("/countries")
def countries_names():
    with open("formatted_data.json", "r") as file:
        raw_data = file.read()
        data = json.loads(raw_data)

    countries = {row["country"] for row in data}
    return {"data": list(countries)}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
