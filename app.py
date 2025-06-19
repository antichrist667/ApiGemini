import pandas as pd
from google import generativeai as genai

# Configurar clave API (pon tu API real aquí)
genai.configure(api_key="TU_API_KEY")

# ✅ Ahora sí definimos la función que el test necesita
def generar_frases_desde_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)
    frases = df["Frase"].dropna().tolist()
    frases_texto = "\n".join(f"- {frase}" for frase in frases)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        "Estas son frases célebres de películas:\n\n"
        + frases_texto +
        "\n\nAnaliza el estilo, tono y estructura de estas frases, y genera 5 frases originales."
    )

    return response.text


if __name__ == "__main__":
    resultado = generar_frases_desde_csv("100frases.csv")
    print(resultado)
