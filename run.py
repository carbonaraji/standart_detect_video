from ultralytics import YOLO
import cv2


model=YOLO("YOUR YOLO MODEL") 
VIDEO_PATH="YOUR VIDEO" 
OUTPUT_PATH="result.jpg" 

cap=cv2.VideoCapture(VIDEO_PATH) 

if not cap.isOpened(): 
    print("не удалось открыть видео")
    exit() 

fps=int(cap.get(cv2.CAP_PROP_FPS)) 
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc=cv2.VideoWriter_fourcc(*"mp4v") 
out=cv2.VideoWriter("output_video.mp4",fourcc, fps, (width, height)) 

print(f"обработка видео: {VIDEO_PATH}") 

while True: 
    ret, frame=cap.read() 
    if not ret: 
        break

    results=model.predict( 
        source=frame,      
        conf=0.5,          
        iou=0.45,          
        save=False,        
        show=False,        
        verbose=False      
    )

    annotated_frame=results[0].plot() 
    out.write(annotated_frame) 
    cv2.imshow("yoloframe", annotated_frame) 

    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break

cap.release() 
out.release() 
cv2.destroyAllWindows() 
print(f"видео обработано")

