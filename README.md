
# Сервис прогноза погоды

# Установка
-  ``` git clone git@github.com:EkaterinaBurenina/weather_servise.git  ```
- ``` cd weather_service```
- ``` export LISTEN_PORT=8003```
- ``` python3 server.py```

# Примеры запросов
request: ```0.0.0.0:8003/v1/current/?city=Tambov``` 

response: ``` {"city": "Tambov", "unit": "celsius", "temperature": 8} ```

request: ```0.0.0.0:8003/v1/forecast/?city=Tambov&dt=2018-10-07``` 

response: ``` {"city": "Tambov", "unit": "celsius", "temperature": 11} ```
