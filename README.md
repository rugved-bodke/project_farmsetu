# FarmSetu

## Task 
- Create a Django Application to parse summarised weather data available from UK MetOffice, save it within the database and serve it via restful API.

## Evaluation Criteria:
- Project Setup
- Parser 
- Data modelling 
- API Docs 
- Tests 
- Docker

## Link 
- Data - https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series#yearOrdered

## Installation Guide
```
git clone https://github.com/rugved-bodke/project_farmsetu.git
cd project_farmsetu
docker build -f Dockerfile -t farmsetu-app:0.1 .
docker-compose up --build -d / docker run farmsetu-app 
```

## Links

Project is hosted on render and database is hosted on same platform.

https://project-farmsetu.onrender.com

API endpoints are:<br>
[GET]

https://project-farmsetu.onrender.com/api/min_temp/<br>
https://project-farmsetu.onrender.com/api/max_temp/<br>
https://project-farmsetu.onrender.com/api/mean_temp/<br>
https://project-farmsetu.onrender.com/api/rainfall/<br>
https://project-farmsetu.onrender.com/api/sunshine/<br>
https://project-farmsetu.onrender.com/api/rain_days/<br>
https://project-farmsetu.onrender.com/api/air_frost/<br>
### Get Connected [📱](tel:9112942949) [📧](mailto:rugvedbodke@yahoo.com) [☕️](https://bold.pro/my/rugved-bodke)

