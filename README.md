# lysimeter_rest_api

# Create container docker
docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

docker run -it -p 1880:1880 --name lysimeter-node-red --link mybroker:broker nodered/node-red-docker
