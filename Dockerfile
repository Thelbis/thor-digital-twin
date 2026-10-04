FROM ros:humble-ros-base

RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws/src

RUN git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git -b main-ros2

WORKDIR /ros2_ws

RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

COPY . /ros2_ws/thor-digital-twin/

EXPOSE 10000

CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && source /ros2_ws/install/setup.bash && ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=0.0.0.0"]
