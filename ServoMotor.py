import matplotlib.pyplot as plt


class ServoMotor:
    def __init__(self):
        # Servo motorun başlangıç açısını 90 derece olarak ayarlıyoruz (nötr pozisyon).
        self.angle = 90

        # Etkileşimli mod etkinleştiriliyor.
        plt.ion()

        self.figure, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'ro-')

        # Grafiğin sınırlarını ayarlıyoruz (0-180 derece).
        self.ax.set_xlim(0, 180)
        self.ax.set_ylim(-1, 1)

        # Görseli güncelleyerek başlangıç durumunu ekranda gösteriyoruz.
        self.update_visual()

    def update_visual(self):
        # Grafiği temizleyip yeniden çiziyoruz.
        self.ax.cla()
        self.ax.set_xlim(0, 180)  # X eksenini servo motor açıları için ayarlıyoruz.
        self.ax.set_ylim(-1, 1)  # Y ekseni sabit tutuluyor (motorun açısal hareketi için gerekli değil).

        # Mevcut açıyı grafikte göstermek için bir çizgi ekliyoruz.
        self.line, = self.ax.plot([self.angle, self.angle], [-1, 1], 'ro-')

        # Grafiği yeniden çiziyoruz ve kısa bir duraklama ekliyoruz.
        plt.draw()
        plt.pause(0.1)

    def move_to(self, target_angle):
        # Servo motorun hedef açıya hareket etmesini simüle ediyoruz.
        self.angle = target_angle  # Hedef açıyı güncelliyoruz.
        self.update_visual()

    def update_angle(self, position, frame_width):
        # Görüntüdeki pozisyona göre servo motorun açısını hesaplıyoruz.

        self.angle = (position / frame_width) * 180
        self.move_to(self.angle)
