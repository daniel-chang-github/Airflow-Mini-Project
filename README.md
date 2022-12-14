# Airflow-Mini-Project


In this project, you’ll use Apache Airflow to create a data pipeline to extract online stock market data and deliver analytical results. You’ll use Yahoo Finance as the data source. Yahoo Finance provides intra-day market price details down a one-minute interval.

The learning objects of this mini project are:
- Use text processing techniques in Python to make sense of logs
- Learn where logs are located in Airflow
- Learn how to monitor automated Airflow DAGs to ensure they are working properly


# Docker
The DAGs are located in mnt/airflow/dags directory

Then execute ./start.sh script. This should build and start all the services.
Execute docker-compose ps and you should see below.
![image](https://user-images.githubusercontent.com/81652137/182059729-65793218-b83d-4cd6-8eb1-ce6f94fabbe0.png)
Go to localhost:8080 for the airflow UI.
The userid and password is airflow.
After completing you can use ./stop.sh to stop the services


# Graph View

![image](https://user-images.githubusercontent.com/81652137/182043061-5af6547d-2aae-4d35-bcbc-1629d1b78141.png)


# Tree View

![image](https://user-images.githubusercontent.com/81652137/182043084-a62760eb-92a6-4604-8bfe-0ab4cbcfbe6d.png)

## Log of the last task
### An example of successful execution
![image](https://user-images.githubusercontent.com/81652137/182045406-1c03f528-3704-42cc-9605-8aecbf1364ce.png)

# Log analyzer

Log analyzer will collect all ERRORs from logs and display them all. It will show the total number of errors, which log the error message is from, and the actual error message.

![image](https://user-images.githubusercontent.com/81652137/182064639-a79a3b00-445b-4177-8a96-ab3c7344dc5f.png)

