init:
	docker compose run airflow-webserver airflow users create -r Admin -u airflow -p 1234 -e airflow@airflow.com -f airflow -l airflow
	docker compose run airflow-webserver airflow db migrate