import json
import pandas as pd

# Carga el JSON
with open('niveles_optimos_generados.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

rows = []
for especie, fases in data.items():
    for fase, valores in fases.items():
        # Construye el prompt y la respuesta
        prompt = f"<s>[INST] Dame los parámetros óptimos para la {fase} de {especie}. [/INST]"
        respuesta = ', '.join([f"{k.capitalize().replace('_', ' ')}: {v}" for k, v in valores.items()])
        fila = {'text': f"{prompt} {respuesta} </s>"}
        rows.append(fila)

# Crea el DataFrame y guárdalo en CSV
df = pd.DataFrame(rows)
df.to_csv('plantas_instruct_dataset.csv', index=False, encoding='utf-8')