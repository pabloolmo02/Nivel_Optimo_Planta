🌱 Nivel Óptimo Planta

Este proyecto permite generar automáticamente los niveles óptimos de parámetros agrícolas para distintas plantas utilizando la API de OpenAI.
A partir de una lista de nombres de plantas, el programa consulta a un modelo de lenguaje y devuelve un archivo en formato JSON con los valores recomendados en las fases de crecimiento y floración.

🚀 Características

- Lectura de una lista de plantas desde un archivo (plantas.txt).

- Consulta a un modelo de IA para obtener recomendaciones agronómicas.

- Generación de un archivo de salida en formato JSON con los parámetros óptimos.

- Estructura clara para cada fase (crecimiento y floración).

- Incluye variables críticas para el desarrollo vegetal:

    Temperatura (°C)

    Humedad del suelo (%)

    pH (rango)

    Conductividad eléctrica (EC, dS/m)

    Macronutrientes: Nitrógeno (N), Fósforo (P) y Potasio (K)

📂 Estructura del proyecto

Nivel_Optimo_Planta/
├── main.py                          # Script principal
├── plantas.txt                      # Lista de plantas a consultar
├── niveles_optimos_generados.json   # Archivo generado con los resultados

⚙️ Requisitos

- Python 3.8 o superior

- Una clave válida de la API de OpenAI

Instalar dependencias:

    **pip install openai**

📝 Uso

1. Edita el archivo plantas.txt y añade una planta por línea. Ejemplo:

Tomate
Rosa
Albahaca


2. Ejecuta el script:

python main.py


3. El programa consultará la API y generará un archivo niveles_optimos_generados.json con el siguiente formato:

{
  "Tomate": {
    "crecimiento": {
      "temp": "20-28",
      "humedad_suelo": "60-75",
      "ph": "6.0-6.8",
      "ec": "1.5-2.5",
      "n": "60-100",
      "p": "20-40",
      "k": "30-60"
    },
    "floración": {
      "temp": "22-26",
      "humedad_suelo": "55-70",
      "ph": "6.0-6.5",
      "ec": "2.0-3.0",
      "n": "50-80",
      "p": "30-50",
      "k": "50-90"
    }
  }
}

🔑 Configuración de la API

En main.py, debes configurar tu clave de OpenAI:

client = openai.OpenAI(api_key="TU_API_KEY")


Se recomienda guardar tu clave en una variable de entorno y leerla desde el script en lugar de dejarla escrita en el código.

⚠️ Notas

- Se añade un time.sleep(2) entre consultas para evitar alcanzar los límites de la API.

- La calidad de los resultados depende del modelo de OpenAI utilizado. Actualmente se usa gpt-3.5-turbo.

- Este proyecto no sustituye el asesoramiento de un agrónomo, es una herramienta de apoyo basada en IA.

🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Si quieres mejorar el proyecto:

  1. Haz un fork del repositorio
  2. Crea una rama nueva (feature/nueva-funcionalidad)
  3. Realiza tus cambios y haz commit
  4. Envía un pull request 🚀

📜 Licencia

Este proyecto está disponible bajo la licencia MIT.
