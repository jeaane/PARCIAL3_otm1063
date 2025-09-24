import pandas as pd
import matplotlib.pyplot as plt
import os

# 📁 Crear carpeta de salida si no existe
os.makedirs("generados", exist_ok=True)

# 📄 Ruta del archivo Excel
archivo_excel = "datos/datos_base.xlsx"

# 📚 Cargar todas las hojas del Excel
excel = pd.ExcelFile(archivo_excel)

# 🔁 Iterar sobre cada hoja
for hoja in excel.sheet_names:
    df = excel.parse(hoja)

    # 📊 Gráfico de barras: Detalle vs Valor
    if "Detalle" in df.columns and "Valor" in df.columns:
        plt.figure(figsize=(10, 6))
        plt.bar(df["Detalle"], df["Valor"], color="cornflowerblue")
        plt.title(f"Gráfico de Barras - {hoja}")
        plt.xlabel("Detalle")
        plt.ylabel("Valor")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"generados/barras_{hoja}.png")
        plt.close()

    # 🥧 Gráfico de pastel: Detalle vs Porcentaje
    if "Detalle" in df.columns and "Porcentaje" in df.columns:
        plt.figure(figsize=(8, 8))
        plt.pie(df["Porcentaje"], labels=df["Detalle"], autopct="%1.1f%%", startangle=90)
        plt.title(f"Gráfico de Pastel - {hoja}")
        plt.savefig(f"generados/pastel_{hoja}.png")
        plt.close()