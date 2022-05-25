import pymongo


def nosql_connection():
    """
    Connects to mongodb
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Bankayadb"]
    return (mydb)


def create_norelationaldb():
    """
    Creates a no relational database, collections
    and add some test values in Mongodb
    """
    mydb = nosql_connection()
    colcustomers = mydb["customers"]
    colitems= mydb["items"]

    mycustomers = [
        {"_id":1,"firstname":"Bruce","lastname":"Wayne"},
        {"_id":2,"firstname":"Clark","lastname":"Kent"},
        {"_id":3,"firstname":"Tony","lastname":"Stark"}
        ]

    myitems = [
        {"_id":1,"title":"USM","price":10.2},
        {"_id":2,"title":"Mouse","price":12.23},
        {"_id":3,"title":"Monitor","price":199.99}
        ]

    try:
        colcustomers.drop()
        colitems.drop()
        id_customers = colcustomers.insert_many(mycustomers)
        id_items = colitems.insert_many(myitems)
    except Exception as ex:
        print("Algo salio mal. Revisa tu instalacion de Mongodb" + ex)
    else:
        print("customers insertados")
        print("items insertados")


def run():
    create_norelationaldb()


if __name__ == "__main__":
    run()