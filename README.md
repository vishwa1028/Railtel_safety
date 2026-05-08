# 🚆 RailTel Advanced Safety & Monitoring System

An AI-powered railway safety monitoring system designed to improve railway track safety using obstacle detection, crack detection, sensor networks, and automated alert systems.

This project simulates a smart railway monitoring solution that continuously analyzes track conditions and sends alerts to drivers, control stations, and maintenance workshops in real time.

---

## ✨ Project Overview

The system focuses on railway safety automation by combining:

- 3D obstacle detection
- Track crack detection
- Sensor network monitoring
- Automated SMS alerts
- Real-time safety analysis
- SQLite logging system
- Image-based obstacle processing

The goal of this project is to demonstrate how AI, computer vision, and sensor-based systems can be integrated into railway infrastructure for proactive safety monitoring.

---

## 🚀 Features

### 🚧 Obstacle Detection
- Simulates 3D obstacle detection
- Calculates:
  - Obstacle volume
  - Track blockage percentage
  - Brake pressure requirement
- Generates automatic braking decisions

### 🛤️ Crack Detection
- Detects simulated railway track cracks
- Measures crack severity
- Generates maintenance alerts

### 📡 Sensor Network
- Simulates multiple railway sensors
- Tracks train movement across positions
- Processes nearby sensor data dynamically

### 📲 SMS Alert System
Automatic alerts sent to:
- Train Driver
- Railway Control Station
- Maintenance Workshop

### 🗄️ Database Logging
- Stores alerts in SQLite database
- Maintains historical safety records

### 🖼️ Image Processing
- Uses OpenCV for obstacle detection
- Detects contours and large objects from images

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Development |
| OpenCV | Image Processing |
| NumPy | Numerical Operations |
| SQLite | Database Logging |
| Serial Communication | GSM Integration |
| PIL | Image Handling |
| JSON | Data Structuring |

---

## 📂 Project Structure

```bash
RailTelSafetySystem/
│
├── main.py
├── railtel_safety.db
├── README.md
├── requirements.txt
│
└── images/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/railtel-safety-system.git
cd railtel-safety-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🧠 System Workflow

```text
Sensor Network
      ↓
Obstacle / Crack Detection
      ↓
Safety Analysis
      ↓
Alert Generation
      ↓
Driver / Control / Workshop Notification
      ↓
Database Logging
```

---

## 🚨 Alert Types

### Driver Alerts
- Obstacle ahead
- Track crack ahead

### Control Station Alerts
- Crack severity
- Sensor readings
- Train location

### Workshop Alerts
- Maintenance requirement
- Repair urgency
- Crack location

---

## 📊 Safety Analysis

The system calculates:
- Brake pressure
- Track blockage percentage
- Crack severity
- Emergency braking decisions

Based on obstacle distance, the system can trigger:
- Emergency Brake
- Hard Brake
- Normal Brake
- Caution Mode

---

## 🖼️ Image Processing Module

The project includes OpenCV-based image processing that:
- Reads railway images
- Detects contours
- Identifies possible obstacles
- Extracts object dimensions

---

## 💾 Database Logging

All alerts are stored in SQLite with:
- Timestamp
- Alert type
- Severity
- Location
- Sensor data

This helps maintain safety records for analysis and maintenance planning.

---

## 🔮 Future Improvements

Possible future enhancements:
- Real hardware sensor integration
- Live GPS tracking
- AI-based crack classification
- Real-time dashboard
- Cloud deployment
- IoT integration
- Deep learning object detection
- Mobile alert application

---

## 📖 Learning Outcomes

This project helped in understanding:
- Railway safety automation
- Sensor network simulation
- Real-time alert systems
- Computer vision basics
- SQLite database handling
- GSM communication
- Safety-critical system design

---

## 👨‍💻 Author

Yelakanti Neeha

Built as an experimental railway safety monitoring and AI-based alert system project. :contentReference[oaicite:0]{index=0}

---

## 📄 License

This project is created for educational and research purposes.
