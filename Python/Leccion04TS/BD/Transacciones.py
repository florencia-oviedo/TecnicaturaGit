import psycopg2 as bd #esto es para conectar con postgresql

conexion = bd.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    #conexion.autocommit = False #esto no deberia estar
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre,apellido,email) values (%s,%s,%s)"
    valores = ('Maria','Esparza','mesparza@gmail.com')
    cursor.execute(sentencia,valores)
    conexion.commit() #hacemos commit manualmente
    print("Termina la transaccion")
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()