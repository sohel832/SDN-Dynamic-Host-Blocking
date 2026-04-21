🚀 SDN Dynamic Host Blocking System
📌 Overview

The SDN Dynamic Host Blocking System is a security-focused project built using Software Defined Networking (SDN) principles. It dynamically detects suspicious hosts and blocks them in real-time using programmable network control.

Unlike traditional networks, SDN separates the control plane and data plane, enabling centralized and flexible network management. This project leverages that capability to implement automated intrusion prevention.

🎯 Objectives
Detect malicious or suspicious hosts in the network
Dynamically block attackers using SDN controller logic
Improve network security using real-time monitoring
Demonstrate SDN-based intrusion prevention system
🧠 Key Concepts Used
Software Defined Networking (SDN)
OpenFlow Protocol
Centralized Controller (POX / Ryu)
Flow Rules Installation
Dynamic Host Blocking
🏗️ System Architecture
+----------------------+
|   SDN Controller     |
| (POX / RYU)          |
+----------+-----------+
           |
           | OpenFlow
           |
+----------v-----------+
|   Open vSwitch       |
+----------+-----------+
           |
   ---------------------
   |        |         |
Host A   Host B   Attacker
⚙️ Technologies Used
Python 🐍
POX Controller
Mininet (Network Emulator)
Open vSwitch
Ubuntu Linux
📂 Project Structure
SDN-Dynamic-Host-Blocking/
│── pox/
│── mininet/
│── scripts/
│── README.md
│── requirements.txt
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/sohel832/SDN-Dynamic-Host-Blocking.git
cd SDN-Dynamic-Host-Blocking
2️⃣ Install Dependencies
sudo apt update
sudo apt install mininet openvswitch-switch python3
3️⃣ Run POX Controller
cd pox
python3 pox.py log.level --DEBUG forwarding.l2_learning
4️⃣ Start Mininet
sudo mn --topo single,3 --controller remote
🔍 Working Mechanism
Network traffic flows through Open vSwitch
Controller monitors packets using OpenFlow
Suspicious behavior is detected
Controller installs flow rules to block attacker
Malicious host is isolated from network

👉 This approach is similar to SDN-based intrusion prevention systems where controllers dynamically enforce security policies

📊 Features

✔ Real-time host blocking
✔ Centralized network control
✔ Scalable architecture
✔ Easy to extend for IDS/IPS
✔ Works in simulated environment (Mininet)

🧪 Testing
Ping between hosts
Simulate malicious traffic
Verify blocking using flow rules

Example:

h1 ping h2
📸 Sample Output
INFO: Blocking host 10.0.0.3
Flow rule installed successfully
🚧 Future Enhancements
Integrate Machine Learning for attack detection
Add GUI Dashboard
Support multiple controllers
Extend to DDoS detection
👨‍💻 Author

Sohel Chapparband

📜 License

This project is for academic and educational purposes.

⭐ Contribution

Feel free to fork this repo and contribute!
