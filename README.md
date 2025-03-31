
#  Análisis de anuncios de venta de vehículos en EE. UU.

Esta aplicación web ha sido desarrollada con **Streamlit** y permite visualizar y analizar datos relacionados con anuncios de coches usados en Estados Unidos. La herramienta ofrece visualizaciones interactivas utilizando **Plotly**, lo que facilita la exploración de patrones y relaciones en el conjunto de datos.

---

##  Funcionalidades

-  Visualización de un **histograma** de la columna `odometer` (kilometraje).
-  Visualización de un **gráfico de dispersión** entre `odometer` y `price`.
-  Interacción mediante botones o casillas de verificación (checkboxes) para controlar qué gráfico mostrar.

---

##  Tecnologías utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)

---

##  Cómo ejecutar la aplicación localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes un archivo `requirements.txt`, puedes instalar las dependencias manualmente:
   ```bash
   pip install streamlit pandas plotly
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

---

##  Despliegue en Render

Para hacer que Streamlit sea compatible con Render, se incluye un archivo de configuración `streamlit/config.toml` con la siguiente configuración:

```toml
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
```

Render utilizará este archivo para configurar correctamente el puerto y la dirección del servidor al alojar la app.

---

##  Estructura del proyecto

```
tu-proyecto/
│
├── app.py                      # Archivo principal de la app Streamlit
├── vehicles_us.csv            # Conjunto de datos
├── streamlit/
│   └── config.toml            # Configuración para despliegue en Render
├── README.md                  # Este archivo
└── requirements.txt           # Lista de dependencias (opcional)
```

---



