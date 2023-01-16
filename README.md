# Demo
Basic python api app with fastapi using poetry and fire with some xml validation using xsd.

# Requirements
- Python >= 3.10
- Poetry >= 1.3.2
- Docker (for local testing)
- Uvicorn (for local testing)

# Quick Start
## Poetry/Environment setup
Install poetry dependencies
```shell
poetry install
```

Lists commands for demo
```shell
poetry run demo -- --help
```

Convert csv data to valid and invalid xml data
```shell
poetry run demo xml 'path/to/csv'
```

Validate xml file against xsd file
```shell
poetry run validate 'path/to/xsd' '/path/to/xml'
```

## Launch DynamoDB(local) and fastapi 
CD into api directory
```
cd api
```

Run docker-compose to start local DynamoDB
```
docker-compose up
```

Start api with uvicorn(port 5000 since DynamoDB uses 8000, can be whatever port you want)
```
uvicorn fast_api:app --reload --port 5000
```

You can navigate to 127.0.0.1:5000/docs to use fastapi Swagger UI docs to test api calls.

# TODO

- Data calculations with api calls/lamda
- Standup using aws with terraform
