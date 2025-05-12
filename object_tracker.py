import cv2
import numpy as np


class ObjectTracker:
    def __init__(self, lower_color, upper_color):
        self.lower_color = np.array(lower_color, dtype="uint8")  # Alt renk sınırı
        self.upper_color = np.array(upper_color, dtype="uint8")  # Üst renk sınırı

    def track(self, frame):
        # Görüntüyü HSV renk uzayına dönüştürüyoruz.
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # HSV renk aralığına göre bir maske oluşturuyoruz.
        mask = cv2.inRange(hsv_frame, self.lower_color, self.upper_color)

        # Maskede kontur (çizgi) arıyoruz. Bu, nesnenin yerini belirlememize yardımcı oluyor.
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        position = None
        if contours:
            # En büyük konturu alıyoruz, bu genelde hedef nesnemiz oluyor.
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)  # Konturu dikdörtgene çeviriyoruz.

            # Dikdörtgenin merkezini hesaplıyoruz. Servo motor bu konuma göre hareket edecek.
            position = (x + w // 2, y + h // 2)

            # Görselde dikdörtgen çizerek nesneyi işaretliyoruz.
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return mask, position
