# 🛠️ Optimizador de Costos Operativos para Cambio de Inserto en Torno

## 💡 Descripción del proyecto

Este sistema permite gestionar insertos de torno y estimar su desgaste real según el uso y el material trabajado. Está desarrollado en **Python** con conexión a una **base de datos MySQL**.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- MySQL Server
- Biblioteca `mysql-connector-python` (instalar con `pip install mysql-connector-python`)
- Base de datos `optimizador_insertos` (estructura incluida en el proyecto)

---

## 🧪 Ejemplo completo de flujo de trabajo

### 1️⃣ Crear un torno
**Opción en el menú**: `8 - Crear nuevo torno`
```
Nombre: Torno CNC 1
Ubicación: Planta A
```

### 2️⃣ Crear un tipo de inserto
**Opción**: `6 - Crear nuevo tipo de inserto`
```
Nombre: Inserto A10
Vida útil estimada: 20
```

### 3️⃣ Registrar un nuevo inserto
**Opción**: `7 - Registrar nuevo inserto`
```
ID del tipo de inserto: 1
ID del torno: 1
Fecha de instalación: 2025-06-01
```

### 4️⃣ Crear un material
**Opción**: `5 - Crear nuevo material`
```
Nombre: Acero Inoxidable
Factor de desgaste: 1.5
```

### 5️⃣ Registrar uso del inserto
**Opción**: `1 - Registrar uso de inserto`
```
ID del inserto: 1
Horas de uso: 4
ID del material: 1
```

🔁 Resultado:
```
✅ Uso registrado. Desgaste real aplicado: 6.00 horas
```

### 6️⃣ Consultar desgaste del inserto
**Opción**: `2 - Calcular desgaste acumulado`
```
ID del inserto: 1
```

🔁 Resultado:
```
📊 Inserto ID 1 - Vida útil estimada: 20 h
⏱️ Desgaste acumulado: 6.00 h
🟢 Aún se puede utilizar. Resta 14.00 h.
```

---

## 📁 Estructura del sistema

- `gestor_insertos.py`: sistema completo con menú interactivo
- `optimizador_insertos.sql`: script para crear la base de datos
- `README.md`: instrucciones de uso y prueba

---

## ✅ Estado del proyecto

✔️ Funcional  
🔄 En desarrollo continuo  
📌 Listo para ampliaciones (exportar reportes, conexión con sensores, etc.)
