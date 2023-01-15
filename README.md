# Demo
Basic python api app with fastapi using poetry and fire with some xml validation using xsd.

# Requirements
- Python >= 3.10
- Poetry >= 1.3.2

# Quick Start

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
# TODO

- Implement dynamodb to work with api
- Data calculations with api call/lamda
- Standup using aws
