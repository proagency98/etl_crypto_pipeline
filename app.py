import streamlit as st
import pandas as pd
from scripts.extract import extract_data

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Criptomonedas",
    page_icon="💰",
    layout="wide"
)

# Título principal
st.title("💰 Dashboard de Criptomonedas")
st.markdown("---")

# Extraer datos
try:
    with st.spinner("Obteniendo datos de criptomonedas..."):
        data = extract_data()
    
    # Convertir a DataFrame
    df = pd.DataFrame(data)
    
    # Mostrar estadísticas básicas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Criptomonedas", len(df))
    
    with col2:
        total_market_cap = df['market_cap'].sum()
        st.metric("Market Cap Total", f"${total_market_cap:,.0f}")
    
    with col3:
        avg_price = df['current_price'].mean()
        st.metric("Precio Promedio", f"${avg_price:.2f}")
    
    with col4:
        total_volume = df['total_volume'].sum()
        st.metric("Volumen Total", f"${total_volume:,.0f}")
    
    st.markdown("---")
    
    # Mostrar tabla de datos
    st.subheader("📊 Datos de Criptomonedas")
    
    # Seleccionar columnas relevantes
    columns_to_show = ['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']
    df_display = df[columns_to_show].copy()
    
    # Renombrar columnas para mejor visualización
    df_display.columns = ['Nombre', 'Símbolo', 'Precio Actual (USD)', 'Market Cap', 'Volumen 24h', 'Cambio 24h (%)']
    
    # Formatear números
    df_display['Precio Actual (USD)'] = df_display['Precio Actual (USD)'].apply(lambda x: f"${x:,.2f}")
    df_display['Market Cap'] = df_display['Market Cap'].apply(lambda x: f"${x:,.0f}")
    df_display['Volumen 24h'] = df_display['Volumen 24h'].apply(lambda x: f"${x:,.0f}")
    df_display['Cambio 24h (%)'] = df_display['Cambio 24h (%)'].apply(lambda x: f"{x:.2f}%")
    
    # Mostrar tabla con paginación
    st.dataframe(df_display, use_container_width=True)
    
    # Gráfico de precios
    st.subheader("📈 Top 10 por Market Cap")
    top_10 = df.head(10)
    
    import plotly.express as px
    
    fig = px.bar(
        top_10, 
        x='name', 
        y='current_price',
        title="Precios Actuales - Top 10 Criptomonedas",
        labels={'name': 'Criptomoneda', 'current_price': 'Precio (USD)'}
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"Error al obtener datos: {str(e)}")
    st.info("Verifica tu conexión a internet y que la API de CoinGecko esté disponible.") 