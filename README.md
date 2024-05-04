# traffic_data_warehouse

## Overview
A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. The company is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. 

The data warehouse take into account future needs, organise data such that a number of downstream projects query the data efficiently. I use the Extract Load Transform (ELT) framework using DBT. The ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis. 




## Objectives
Building data warehouse techstack
- Consisting of
    
    - A “data warehouse” (PostgresQL)
    - An orchestration service (Airflow)
    - An ELT tool (dbt)
    - A reporting environment (redash)
    - Fully dockerized

## Screenshot
![Screenshot 2024-05-04 115241](https://github.com/nyutu-grace/traffic_data_warehouse/assets/135698958/a1a00025-b9a1-4d1a-8045-d2da21a72a50)


##  Dataset
- [Data(pNEUMA dataset )](https://open-traffic.epfl.ch/index.php/downloads/#1599047632450-ebe509c8-1330)
## Project Structure
- data: Contains the dataset
- dbt: Contains dbt related files
- airflow: contains airflow related files
- scripts: Contains script codes
- logs: contains log files
- tests: Unit test files




  
