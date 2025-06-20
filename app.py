import pandas as pd
from google import generativeai as genai


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("La variable de entorno GEMINI_API_KEY no está definida.")
genai.configure(api_key=api_key)



df = pd.read_csv("100frases.csv")
frases = df["Frase"].dropna().tolist()



frases_texto = "\n".join(f"- {frase}" for frase in frases)      

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Estas son frases célebres de películas:\n\n"
    + frases_texto +
    "\n\nAnaliza el estilo, tono y estructura de estas frases, y genera 5 frases originales."
)

print(response.text)
