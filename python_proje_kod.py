#!/usr/bin/env python
# coding: utf-8

# In[51]:


class Solucan:
    def __init__(self, sinif, cins):      #iki değişken oluşturuyoruz.
        self.sinifi = sinif
        self.cinsi = cins
    def __str__(self):           #__str__ ile print fonksiyonunu yazıyoruz.
        return "Solucanlar; Yassı, Yuvarlak, Halkalı olarak ayrılırlar."
    def tanit(self):    #kendimiz fonksiyonlar oluşturuyoruz.
        print(f"{self.cinsi}, hayvanlar aleminin {self.sinifi} sınıfında bulunur.")
    def ozellik_ver(self):
        print("Ömrü 2-6 yıl kadardır.")
        

#Kodun çalıştırılması       
solucan1 = Solucan("Omurgasızlar","Yassı Solucan")
print(solucan1.sinifi)    #özellikleri çağırırken parantez kullanmıyoruz.
print(solucan1.cinsi)
print(solucan1)
solucan1.tanit()        #fonksiyonları çağırırken parantez kullanıyoruz.
solucan1.ozellik_ver()


# In[52]:


class Kurbaga(Solucan): #İçerisine Solucan yazarak Solucan class'ından miras alıyoruz.
    def __str__(self):  #__str__ fonksiyonunu override ediyoruz. Artık Solucan class'ındaki yerine bu geçerli olacak.
        return """Kurbağalar: Hayvanlar aleminin Omurgalılar sınıfında bulunurlar.
        Toplam 33 familyaya dağılmış yaklaşık 5250 türü bulunur."""
    def ozellik_ver(self):
        print("Amfibi (ikiyaşamlı) canlılardır.")
    def puan_ver(self):
        puan = int(input("Kurbağalara 10 üzerinden kaç puan verirdiniz?"))
        if puan <10:
            print("Yanlış cevap. 10 puan olacaktı.")
        else:
            print("Çok doğru")
        

#Kodun çalıştırılması
kurbaga1 = Kurbaga("Omurgalılar", "Toprak Kurbağası")
print(kurbaga1.sinifi)
print(kurbaga1.cinsi)
print(kurbaga1)
kurbaga1.tanit()
kurbaga1.ozellik_ver()
kurbaga1.puan_ver()


# In[53]:


class Balik():
    def __init__(self,sinif, cins):
        self.sinifi = sinif
        self.cinsi = cins
    def ornek_ver(self):
        balik_listesi = ["Yılan Balığı","Vatoz Balığı", "Somon", "Orkinos"]
        if self in balik_listesi:
            balik_listesi.remove(self)
        else:
            print("Balıklara örnekler:\n", balik_listesi)
    def pop_quiz(self):
        cevap = input("Balık yemeyenlere ne denir?")
        if cevap.lower() == "pesketaryen":
            print("Doğru!!")
        else:
            print("Yanlış.. Pesketaryen.")
    

#Kodun çalışması
balik1 = Balik("Omurgalılar", "Levrek")
print(balik1.sinifi)
print(balik1.cinsi)
balik1.ornek_ver()
balik1.pop_quiz()


# In[54]:


class Sunger():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):         #normalde listelerde çalışan len() fonksiyonunu biz tanımlıyoruz.
        print("Tanımlanmış yaklaşık 5000 türü vardır.")
    def soru_sor(self):
        cvp = input("En ünlü sünger kimdir?")
        if cvp.lower() == "süngerbob":
            print("Doğru cevap!!")
        else:
            print("Bilemedin, süngerbob olacaktı.")
    def bilgi_ver(self):
        print("Süngerler, en ilkel çok hücreli canlı gruplarındandır.")

#Kodun çalışması
sunger1 = Sunger("Omurgasızlar", "Deniz süngeri")
print(sunger1.sinifi)
print(sunger1.cinsi)
sunger1.__len__()
sunger1.bilgi_ver()
sunger1.soru_sor()
    


# In[55]:


