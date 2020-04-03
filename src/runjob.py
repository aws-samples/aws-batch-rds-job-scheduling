import boto3
import base64
from botocore.exceptions import ClientError
import json
import psycopg2

def job_exec():

    secret_name = "batchjob-secret"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    response = client.get_secret_value(
    SecretId=secret_name
    )

    secret = json.loads(response['SecretString'])
    
    print(secret['username'])
    #print(secret['password'])
    print(secret['dbname'])
    print(secret['host'])
    
    db_host=secret['host']
    db_user=secret['username']
    db_pwd=secret['password']
    db_name=secret['dbname']

    conn = psycopg2.connect(database=db_name, user=db_user,password=db_pwd, host=db_host)
    cur = conn.cursor()

    # Call stored procedure
    cur.callproc('low_high_salaries', (10,))
    # process and print highest and lowest salary in dept 10
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
    # close the communication with the PostgreSQL database server
    cur.close()
    conn.close() 

job_exec()  