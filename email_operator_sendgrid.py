import datetime

import airflow
from airflow.operators.email import EmailOperator


with airflow.DAG (
    "composer_sample_sendgrid",
    start_date = datetime.datetime(2022,1,1),
) as dag:
    task_email = EmailOperator(
        task_id = "send-email"
        conn_id = "sendgrid_default"
        to = "kulraj0000@gmail.com"
        subject = "EmailOperator test for Sendgrid"
        html_content = "This is a test message sent through sendgrid",
        dag = dag,
    )