class Eklembacak():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):
        print("Tanımlanmış yaklaşık 1 milyon türü vardır.")
    
    def bilgi_ver(self):
        print("Eklembacaklılar, Omurgasızların en büyük grubudur.")
    
    def ornek_ver(self):
        print("Karada örümcekler, akrepler ve böcekler;/n denizlerdeyse yengeçler ve karidesler eklembacaklılara örnektir.")
    
#Kodun çalışması
eklembacak1 = Eklembacak("Omurgasızlar", "Örümcek")
print(eklembacak1.sinifi)
print(eklembacak1.cinsi)
eklembacak1.bilgi_ver() 
eklembacak1.__len__()


# In[56]:


class Kedi:
    def __init__(self, cins, goz_renk, tuy_renk):
        self.cins = cins
        self.goz_renk = goz_renk
        self.tuy_renk = tuy_renk
    def miyavla(self):
        print("Miyaaaav")
    def insan_yasi_karsiligi(self, kedi_yasi):
        if kedi_yasi == 1:
            print("1 yaşındaki kedinin insan yaşı: 15")
        elif kedi_yasi == 2:
            print("2 yaşındaki kedinin insan yaşı: 24")
        else:
            print(f"{kedi_yasi} yaşındaki kedinin yaşı:")
            kedi_yasi = 24 + (kedi_yasi-2)*4
            print(kedi_yasi)


#Kodun çalışması
kedi1 = Kedi("Sibirya","mavi","beyaz")
print(kedi1.goz_renk)
print(kedi1.tuy_renk)
print(kedi1.cins)
kedi1.miyavla()
kedi1.insan_yasi_karsiligi(6)


# In[57]:


class Kopek:
        def __init__(self,cins= "",cinsiyet="",yas="1"):  #kullanıcı verileri girmeyince attribute'ların alacağı değerleri belirliyoruz.
            self.cinsi = cins
            self.cinsiyeti = cinsiyet
            self.yasi = yas
        def ses_cikar(self):
            print("Havhavhav")
        def insan_yasina_cevir(self):
            x = self.yasi
            if x == 1:
                print("1 yaşındaki köpeğin insan yaşı: 15")
            elif x == 2:
                print("2 yaşındaki köpeğin insan yaşı: 24")
            else:
                insan_yasi = 24 + ((x-2)*5)
                print(f"{x} yaşındaki köpeğin yaşı:{insan_yasi}")
                
            #Operator overloading: Python'da var olan bir operator fonksiyonun bizim class'ımızda çalışması için tekrar yazmak. 
            #Mesela __add__(self,other) => toplama, __sub__(self,other) => çıkarma , __mul__(self,other) =>çarpma
        def __add__(self,other): #Operator overloading yapıyoruz.
            return self.yasi + other.yasi   #burada other dediğimiz toplayacağımız diğer class elemanı
        

#kodun çalışması     
kopek1 = Kopek("Labrador","erkek",2)   
kopek2 = Kopek("Poodle","dişi",4)
print(kopek1.cinsi)
print(kopek1.cinsiyeti)
print(kopek2.yasi)
kopek2.ses_cikar()
kopek1.insan_yasina_cevir()

print(kopek1 + kopek2)  #__add__ fonksiyonumuzla 2 köpeğin yaşlarını topluyoruz.


# In[58]:


class Papagan(Kopek):   #miras
    def ses_cikar(self):     #override
        x = input("Bir şey yaz.")
        print(x)
    def insan_yasina_cevir(self):    #override
        pass

#kodun çalışması         
papagan1 = Papagan("Sultan","erkek",55)
papagan2 = Papagan("Afrika Gri","dişi",45)  
print(papagan1.cinsi)
print(papagan2.cinsiyeti)
print(papagan2.yasi)
papagan1.ses_cikar()
papagan2.insan_yasina_cevir()

print(papagan1 + papagan2) #__add__ fonksiyonunu çağırabiliyoruz çünkü Kopek class'ından miras aldık.


# In[ ]:




