import pandas as pd
from google import generativeai as genai

# Configurar clave API
genai.configure(api_key="AIzaSyAfWj_Yx6TV6b96lo_7_tMyxjhf3pI26-4")

# Leer archivo CSV
df = pd.read_csv("100frases.csv")
frases = df["Frase"].dropna().tolist()
frases_texto = "\n".join(f"- {frase}" for frase in frases)

# Crear el modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Generar contenido
response = model.generate_content(
    "Estas son frases célebres de películas:\n\n"
    + frases_texto +
    "\n\nAnaliza el estilo, tono y estructura de estas frases, y genera 5 frases originales."
)

# Mostrar resultado
print(response.text)
