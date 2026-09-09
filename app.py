import streamlit as st

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

# 5. RENDERIZAR TABLERO
st.write("---")
dibujar_tablero(mapa_edificio, robot_alfa, robot_beta)
st.write("---")

# 6. PANEL DE ESTADO
st.sidebar.header("📊 Estado del Sistema")
st.sidebar.write(f"**Posición Robot Alfa:** {robot_alfa}")
st.sidebar.write(f"**Posición Robot Beta:** {robot_beta}")
st.sidebar.write("**Estado del Entorno:** Mapa desconocido para los agentes.")
