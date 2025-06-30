#Importamos las librerías
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df=pd.read_csv("productos.csv")

#Mostramos solo las primeras filas
#print("Vista previa de los datos: ")
#print(df.head())

#Mostramos información general
#print("\nInformación general:")
#print(df.info())

#def recomendar_por_reglas(df,producto_id,margen_precio=20):
    #Buscar producto por el id
   # producto=df[df['id']==producto_id].iloc[0]
   # categoria=producto['categoria']
   # precio=producto['precio']
    
    #Buscar productos similares
   # similares=df[
   #     (df['categoria']==categoria) &
   #     (df['id']!=producto_id) &
   #     (abs(df['precio']-precio)<=margen_precio)
   # ]
    
   # return similares


#Generamos matriz TF-IDF
print("Columnas del DataFrame:", df.columns.tolist())  # Verificar columnas
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['descripcion'])

#Calculamos similitud coseno
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#Función de recomendación por similitud coseno
def recomendar_por_similitud(df, producto_id, top_n=3):
    index = df[df['id'] == producto_id].index[0]  # Posición del producto
    sim_scores = list(enumerate(cosine_sim[index]))  # Similitud con todos
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Ordenar
    sim_scores = sim_scores[1:top_n+1]  # Omitimos el propio producto

    indices_recomendados = [i[0] for i in sim_scores]
    return df.iloc[indices_recomendados]


print("Recomendaciones por similitud de descripción para el producto con ID 1:")
recomendaciones = recomendar_por_similitud(df, 1, top_n=2)
print(recomendaciones)






    # Probar la función con un producto (por ejemplo, ID 1)
#resultados = recomendar_por_reglas(df, 1, margen_precio=30)
#print(resultados)
