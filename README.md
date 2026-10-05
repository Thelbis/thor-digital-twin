# Thor 6-DOF Digital Twin

A bi-directional digital twin of the Thor 6-DOF robotic arm combining ROS 2 (Humble) and Unity.

## Features
* **Rigid Physics Simulation:** Utilizes Unity `ArticulationBody` components with custom joint control scripts.
* **Bi-directional Communication:**
  * **Publisher:** Streams real-time joint positions to `/joint_states` at 20 Hz.
  * **Subscriber:** Listens to `/link_1` through `/link_6` (using `std_msgs/Float32`).
* **Containerized Backend:** Fully containerized ROS 2 environment running `ros_tcp_endpoint`.

## Quick Start (Docker Hub)
Pull and run the pre-built ROS 2 container directly:
## Local Setup
1. **Clone the Repository:**
2. **Build Docker Image:**
3. **Run Container:**
