# Everest Weather Gathering
simple scrapping tool to get the data from National Geographic in order to build a database to do some prediction
https://nationalgeographic.org/earthpulse/weather/api/v1/history/combined

# Background
National Geographics have done an awesome job at installing weather station on Mount Everest and are sharing their reading to the whole world freely !

The whole story along with video is available here
https://www.nationalgeographic.com/adventure/article/mount-everest-highest-weather-station-perpetual-planet

![meteo station positions](https://www.nationalgeographic.com/interactive-assets/nggraphics/ngadventure-1906-ngs-everest-map/build-2019-06-12_14-59-00/ngm-assets/img/ngadventure-1906-ngs-everest-map_ai2html-mobile.jpg)

# Stations
there are 5 stations on the mountain.

| station id | station name | altitude |   lat   |   long  |
|------------|--------------|----------|---------|---------|
|      1     | Basecamp     | 5,315 m  | 27.9952 | 86.8406 |
|      2     | Camp II      | 6,464 m  | 27.981  | 86.9023 |
|      3     | South Col    | 7,945 m  |         |         |
|            | Balcony      | 8,430 m  |         |         |
|      6     | Phortse      | 3,810 m  | 27.8456 | 86.7472 |



# Database
code is running in AWS cloud.
the database can be accessible here

http://ec2-34-209-92-115.us-west-2.compute.amazonaws.com:8090/database.csv

