import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class AnalogSerialPublisher(Node):
    def __init__(self):
        super().__init__('analog_serial_pub')
        # Crea un publicador en el tópico '/analog' para mensajes tipo Int32
        self.publisher_ = self.create_publisher(Int32, '/analog', 10)
        # Inicia la conexión serial con el ESP32
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # Temporizador para leer el puerto serial cada 0.01 segundos
        self.timer_ = self.create_timer(0.01, self.read_serial)
        self.get_logger().info('ESP32 conectada')

    def read_serial(self):
        # Verifica si hay datos disponibles en el puerto serial físico
        if self.serial_.in_waiting > 0:
            # Lee la línea, la decodifica y elimina espacios en blanco
            linea = self.serial_.readline().decode().strip()
            # Si el dato es un número válido, lo empaqueta y lo publica en el tópico
            if linea.isdigit():
                valor = int(linea)
                msg = Int32()
                msg.data = valor
                self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSerialPublisher()
    rclpy.spin(node) # Mantiene el nodo activo
    node.serial_.close() # Cierra el puerto serial al terminar de forma segura
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()