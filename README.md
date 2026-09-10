# 🛡️ Simulación de Robots de Rescate - IA (Unidad 1)

Este proyecto es una simulación interactiva desarrollada en **Python** y **Streamlit** donde dos agentes autónomos (robots) exploran un mapa desconocido, evalúan riesgos y calculan rutas óptimas de rescate.

---

### 👥 Control de Actividades por Integrante

#### 🏛️ Unidad 1: Fundamentos y Agentes (Entrega Actual)

*   **Integrante 1 (Arquitecta del Entorno):** 
    *   [x] Configuración inicial del repositorio en GitHub y ramas de trabajo.
    *   [x] Creación de la interfaz web base con `Streamlit` y estilos en `estilos.css`.
    *   [x] Diseño de la matriz/cuadrícula del edificio (5x5) con muros y víctimas.
    *   [x] Implementación del nacimiento del Sistema Multi-Agente (Robot Alfa y Robot Beta) en el mapa 
    **  [x] Implementación del ciclo Percepción-Estado-Acción dinámico mediante la memoria de la página (`st.session_state`).
    *   [x] Panel de control del operador con sistema de alertas críticas en la barra lateral (letras rojas en mayúsculas) y botón de reinicio automático. 
  
    **Módulo de Navegación y Búsqueda Heurística (U1.8.2, U1.8.3):**
    *   [x] Creación del módulo independiente `navegacion.py`.
    *   [x] Implementación real del **Algoritmo A*** utilizando estructuras de prioridad (`heapq`) para calcular la ruta óptima en el espacio de estados.
    *   [x] Programación de la **distancia Manhattan** como función heurística aplicada de forma independiente para ambos robots.
    *   [x] Lógica de evasión de obstáculos en tiempo real (los robots recalculan la ruta automáticamente para rodear los muros con valor 1).

*   **Memoria Escrita (U1.2, U1.3, U1.5, U1.6):**
    *   [x] Redacción del Marco Histórico de la IA aplicada a la robótica de rescate.
    *   [x] Justificación de las Teorías del Aprendizaje y el Modelo Cognoscitivo del agente racional.
    *   [x] Desarrollo del Modelo de Adquisición del Conocimiento (Análisis epistemológico: Empirismo vs Racionalismo).


### 🛠️ Instrucciones para el Equipo (Cómo correr el proyecto)

1. Descargar los cambios más recientes de la rama principal:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Instalar la librería visual si aún no la tienen:
   ```bash
   pip install streamlit
   ```
3. Ejecutar la simulación localmente:
   ```bash
   streamlit run app.py
   ```
