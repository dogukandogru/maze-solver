Programı çalıştırabilmek için öncelikle Python3 veya daha üst bir versiyon bilgisayarınızda kurulu olmalıdır.

Daha sonra gerekli kütüphaneleri yüklemek için konsolda şu komutu çağırmalısınız.

"pip install -r requirements"

Bu komut tüm gerekli kütüphaneleri otomatik olarak kuracaktır.

"main.py" dosyasını çalıştırarak projeyi başlatabilirsiniz.

Program ilk olarak sizden 5 ile 100 arasında bir labirent boyutu girmeniz istenecektir. Girdiğiniz boyutlardaki labirent otomatik ve rastgele bir biçimde oluşturulacaktır.

Boyut girişi yapıldıktan sonra, program size oluşturulan labirenti gösterecek ve iki seçenek sunacaktır. Bunlar başlangıç ve bitiş pozisyonlarını otomatik mi yoksa manuel mi eklemek istediğiniz ile alakalıdır. İstediğiniz seçeneği seçerek devam edebilirsiniz.

Otomatik seçeneğini seçerseniz başlangıç pozisyonu rastgele oluşturulacaktır. Daha sonra program sizden kaç tane bitiş noktası istediğinizi soracaktır. Buna da istediğiniz rakamı girerek enter tuşuna basabilirsiniz. Daha sonra girdiğiniz sayı adetinde bitiş noktası oluşturulup labirente eklenecektir

Eğer manuel seçeneğini seçerseniz program sizden başlangıç noktasının koordinatlarını isteyecektir. Bu koordinatları girdikten sonra yine size kaç adet bitiş noktası istediğinizi soracaktır. Buna da isteğiniz doğrultusunda cevap verdikten sonra tüm bitiş noktalarının koordinatlarını tek tek yazmanız gerekmektedir.

Bu adımdan sonra program size labirenti hangi algoritmayı kullanarak çözmek istersiniz sorusunu soracaktır. Burada toplam dört seçenek bulunmaktadır. Bunlar DFS, BFS, UCS veya hepsi şeklindedir. 

Program burada seçtiğiniz seçeneğe göre algoritmayı veya algoritmaları kullanarak labirentte ilk karşılaşacağı hedef noktasını bulana kadar labirenti çözecektir. 

Program labirenti çözdükten sonra labirentteki çözüm yolunu ekrana basacaktır ve alt kısımda algoritmanın kaç saniye sürdüğünü de detaylı bir biçimde verecektir. Labirentte görülen yeşil kare başlangıç noktası, mavi kareler gidilen yolu, mor kareler ise bitiş noktalarını temsil ediyor.

Program en son kısımda tekrar denemek ister misiniz diye soracaktır. Bu seçeneği evet şeklinde cevaplarsanız süreç baştan başlayacak, hayır şeklinde cevaplarsanız ise program sonlanacaktır.

