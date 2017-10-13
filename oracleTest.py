import cx_Oracle
import os
import sys

def handler(event, context):

    #f = open('/tmp/HOSTALIASES','w')
    #str_host = os.uname()[1]
    #f.write(str_host + ' localhost\n')
    #f.close()
    #os.environ["HOSTALIASES"] = "/tmp/HOSTALIASES"
    
    sys.path.append('./lib')
    print(sys.path)

    print(os.environ["LD_LIBRARY_PATH"])
    os.environ["LD_LIBRARY_PATH"] += ":./lib"
    print(os.environ["LD_LIBRARY_PATH"])

    print("This is a log message from Python 3.6!")

    con = cx_Oracle.connect("admin", "adminadmin", "myoracletest.cvbjqjhsfcqp.us-west-2.rds.amazonaws.com/ORCL")
    #dsnStr = cx_Oracle.makedsn("myoracletest.cvbjqjhsfcqp.us-west-2.rds.amazonaws.com", "1521", "ORCL")
    #con = cx_Oracle.connect(user="admin", password="adminadmin", dsn=dsnStr)

    print (con.version)
    #print(os.environ)

    cursor = con.cursor()
    querystring = "select * from Customers"

    for result in cursor.execute(querystring):
        print(result)
    print()

    return { "body" : "hellow from Python 3.6" }