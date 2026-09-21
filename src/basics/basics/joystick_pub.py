import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class JoystickPub(Node):
    def __init__(self):
        super().__init__('joystick_pub') # Nombra el nodo
        self.publisher_ = self.create_publisher(String, '/joystick_data', 10) # Tópico personalizado
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1) # Abre puerto físico
        self.timer_ = self.create_timer(0.05, self.read_serial) # Timer rápido para evitar lag

    def read_serial(self):
        if self.serial_.in_waiting > 0: # Si hay datos entrantes
            linea = self.serial_.readline().decode().strip() # Lee y limpia la cadena
            if "," in linea: # Valida que vengan ambos ejes
                msg = String()
                msg.data = linea
                self.publisher_.publish(msg) # Publica a ROS 2

def main(args=None):
    rclpy.init(args=args)
    node = JoystickPub()
    rclpy.spin(node) # Mantiene el publicador activo
    node.serial_.close() # Cierra el puerto al apagar
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()