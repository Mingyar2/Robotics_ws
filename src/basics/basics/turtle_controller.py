import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller') # Nombra el nodo
        self.subscription = self.create_subscription(String, '/joystick_data', self.joy_callback, 10) # Suscriptor de datos
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) # Publicador a Turtlesim
        
        self.max_lin = 2.0 # Velocidad lineal máxima ajustada
        self.max_ang = 2.0 # Velocidad angular máxima ajustada

    def joy_callback(self, msg):
        try:
            valores = msg.data.split(',') # Separa X y Y
            x_adc = int(valores[0])
            y_adc = int(valores[1])
            
            # Zona muerta del 10% alrededor del centro (2048)
            if 1843 < x_adc < 2252: x_adc = 2048
            if 1843 < y_adc < 2252: y_adc = 2048
                
            twist = Twist()
            # Mapeo matemático proporcional de (0-4095) a (-2.0 a +2.0)
            twist.linear.x = ((y_adc - 2048) / 2048.0) * self.max_lin * -1.0 
            twist.angular.z = ((x_adc - 2048) / 2048.0) * self.max_ang * -1.0
            
            self.publisher_.publish(twist) # Ejecuta movimiento
        except Exception:
            pass # Ignora lecturas basura

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node) # Mantiene la escucha
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()