# 🔥 Real-Time Fire and Smoke Detection

This project detects fire and smoke in real-time using a webcam feed. It uses Python, OpenCV, and HSV color space filtering to identify fire-smoke like regions. This solution is designed to provide early alerts for fire hazards in indoor environments.

---

## 📽️ Demo

> 🔴 Fire Detected!  
> ✅ Real-time detection through camera feed



---
## ✅ Install Requirements

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```
<details> <summary>📄 <code>requirements.txt</code> contents</summary>
opencv-python  
numpy
</details>

## Run the Application
  python main.py  
  Press q to quit the webcam feed.
## 🧠 How It Works
Captures video from the webcam in real-time.

Converts each frame to HSV color space.

Applies a color filter to detect fire-like regions (orange/yellow).

If enough pixels match fire color, it displays "Fire Detected!" on screen.

## ⚠️ Limitations
This is a basic color-based detection system and may give false positives in the presence of similar colors.

Smoke detection is not included in this version (can be added using motion/blur detection or deep learning).

## 🌟 Future Enhancements
🔲 Integrate smoke detection using edge blur + motion tracking

📦 Add YOLOv5/YOLOv8 model for more accurate fire/smoke classification

📲 Trigger SMS or Email alerts (Twilio/Gmail API)

🔊 Add buzzer or voice alarm for real-world alerts

