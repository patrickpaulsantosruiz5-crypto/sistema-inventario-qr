import qrcode

# Información del producto de ejemplo para el inventario
data = "PROD-001: Taladro Percutor Inalámbrico - Stock: 15 unidades"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en la carpeta del proyecto
img.save("codigo_qr_producto.png")

print("¡Código QR generado y guardado exitosamente como 'codigo_qr_producto.png'!")