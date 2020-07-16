from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'db_host': os.getenv("MYSQL_HOST"),
    'db_user': os.getenv("MYSQL_USER"),
    'db_password': os.getenv("MYSQL_PASSWORD"),
    'db_name': os.getenv("MYSQL_DB"),
    'db_port': os.getenv("MYSQL_PORT")
}