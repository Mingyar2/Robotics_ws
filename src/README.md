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
