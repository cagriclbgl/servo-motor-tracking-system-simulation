import cv2
import pyautogui

from object_tracker import ObjectTracker
from ServoMotor import ServoMotor

def main():
    # Ekran boyutlarını alıyoruz.
    screen_width, screen_height = pyautogui.size()

    video_path = "C:\\Users\\Cagri\\Desktop\\ornek_video.mp4"
    cap = cv2.VideoCapture(video_path)

    lower_color = (0, 182, 153)  # Algılama için alt HSV sınırı
    upper_color = (71, 255, 255)  # Algılama için üst HSV sınırı

    tracker = ObjectTracker(lower_color, upper_color)
    servo_motor = ServoMotor()

    if not cap.isOpened():
        print("Video açılamadı! Lütfen dosya yolunu kontrol edin.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video sonuna ulaşıldı veya görüntü alınamadı!")
            break

        # Performans ve görselleştirme için görüntüyü yeniden boyutlandırıyoruz.
        frame = cv2.resize(frame, (640, 480))

        # Hedef nesneyi takip eden algoritmayı çağırıyoruz.
        mask, position = tracker.track(frame)

        enhanced_mask = cv2.dilate(mask, None, iterations=2)  # Maske genişletiliyor.
        enhanced_mask = cv2.erode(enhanced_mask, None, iterations=1)  # Gürültü azaltılıyor.

        # Eğer nesne algılandıysa, servo motorun açısını güncelliyoruz.
        if position is not None:
            frame_width = frame.shape[1]
            servo_motor.update_angle(position[0], frame_width)

        # Pencereleri oluşturuyoruz.
        window_name = "Orijinal"
        cv2.imshow(window_name, frame)

        # Pencerenin boyutları (örnek görüntü boyutu kullanılarak alınıyor).
        window_width = 640
        window_height = 480

        # Pencerenin konumunu hesaplıyoruz.
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Pencereyi ekranın ortasına taşıyoruz.
        cv2.moveWindow(window_name, x, y)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Video bitti. Pencereler açık kalacak, çıkış için herhangi bir tuşa basın.")
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
