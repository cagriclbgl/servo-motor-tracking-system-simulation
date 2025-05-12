Bu proje, bir servo motorun, kırmızı topun hareketini takip etmesini simüle eden basit bir sistemdir. HSV kalibrasyonu sayesinde topun daha doğru bir şekilde takip edilmesi sağlanır. Proje, grafiksel bir simülasyon ile servo motorun yönelimi görselleştirilir.

## Proje Özeti

Bu sistemde, bir kırmızı top bir siyah zemin üzerinde hareket etmektedir. Servo motor, topu takip etmek için yöneltilir. HSV (Hue, Saturation, Value) renk uzayı kalibrasyonu kullanılarak kırmızı topun renk değerleri optimize edilir. Bu sayede nesne takibi daha doğru ve hassas hale gelir.

### Özellikler:
- Servo motor simülasyonu: Servo motorun topu takip etmek için yapması gereken hareketler grafiksel olarak simüle edilir.
- HSV kalibrasyonu: Kırmızı topun daha doğru bir şekilde izlenebilmesi için HSV renk kalibrasyonu yapılır.
- Grafiksel görselleştirme: Servo motorun yönelimi ve topun hareketi bir grafik üzerinde gösterilir.

## Kullanılan Teknolojiler

- Python 3.x
- OpenCV (Görüntü işleme ve nesne takibi için)
- Matplotlib (Grafiksel görselleştirme için)

## Gereksinimler

Projenin çalışabilmesi için aşağıdaki Python kütüphanelerine ihtiyacınız olacak:

pip install opencv-python matplotlib

## Kullanım

1. Proje dosyalarını indirin ve gerekli kütüphaneleri yükleyin:
    pip install opencv-python matplotlib

2. Ana dosya olan `main.py`'yi çalıştırarak simülasyonu başlatın:
    python main.py

3. Sonuç: Çalıştırma sonrası bir grafik penceresi açılacak ve burada kırmızı topun hareketine göre servo motorun yönelimi görselleştirilecektir. Ayrıca, HSV kalibrasyonu sayesinde topun izlenebilirliği arttırılmış olacaktır.

## İleriye Yönelik Geliştirmeler

- Gerçek servo motor ile entegrasyon: Bu proje, gerçek bir servo motor ile çalışacak şekilde geliştirilebilir.
- Nesne takibi: Sisteme farklı renklerde ve şekillerde nesneler eklenebilir.
- Hız ve hassasiyet iyileştirmeleri: Takip hızını ve doğruluğu arttıracak algoritmalar eklenebilir.



