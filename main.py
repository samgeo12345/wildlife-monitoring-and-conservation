import cv2
video_path = "videos/elephant.mp4"
shootvideo = cv2.VideoCapture(video_path)
fgbg = cv2.createBackgroundSubtractorMOG2()
while shootvideo.isOpened():
    ret, frame = shootvideo.read()
    if not ret:
        break
    frame = cv2.resize(frame, (800, 450))
    fgmask = fgbg.apply(frame)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Wildlife Motion Detection', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
shootvideo.release()
cv2.destroyAllWindows()
