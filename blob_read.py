import psycopg2
try:
        # read data from a picture
        drawing = open('C:\\Users\\jungiewicz_a\\Desktop\\Siemens-Veros.pdf', 'rb').read()
        # read database configuration

        conn = psycopg2.connect("dbname=testdb user=postgres password=l")
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO drawing(drawing) " +
                    "VALUES(%s)",
                    (psycopg2.Binary(drawing),))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)