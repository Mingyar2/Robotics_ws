import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist  # Importamos el mensaje espacial Twist

class VelocityTurtlePublisher(Node):
    def __init__(self):
        super().__init__('velocity_turtle_pub')
        
        # El tópico estándar de Turtlesim para recibir velocidad es '/turtle1/cmd_vel'
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        self.vel_x = 0.0
        self.detenido = False # flag para saber cuándo parar
        
        # timer configurado a medio segundo (0.5)
        self.timer_ = self.create_timer(0.5, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist() #  la instancia del mensaje
        
        if not self.detenido:
            msg.linear.x = self.vel_x #  velocidad translacional en el eje X
            self.publisher_.publish(msg)
            self.get_logger().info(f'Traslacion = {self.vel_x:.1f}')
            
            # el incremento o aumento  de 0.1 hasta llegar a 1.2
            if self.vel_x < 1.2:
                self.vel_x = round(self.vel_x + 0.1, 1)
            else:
                self.detenido = True
        else:
            # Una vez alcanzado 1.2, se manda velocidad 0.0 para que se detenga por completo
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Límite alcanzado (1.2). Tortuga detenida.')

def main(args=None):
    rclpy.init(args=args)
    node = VelocityTurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
