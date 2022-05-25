import mysql.connector
from mysql_setup import sql_connection


def create_relationaldb_dwh(mydbsql):
    """
    Creates a relational database, tables
    and add some test values in Mysql
    """
    mycursor = mydbsql.cursor()

    try:
        mycursor.execute("""
            DROP DATABASE IF EXISTS bankaya_dwh;
            CREATE DATABASE bankaya_dwh;
            USE bankaya_dwh;

            CREATE TABLE IF NOT EXISTS dwh_customers(
                customer_id              INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                first_name               NVARCHAR(50)NULL,
                last_name                NVARCHAR(50)NULL,
                phone                    BIGINT NULL,
                curp                     NVARCHAR(18)NOT NULL UNIQUE,
                rfc                      NVARCHAR(13)NOT NULL UNIQUE,
                adress                   NVARCHAR(300)NULL,
                created_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                active_flg               TINYINT(1)NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS dwh_items(
                item_id                  INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                item_name                NVARCHAR(50)NOT NULL,
                item_price               DOUBLE(12,2)NOT NULL DEFAULT 0.0,
                created_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                active_flg               TINYINT(1)NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS dwh_sales(
                operation_id             INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                client_id                INTEGER NOT NULL,
                item_id                  INTEGER NOT NULL,
                item_price               DOUBLE(12,2)NOT NULL,
                comment                  NVARCHAR(300)NULL,
                created_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                active_flg               TINYINT (1)NOT NULL DEFAULT 1
            );"""
            )
    except Exception as ex:
        print("Algo salio mal. Revisa tu instalacion de MySQL y tus credenciales" + ex)
    else:
        print("Creacion exitosa")


def run():
    create_relationaldb_dwh(sql_connection())


if __name__ == "__main__":
    run()