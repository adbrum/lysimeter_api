# Create container docker
docker run -it -p 1883:1883 -p 9001:9001 -v --name lysimeter-mosquitto mosquitto.conf:/mosquitto/config/mosquitto -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

docker run -it -p 1880:1880 --name lysimeter-nodered --link lysimeter-mosquitto:broker nodered/node-red-docker

# Create container lysimeter_rest_api
docker build . ou docker-compose up --build
