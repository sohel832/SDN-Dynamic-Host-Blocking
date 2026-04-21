🚀 SDN Dynamic Host Blocking System
📌 Overview

The SDN Dynamic Host Blocking System is a security-focused project built using Software Defined Networking (SDN). It dynamically detects suspicious hosts and blocks them in real time using programmable network control.

Unlike traditional networks, SDN separates the control plane and data plane, enabling centralized and flexible network management.

🎯 Objectives
Detect malicious or suspicious hosts
Dynamically block attackers using SDN controller logic
Improve network security with real-time monitoring
Demonstrate SDN-based intrusion prevention
🧠 Key Concepts
Software Defined Networking (SDN)
OpenFlow Protocol
Centralized Controller (POX)
Flow Rule Installation
Dynamic Host Blocking
🏗️ System Architecture
        +----------------------+
        |   SDN Controller     |
        |     (POX)            |
        +----------+-----------+
                   |
                OpenFlow
                   |
        +----------v-----------+
        |    Open vSwitch      |
        +----------+-----------+
                   |
        ------------------------
        |        |            |
      Host A   Host B     Attacker
⚙️ Technologies Used
Python 🐍
POX Controller
Mininet
Open vSwitch
Ubuntu Linux
📂 Project Structure
SDN-Dynamic-Host-Blocking/
│── dynamic_blocking.py
│── topology.py
│── README.md
🚀 Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/sohel832/SDN-Dynamic-Host-Blocking.git
cd SDN-Dynamic-Host-Blocking
2️⃣ Install Dependencies
sudo apt update
sudo apt install mininet openvswitch-switch python3
▶️ Execution Steps
Step 1: Run POX Controller
cd pox
python3 pox.py log.level --DEBUG forwarding.l2_learning
Step 2: Run Mininet Topology
sudo python3 topology.py
🔍 Working Mechanism
Network traffic flows through Open vSwitch
Controller monitors packets using OpenFlow
Suspicious activity is detected
Controller installs flow rules
Attacker is blocked from communication
📊 Features

✔ Real-time host blocking
✔ Centralized network control
✔ Scalable architecture
✔ Easy to extend for IDS/IPS
✔ Works in Mininet simulation

🧪 Testing
Test Connectivity
h1 ping h2
Expected Output
INFO: Blocking host 10.0.0.3
Flow rule installed successfully
🚧 Future Enhancements
Machine Learning-based attack detection
GUI dashboard
Multi-controller support
DDoS detection
👨‍💻 Author

Sohel Chapparband

📜 License

This project is for academic and educational purposes.
