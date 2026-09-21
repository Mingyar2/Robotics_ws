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
Se adaptaron los nodos de publicación y suscripción para interactuar directamente con el simulador Turtlesim, logrando controlar el movimiento traslacional de la tortuga mediante incrementos periódicos de velocidad hasta detenerla en un límite establecido.

**Explicación de modificaciones:**
Para lograr el objetivo, se migró del tipo de mensaje estándar `Float32` al mensaje geométrico `geometry_msgs/Twist`. Se configuró el publicador para enviar datos al tópico `/turtle1/cmd_vel`, ajustando el temporizador a 0.5 segundos. La lógica interna se modificó para que, al superar la velocidad de 1.2 en el eje X, el nodo comience a enviar una velocidad de 0.0, deteniendo la tortuga por completo en lugar de reiniciar el ciclo.

**Comandos utilizados:**
* Simulador: `ros2 run turtlesim turtlesim_node`
* Ejecución de nuevos nodos: `ros2 run basics velocity_turtle_pub` y `ros2 run basics velocity_turtle_subs`
* Análisis y comprobación: `ros2 node list`, `ros2 topic list` y `rqt_graph`.

**Problemas encontrados y soluciones:**
1. *Problema:* El uso del tópico y tipo de mensaje anterior no afectaba al simulador.
   *Solución:* Se actualizó la dependencia en `package.xml` para incluir `geometry_msgs`, y se redirigió el flujo de comunicación hacia el tópico predeterminado `/turtle1/cmd_vel` de Turtlesim.

**Evidencia en video (Actividad 2):**
https://drive.google.com/drive/folders/1cGgV3uluH7qB-fDrqvxCo4OXLkDQRR1C?usp=drive_link

---

## Práctica 3: ROS 2 y ESP32

**Descripción breve:** 
Configuración de un espacio de trabajo en ROS 2 para establecer comunicación serial bidireccional con un microcontrolador ESP32.

**Explicación de funcionamiento (LED):**
El sistema del LED utiliza un nodo publicador (`led_blink.py`) que genera comandos de estado (0 y 1) en el tópico `/led_command` periódicamente. Un nodo subscriptor (`serial_bridge.py`) escucha este tópico y escribe físicamente el dato en el puerto serial conectado al ESP32, encendiendo o apagando el LED de la placa de desarrollo.

**Explicación de funcionamiento (Potenciómetro):**
El sistema de lectura analógica utiliza el ESP32 para leer la variación de voltaje del potenciómetro y enviarla por el puerto serial. Un nodo publicador en ROS 2 (`analog_serial_pub.py`) intercepta este puerto y publica la lectura como un dato de tipo Int32 en el tópico `/analog`. Simultáneamente, el nodo subscriptor (`analog_subs.py`) se mantiene a la escucha de este tópico y registra los cambios en la terminal en tiempo real.

**Evidencia en video (Práctica 3):**
https://drive.google.com/file/d/1BN5PVfTQJ86hhEGQilGJHWaXFFlGhi1n/view?usp=sharing

## Tarea 4: Control con Joystick y ESP32

**Descripción:** Sistema para controlar el movimiento de Turtlesim usando un módulo joystick y un ESP32 mediante comunicación serial.

**Explicación de nodos y tópicos:**
1. **`joystick_pub.py` (Publicador):** Lee el puerto serial de la ESP32 y publica los valores de 12 bits en el tópico `/joystick_data` usando mensajes `std_msgs/String`.
2. **`turtle_controller.py` (Subscriptor):** Escucha `/joystick_data`, aplica zona muerta y control proporcional, y publica en el tópico `/turtle1/cmd_vel` con mensajes `geometry_msgs/Twist` para mover la tortuga.

**Límites y Zona Muerta:**
* **Límites de velocidad:** Lineal = 2.0 m/s, Angular = 2.0 rad/s. Justificación: Valores mayores dificultan el control suave y provocan colisiones rápidas con los bordes del simulador.
* **Zona muerta:** Rango de 1848 a 2248 (~10% alrededor del centro de 2048). Razón: El potenciómetro del joystick tiene ruido mecánico/eléctrico, esta tolerancia evita que la tortuga se mueva sola en posición de reposo.

**Comandos:** `ros2 run turtlesim turtlesim_node`, `ros2 run basics joystick_pub`, `ros2 run basics turtle_controller`.

**Problemas:** Ruido en el ADC generaba lecturas con comas extra. Se solucionó validando la estructura del String con un `try-except` y comprobando la coma separadora.

**Video:** [https://drive.google.com/drive/folders/1cGgV3uluH7qB-fDrqvxCo4OXLkDQRR1C?usp=drive_link]
