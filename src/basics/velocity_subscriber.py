import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class VelocitySubscriber(Node):
    def __init__(self):
        # Define el nombre del nodo subscriptor
        super().__init__('velocity_subscriber')
        # Se suscribe al tópico '/velocity' y vincula la función callback
        self.subscription = self.create_subscription(
            Float32,
            '/velocity',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        # Función que se ejecuta al recibir un mensaje; lo imprime en consola
        self.get_logger().info(f'He escuchado: Vel = {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = VelocitySubscriber()
    rclpy.spin(node) # Mantiene el nodo escuchando
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
