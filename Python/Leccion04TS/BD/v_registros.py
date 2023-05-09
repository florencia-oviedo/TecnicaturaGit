import psycopg2 #esto es para conectar con postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #placeholder
            entrada = input("Digite los id_persona (separados por coma): ")
            llaves_primarias = (tuple(entrada.split(',')),) #convertimos en tupla lo q ingrese el usuario
            cursor.execute(sentencia,llaves_primarias) #De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() #recuperamos todos los registros que seran una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
