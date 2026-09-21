import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class LedBlink(Node):
    def __init__(self):
        super().__init__('led_blink')
        # Crea un publicador en el tópico '/led_command' de tipo Int32
        self.publisher_ = self.create_publisher(Int32, '/led_command', 10)
        self.estado = 1 # Variable inicial para alternar el estado
        
        # Temporizador que ejecuta blink_callback cada 1.0 segundos
        self.timer_ = self.create_timer(1.0, self.blink_callback)
        self.get_logger().info('Nodo iniciado')
        self.publicar_estado()

    def blink_callback(self):
        # Alterna el valor del estado entre 0 y 1
        if self.estado == 1:
            self.estado = 0
        else:
            self.estado = 1
        self.publicar_estado()

    def publicar_estado(self):
        # Construye el mensaje y lo publica en el tópico
        msg = Int32()
        msg.data = self.estado
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {self.estado}')

def main(args=None):
    rclpy.init(args=args)
    node = LedBlink()
    rclpy.spin(node) # Mantiene el nodo ejecutándose
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
