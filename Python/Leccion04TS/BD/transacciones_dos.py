import psycopg2 as bd #esto es para conectar con postgresql

conexion = bd.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    conexion.autocommit = False #esto no deberia estar, se inicia la transaccion
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre,apellido,email) values (%s,%s,%s)"
    valores = ('Jorge','Prol','jprol@gmail.com')
    cursor.execute(sentencia,valores)
    sentencia = "UPDATE persona SET nombre=%s , apellido=%s, email =%s WHERE id_persona =%s"
    valores = ('Juan Carlos','Perez','jcperez@gmail.com',1)
    cursor.execute(sentencia,valores)
    conexion.commit() #hacemos commit manualmente, se cierra la transaccion
    print("Termina la transaccion")
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()