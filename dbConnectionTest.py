import psycopg2
import config
import public_config
import private_config


def getDbConfig(settings):
    db_settings = settings['db_settings']

    # For now you can keep the True value, but here a check can come (by environment variable, or ip, or url, or ...)
    is_dev = True
    # here comes a check if server is test
    is_test = False
    # here comes a check if server is prod
    is_prod = False

    if is_dev:
        return db_settings['dev']
    elif is_test:
        return db_settings['test']
    elif is_prod:
        return db_settings['prod']
    
    return dict()

try:
    # get config data
    config_data = getDbConfig(config.getSettings())
    # setup connection string
    connect_str = "dbname='" + config_data['db_name'] + "' user='" + config_data['user'] + "' host='" + config_data['host'] + "' password='" + config_data['password'] + "'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # removing the test table if it already exists
    cursor.execute("""DROP TABLE IF EXISTS connection_check;""")
    # create a new table with a single column called "name"
    cursor.execute("""CREATE TABLE connection_check (name varchar(40));""")
    # Insert a row to see something in the output
    cursor.execute("""INSERT INTO connection_check VALUES ('It works!');""")
    # run a SELECT statement
    cursor.execute("""SELECT * FROM connection_check;""")
    # Fetch and print the result of the last execution
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)