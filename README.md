# HandTracking
En


This project is a computer vision application that uses hand tracking to adjust the computer sound. It was developed as part of a computer vision lecture.


Tr


Bu proje, bilgisayar sesini ayarlamak için el takibi kullanarak bir bilgisayarlı görüntüleme uygulamasıdır. Bu proje, bilgisayarlı görme dersi kapsamında geliştirilmiştir.
Proje kodlarının ve amacının detaylı açıklamayı sunuda bulabilirsiniz.
[Bilgisayarlı Görme Proje Ödevi.pptx](https://github.com/codeBusch/HandTracking/files/11585441/Bilgisayarli.Gorme.Proje.Odevi.pptx)

## Proje Kurulumu

1. Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
pip install opencv-python mediapipe pycaw

2. `main.py` dosyasını çalıştırarak uygulamayı başlatın:


3. Uygulama, kameranızı kullanacak ve el takibini gerçekleştirecektir. El hareketlerinizin bilgisayar sesini nasıl ayarladığını gözlemleyebilirsiniz.

## Nasıl Kullanılır

1. Uygulama başladığında, kameranız aktif hale gelecektir.
2. Kameranın alanına ellerinizi getirin ve uygulama, el takibini gerçekleştirmeye başlayacaktır.
3. Baş parmağınızın ucu ve işaret parmağınızın ucu arasındaki mesafe, bilgisayar sesini ayarlamak için kullanılacaktır.
4. Mesafe ne kadar uzunsa, ses seviyesi o kadar yüksek olacak; mesafe ne kadar kısa ise, ses seviyesi o kadar düşük olacak.
5. Ses seviyesini istediğiniz gibi ayarlamak için el hareketlerinizi kullanabilirsiniz.

## Örnek Video

Projeyi çalışırken ve el hareketlerini nasıl kullandığınızı gösteren bir video örneğini aşağıdaki bağlantıdan izleyebilirsiniz:
https://youtu.be/TfCp4v1nxLw

## Katkıda Bulunma

Bu proje geliştirilmeye açıktır. Eğer projeye katkıda bulunmak isterseniz, lütfen bir "pull request" oluşturun. Yeni özellikler eklemek, hataları düzeltmek veya belgeleri geliştirmek için katkılarınızı bekliyoruz.




