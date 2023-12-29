import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="C:\oracle\instantclient_21_12")
dsn = cx_Oracle.makedsn("54.213.164.78", "1521")


def leer(usuario, password, dsn=dsn):
    dict_usuarios = {}
    conexion = cx_Oracle.connect(user="JAVIER_ARRIAGADA", password="654321", dsn=dsn)
    cursor = conexion.cursor()
    cursor.execute('''Select nombre_usuario,password
              from MAXIMILIANO_DIAZ_MARCHANT.REGISTRO_USUARIO''')
    filas = cursor.fetchall()
    for fila in filas:
        dict_usuarios[fila[0]] = fila[1]
    cursor.close()
    if usuario in dict_usuarios.keys() and password in dict_usuarios.values():
        return True
    else:
        return False


def escribir(usuario, password, dsn=dsn):
    conexion = cx_Oracle.connect(user="JAVIER_ARRIAGADA", password="654321", dsn=dsn)
    comando_sql = f'''INSERT INTO MAXIMILIANO_DIAZ_MARCHANT.REGISTRO_USUARIO (nombre_usuario, password) VALUES 
      ('{usuario}','{password}')'''
    cursor = conexion.cursor()
    cursor.execute(comando_sql)
    cursor.close()
    conexion.commit()


def modificar_usuario(usuario, password, n_password, dsn=dsn):
    conexion = cx_Oracle.connect(user="JAVIER_ARRIAGADA", password="654321", dsn=dsn)
    comando_sql = f'''UPDATE MAXIMILIANO_DIAZ_MARCHANT.REGISTRO_USUARIO SET
    password = '{n_password}' where nombre_usuario = '{usuario}' and password = '{password}' '''
    cursor = conexion.cursor()
    cursor.execute(comando_sql)
    cursor.close()
    conexion.commit()


def ingresar_carga(destinatario, d_origen, d_envio, peso, volumen, fecha, dsn=dsn):
    conexion = cx_Oracle.connect(user="JAVIER_ARRIAGADA", password="654321", dsn=dsn)
    comando_sql = f'''INSERT INTO MAXIMILIANO_DIAZ_MARCHANT.CARGA (destinatario, direccion_origen, direccion_destino,
    peso, volumen, fecha)  VALUES 
        ('{destinatario}',
        '{d_origen}',
       '{d_envio}', {peso}, {volumen}, to_date('{fecha}','yyyy-mm-dd'))'''
    cursor = conexion.cursor()
    cursor.execute(comando_sql)
    cursor.close()
    conexion.commit()
