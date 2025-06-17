# Sor_Bul Mini Akinatör

Python ve Tkinter kullanılarak geliştirilmiş, kullanıcıdan aldığı evet/hayır cevaplarına göre karakter tahmini yapan mini bir Akinatör uygulamasıdır.

---

## Özellikler

- Var olan karakterler arasında tahmin yapar.
- Yeni karakter ekleme imkanı sağlar.
- Yeni sorular ekleyerek uygulamayı genişletme imkanı sunar.

---

⚠️ **ÖNEMLİ NOT**

Eğer bir karakter için sistemde henüz uygun soru yoksa, bu karakter doğru tahmin edilemez.  
Örneğin Cristiano Ronaldo gibi bir karakteri eklemek istiyorsanız:

1. **Önce "Yeni Soru Ekle" kısmından** `is_footballer` gibi bir özellik eklemelisiniz (örneğin: "Futbolcu mu?"). 


2. **Ardından, "Yeni Karakter Ekle" bölümünden** Cristiano Ronaldo'yu tanımlarken bu soruya "Evet", diğer uygun sorulara da gerçek değerlerini vermelisiniz.

Yeni karakter eklemeden önce gerekli soruların eklenmiş olması gerekir.  
Soru ve karakter ekleme işlemleri ayrı ayrı yapılmalıdır.

---
Kod Açıklaması
characters.json dosyasında karakterlerin bilgileri tutulur.

questions.json dosyasında soruların anahtarları ve açıklamaları saklanır.

Uygulama, Tkinter ile grafik arayüz sağlar.

Ana menüde:

Karakter Tahmini Yap: Sorular sorularak kullanıcının düşündüğü karakter tahmin edilmeye çalışılır.

Yeni Karakter Ekle: Yeni bir karakter tanımlanır ve karakterin sorulara verdiği cevaplar kaydedilir.

Yeni Soru Ekle: Sistemde olmayan yeni sorular eklenir, böylece karakter çeşitliliği artırılır.

Karakter tahmini, kullanıcının sorulara verdiği cevaplara göre karakter listesi süzülerek yapılır.

Eğer hiçbir karakter tam olarak eşleşmezse, en çok eşleşen karakter tahmin olarak gösterilir.

Yeni soru ve karakter ekleme işlemleri, JSON dosyalarına kaydedilir, böylece uygulama kapandıktan sonra bilgiler korunur.

Kullanım Önerileri
Önce karakterlerin özelliklerine uygun soruları ekleyin.

Ardından yeni karakterleri ekleyerek sisteminizi genişletin.

Sorular ve karakterler arttıkça tahmin doğruluğu artacaktır.

Projeyi geliştirmek için farklı özellikler ve sorular ekleyebilirsiniz.

## Örnek Karakter ve Soru

Projeye eklenmiş örnek bir karakter:

```json
{
  "name": "Cristiano Ronaldo",
  "is_food": false,
  "is_real": true,
  "is_male": true,
  "is_live": true,
  "is_teacher": false,
  "is_employee": false,
  "is_student": false,
  "is_management": false,
  "is_handsome": true,
  "is_beatiful": true,
  "is_footballer": true
}
