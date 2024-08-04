# FastAPI + Kafka
## _Example, template app_

An example of a web application using Kafka and FastAPI. 

- Python ^3.10 + Poetry
- Separated environments
- Simple building via Docker Compose (+source code mounted into container)

## Installation
Required Python 3.10
Install packages:
```sh
poetry shell    # .vevn should be created
poetry install  # Installs requeired packages 
```

## Development
1. Via containers.
    * Default values for env. variables are set in docker-compose.yaml
    * The src directory mounted in Docker container, so You can develop with running container and see your changes almost permanently (rebuild if some packages were added).
    * One network with hostnanes.
2. Via uvicorn 
    * Debug web-app

## Docker
Tested on versions Docker Compose v2.24 and Docker v25.0.3.


```sh
chmod -R a+rw .         # Give permissions
docker-compose build    # Build containers
docker-compose up -d    # Run containers
```
There You will see 4 service: BackEnd app, Kafka and Redis (via broker) and Zookeeper for metada.

```sh
docker-compose down     # To stop services
```

## Uvicorn
Run as usual FastAPI app:
```sh
uvicorn src.main:app --reload      # If workdir -> Connect
uvicorn main:app --reload          # If workdir -> src
```
Kafka should be started on start up via context.  
For local developmet rename `src/settings/.env.example` into `.env` and uncomment all params. This `.env` will be used to set up FastAPI configuration (develop and prod are available)
## License
MIT


