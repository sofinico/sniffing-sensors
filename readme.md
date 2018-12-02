## Procesar una medición

* `abftotxt.m` convierte el archivo `.abf` en `.txt`
* `reescaleo.py` recibe los `.txt`, los re-escalea y los vuelve a guardar como `.txt`



## 24 PC 

#### dormido

- Post-Filtro indica un filtrado digital low-pass de 2000Hz

- Los `.txt` se guardaron en las compus del labo con `reescaleoyfiltro.m` 


## AWM 3100

## AWM 2100

- `primera_invivo_sinolor.txt` datos raw de la primera medición in vivo con el 2100 en una prueba que no hubo olores, pero sirve para ver cómo se ven los ciclos en la medición in vivo con este sensor.

#### dormido

- El sensor está ubicado de modo tal que la exhalación es positiva

- `cerca.txt` y `lejos.txt` datos crudos re-escaleados. Tienen un ruido de base de 50 Hz.

- `procesado.txt` trazo de la respiración (cerca o lejos, no sé cuál) luego de haber sido procesada por `picosInhalacion.m` de Seba

- `inhalaciones.txt` puntos de inicio, final y pico de las inhalaciones, extraídas por `picosInhalacion.m` también

#### 

