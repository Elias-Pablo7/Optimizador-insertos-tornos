import mysql.connector
from datetime import date

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",  # Reemplazá con tu contraseña real
    database="optimizador_insertos"
)

cursor = conexion.cursor(dictionary=True)

def registrar_uso():
    try:
        listar_insertos()
        id_inserto = int(input("🔧 Ingresá el ID del inserto: "))
        horas_usadas = float(input("⏱️ Ingresá las horas de uso: "))
        listar_materiales()
        id_material = int(input("🧱 Ingresá el ID del material: "))

        cursor.execute("SELECT factor_desgaste FROM materiales WHERE id = %s", (id_material,))
        material = cursor.fetchone()
        if not material:
            print("❌ Material no encontrado.")
            return

        factor = material['factor_desgaste']
        desgaste_real = horas_usadas * factor

        cursor.execute("""
            INSERT INTO uso_insertos (id_inserto, fecha, horas_usadas, id_material)
            VALUES (%s, %s, %s, %s)
        """, (id_inserto, date.today(), horas_usadas, id_material))
        conexion.commit()

        print(f"✅ Uso registrado. Desgaste real aplicado: {desgaste_real:.2f} horas")
    except Exception as e:
        print("❌ Error:", e)

def calcular_total_desgaste():
    try:
        listar_insertos()
        id_inserto = int(input("🔧 Ingresá el ID del inserto a analizar: "))

        cursor.execute("""
            SELECT ti.vida_util_estimada
            FROM insertos i
            JOIN tipos_insertos ti ON i.id_tipo = ti.id
            WHERE i.id = %s
        """, (id_inserto,))
        result = cursor.fetchone()
        if not result:
            print("❌ Inserto no encontrado.")
            return

        vida_util = result['vida_util_estimada']

        cursor.execute("""
            SELECT ui.horas_usadas, m.factor_desgaste
            FROM uso_insertos ui
            JOIN materiales m ON ui.id_material = m.id
            WHERE ui.id_inserto = %s
        """, (id_inserto,))

        total_desgaste = sum(row['horas_usadas'] * row['factor_desgaste'] for row in cursor.fetchall())

        print(f"\n📊 Inserto ID {id_inserto} - Vida útil estimada: {vida_util} h")
        print(f"⏱️ Desgaste acumulado: {total_desgaste:.2f} h")
        if total_desgaste >= vida_util:
            print("⚠️ El inserto ha superado su vida útil. Debe cambiarse.")
        else:
            print(f"🟢 Aún se puede utilizar. Resta {vida_util - total_desgaste:.2f} h.")
    except Exception as e:
        print("❌ Error:", e)

def listar_insertos():
    print("\n📋 LISTADO DE INSERTOS:")
    cursor.execute("""
        SELECT i.id, ti.nombre AS tipo, t.nombre AS torno, i.estado
        FROM insertos i
        JOIN tipos_insertos ti ON i.id_tipo = ti.id
        JOIN tornos t ON i.id_torno = t.id
    """)
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(f"  ID: {row['id']} | Tipo: {row['tipo']} | Torno: {row['torno']} | Estado: {row['estado']}")
    else:
        print("  (No hay insertos cargados)")

def listar_materiales():
    print("\n🧱 LISTADO DE MATERIALES:")
    cursor.execute("SELECT id, nombre, factor_desgaste FROM materiales")
    resultados = cursor.fetchall()
    for row in resultados:
        print(f"  ID: {row['id']} | {row['nombre']} (Factor: {row['factor_desgaste']})")

def crear_material():
    try:
        nombre = input("🆕 Ingresá el nombre del nuevo material: ")
        factor = float(input("⚙️ Ingresá el factor de desgaste (ej: 1.0): "))
        cursor.execute("INSERT INTO materiales (nombre, factor_desgaste) VALUES (%s, %s)", (nombre, factor))
        conexion.commit()
        print("✅ Material creado correctamente.")
    except Exception as e:
        print("❌ Error:", e)

def crear_tipo_inserto():
    try:
        nombre = input("🆕 Ingresá el nombre del tipo de inserto: ")
        vida = float(input("🕒 Ingresá la vida útil estimada (en horas): "))
        cursor.execute("INSERT INTO tipos_insertos (nombre, vida_util_estimada) VALUES (%s, %s)", (nombre, vida))
        conexion.commit()
        print("✅ Tipo de inserto creado correctamente.")
    except Exception as e:
        print("❌ Error:", e)

def crear_inserto():
    try:
        cursor.execute("SELECT id, nombre FROM tipos_insertos")
        tipos = cursor.fetchall()
        print("\n📂 TIPOS DE INSERTOS DISPONIBLES:")
        for t in tipos:
            print(f"  ID: {t['id']} | {t['nombre']}")
        tipo_id = int(input("👉 Ingresá el ID del tipo de inserto: "))

        cursor.execute("SELECT id, nombre FROM tornos")
        tornos = cursor.fetchall()
        print("\n🛠️ TORNOS DISPONIBLES:")
        for t in tornos:
            print(f"  ID: {t['id']} | {t['nombre']}")
        torno_id = int(input("👉 Ingresá el ID del torno asignado: "))

        fecha = input("📅 Ingresá la fecha de instalación (YYYY-MM-DD): ")

        cursor.execute("""
            INSERT INTO insertos (id_tipo, id_torno, fecha_instalacion)
            VALUES (%s, %s, %s)
        """, (tipo_id, torno_id, fecha))
        conexion.commit()
        print("✅ Inserto registrado correctamente.")
    except Exception as e:
        print("❌ Error:", e)

def crear_torno():
    try:
        nombre = input("🛠️ Ingresá el nombre del torno: ")
        ubicacion = input("📍 Ingresá la ubicación: ")
        cursor.execute("INSERT INTO tornos (nombre, ubicacion) VALUES (%s, %s)", (nombre, ubicacion))
        conexion.commit()
        print("✅ Torno creado correctamente.")
    except Exception as e:
        print("❌ Error:", e)

def menu():
    while True:
        print("\n=== MENÚ DE GESTIÓN DE INSERTOS ===")
        print("1 - Registrar uso de inserto")
        print("2 - Calcular desgaste acumulado")
        print("3 - Listar insertos")
        print("4 - Listar materiales")
        print("5 - Crear nuevo material")
        print("6 - Crear nuevo tipo de inserto")
        print("7 - Registrar nuevo inserto")
        print("8 - Crear nuevo torno")
        print("9 - Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            registrar_uso()
        elif opcion == "2":
            calcular_total_desgaste()
        elif opcion == "3":
            listar_insertos()
        elif opcion == "4":
            listar_materiales()
        elif opcion == "5":
            crear_material()
        elif opcion == "6":
            crear_tipo_inserto()
        elif opcion == "7":
            crear_inserto()
        elif opcion == "8":
            crear_torno()
        elif opcion == "9":
            print("👋 Saliendo del sistema.")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
    cursor.close()
    conexion.close()
