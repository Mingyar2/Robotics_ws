import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #la nueva libreria que cambia respecto a la original 

class VelocityTurtleSubscriber(Node):
    def __init__(self):
        super().__init__('velocity_turtle_subs')
        
        # Se suscribe al mismo tópico o canal de la tortuga para escuchar sus comandos
        self.subscription_ = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.velocity_callback,
            10)

    def velocity_callback(self, msg):
        # Lee la velocidad translacional (eje X) del mensaje Twist
        Velocity = msg.linear.x
        self.get_logger().info(f'Escuchando tortuga: Vel = {Velocity:.1f} m/s')

def main(args = None):
    rclpy.init(args=args)
    node = VelocityTurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
