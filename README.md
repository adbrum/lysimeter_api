# Create container Mosquitto
docker run -it -p 1883:1883 -p 9001:9001 -v --name lysimeter-mosquitto mosquitto.conf:/mosquitto/config/mosquitto -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

# Create container NODE-RED
docker run -it -p 1880:1880 --name lysimeter-nodered --link lysimeter-mosquitto:broker nodered/node-red-docker

# Create container Rest-Api, MongoDB, Python/Django
docker build . 
ou docker-compose up --build

# DB Django
docker exec -it [NOME DO CONTAINER] python manage.py makemigrations \n
docker exec -it [NOME DO CONTAINER] python manage.py migrate
docker exec -it [NOME DO CONTAINER] python manage.py createsuperuser
