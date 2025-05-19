def conectar(consulta_sql):
    import mysql.connector 

    config = {
        'user':'uuwzz1ups71lzb72',
        'password':'aFadbp1JsNtX6kPnyDtt',
        'host':'be0g17yb6tf4vnwbpikh-mysql.services.clever-cloud.com',
        'database':'be0g17yb6tf4vnwbpikh',
        'raise_on_warnings': True
    }

    try: 
        conexion = mysql.connector.connect(**config)
        print("✅ Conexión exitosa a la base de datos.")

        consultas = conexion.cursor()
        print("🔍 Consulta que se va a ejecutar:", consulta_sql)
        consultas.execute(consulta_sql)
        resultado = consultas.fetchall()

        consultas.close()
        conexion.close()
        return resultado

    except mysql.connector.Error as err:
        print(f"💀 Error al conectarse o ejecutar la consulta: {err}")
        print(f"Error al conectarse a la base de datos: {err}")
