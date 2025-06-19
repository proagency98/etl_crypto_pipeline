# 🚀 Pipeline ETL de Criptomonedas

Un pipeline ETL (Extract, Transform, Load) completo para obtener, procesar y visualizar datos de criptomonedas en tiempo real desde la API de CoinGecko.

## 📋 Descripción del Proyecto

Este proyecto implementa un pipeline ETL que:

- **Extract**: Obtiene datos de las 100 criptomonedas con mayor capitalización de mercado desde la API de CoinGecko
- **Transform**: Procesa y limpia los datos para su análisis
- **Load**: Almacena los datos en una base de datos (preparado para SQLAlchemy)
- **Visualización**: Incluye un dashboard web interactivo para mostrar los datos

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Requests**: Para peticiones HTTP a la API
- **Pandas**: Para manipulación y análisis de datos
- **SQLAlchemy**: Para conexión con bases de datos
- **Streamlit**: Para el dashboard web
- **Plotly**: Para gráficos interactivos

## 📁 Estructura del Proyecto

```
etl_crypto_pipeline/
├── README.md
├── app.py                 # Dashboard web con Streamlit
├── data/                  # Directorio para almacenar datos
├── scripts/
│   └── extract.py         # Módulo de extracción de datos
└── venv/                  # Entorno virtual (se crea automáticamente)
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet

### Pasos de Instalación

1. **Clona o descarga el proyecto:**
   ```bash
   cd /ruta/a/tu/proyecto
   ```

2. **Crea un entorno virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Activa el entorno virtual:**
   ```bash
   source venv/bin/activate  # En macOS/Linux
   # o
   venv\Scripts\activate     # En Windows
   ```

4. **Instala las dependencias:**
   ```bash
   pip install requests pandas sqlalchemy streamlit plotly
   ```

## 🎯 Cómo Usar el Proyecto

### 1. Extracción de Datos

El módulo `scripts/extract.py` contiene la función principal para extraer datos:

```python
from scripts.extract import extract_data

# Obtener datos de criptomonedas
data = extract_data()
```

### 2. Dashboard Web

Para ejecutar el dashboard web:

```bash
streamlit run app.py
```

El dashboard incluye:
- 📊 Métricas en tiempo real
- 📋 Tabla de datos de criptomonedas
- 📈 Gráficos interactivos
- 💰 Información de precios y market cap

### 3. Datos Disponibles

El pipeline extrae la siguiente información para cada criptomoneda:
- Nombre y símbolo
- Precio actual en USD
- Capitalización de mercado
- Volumen de trading (24h)
- Cambio de precio (24h)
- Y más...

## 🔧 Configuración de Base de Datos

El proyecto está preparado para usar SQLAlchemy. Para configurar una base de datos:

1. **Instala el driver de tu base de datos preferida:**
   ```bash
   pip install psycopg2-binary  # Para PostgreSQL
   # o
   pip install pymysql          # Para MySQL
   # o
   pip install sqlite3          # Para SQLite (incluido con Python)
   ```

2. **Configura la conexión en tu script de carga**

## 📊 Características del Dashboard

- **Interfaz moderna y responsive**
- **Datos en tiempo real** desde CoinGecko
- **Métricas clave** de criptomonedas
- **Gráficos interactivos** con Plotly
- **Tabla de datos** con paginación
- **Manejo de errores** robusto

## 🔍 API Utilizada

Este proyecto utiliza la [API pública de CoinGecko](https://www.coingecko.com/en/api), que proporciona:
- Datos gratuitos y en tiempo real
- Sin necesidad de API key para uso básico
- Límites de rate limit generosos

## 🚨 Limitaciones y Consideraciones

- **Rate Limiting**: La API de CoinGecko tiene límites de uso
- **Datos en Tiempo Real**: Los datos se actualizan cada vez que se ejecuta el script
- **Dependencia de Internet**: Requiere conexión a internet para funcionar

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la documentación
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de que el entorno virtual esté activado
4. Comprueba tu conexión a internet

## 🔮 Próximas Mejoras

- [ ] Implementación completa de la fase Load con SQLAlchemy
- [ ] Más tipos de gráficos y visualizaciones
- [ ] Alertas de precio configurables
- [ ] Exportación de datos a diferentes formatos
- [ ] Integración con más APIs de criptomonedas

---

**¡Disfruta explorando los datos de criptomonedas! 🚀**
