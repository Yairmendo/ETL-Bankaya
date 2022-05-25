import pandas as pd
from mysql_setup import sql_connection
from mongo_setup import nosql_connection


def sql_extraction():
    """
    Extract data from a relational data base
    """
    try:
        mysqldb = sql_connection(1)
        mycursor = mysqldb.cursor()
        mycursor.execute(
            """
            SELECT * FROM customers
            """
        )
        sqlcustomers = mycursor.fetchall()
        dfsqlcustomers = pd.DataFrame(sqlcustomers,columns=[
            "customer_id","first_name","last_name","phone","curp","rfc","adress"])

        mycursor.execute(
            """
            SELECT * FROM items
            """
        )
        sqlitems = mycursor.fetchall()
        dfsqlitems = pd.DataFrame(sqlitems,columns=[
            "item_id","item_name","item_price"])
        mycursor.execute(
            """
            SELECT * FROM sales WHERE SUBSTRING(created_at,1,10) = CURDATE();
            """
        )
        sqlsales = mycursor.fetchall()
        dfsqlsales = pd.DataFrame(sqlsales,columns=[
            "operation_id","client_id","item_id","item_price",
            "comment","created_at","updated_at","active_flg"]
            )
    except Exception as ex:
        print(ex)
    else:
        print("SQL Successful extraction")
        return dfsqlcustomers,dfsqlitems,dfsqlsales


def nosql_extraction():
    """
    Extract data from a no relational data base
    """
    try:
        mynosqldb = nosql_connection()
        colcustomers = mynosqldb["customers"]
        dfnosqlcustomers = pd.DataFrame(colcustomers.find({},{"_id":0,"firstname":1,"lastname":1}))
        colitems = mynosqldb["items"]
        dfnosqlitems = pd.DataFrame(colitems.find({},{"_id":0,"title":1,"price":1}))
    except Exception as ex:
        print(ex)
    else:
        print("Mongodb Successful extraction")
        return (dfnosqlcustomers,dfnosqlitems)



def extract():
    """
    Extract data from a relational data base and no relational data
    """
    return(sql_extraction(),nosql_extraction())


def transform(dfsql,dfnosql):
    """
    Transform data from a relational data base and no relational data
    """
    print(dfsql)
    print(dfnosql)

def load():
    pass

def run():
    a,b = extract()
    transform(a,b)

if __name__ == "__main__":
    run()