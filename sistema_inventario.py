import qrcode
import gspread
from google.oauth2 import service_account

# 1. Definir los datos del producto
id_producto = "PROD-001"
nombre_producto = "Taladro Percutor Inalámbrico"
stock = 15
estado = "Activo"

# 2. Generar el código QR
datos_qr = f"ID: {id_producto} | Producto: {nombre_producto} | Stock: {stock} | Estado: {estado}"
imagen_qr = qrcode.make(datos_qr)

nombre_archivo_qr = f"qr_{id_producto}.png"
imagen_qr.save(nombre_archivo_qr)
print(f"Código QR generado y guardado como: {nombre_archivo_qr}")

# 3. Sincronizar con Google Sheets
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = service_account.Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Abrir la hoja y agregar la fila
sheet = client.open("Inventario_Talara_Motors").sheet1
nuevo_producto = [id_producto, nombre_producto, stock, estado, nombre_archivo_qr]
sheet.append_row(nuevo_producto)

print("¡Datos del inventario sincronizados correctamente con Google Sheets!")