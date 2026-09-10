import streamlit as st

import navegacion

# 1. Configuración del título de la página
st.title("🛡️ Simulación de Robots de Rescate - Unidad 1")
st.subheader("Avance de la Arquitecta del Entorno (Integrante 1)")
st.write("Representación del entorno Percepción-Estado-Acción con 2 Robots.")

# 2. CARGAR EL CSS SEPARADO
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. DEFINICIÓN DEL ENTORNO (Escrito en una sola línea para evitar errores de corte)
mapa_edificio = [[0, 1, 0, 0, 2], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0]]

# Posiciones de los robots
robot_alfa = (0, 0)
robot_beta = (4, 4)

# 4. FUNCIÓN PARA DIBUJAR EL TABLERO
def dibujar_tablero(mapa, r_alfa, r_beta):
    st.write("") 
    for fila_idx, fila in enumerate(mapa):
        cols = st.columns(5)
        for col_idx, casilla in enumerate(fila):
            
            if (fila_idx, col_idx) == r_alfa:
                contenido = "🤖 <span style='color:#ff5555;'>R-Alfa</span>"
            elif (fila_idx, col_idx) == r_beta:
                contenido = "🤖 <span style='color:#55ff55;'>R-Beta</span>"
            elif casilla == 1:
                contenido = "🧱 Muro"
            elif casilla == 2:
                contenido = "🚨 Víctima"
            else:
                contenido = "<span style='color:#8b949e;'>🌌 Vacío</span>"
            
            html_casilla = f"<div class='casilla-moderna'>{contenido}</div>"
            cols[col_idx].markdown(html_casilla, unsafe_allow_html=True)

# 5. INICIALIZAR LA MEMORIA DINÁMICA (Para que el robot se mueva al hacer clic)
if "pos_alfa" not in st.session_state:
    st.session_state.pos_alfa = (0, 0)
if "pos_beta" not in st.session_state:
    st.session_state.pos_beta = (4, 4)

# 6. RENDERIZAR TABLERO (Usando las posiciones dinámicas de la memoria)
st.write("---")
dibujar_tablero(mapa_edificio, st.session_state.pos_alfa, st.session_state.pos_beta)
st.write("---")

# 7. INTERACCIÓN: Panel de Control del Operador con Botón Multi-Agente
st.subheader("🕹️ Panel de Control del Operador")

# Ubicación de la víctima
pos_victima = (0, 4)

# Si ya llegaron, mostramos botón de reiniciar; si no, el de dar paso
if st.session_state.pos_alfa == pos_victima or st.session_state.pos_beta == pos_victima:
    if st.button("🔄 Reiniciar Simulación"):
        st.session_state.pos_alfa = (0, 0)
        st.session_state.pos_beta = (4, 4)
        st.rerun()
else:
    if st.button("👣 Dar siguiente paso de rescate (Ambos Robots)"):
        # MOVIMIENTO ROBOT ALFA
        ruta_alfa = navegacion.algoritmo_a_estrella(mapa_edificio, st.session_state.pos_alfa, pos_victima)
        idx_alfa = ruta_alfa.index(st.session_state.pos_alfa)
        if idx_alfa < len(ruta_alfa) - 1:
            st.session_state.pos_alfa = ruta_alfa[idx_alfa + 1]
            
        # MOVIMIENTO ROBOT BETA
        ruta_beta = navegacion.algoritmo_a_estrella(mapa_edificio, st.session_state.pos_beta, pos_victima)
        idx_beta = ruta_beta.index(st.session_state.pos_beta)
        if idx_beta < len(ruta_beta) - 1:
            st.session_state.pos_beta = ruta_beta[idx_beta + 1]
            
        st.rerun()

# 8. PANEL DE ESTADO EN LA BARRA LATERAL (SIDEBAR)
st.sidebar.header("📊 Estado del Sistema")
st.sidebar.write(f"**Posición Robot Alfa:** {st.session_state.pos_alfa}")
st.sidebar.write(f"**Posición Robot Beta:** {st.session_state.pos_beta}")

# CALCULAR DISTANCIAS MANHATTAN
dist_alfa = navegacion.calcular_distancia_manhattan(st.session_state.pos_alfa, pos_victima)
dist_beta = navegacion.calcular_distancia_manhattan(st.session_state.pos_beta, pos_victima)

st.sidebar.write(f"**Distancia Alfa a Víctima:** {dist_alfa} casillas")
st.sidebar.write(f"**Distancia Beta a Víctima:** {dist_beta} casillas")

# --- ANUNCIO EN LETRAS ROJAS Y MAYÚSCULAS AL FINAL DEL LATERAL ---
if st.session_state.pos_alfa == pos_victima or st.session_state.pos_beta == pos_victima:
    st.sidebar.write("---")
    st.sidebar.markdown("<h3 style='color: #ff5555; text-align: center;'>🚨 VÍCTIMA LOCALIZADA - MISIÓN DE RESCATE EXITOSA</h3>", unsafe_allow_html=True)
