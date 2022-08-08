import pymysql
pymysql.install_as_MySQLdb()
import csv

def flow_data_to_mysql():
    DATA_PATH = 'Data/data.csv'

    mydb = pymysql.connect(
        host='localhost', 
        user='tahir', 
        password='********',
    )

    with open(DATA_PATH) as csv_file:
        csv_file = csv.reader(csv_file, delimiter=',')
        all_values = []
        for row in csv_file:
            value = (row[0], row[1])
            all_values.append(value)

    # Drop Column names from list
    all_values = all_values[1:]

    # # CREATE DATABASE IN MYSQL
    create_database_in_mysql = '''
        CREATE DATABASE IF NOT EXISTS `worlddata`;
    '''

    # # USE DATABASE IN MYSQL
    use_database_in_mysql = '''
        USE `worlddata`;
    '''

    # # CREATE TABLE IN MYSQL
    create_table_in_mysql = '''
        CREATE TABLE IF NOT EXISTS `reachescountries` (
            Country VARCHAR(100),
            Adjusted_GDP_capita VARCHAR(100)
        );
    '''

    # INSERT CSV FILE TO MYSQL TABLE
    insert_data_to_mysql = '''
        INSERT INTO `reachescountries`(
            `Country`, 
            `Adjusted_GDP_capita`
        ) 
        VALUES (%s, %s);
    '''

    # EXECUTE THE QUERY
    mycursor = mydb.cursor()
    mycursor.execute(create_database_in_mysql)
    mycursor.execute(use_database_in_mysql)
    mycursor.execute(create_table_in_mysql)
    mycursor.executemany(insert_data_to_mysql, all_values)
    mydb.commit()

    print('\n\n[INFO]------DATA FLOW TO DATABASE DONE')
