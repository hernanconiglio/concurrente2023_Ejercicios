# Condiciones de Carrera: Exclusión Mutua y Seccion Crítica

## Ejercicio y Cuestionario - Clase 4 (5/5/2022):

```
globalContador.py
```
El siguente programa lanza un conjunto de threads cuyo código es un contador que incrementa una variable global (*contador*) una cierta cantidad de veces. El resultado del programa es la impresión del contenido final de la variable global.

Leer y analizar el código y tratar de deducir que hace cada bloque.

## Preguntas (responder en el campus):

1. Cual es el valor esperado de la variable ***contador***. En que condiciones se obtendría este valor esperado.
2. Ejecute el programa varias veces y explicar a que se deben los resultados que observa.
3. Identifique las Secciones Críticas (incluir las lineas de código en la respuesta).
4. Modifique el programa, utilizando Locks de modo que se asegure la exclusión mutua en las secciones críticas.
5. Que es una "condición de carrera"? Que consecuencias trae y cuando se produce?
6. Que es una Sección Crítica? 
7. Que es la Exclusión Mútua?
8. Que son los Locks o Mutex? *Bonus (opcional): que es un "deadlock"?, como se produce y que consecuencias tiene?*


<sub>[Daniel Buaon - Unahur-Programacion-Concurrente](https://github.com/Unahur-Programacion-Concurrente)</sub>
