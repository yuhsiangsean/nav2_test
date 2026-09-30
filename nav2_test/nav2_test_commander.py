import rclpy

from rclpy.node import Node

from std_msgs.msg import Int32


class Nav2TestCommander(Node):

    def __init__(self):

        super().__init__('nav2_test_commander')

        self.publisher = self.create_publisher(
            Int32,
            '/nav2_test/command',
            10
        )

    # ================================================================
    # Blocking input loop
    #
    # Runs in its own terminal/process, separate from
    # nav2_test_control's node (which prints frequent status logs).
    # That keeps this prompt from being scrolled away by log spam.
    # ================================================================

    def run(self):

        prompt = (
            '\n[Command] 1=hover(0.5m)  2=land  '
            '3=+X 0.5m  4=+Y 0.5m  '
            '5=goto(0.5,0)  6=goto(0,0.5)  > '
        )

        while rclpy.ok():

            try:
                line = input(prompt).strip()
            except EOFError:
                break

            if line not in ('1', '2', '3', '4', '5', '6'):

                print(f'Unknown command "{line}", use 1-6')

                continue

            msg = Int32()

            msg.data = int(line)

            self.publisher.publish(msg)

            print(f'Sent command {line}')


def main(args=None):

    rclpy.init(args=args)

    node = Nav2TestCommander()

    try:

        node.run()

    except KeyboardInterrupt:

        pass

    finally:

        node.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':

    main()
