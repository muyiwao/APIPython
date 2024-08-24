# Flask API Project

## Overview
This project is a Flask API that connects to a PostgreSQL database and exposes endpoints for data retrieval.

## Enhancement
Integrate automated testing using Pytest and implement data validation with Great Expectations to ensure data quality and robustness of the Flask API.

## Setup
### Clone the repository:
```bash
git clone https://github.com/muyiwao/APIPython.git
cd APIPython
```

## Project Structure
```bash
APIPython/
│
├── great_expectations/
│   ├── notebooks/
│   │   ├── edit_expectation_suite.ipynb
│
├── src/
│   ├── __init__.py
│   ├── dbapi.py
│   ├── pythonPostgress.py
│
├── tests/
│   ├── __init__.py
│   ├── test_dbapi.py

├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── .env
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
└── data/
    ├── customers.csv
    └── data.json

```

## Documentation
[DOC - Automated Flask API: Data Retrieval and API Deployment](https://docs.google.com/document/d/1x2HqVoatImTDcMQ8bwDp_8liu50ZY28idWoBswVBboA/edit?usp=sharing)

[PPT - Automated Flask API: Data Retrieval and API Deployment](https://docs.google.com/presentation/d/1POA9AAxhL9brIXMqqRh0sMiqjhSvTKNCBguFZPrcpek/edit?usp=sharing)



