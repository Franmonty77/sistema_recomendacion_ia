#Importamos las librerías
import pandas as pd

df=pd.read_csv("productos.csv")

#Mostramos solo las primeras filas
#print("Vista previa de los datos: ")
#print(df.head())

#Mostramos información general
#print("\nInformación general:")
#print(df.info())

def recomendar_por_reglas(df,producto_id,margen_precio=20):
    #Buscar producto por el id
    producto=df[df['id']==producto_id].iloc[0]
    categoria=producto['categoria']
    precio=producto['precio']
    
    #Buscar productos similares
    similares=df[
        (df['categoria']==categoria) &
        (df['id']!=producto_id) &
        (abs(df['precio']-precio)<=margen_precio)
    ]
    
    return similares

    # Probar la función con un producto (por ejemplo, ID 1)
resultados = recomendar_por_reglas(df, 1, margen_precio=30)
print(resultados)
