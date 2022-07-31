from airflow.models import DAG
from datetime import timedelta,datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor

import download_price

import get_open_close_diff

today = datetime.today()
today = today.replace(hour= 17 ,minute= 49, second=0, microsecond= 0) 

default_args = {
            "owner": "airflow",
            "start_date": today,
            "depends_on_past": False,
            "email_on_failure": False,
            "retries": 2, # retry twice
            "retry_delay": timedelta(minutes=5) # five minutes interval
}

dag = DAG(
    dag_id = 'marketvol2',
    schedule_interval="0 18 * * 1-5", # Running at 6pm for weekdays
    default_args = default_args,
    description = 'A simple DAG',    
 )

task_0 = BashOperator(
    task_id="task_0",
    bash_command='''mkdir -p $AIRFLOW_HOME/tmp/data/''' + str(today), #naming the folder with the current day
    dag = dag
)
task_1 = PythonOperator(
    task_id="task_1",
    python_callable= download_price.main,
    op_kwargs={'ticker': 'AAPL'},
    dag = dag
)

task_2 = PythonOperator(
    task_id="task_2",
    python_callable= download_price.main,
    op_kwargs={'ticker': 'TSLA'},
    dag = dag
)

task_3 = BashOperator(
    task_id="task_3",
    bash_command='''mv $AIRFLOW_HOME/AAPL_data.csv $AIRFLOW_HOME/tmp/data/'''+ str(today.date()), # .date is removing the time.
    dag = dag
)

task_4 = BashOperator(
    task_id="task_4",
    bash_command='''mv $AIRFLOW_HOME/TSLA_data.csv $AIRFLOW_HOME/tmp/data/'''+ str(today.date()), # .date is removing the time.
    dag = dag
)

task_5 = PythonOperator(
    task_id="task_5",
    python_callable=get_open_close_diff.main,
    dag = dag
)

task_0 >> [task_1,task_2]

task_1 >> task_3
task_2 >> task_4

[task_3,task_4]>>task_5