import psycopg2 #esto es para conectar con postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) #De esta manera ejecutamos la sentencia
registros = cursor.fetchall() #recuperamos todos los registros que seran una lista
print(registros) #[(1, 'Juan', 'Perez', 'jperez@gmail.com'), (2, 'Carla', 'Gomez', 'kgomez@gmail.com')]
cursor.close()
conexion.close()
