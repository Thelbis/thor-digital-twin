FROM ros:humble-ros-base

WORKDIR /ros2_ws

RUN apt-get update && apt-get install -y \
    ros-humble-ros-tcp-endpoint \
    && rm -rf /var/lib/apt/lists/*

COPY . /ros2_ws/thor-digital-twin/

SHELL ["/bin/bash", "-c"]
EXPOSE 10000

CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0"]
