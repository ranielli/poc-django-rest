# Customer API test 

## Features
* Import csv file via django command
* get the longitude and latitude of the address
* access each registered customer
* API unit tests

## technologies used :
* django rest framework
* django
* docker
* geocode google
* sqlite

 ### Prerequisites

Before starting, you will need to have the following tools installed on your machine:
[Git](https://git-scm.com), [Docker](https://docs.docker.com/engine/install/ubuntu/). 

### 🎲 Run o Back End (server)

```bash
# Clone this repository
$ git clone https://github.com/ranielli/challenge-drf.git

# Access the project folder in terminal/cmd
$ cd challeng-drf


# install dependencies and create database
$  docker-compose run app ./manage.py migrate

# Run the application in development mode
$ docker-compose up

# The server will start on port:8000- acesse <http://localhost:8000/api/v1/customers/>
```
