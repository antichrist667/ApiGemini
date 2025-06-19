import pandas as pd
from google import generativeai as genai

# 🔐 SECURITY ISSUE: Clave API expuesta directamente en el código
API_KEY = "AIzaSyAfWj_Yx6TV6b96lo_7_tMyxjhf3pI26-4"
genai.configure(api_key=API_KEY)


# 💨 CODE SMELL: Código duplicado sin necesidad
df = pd.read_csv("100frases.csv")
df = pd.read_csv("100frases.csv")  # línea duplicada a propósito

frases = df["Frase"].dropna().tolist()

# 🐞 BUG: Uso de variable que no está definida correctamente
if len(frases) > 0:
    print("Cantidad de frases:", total_frases)  # 'total_frases' no está definida

frases_texto = "\n".join(f"- {frase}" for frase in frases)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Estas son frases célebres de películas:\n\n"
    + frases_texto +
    "\n\nAnaliza el estilo, tono y estructura de estas frases, y genera 5 frases originales."
)

print(response.text)
