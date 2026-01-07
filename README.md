# SeeForAll 👁️‍🗨️  
### Real-Time AI Vision Assistant for the Visually Impaired

SeeForAll is a real-time computer vision–based assistive system that detects objects using **YOLOv8** and provides **audio narration** describing what is present in front of the user.  
The project is designed to help visually impaired users understand their surroundings through spoken feedback.

---

## 🚀 Project Motivation

Visually impaired individuals often face difficulty identifying obstacles, people, and objects around them.  
SeeForAll bridges this gap by combining **AI-based object detection** with **text-to-speech narration**, enabling users to hear what the camera sees in real time.

---

## ✨ Key Features

- 🔍 Real-time object detection using YOLOv8  
- 🔊 Voice narration of detected objects  
- 🧭 Direction awareness (left / ahead / right)  
- 📏 Distance estimation (far / near / very close)  
- 🧠 Smart narration control to avoid repeated speech  
- 🖥️ Live detection window for visual feedback  

---

## 🛠️ Technologies Used

- Python 3.10  
- YOLOv8 (Ultralytics)  
- OpenCV  
- PyTorch  
- PyTTSx3 (offline text-to-speech)  
- Multithreading & Queues  

---

## ⚙️ How It Works

1. The webcam captures live video frames  
2. YOLOv8 detects objects in each frame  
3. For each detected object:
   - Position is calculated (left / ahead / right)
   - Distance is estimated using bounding box size  
4. A narration message is generated  
5. The system speaks the detected objects in real time  

---

## 📂 Project Structure

SeeForAll/
│
├── see_for_all.py # Main application code
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files & folders

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/abPragathi007/SeeForAll.git
cd SeeForAll
2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment

-->Windows
venv\Scripts\activate

--> Linux / macOS
source venv/bin/activate
4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the application
python see_for_all.py


Press Q to quit the application.

⚠️ Important Notes

A working webcam is required

Speakers or headphones are required for narration

This project runs only on a local system

It does not run on GitHub Pages or Codespaces

YOLO model weights download automatically on first run

🧪 Limitations

Distance estimation is approximate

Performance depends on lighting conditions

Requires a system with camera and audio support
🔮 Future Enhancements

🚦 Obstacle danger alerts for very close objects

🎤 Voice commands (mute / resume narration)

📱 Mobile camera support (IP webcam)

🌐 Web-based version for image/video uploads

🧭 Navigation and path guidance

👩‍💻 Author

Pragathi
AI & Computer Vision Enthusiast

📜 License

This project is open-source and available under the MIT License.


---

## ✅ After pasting this (FINAL STEP)

Run these commands:

```powershell
git add README.md
git commit -m "Add complete project documentation"
git push