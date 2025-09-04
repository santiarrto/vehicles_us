# 🚗 Vehicle Sales Report App

Aplicación web interactiva desarrollada en **Python** que permite explorar y visualizar datos de anuncios de automóviles en Estados Unidos. Incluye análisis exploratorio con **pandas** y gráficos dinámicos con **plotly-express**, integrados en una interfaz web mediante **Streamlit**.

---

## 📋 Índice
- [Requisitos previos](#-requisitos-previos)
- [Paso 1. Configuración](#-paso-1-configuración)
- [Paso 2. Descarga del archivo de datos](#-paso-2-descarga-del-archivo-de-datos)
- [Paso 3. Análisis exploratorio de datos (EDA)](#-paso-3-análisis-exploratorio-de-datos-eda)
- [Paso 4. Desarrollo del cuadro de mandos (Streamlit)](#-paso-4-desarrollo-del-cuadro-de-mandos-streamlit)
- [Ejecución local](#️-ejecución-local)
- [Despliegue en Render](#-despliegue-en-render)
- [Solución de problemas comunes](#-solución-de-problemas-comunes)
- [Recursos](#-recursos)

---

## ✅ Requisitos previos

Asegúrate de contar con:

- [Python 3.9+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- Cuentas en:
  - [GitHub](https://github.com/)
  - [Render](https://render.com/) (inicia sesión con **GitHub**)

> Este proyecto utiliza **pandas**, **plotly-express** y **streamlit**.

---

## ⚙️ Paso 1. Configuración

1. **Crea el repositorio en GitHub** (con `README.md` y `.gitignore` de plantilla **Python**).
2. **Clona** el repositorio y entra al directorio del proyecto:
   ```bash
   git clone https://github.com/<tu_usuario>/<tu_repositorio>.git
   cd <tu_repositorio>
   ```
3. **Crea y activa** un entorno virtual (recomendado: `vehicles_env`):
   - Windows (PowerShell):
     ```powershell
     python -m venv vehicles_env
     .ehicles_env\Scriptsctivate
     ```
   - macOS / Linux:
     ```bash
     python -m venv vehicles_env
     source vehicles_env/bin/activate
     ```
4. **Instala las librerías necesarias** en el entorno:
   ```bash
   pip install pandas plotly_express streamlit
   ```
   > Si usas **conda**, recuerda instalar `nbformat` para habilitar plotly express en notebooks:
   ```bash
   conda install -n vehicles_env nbformat
   ```
5. **Crea el archivo `requirements.txt`** (sin fijar versiones), con el siguiente contenido:
   ```txt
   pandas
   plotly_express
   streamlit
   ```
6. **Configura VS Code**:
   - Abre la carpeta del proyecto en VS Code.
   - Selecciona el **intérprete de Python** del entorno virtual creado.

---

## 📥 Paso 2. Descarga del archivo de datos

1. Descarga el dataset `vehicles_us.csv` (anuncios de coches en EE. UU.) o utiliza un CSV propio.
2. Coloca el archivo en la **raíz del proyecto** (junto a `app.py`).

---

## 📊 Paso 3. Análisis exploratorio de datos (EDA)

1. Crea un directorio `notebooks/` y dentro un notebook **`EDA.ipynb`**.
2. Ejemplos con **plotly-express**:

**Histograma**
```python
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('../vehicles_us.csv')  # ajusta la ruta si el CSV está en otra carpeta
fig = px.histogram(car_data, x="odometer")
fig.show()
```

**Gráfico de dispersión**
```python
import plotly.express as px

fig = px.scatter(car_data, x="odometer", y="price")
fig.show()
```

> En la [galería de plotly-express](https://plotly.com/python/plotly-express/) encontrarás más ejemplos de gráficos básicos.

---

## 🖥️ Paso 4. Desarrollo del cuadro de mandos (Streamlit)

Crea el archivo **`app.py`** en la raíz del proyecto con el siguiente ejemplo mínimo:

```python
import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

st.header("🚗 Reportes de vehículos en Estados Unidos")

# Botón para histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Opcional: reemplazar botones por casillas de verificación
# build_histogram = st.checkbox('Construir un histograma')
# if build_histogram:
#     st.write('Construir un histograma para la columna odómetro')
#     fig = px.histogram(car_data, x='odometer')
#     st.plotly_chart(fig, use_container_width=True)
```

---

## ▶️️ Ejecución local

Desde la **raíz del proyecto** (con el entorno activado):

```bash
streamlit run app.py
```

Si el comando anterior no funciona en tu entorno, usa el módulo de Python para garantizar el intérprete correcto:

```bash
python -m streamlit run app.py
```

La aplicación quedará disponible en: <http://localhost:8501>

---

## ☁️ Despliegue en Render

1. **Sube** tu proyecto a GitHub (incluye `app.py`, `vehicles_us.csv` y `requirements.txt`).
2. Entra a **Render** y conecta tu cuenta de **GitHub**.
3. Crea un nuevo **Web Service** y selecciona tu repositorio.
4. Configura el **Comando de inicio**:
   ```bash
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```
5. Render instalará las dependencias desde `requirements.txt` y desplegará la app.

---

## 🧩 Solución de problemas comunes

- **`ModuleNotFoundError: No module named 'pandas'`**  
  Instala la librería en el entorno activo:
  ```bash
  pip install pandas
  ```

- **`bash: streamlit: command not found`**  
  Ejecuta con el intérprete actual:
  ```bash
  python -m streamlit run app.py
  ```
  O añade la carpeta `Scripts` (Windows) al **PATH**.

- **Permisos / Puertos**  
  Asegúrate de que ningún proceso esté usando el puerto `8501` o ajusta el puerto:
  ```bash
  streamlit run app.py --server.port 8502
  ```

---

## 📚 Recursos

- [Documentación de pandas](https://pandas.pydata.org/docs/)
- [Documentación de plotly-express](https://plotly.com/python/plotly-express/)
- [Documentación de Streamlit](https://docs.streamlit.io/)

---

¡Listo! Con esto puedes desarrollar, ejecutar y desplegar tu aplicación de reportes de vehículos en Estados Unidos.
