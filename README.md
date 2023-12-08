## _**TITLE**_:
Nuit d'Info Hackathon Project: Open Data et Géo-Intelligence

## _**DESCRIPTION**_: 
Welcome to GeoPollution API, a project developed during the "Nuit d'Info" hackathon proposed by Camp to Camp. This API is designed to provide users with valuable insights into air pollution in world cities, leveraging the power of data integration and manipulation.

## _**USED TECHNOLOGIES**_:
Flask: The web framework that powers our API, offering a lightweight and modular architecture.
Pandas: A powerful data manipulation library used for merging and analyzing datasets.
Thefuzz: Employed for fuzzy string matching, enhancing the accuracy of data integration.
Deep_translator: Applied for multilingual support, ensuring accessibility for a global audience.

## _**ENDPOINTS**_

Endpoint: /countries
Description: Retrieve a list of all countries with available air pollution data.

Endpoint: /?country=xxx
Description: Get air pollution data for a specific country by providing the country name in the query parameter.

Endpoint: /?city=xxx
Description: Retrieve air quality information for a specific city by specifying the city name in the query parameter.

Endpoint: /?type=xxx
Description: Filter air pollution data based on a specific type, such as particulate matter or pollutant gases.

## _**INSTALLATION**_:
```
pip install -r requirements.txt
flask --app main run       
```

## _**RESOURCES**_:
- [Global Air Pollution Dataset - kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)
- [World Cities Database - simple maps](https://simplemaps.com/data/world-cities)