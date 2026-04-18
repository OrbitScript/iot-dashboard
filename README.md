# 🚀 Universal IoT Real-Time Dashboard

A professional, real-time IoT dashboard built with Python and Streamlit that connects to MQTT-enabled devices for live data visualization.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Real-time MQTT Integration** - Subscribe to MQTT topics and receive live updates
- **Live Auto-Updating Charts** - Visualize environmental data with interactive charts
- **Hardware Agnostic** - Compatible with ESP32, Arduino, Raspberry Pi, and any MQTT-capable device
- **Clean UI** - Modern, responsive dashboard built with Streamlit
- **Data History** - Maintains last 50 data points for trend analysis

## 📊 Dashboard Preview

The dashboard displays:
- Real-time temperature readings (°C)
- Humidity levels (%)
- Signal strength (dBm)
- Historical trend charts
- Raw data feed table

## 🛠 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/iot-dashboard.git
cd iot-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Running the Simulator (for testing)

In a separate terminal, run the data simulator:

```bash
python simulator.py
```

The simulator publishes random sensor data to the MQTT broker for testing purposes.

## 🔧 Configuration

### MQTT Settings

Edit these variables in `app.py` and `simulator.py` to match your setup:

```python
MQTT_BROKER = "broker.emqx.io"  # Your MQTT broker address
MQTT_TOPIC = "python/iot/dashboard/demo"  # Your MQTT topic
```

### Connecting Your IoT Device

To connect your own device, publish JSON data to your MQTT topic in this format:

```json
{
  "Temperature": 25.5,
  "Humidity": 48.2,
  "Signal": -55
}
```

#### Example ESP32/Arduino Code

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* mqtt_broker = "broker.emqx.io";
const char* topic = "python/iot/dashboard/demo";

WiFiClient espClient;
PubSubClient client(espClient);

void publishData() {
  StaticJsonDocument<200> doc;
  doc["Temperature"] = readTemperature(); // Your sensor reading
  doc["Humidity"] = readHumidity();       // Your sensor reading
  doc["Signal"] = WiFi.RSSI();
  
  char buffer[256];
  serializeJson(doc, buffer);
  client.publish(topic, buffer);
}
```

## 📁 Project Structure

```
iot-dashboard/
├── app.py              # Main dashboard application
├── simulator.py        # Data simulator for testing
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore rules
```

## 🔒 Security Notes

- The default configuration uses a public MQTT broker (`broker.emqx.io`) for demonstration
- For production use, implement authentication and use a private MQTT broker
- Consider using TLS/SSL for encrypted communications

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- MQTT client powered by [Paho MQTT](https://www.eclipse.org/paho/)
- Public MQTT broker provided by [EMQX](https://www.emqx.io/)

## 📧 Contact

For questions or support, please open an issue in the GitHub repository.

---

**Happy Monitoring! 📊**
