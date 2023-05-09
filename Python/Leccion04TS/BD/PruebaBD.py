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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #placeholder
            id_persona = input("Digite un número para la id_persona: ")
            cursor.execute(sentencia,(id_persona,)) #De esta manera ejecutamos la sentencia
            registros = cursor.fetchone() #recuperamos todos los registros que seran una lista
            print(registros) #[(1, 'Juan', 'Perez', 'jperez@gmail.com'), (2, 'Carla', 'Gomez', 'kgomez@gmail.com')]
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#cursor.close() Ya no es necesario porque usamos with

# https://www.psycopg.org/docs/usage.html