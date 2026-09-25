import mysql.connector
import csv
import boto3

conexion = mysql.connector.connect(
    host="mysql_c",
    port=3306,
    user="root",
    password="utec",
    database="empresa"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM empleados")

registros = cursor.fetchall()

columnas = [columna[0] for columna in cursor.description]

ficheroUpload = "data.csv"

with open(ficheroUpload, "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)

    writer.writerow(columnas)

    writer.writerows(registros)

cursor.close()
conexion.close()

nombreBucket = "xgg-output-01"

s3 = boto3.client("s3")

response = s3.upload_file(
    ficheroUpload,
    nombreBucket,
    ficheroUpload
)

print(response)
print("Ingesta completada")
