# 🛡️ Simulación de Robots de Rescate - IA (Unidad 1)

Este proyecto es una simulación interactiva desarrollada en **Python** y **Streamlit** donde dos agentes autónomos (robots) exploran un mapa desconocido, evalúan riesgos y calculan rutas óptimas de rescate.

---

### 👥 Control de Actividades por Integrante

#### 🏛️ Unidad 1: Fundamentos y Agentes (Entrega Actual)

*   **Integrante 1 (Arquitecta del Entorno):** 
    *   [x] Configuración inicial del repositorio en GitHub y ramas de trabajo.
    *   [x] Creación de la interfaz web base con `Streamlit` y estilos en `estilos.css`.
    *   [x] Diseño de la matriz/cuadrícula del edificio (5x5) con muros y víctimas.
    *   [x] Implementación del nacimiento del Sistema Multi-Agente (Robot Alfa y Robot Beta) en el mapa (**U1.7**).
*   **Integrante 2 (Experto en Navegación):**
    *   [ ] Crear el archivo `navegacion.py`.
    *   [ ] Implementar el Algoritmo $A^*$ utilizando la **distancia Manhattan** como heurística (**U1.8.2, U1.8.3**).
    *   [ ] Conectar la ruta óptima calculada con el tablero visual de la Integrante 1.
*   **Integrantes 3, 4 y 5 (Redactores de la Memoria Escrita):**
    *   [ ] Redactar el Marco Histórico de la IA y robótica de rescate (**U1.2**).
    *   [ ] Relacionar las Teorías del Aprendizaje y el Modelo Cognoscitivo con la arquitectura Percepción-Estado-Acción de los robots (**U1.3, U1.6**).
    *   [ ] Desarrollar el Modelo de Adquisición del Conocimiento (**U1.5**).

---

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
