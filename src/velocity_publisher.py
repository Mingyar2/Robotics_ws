import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class VelocityPublisher(Node):
    def __init__(self):
         # aqui se inicia la clase heredando de Node y nombra el nodo
        super().__init__('velocity_publisher')
# Crea el publicador: tipo Float32, tópico '/velocity', cola de 10
        self.publisher_ = self.create_publisher(Float32,'/velocity',10)
        self.Vel = 0.0 #aqui se inicializa la variable
        self.timer_ = self.create_timer(0.5,self.publish_velocity) #este es el tempo para ejecutar la funcion c .5seg
    def publish_velocity(self):
        msg = Float32()
        msg.data = self.Vel
        self.publisher_.publish(msg) #aqui se publica el mensaje
        self.get_logger().info(f'Vel = {self.Vel:.1f} m/s') #aqui imprimo el mensaje
#loop de logica de incremento y que se reinicie
        if self.Vel < 1.5:
            self.Vel = round(self.Vel + 0.1, 1)
        else:
            self.Vel = 0.0

def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    rclpy.spin(node) #esto mantiene el nodo activo
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
