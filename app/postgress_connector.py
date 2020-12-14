# Pequeño script para devolver todo el contenido de la tabla de prueba

import psycopg2

host = "172.27.0.1" # gateway db



conn = psycopg2.connect(host=host, port = 5432, database="postgres", user="admin", password="admin")

cur = conn.cursor()

cur.execute("""SELECT * FROM tabla_prueba""")
query_results = cur.fetchall()
print(query_results)

cur.close()
conn.close()
