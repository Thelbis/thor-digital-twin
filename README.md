# Thor 6-DOF Digital Twin (Unity + ROS 2)

A bi-directional digital twin of the Thor 6-DOF robotic arm combining ROS 2 (Humble) and Unity, developed for manufacturing cell simulation research. This project establishes a real-time communication bridge between a robust Unity physics simulation and a containerized ROS 2 environment using Docker.

## Features
* **Rigid Physics Simulation:** Utilizes Unity `ArticulationBody` components with custom dynamic locking to prevent unactuated gripper segments from sprawling.
* **Bi-directional Communication:** 
  * **Publisher:** Streams real-time joint positions to `/joint_states` at 20 Hz.
  * **Subscriber:** Listens to `/link_1` through `/link_6` (using `std_msgs/Float32`) for external actuation commands.
* **Containerized Backend:** Fully containerized ROS 2 environment running `ros_tcp_endpoint` via Docker, ensuring cross-platform compatibility.

## Prerequisites
* **Unity:** 2022.3 LTS (or newer) with the `Unity-Robotics-Hub` TCP Connector package installed.
* **Docker:** Installed and running on the host machine.
* **Git:** To clone the repository.

## Installation & Setup

### 1. Clone the Repository

