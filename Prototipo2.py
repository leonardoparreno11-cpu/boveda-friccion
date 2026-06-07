import streamlit as st
from datetime import datetime, timedelta
import time  # Necesario para crear la cuenta regresiva en tiempo real

# Configuración de la página
st.set_page_config(page_title="Bóveda de Fricción Cognitiva V2", layout="centered")

# Inicializar variables de estado (para simular la base de datos de la cuenta)
if 'bolsillo' not in st.session_state:
    st.session_state.bolsillo = 15.50
if 'boveda' not in st.session_state:
    st.session_state.boveda = 180.00
if 'candado_activo' not in st.session_state:
    st.session_state.candado_activo = False
if 'racha_ahorro' not in st.session_state:
    st.session_state.racha_ahorro = 45  # Días consecutivos de ahorro simulados
if 'bloqueo_hasta' not in st.session_state:
    st.session_state.bloqueo_hasta = None

# Comprobación inicial del estado de bloqueo
ahora = datetime.now()
esta_bloqueado = False
if st.session_state.bloqueo_hasta and ahora < st.session_state.bloqueo_hasta:
    esta_bloqueado = True

# Interfaz Principal
st.title("🛡️ Bóveda de Fricción Cognitiva")
st.write("Bienvenido. Aquí proteges tu futuro.")

# Mostrar los saldos y métricas
col1, col2 = st.columns(2)
with col1:
    st.success(f"💸 Dinero Diario (Bolsillo)\n\n### ${st.session_state.bolsillo:.2f}")
with col2:
    st.info(f"🔒 Bóveda Tecnológica (Ahorro)\n\n### ${st.session_state.boveda:.2f}")

st.caption(f"🔥 Racha de ahorro continuo: **{st.session_state.racha_ahorro} días**")
st.divider()

# Control de flujo según el estado de bloqueo
if esta_bloqueado:
    st.error("⛔ SISTEMA BLOQUEADO. Debido a un ingreso erróneo en el Candado Académico, tu bóveda está inhabilitada para proteger tu capital.")
    
    # Contenedor vacío que permitirá actualizar el texto dinámicamente
    reloj_placeholder = st.empty()
    
    # Bucle que actualiza el temporizador visualmente cada segundo
    while datetime.now() < st.session_state.bloqueo_hasta:
        tiempo_restante = st.session_state.bloqueo_hasta - datetime.now()
        minutos = int(tiempo_restante.total_seconds() // 60)
        segundos = int(tiempo_restante.total_seconds() % 60)
        
        # Sobrescribir el mensaje en el contenedor con el tiempo exacto
        reloj_placeholder.warning(f"⏳ Tiempo de fricción restante: {minutos:02d} minutos con {segundos:02d} segundos.")
        time.sleep(1)  # Pausar la ejecución por 1 segundo antes de volver a calcular
        
    # Una vez que el tiempo se agota, se limpia la variable y se reinicia la app
    st.session_state.bloqueo_hasta = None
    st.rerun()

else:
    # Sección de retiro normal
    st.subheader("Transferir de Bóveda a Bolsillo")
    st.write("¿Seguro que quieres gastar tus ahorros?")

    monto = st.number_input("Monto a retirar:", min_value=1.0, max_value=float(st.session_state.boveda), step=1.0)

    # Botones de acción (Retiro normal vs. Emergencia)
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Iniciar Retiro (Candado)"):
            st.session_state.candado_activo = True
    with col_btn2:
        if st.button("🚨 Retiro de Emergencia"):
            st.session_state.boveda -= monto
            st.session_state.bolsillo += monto
            st.session_state.racha_ahorro = 0  # Penalización aplicada
            st.session_state.candado_activo = False
            st.rerun()

    # Notificación de penalización visual tras el reinicio
    if st.session_state.racha_ahorro == 0 and not st.session_state.candado_activo:
         st.warning("⚠️ Retiro de emergencia ejecutado exitosamente. Se ha aplicado la penalización y tu racha de ahorro ha vuelto a 0 días.")

    # Lógica del Candado Académico
    if st.session_state.candado_activo:
        st.warning("⚠️ ALERTA DE FRICCIÓN: Candado Académico Activado")
        st.write("Para confirmar el retiro de tus ahorros, demuestra que tu cerebro racional está al mando resolviendo el siguiente problema:")
        
        # El reto matemático
        st.latex(r"p = \sqrt{x} + 100")
        st.write("Si la demanda es de $x = 400$ unidades, ¿cuál es el precio $p$?")
        
        respuesta = st.text_input("Ingresa el valor numérico exacto de p:")
        
        if st.button("Verificar y Transferir"):
            # La respuesta correcta es 120
            if respuesta == "120":
                st.error("Respuesta correcta. Transferencia realizada. (Tus ahorros han disminuido).")
                st.session_state.boveda -= monto
                st.session_state.bolsillo += monto
                st.session_state.candado_activo = False
                st.rerun()
            elif respuesta != "":
                # Activación del castigo de 10 minutos
                st.session_state.bloqueo_hasta = datetime.now() + timedelta(minutes=10)
                st.session_state.candado_activo = False
                st.rerun()
