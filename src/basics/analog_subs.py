import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class AnalogSubscriber(Node):
    def __init__(self):
        super().__init__('analog_subscriber')
        # Se suscribe al tópico '/analog' y vincula la función callback
        self.subscription_ = self.create_subscription(Int32, '/analog', self.analog_callback, 10)
        self.get_logger().info('Esperando datos')

    def analog_callback(self, msg):
        # Extrae el dato recibido y lo imprime en la consola de la terminal
        valor = msg.data
        self.get_logger().info(f'ADC = {valor}')

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSubscriber()
    rclpy.spin(node) # Mantiene el nodo a la escucha
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()