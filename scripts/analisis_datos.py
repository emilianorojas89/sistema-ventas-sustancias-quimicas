import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/dataset.csv")

df["Facturacion"] = df.iloc[:, 3] * df.iloc[:, 4]

ventas_totales = df["Facturacion"].sum()
producto_mas_vendido = df.groupby("Producto").sum(numeric_only=True).iloc[:, 0].idxmax()
ventas_por_mes = df.groupby("Mes")["Facturacion"].sum()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
print("\nVentas por mes:")
print(ventas_por_mes)

ventas_por_mes.plot(kind="bar", title="Evolución de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Facturación")
plt.tight_layout()
plt.savefig("resultados/grafico_resultados.png")
plt.show()
