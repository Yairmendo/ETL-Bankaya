import mysql.connector

def sql_connection(dbcase = 0):
    """
    Connects to a Mysqldb
    """
    hostdb = "localhost"
    userdb = "root"
    passworddb = "toor"
    databasedb = "bankaya"
    try:
        if dbcase == 0:
            mydbsql = mysql.connector.connect(
                host = hostdb,
                user = userdb,
                password = passworddb
                )
        if dbcase == 1:
            mydbsql = mysql.connector.connect(
                host = hostdb,
                user = userdb,
                password = passworddb,
                database = databasedb
                )
        if dbcase == 2:
            mydbsql = mysql.connector.connect(
                host = hostdb,
                user = userdb,
                password = passworddb,
                database = "bankaya_dwh"
                )
    except Exception as ex:
            print(ex)
    else:
        print("Successful connection")

    return mydbsql


def create_relationaldb(mydbsql):
    """
    Creates a relational database, tables
    and add some test values in Mysql
    """
    mycursor = mydbsql.cursor()
    try:
        mycursor.execute(("""
            DROP DATABASE IF EXISTS bankaya;
            CREATE DATABASE bankaya;
            USE bankaya;

            CREATE TABLE IF NOT EXISTS customers(
                customer_id              INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                first_name               NVARCHAR(50)NULL,
                last_name                NVARCHAR(50)NULL,
                phone                    BIGINT NULL,
                curp                     NVARCHAR(18)NOT NULL UNIQUE,
                rfc                      NVARCHAR(13)NOT NULL UNIQUE,
                adress                   NVARCHAR(300)NULL
            );


            CREATE TABLE IF NOT EXISTS items(
                item_id                 INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                item_name               NVARCHAR(50)NOT NULL,
                item_price              DOUBLE(12,2)NOT NULL DEFAULT 0.0

            );


            CREATE TABLE IF NOT EXISTS sales(
                operation_id             INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                client_id                INTEGER NOT NULL,
                item_id                  INTEGER NOT NULL,
                item_price               DOUBLE(12,2)NOT NULL,
                comment                  NVARCHAR(300)NULL,
                created_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at               TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                active_flg               TINYINT(1)NOT NULL DEFAULT 1
            );"""
            ))
    except Exception as ex:
        print("Algo salio mal. Revisa tu instalacion de MySQL y las credenciales" +ex)
    else:
        print("Successful creation")


def fill_sqldb(mydbsql):
    """
    Insert some testing values in Mysql
    """
    mycursor = mydbsql.cursor()
    try:
        sql = "INSERT INTO customers(first_name,last_name,phone,curp,rfc,adress) VALUES(%s,%s,%s,%s,%s,%s)"
        val = [
            ("Bruce","Wayne","5589864799","WAKB390330HNEYYR08", "WAKB390330PL7", "Mexico, Ciudad de Mexico, Centro, Miguel Hidalgo, Av. Revolucion 14"),
            ("Clark","Kent","5589864700","KECC380614HNELLL09", "KECC380614PL7", "Mexico, Ciudad de Mexico, Centro, Miguel Hidalgo, Av. Revolucion 15"),
            ("Tony","Stark","5589864701","STCT630307HNETLN07", "STCT630307PL7", "Mexico, Ciudad de Mexico, Centro, Miguel Hidalgo, Av. Revolucion 16"),
            ("Saitama","Charanko","5589864702","WAKB390331HNEYYR07", "WAKB390331PL7", "Mexico, Ciudad de Mexico, Centro, Miguel Hidalgo, Av. Revolucion 17"),
            ("Chuck","Norris","5589864703","WAKB390329HNEYYR00", "WAKB390329PL7", "Mexico, Ciudad de Mexico, Centro, Miguel Hidalgo, Av. Revolucion 18")
        ]
        mycursor.executemany(sql, val)
        mydbsql.commit()
        sql = "INSERT INTO items(item_name, item_price) VALUES(%s,%s)"
        val = [
            ("USM","10.2"),
            ("Mouse","12.23"),
            ("Monitor","199.99"),
            ("Keyboard","50.50"),
            ("USB","10.12")
        ]
        mycursor.executemany(sql, val)
        mydbsql.commit()
        sql = "INSERT INTO sales(client_id, item_id, item_price) VALUES(%s,%s,%s)"
        val = [
            ("5","1","10.2"),
            ("4","2","12.23"),
            ("3","3","199.99"),
            ("2","4","50.50"),
            ("1","5","10.12"),
            ("3","3","199.99")
        ]
        mycursor.executemany(sql, val)
        mydbsql.commit()
    except Exception as ex:
        print("Algo salio mal. Revisa tu instalacion de MySQL y las credenciales" + ex)
    else:
        print(mycursor.rowcount, " was inserted")


def run():
    create_relationaldb(sql_connection(0))
    fill_sqldb(sql_connection(1))

if __name__ == "__main__":
    run()