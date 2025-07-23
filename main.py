import openai
import json
import time

# Configura tu clave de API
client = openai.OpenAI(api_key="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")

# Lee el archivo de plantas
with open("plantas.txt", "r", encoding="utf-8") as f:
    plantas = [line.strip() for line in f if line.strip()]

# Prompt base
def construir_prompt(planta):
    return f"""
Eres un experto en agronomía. Para la siguiente planta, genera un JSON con los niveles óptimos en dos fases: crecimiento y floración. Incluye:
- temperatura (°C)
- humedad_suelo (%)
- ph (rango)
- ec (dS/m)
- nitrógeno (n), fósforo (p), potasio (k) en mg/kg

Planta: {planta}

Devuélvelo solo como JSON, con esta estructura:

{{
  "crecimiento": {{
      "temp": "20-28",
      "humedad_suelo": "60-75",
      "ph": "6.0-6.8",
      "ec": "1.5-2.5",
      "n": "60-100",
      "p": "20-40",
      "k": "30-60"
  }},
  "floración": {{
      ...
  }}
}}
"""

# Resultado final
niveles_optimos = {}

# Procesar cada planta
for planta in plantas:
    print(f"Consultando datos para: {planta}")
    prompt = construir_prompt(planta)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # o "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "Eres un experto en agricultura."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content
        datos = json.loads(content)
        niveles_optimos[planta] = datos

    except Exception as e:
        print(f"Error con {planta}: {e}")
    
    time.sleep(2)  # evitar exceder límites

# Guardar a archivo
with open("niveles_optimos_generados.json", "w", encoding="utf-8") as f:
    json.dump(niveles_optimos, f, indent=4, ensure_ascii=False)

print("✅ Datos guardados en niveles_optimos_generados.json")
