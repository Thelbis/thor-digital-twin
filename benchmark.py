import sys
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import JointState

class SettlingBenchmark(Node):
    def __init__(self):
        super().__init__('settling_benchmark')
        # Target Link 3
        import sys
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import JointState

class FlexibleBenchmark(Node):
    def __init__(self, joint_num, target_deg):
        super().__init__('flexible_benchmark')
        self.joint_num = joint_num
        self.target_deg = target_deg
        self.target_rad = target_deg * (3.14159265 / 180.0)
        
        # Topic and Subscription setup
        self.pub = self.create_publisher(Float32, f'/link_{joint_num}', 10)
        self.sub = self.create_subscription(JointState, '/joint_states', self.state_callback, 10)
        
        self.start_time = 0.0
        self.test_active = False
        self.timer = self.create_timer(2.0, self.fire_command)

    def fire_command(self):
        self.timer.cancel()
        self.get_logger().info(f'Commanding link_{self.joint_num} to {self.target_deg}°...')
        self.start_time = time.time()
        self.pub.publish(Float32(data=self.target_deg))
        self.test_active = True

    def state_callback(self, msg):
        if not self.test_active:
            return
            
        # Array index is joint_num - 1 (e.g. link_1 -> index 0)
        idx = self.joint_num - 1
        current_pos = msg.position[idx] 
        
        if abs(current_pos - self.target_rad) < 0.001:
            total_time = time.time() - self.start_time
            self.get_logger().info(f'Target acquired! Total round-trip time: {total_time:.3f} seconds')
            self.test_active = False

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 benchmark.py <joint_number> <target_degrees>")
        print("Example: python3 benchmark.py 3 30")
        return

    joint_num = int(sys.argv[1])
    target_deg = float(sys.argv[2])

    rclpy.init()
    node = FlexibleBenchmark(joint_num, target_deg)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
