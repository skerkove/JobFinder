

cities={
        "city":{
                "Minneapolis":{
                        "lat": 5,
                        "lon": 6
                        },
                "Chicago":{
                        "lat": 6,
                        "lon": 7
                        },
                "New York":{
                        "lat": 7, 
                        "lon": 9
                        },
                "Los Angelos":{
                        "lat": 8,
                        "lon": 10
                        }
            }
    }

def locList(cities):
    cityList = []
    for city in cities["city"]:
        city = city.replace(" ", "+")
        cityList.append(city)
    return(cityList)