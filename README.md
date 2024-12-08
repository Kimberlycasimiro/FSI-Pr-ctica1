# Práctica 1 - Búsqueda por Ramificación y Acotación

**Asignatura:** Fundamentos de los Sistemas Inteligentes (FSI)  
**Grado:** Ciencia e Ingeniería de Datos (GCID)  
**Universidad:** Universidad de Las Palmas de Gran Canaria (ULPGC)  
**Año Académico:** 2024 / 2025   
**Autores:** Mendoza Peña, Raúl y Casimiro Torres, Kimberly 

## Descripción

Esta práctica tiene como objetivo implementar en el grafo de las ciudades de Rumanía, las estrategias de búsqueda por **Ramificación y Acotación** (B&B) y **Ramificación y Acotación con Subestimación** (B&B Subestimación), utilizando la heurística basada en la distancia euclídea. Ambas estrategias se integran al código base respetando su funcionalidad original. Además, se ha implementado un sistema para contabilizar la cantidad de nodos generados y visitados, la ruta solución, el coste total y el tiempo de ejecución de las búsquedas

Todas las tareas opcionales también se encuentran implementadas, incluyendo la aplicación completa del algoritmo al grafo de Rumanía y la demostración de cómo una heurística que sobreestima puede llevar a soluciones no óptimas. Finalmente, los resultados obtenidos se presentan en una tabla comparativa que permite evaluar de forma clara las diferencias en eficiencia y rendimiento entre las estrategias implementadas, destacando su comportamiento en distintos escenarios.

## Funcionalidades Implementadas

### Utils

En el archivo `utils.py` se han incorporado nuevas clases y funcionalidades para soportar las estrategias de búsqueda avanzadas, además de mejorar las estructuras existentes.

1. **Clases Añadidas:**

-  `StackQueue:` Estructura tipo pila con estadísticas para búsquedas en profundidad.
-  `PriorityQueue:` Cola de prioridad para la estrategia de Ramificación y Acotación.
-  `PriorityQueueWithSubestimation:` Cola de prioridad que incorpora la heurística de la distancia euclídea para la estrategia de Ramificación y Acotación con Subestimación.

1. **Nuevas funcionalidades comunes:**

-  **Resultados detallados:** Cada clase incluye un método `print_results` para mostrar:

    - Número de nodos generados 
    - Número de nodos visitados 
    - La ruta solución encontrada 
    - Coste total de la solución encontrada
    - Tiempo de ejecución de la búsqueda

### Search

En el archivo `search.py` se han añadido nuevas estrategias de búsqueda y se han mejorado las existentes para ampliar las capacidades del sistema y proporcionar análisis detallados de los resultados.

1.  **Estrategias Añadidas:**

-  **Ramificación y Acotación** (`branch_and_bound_graph_search(problem)`): Implementa la estrategia de Ramificación y Acotación, priorizando nodos con menor coste acumulado y mostrando estadísticas y tiempo de ejecución. 
-  **Ramificación y Acotación con Subestimación** (`branch_and_bound_with_subestimation_graph_search(problem)`): Integra la estrategia de Ramificación y Acotación con Subestimación, utilizando una heurística basada en la distancia euclidiana y proporcionando estadísticas detalladas y tiempo de ejecución.

2.  **Mejoras en estrategias existentes:**

-  **Búsqueda en amplitud** (`breadth_first_graph_search(problem)`): Aunque ya utilizaba la estructura *FIFOQueue* para realizar la búsqueda, ahora incluye medición de tiempo de ejecución y proporciona resultados detallados.

-  **Búsqueda en profundidad** (`depth_first_graph_search(problem)`): Se reemplazó la estructura *Stack* por *StackQueue*, añadiendo funcionalidades como el cálculo de estadísticas y resultados detallados.


3.  **Nuevas funcionalidades comunes:**

-  **Estadísticas detalladas:** 
    - Contabilización de nodos generados y visitados, con y sin repetición.
    - Presentación de la ruta solución y del coste total encontrado

-  **Medición de tiempo:** Se calcula el tiempo total de ejecución utilizando `perf_counter()`, desde el inicio hasta la obtención de la solución.


### Run

En el archivo `run.py` se han añadido casos de prueba y se han mejorado las funcionalidades existentes para evaluar y comparar diferentes estrategias de búsqueda en el grafo de Rumanía.

1. **Casos añadidos:**

Se han definido múltiples problemas de búsqueda, cada uno con un nodo de origen y un nodo de destino, para probar las diferentes estrategias implementadas:

- **Caso 1:** Origen: Arad (`A`) → Destino: Bucharest (`B`).
- **Caso 2:** Origen: Oradea (`O`) → Destino: Eforie (`E`).
- **Caso 3:** Origen: Giurgiu (`G`) → Destino: Zerind (`Z`).
- **Caso 4:** Origen: Neamt (`N`) → Destino: Dobreta (`D`).
- **Caso 5:** Origen: Mehadia (`M`) → Destino: Fagaras (`F`).

2. **Mejoras añadidas:**

- **Ejecución de estrategias de búsqueda:**
  - Cada caso ejecuta las siguientes estrategias:
    - Búsqueda en amplitud.
    - Búsqueda en profundidad.
    - Ramificación y Acotación.
    - Ramificación y Acotación con Subestimación.
  - Las estrategias calculan y muestran estadísticas detalladas, como:
    - Nodos generados y visitados.
    - Ruta solución.
    - Coste total.
    - Tiempo de ejecución.

## Resultados

### Conclusión

**Ramificación y Acotación con Subestimación** es la estrategia más eficiente, sobresaliendo en todos los aspectos clave: nodos generados, nodos visitados y tiempo de ejecución. Su uso de heurísticas permite priorizar nodos prometedores, lo que no solo reduce la carga computacional, sino que también garantiza soluciones óptimas con una exploración más controlada del espacio de búsqueda. Esto la convierte en la mejor opción para problemas complejos donde la eficiencia y la calidad son esenciales.

**Búsqueda en amplitud** se presenta como una alternativa confiable en escenarios donde no se dispone de una función heurística. Aunque garantiza encontrar soluciones aceptables, su enfoque exhaustivo incrementa significativamente el número de nodos generados y visitados, lo que la hace menos eficiente en comparación con estrategias basadas en heurísticas.

**Búsqueda en profundidad**, por su naturaleza de exploración exhaustiva de un único camino antes de retroceder, resulta poco efectiva en problemas donde el coste importa. Su falta de priorización y análisis de costes acumulados conduce a rutas costosas y una mayor generación de nodos innecesarios, limitando su aplicabilidad en problemas prácticos.

**Ramificación y Acotación**, aunque asegura soluciones óptimas explorando todos los caminos posibles, queda eclipsada por su variante con subestimación. Si bien es efectiva, su eficiencia se ve superada al no integrar heurísticas que permitan reducir el espacio de búsqueda.