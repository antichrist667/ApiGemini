import pandas as pd
from google import generativeai as genai


genai.configure(api_key="AIzaSyAfWj_Yx6TV6b96lo_7_tMyxjhf3pI26-4")


df = pd.read_csv("100frases.csv")
frases = df["Frase"].dropna().tolist()

if True:
    print("Esto no debería estar aquí (smell)")


frases = 42  
frases_texto = "\n".join(f"- {frase}" for frase in frases)      

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Estas son frases célebres de películas:\n\n"
    + frases_texto +
    "\n\nAnaliza el estilo, tono y estructura de estas frases, y genera 5 frases originales."
)

print(response.text)
