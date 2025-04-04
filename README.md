# 3D Shapes Visualization and Tracking System
## Project Overview
A real-time interactive system that visualizes and tracks the positions of 3D shapes (cube and cone) with synchronized web display.
- This project provides a real-time 3D visualization system that allows users to:
  - Control a cube and cone in a 3D space using keyboard inputs
  - View the positions of both shapes in a web interface
  - See both shapes' movements visualized in a single graph with a shared origin point

## 🌟 Features

- **Interactive 3D Control**:
  - 🟦 Cube manipulation with WASD-QE keys
  - 🔺 Cone control using arrow keys + TAB/SHIFT
- **Real-time Visualization**:
  - Single coordinate system with shared origin
  - Color-coded vectors (blue for cube, red for cone)
- **Web Interface**:
  - Live coordinate tracking
  - Connection status monitoring
  - Responsive design
## Installation
- **1.Clone the Repository:**
   - [ git clone]() [repository-url]()
   - [cd [repository-name]]()
- **2.Install dependencies:**
    - [pip install -r requirements.txt]()
- **3.manually install:**
  - [pip install open3d flask flask-socketio eventlet python-socketio]()
## Running The System
  - **1.Start the server (in one terminal):**
    - [python server/server.py]()
  - **2.Start the visualizer (in another terminal):**
    - [python client/cube_app.py]()
  - **3.Access the web interface at:**
    - [http://localhost:5000]()
## 🎮 Control Scheme

| Command       | Cube Action (🟦) | Cone Action (🔺) |
|---------------|------------------|------------------|
| W / ↑         | Move Up          | Move Up          |
| A / ←         | Move Left        | Move Left        |
| S / ↓         | Move Down        | Move Down        |
| D / →         | Move Right       | Move Right       |
| Q / TAB       | Move Forward     | Move Forward     |
| E / SHIFT     | Move Back        | Move Back        |

## 📦 System Architecture

```mermaid
graph TD
    A[Open3D Visualizer] -->|Socket.IO| B[Flask Server]
    B -->|Socket.IO| C[Web Interface]
    C --> D[D3.js Visualization]
