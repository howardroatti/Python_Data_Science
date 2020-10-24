#importando as bibliotecas que vamos usar nesse exemplo
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

#Definindo alguns argumentos básicos
default_args = {
        'owner': 'Howard',
        'depends_on_past': False,
        'start_date': datetime(2020, 4, 4),
        'retries': 0
        }

'''Nomeando a DAG e definindo quando ela vai ser executada (você pode
usar argumentos de Crontab também caso queira que a DAG execute por
exemplo todos os dias as 8 da manhã'''

with DAG(
        'dag_poc_mysql_into_postgres',
        schedule_interval=timedelta(minutes=60),
        catchup=False,
        default_args=default_args
        ) as dag:
#Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
    t1 = BashOperator(task_id='insert_into_mysql',
                      bash_command="""
                      cd $AIRFLOW_HOME/dags/etl_scripts/
                      python3 elt_insert_into_mysql.py
                      """)

    t2 = BashOperator(task_id='select_from_mysql_insert_into_postgres',
                      bash_command="""
                      cd $AIRFLOW_HOME/dags/etl_scripts/
                      python3 elt_select_mysql_insert_postgres.py
                      """)
#Definindo o padrão de execução, nesse caso executamos t1 e depois t2
    t1 >> t2
