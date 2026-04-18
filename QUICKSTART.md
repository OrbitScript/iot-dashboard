# Quick Start Guide

Get your IoT Dashboard up and running in 5 minutes!

## 🚀 Installation

### Option 1: Automated Setup (Linux/Mac)

```bash
git clone https://github.com/yourusername/iot-dashboard.git
cd iot-dashboard
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup (All Platforms)

```bash
git clone https://github.com/yourusername/iot-dashboard.git
cd iot-dashboard
pip install -r requirements.txt
```

## ▶️ Running

### Start the Dashboard

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

### Start the Simulator (for testing)

In a **new terminal window**:

```bash
python simulator.py
```

You should see data appearing on your dashboard within seconds!

## 🔧 Connecting Your Device

### Step 1: Install MQTT Library on Your Device

**ESP32/Arduino:**
```cpp
#include <PubSubClient.h>
```

**Raspberry Pi:**
```bash
pip install paho-mqtt
```

### Step 2: Publish Data

Send JSON in this format:
```json
{
  "Temperature": 25.5,
  "Humidity": 48.2,
  "Signal": -55
}
```

### Step 3: Update Settings

In both `app.py` and your device code:
- Set `MQTT_BROKER` to your broker address
- Set `MQTT_TOPIC` to a unique topic name

## 📊 What You'll See

- **Real-time metrics**: Temperature, Humidity, Signal Strength
- **Live charts**: Historical trends updating every 2 seconds
- **Data table**: Raw data feed with timestamps

## 🆘 Troubleshooting

**Dashboard not updating?**
- Check that simulator is running
- Verify both use the same MQTT broker and topic
- Check your internet connection

**Can't install dependencies?**
- Upgrade pip: `pip install --upgrade pip`
- Try Python 3.8+: `python3.8 -m pip install -r requirements.txt`

**Port already in use?**
- Streamlit uses port 8501 by default
- Change with: `streamlit run app.py --server.port 8502`

## 📚 Next Steps

- Customize the UI in `app.py`
- Add more sensors/metrics
- Deploy to cloud (Streamlit Cloud, Heroku, etc.)
- Implement authentication for production use

Happy monitoring! 🎉
