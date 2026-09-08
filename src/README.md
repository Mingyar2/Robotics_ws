# Práctica: Nodos y Tópicos en ROS 2

**Nombre:** Mingyar Romero Medellín

**Descripción breve de la actividad:**
Creación y configuración de un espacio de trabajo en ROS 2 para implementar la comunicación básica entre dos nodos mediante un tópico.

**Explicación de funcionamiento:**
El sistema se compone de dos nodos escritos en Python. El nodo publicador (`velocity_publisher.py`) genera un valor numérico que incrementa de 0.0 a 1.5 y lo envía periódicamente. El nodo subscriptor (`velocity_subscriber.py`) se mantiene a la escucha y recibe los valores en tiempo real para imprimirlos en consola. La comunicación entre ambos utiliza el tópico `/velocity` con el tipo de mensaje `Float32` de la biblioteca `std_msgs`.

**Comandos utilizados para comprobación:**
* Compilación: `colcon build`
* Ejecutar nodos: `ros2 run basics velocity_publisher` y `ros2 run basics velocity_subscriber`
* Comprobación: `ros2 node list`, `ros2 topic list` y `rqt_graph`

**Problemas encontrados y soluciones:**
1. *Problema:* El manual sugería nombrar el ejecutable con mayúsculas en el archivo `setup.py`. 
   *Solución:* Se igualó la sintaxis a minúsculas estrictas para coincidir con el script en Python y evitar errores de ejecución.

**Evidencia en video:**
https://drive.google.com/file/d/1BN5PVfTQJ86hhEGQilGJHWaXFFlGhi1n/view?usp=sharing
---
## Actividad 2: Control de Turtlesim

**Descripción breve de la actividad:**
Se adaptaron los nodos de publicación y suscripción para interactuar directamente con el s>

**Explicación de modificaciones:**
Para lograr el objetivo, se migró del tipo de mensaje estándar `Float32` al mensaje geomét>

**Comandos utilizados:**
* Simulador: `ros2 run turtlesim turtlesim_node`
* Ejecución de nuevos nodos: `ros2 run basics velocity_turtle_pub` y `ros2 run basics velo>
* Análisis y comprobación: `ros2 node list`, `ros2 topic list` y `rqt_graph`.

**Problemas encontrados y soluciones:**
1. *Problema:* El uso del tópico y tipo de mensaje anterior no afectaba al simulador.
   *Solución:* Se actualizó la dependencia en `package.xml` para incluir `geometry_msgs`, >

**Evidencia en video (Actividad 2):**
Se anexa el link de la carpete de drive en la que estarán los videos 
https://drive.google.com/drive/folders/1cGgV3uluH7qB-fDrqvxCo4OXLkDQRR1C?usp=drive_link 


