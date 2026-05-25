import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Bóveda de Fricción Cognitiva", layout="centered")

# Inicializar variables de estado (para simular la base de datos de la cuenta)
if 'bolsillo' not in st.session_state:
    st.session_state.bolsillo = 15.50
if 'boveda' not in st.session_state:
    st.session_state.boveda = 180.00
if 'candado_activo' not in st.session_state:
    st.session_state.candado_activo = False

# Interfaz Principal
st.title("🛡️ Bóveda de Fricción Cognitiva")
st.write("Bienvenido. Aquí proteges tu futuro.")

# Mostrar los saldos
col1, col2 = st.columns(2)
with col1:
    st.success(f"💸 Dinero Diario (Bolsillo)\n\n### ${st.session_state.bolsillo:.2f}")
with col2:
    st.info(f"🔒 Bóveda Tecnológica (Ahorro)\n\n### ${st.session_state.boveda:.2f}")

st.divider()

# Sección de retiro
st.subheader("Transferir de Bóveda a Bolsillo")
st.write("¿Seguro que quieres gastar tus ahorros?")

monto = st.number_input("Monto a retirar:", min_value=1.0, max_value=float(st.session_state.boveda), step=1.0)

# Botón para iniciar el retiro
if st.button("Iniciar Retiro"):
    st.session_state.candado_activo = True

# Lógica del Candado Académico
if st.session_state.candado_activo:
    st.warning("⚠️ ALERTA DE FRICCIÓN: Candado Académico Activado")
    st.write("Para confirmar el retiro de tus ahorros, demuestra que tu cerebro racional está al mando resolviendo el siguiente problema:")
    
    # El reto matemático
    st.latex(r"p = \sqrt{x} + 100")
    st.write("Si la demanda es de $x = 400$ unidades, ¿cuál es el precio $p$?")
    
    respuesta = st.text_input("Ingresa el valor de p:")
    
    if st.button("Verificar y Transferir"):
        # La respuesta correcta es raiz(400) + 100 = 20 + 100 = 120
        if respuesta == "120":
            st.error("Respuesta correcta. Transferencia realizada (Tus ahorros han disminuido).")
            # Actualizar saldos
            st.session_state.boveda -= monto
            st.session_state.bolsillo += monto
            st.session_state.candado_activo = False
            st.rerun() # Recargar la página para ver los nuevos saldos
        elif respuesta != "":
            st.success("❌ Respuesta incorrecta. Tu impulso falló. Tu dinero sigue protegido en la Bóveda.")