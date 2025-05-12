import cv2
import numpy as np

def nothing(x):
    # Trackbar için gerekli ama işlevsiz bir geri çağırma fonksiyonu.
    pass

# Kamera ile bağlantı kuruyoruz.
cap = cv2.VideoCapture(0)

# HSV değerlerini ayarlamak için trackbar'ları oluşturuyoruz.
cv2.namedWindow('Trackbars')
cv2.createTrackbar('LH', 'Trackbars', 0, 180, nothing)  # Alt Hue
cv2.createTrackbar('LS', 'Trackbars', 0, 255, nothing)  # Alt Saturation
cv2.createTrackbar('LV', 'Trackbars', 0, 255, nothing)  # Alt Value
cv2.createTrackbar('UH', 'Trackbars', 0, 180, nothing)  # Üst Hue
cv2.createTrackbar('US', 'Trackbars', 0, 255, nothing)  # Üst Saturation
cv2.createTrackbar('UV', 'Trackbars', 0, 255, nothing)  # Üst Value

while True:
    ret, frame = cap.read()
    if not ret:
        # Kamera bağlantısı kesildiyse veya bir hata oluştuysa döngüyü bitiriyoruz.
        break

    # Görüntüyü HSV renk uzayına çeviriyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lar üzerinden HSV değerlerini alıyoruz.
    l_h = cv2.getTrackbarPos('LH', 'Trackbars')
    l_s = cv2.getTrackbarPos('LS', 'Trackbars')
    l_v = cv2.getTrackbarPos('LV', 'Trackbars')
    u_h = cv2.getTrackbarPos('UH', 'Trackbars')
    u_s = cv2.getTrackbarPos('US', 'Trackbars')
    u_v = cv2.getTrackbarPos('UV', 'Trackbars')

    # Maske oluşturmak için renk aralığını belirliyoruz.
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Maskeyi orijinal görüntüye uyguluyoruz.
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri ekranda gösteriyoruz.
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    # 'q' tuşuna basılarak çıkış sağlanabilir.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(f"Lower HSV: {lower_bound}")
        print(f"Upper HSV: {upper_bound}")
        break

cap.release()
cv2.destroyAllWindows()
