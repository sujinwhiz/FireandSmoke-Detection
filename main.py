import cv2
import numpy as np

# Open webcam (0 = default camera)q
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define fire color range in HSV
    lower = np.array([18, 50, 50])
    upper = np.array([35, 255, 255])

    # Create a mask for fire color
    mask = cv2.inRange(hsv, lower, upper)

    # Apply mask on original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Count the number of fire pixels
    fire_pixels = cv2.countNonZero(mask)
    if fire_pixels > 1000:  # Adjust threshold as needed
        cv2.putText(frame, "Fire Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

    # Display result
    cv2.imshow("Fire Detection", frame)
    cv2.imshow("Fire Mask", result)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
