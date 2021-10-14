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

### 🎲 Run the Back End (server)

```bash
# Clone this repository
$ git clone https://github.com/ranielli/challenge-drf.git

# Access the project folder in terminal/cmd
$ cd challeng-drf

# install dependencies, create database and run migrates
$  docker-compose run app ./manage.py migrate

# Import csv with the customers command (It's important to run it to the end otherwise it won't save the objects)
$  docker-compose run app ./manage.py load_csv_customers customers.csv

# Run the application
$ docker-compose up

# The server will start on port:8000- acesse <http://localhost:8000/api/v1/customers/>
```
