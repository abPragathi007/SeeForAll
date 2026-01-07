import cv2
from ultralytics import YOLO
import pyttsx3
import threading
import queue
import time

# ===================== CONFIG =====================
CONF_THRESH = 0.45
SPEAK_INTERVAL = 0.8        # Minimum time between narrations
REFRESH_INTERVAL = 4.0      # Repeat reminder if scene unchanged
TTS_RATE = 210
# ==================================================

speech_queue = queue.Queue(maxsize=1)
stop_signal = threading.Event()

# ===================== TTS WORKER =====================
def tts_worker():
    while not stop_signal.is_set():
        try:
            message = speech_queue.get(timeout=0.2)
            if message is None:
                break

            print(f"DEBUG: Speaking -> {message}")

            engine = pyttsx3.init()
            engine.setProperty('rate', TTS_RATE)
            engine.say(message)
            engine.runAndWait()
            engine.stop()
            del engine

            speech_queue.task_done()
        except queue.Empty:
            continue
        except Exception as e:
            print(f"TTS Error: {e}")

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(message):
    while not speech_queue.empty():
        try:
            speech_queue.get_nowait()
        except:
            break
    try:
        speech_queue.put_nowait(message)
    except:
        pass

# ===================== YOLO SETUP =====================
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

def get_position(x_center, frame_width):
    if x_center < frame_width / 3:
        return "left"
    elif x_center > 2 * frame_width / 3:
        return "right"
    else:
        return "ahead"

def estimate_distance(box_height, frame_height):
    ratio = box_height / frame_height
    if ratio > 0.45:
        return "very close"
    elif ratio > 0.25:
        return "near"
    else:
        return "far"

# ===================== STATE =====================
last_scene_signature = set()
last_speak_time = 0

print("🎯 System Started. Checking for objects...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        results = model(frame, verbose=False)[0]

        current_narrations = []
        current_signature = set()

        if results.boxes is not None:
            for box in results.boxes:
                if float(box.conf[0]) < CONF_THRESH:
                    continue

                cls_id = int(box.cls[0])
                name = model.names[cls_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x_center = (x1 + x2) / 2
                box_height = y2 - y1

                position = get_position(x_center, w)
                distance = estimate_distance(box_height, h)

                signature = f"{name}-{position}-{distance}"
                current_signature.add(signature)
                current_narrations.append(f"{name} {position}, {distance}")

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Draw label on screen
                label = f"{name} | {position} | {distance}"
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        # ===================== SPEAK LOGIC =====================
        current_time = time.time()
        scene_changed = current_signature != last_scene_signature
        time_elapsed = current_time - last_speak_time

        if current_narrations:
            if (scene_changed and time_elapsed >= SPEAK_INTERVAL) or \
               (time_elapsed >= REFRESH_INTERVAL):

                message = ", ".join(current_narrations)
                speak(message)
                last_scene_signature = current_signature
                last_speak_time = current_time

        cv2.imshow("Detection Window", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    stop_signal.set()
    cap.release()
    cv2.destroyAllWindows()
