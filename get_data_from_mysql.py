import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd


def get_table():

    mydb = pymysql.connect(
        host='localhost', 
        user='tahir', 
        password='********',
        database='worlddata'
    )

    # GET TABLE FROM DATABASE
    query = '''
        SELECT * FROM reachescountries;
    '''

    # CURSOR
    mycursor = mydb.cursor()
    mycursor.execute(query)

    # GET RESULT OBJECT
    result = mycursor.fetchall()
    headers = [i[0] for i in mycursor.description]

    # CONVERT RESULT TO DATAFRAME 
    data = pd.DataFrame(result, columns=headers)
    
    print('\n\n[INFO]------GETTING DATA FROM DATABASE DONE')

    return data


