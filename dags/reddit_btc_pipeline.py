from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import ShortCircuitOperator
from datetime import datetime
import subprocess

default_args = {
    'start_date': datetime(2025, 5, 20),
}

def check_new_posts_logic():
    result = subprocess.run(
        ['python', 'scripts/check_new_reddit_posts.py'],
        cwd='/opt/airflow/user_pipeline',
        capture_output=True,
        text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    return result.stdout.strip().lower() == "true"

with DAG(
         dag_id = "reddit_btc_pipeline",
         schedule="0 */1 * * *",  
         default_args=default_args,
         catchup=False
         )as dag:
    
    check_new_posts = ShortCircuitOperator(
        task_id = "check_new_reddit_posts",
        python_callable = check_new_posts_logic
    )

    fetch_btc_price = BashOperator(
        task_id="fetch_btc_price",
        bash_command="cd /opt/airflow/user_pipeline && python scripts/fetch_BTC_price.py"
    )

    run_pipeline = BashOperator(
        task_id="run_pipeline",
        bash_command="cd /opt/airflow/user_pipeline && python scripts/daily_pipeline.py"
    )

    check_new_posts >> fetch_btc_price >> run_pipeline
