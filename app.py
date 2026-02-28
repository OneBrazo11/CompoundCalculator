import streamlit as st

st.title("Gusty´s Calculadora de Interés Compuesto")

# Campos de entrada
capital = st.number_input("Cantidad de dinero inicial", min_value=0.0, value=100.0, step=10.0)
interes = st.number_input("Porcentaje de ganancia por periodo (%)", min_value=0.0, value=1.0, step=0.5)
periodos = st.number_input("Número de periodos (ej. días o apuestas)", min_value=1, value=30, step=1)

# Botón y cálculo
if st.button("Calcular"):
    tasa = interes / 100
    monto_final = capital * ((1 + tasa) ** periodos)
    ganancia_neta = monto_final - capital
    
    st.success(f"Monto Total Final: ${monto_final:,.2f}")
    st.info(f"Posible Ganancia Neta: ${ganancia_neta:,.2f}")
