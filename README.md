# Técnicas de Visualización de Datos  
Recopilación de tres técnicas de visualización.

---

## 1. Venn Diagram (Diagrama de Venn)

### Definición General

**Nombre y Descripción:**  
También conocido como *diagrama primario*, *de conjunto* o *lógico*, representa todas las relaciones lógicas posibles entre una colección finita de conjuntos diferentes.

**Funcionamiento:**  
Cada conjunto se representa mediante un círculo.  
- El **tamaño del círculo** indica la importancia o magnitud del grupo.  
- El **solapamiento** entre círculos representa la intersección o elementos comunes.

**Origen y Aplicaciones:**  
- Recibe su nombre en honor a John Venn (1834-1923), matemático inglés, lo creó para representar visualmente proposiciones lógicas de matemáticas.
- Clasificar productos, analizar las preferencias de un grupo de gente y organizar las consultas de la base de datos.

---

### Tipo y Estructura de Datos

**Datos admitidos:**  
- Variables categóricas organizadas en listas independientes.  
- Ideal para comparar dos o más listas de elementos únicos.

**Limitaciones y Requisitos:**  
- **Límite de grupos:** No más de 3; más de eso reduce la legibilidad.  
- **Proporcionalidad:** En diagramas de dos grupos, las áreas deben ser proporcionales a los valores.  
- **Anotación:** Recomendable incluir valores numéricos dentro de cada área.

---

## 2. Proportional Symbol Map (Mapa de Símbolos Proporcionales / Bubble Map)

### Definición General

**Nombre y Descripción:**  
Conocido como *Bubble Map*, utiliza círculos de diferentes tamaños colocados sobre un mapa para representar valores numéricos.

**Funcionamiento:**  
Los círculos se ubican en coordenadas geográficas específicas o en el baricentro de una región.  
Su ventaja principal es evitar el sesgo visual de los mapas coropléticos, donde regiones grandes parecen más relevantes de lo que son.

**Origen y Aplicaciones:**
- Creado a mediados del siglo 19 por el militar Henry Drury Harness para analizar y visualizar datos de tráfico, flujo de pasajeros y población para los Comisionados Ferroviarios de Irlanda.
- Distribución de población por ciudades  
- Resultados electorales por estado  
- Localización de puntos de interés con un valor asociado

---

### Tipo y Estructura de Datos

**Datos admitidos:**  
- Datos geográficos (latitud/longitud o nombres de regiones)  
- Variable cuantitativa asociada

**Limitaciones y Requisitos:**  
- **Métrica visual:** El tamaño debe mapearse al **área** del círculo, no al diámetro.  
- **Solapamiento:** Usar transparencia si las burbujas se superponen.  
- **Leyenda:** Debe incluirse para interpretar correctamente los tamaños.

---

## 3. Spiral Plot (Diagrama en Espiral)

### Definición General

**Nombre y Descripción:**  
Técnica especializada para representar series temporales.  
A diferencia de los gráficos lineales, los datos se proyectan a lo largo de una espiral.

**Funcionamiento:**  
Permite visualizar la evolución de valores numéricos en el tiempo de forma compacta, facilitando la comparación de periodos largos en poco espacio.

**Origen y Aplicaciones:**
- Creado por Arquímedes para representar un punto que se mueve hacia afuera a velocidad constante, con el objetivo de resolver problemas geométricos.
- Detección de patrones cíclicos o estacionales  
- Variaciones de temperatura anuales  
- Consumos periódicos

---

### Tipo y Estructura de Datos

**Datos admitidos:**  
- Series temporales: valores cuantitativos ordenados cronológicamente.

**Limitaciones y Requisitos:**  
- **Tamaño del conjunto:** Debe cubrir varios ciclos (meses o años) para justificar la espiral.  
- **Alternativas:** Si el dataset es pequeño o no presenta ciclos claros, un gráfico de líneas es más adecuado.

---

Link: https://afkmartin.github.io/M2.859-VDD-PEC2-UOC/