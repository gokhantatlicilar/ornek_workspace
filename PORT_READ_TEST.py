Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
from Tkinter as tk
from Tkinter import *

pencere = Tk ()
pencere.title("Avcı")
pencere.geometry("300x300+100+100")  #Pencere oluşturldu

def kayit():
	kayit_pencere = tk.Toplevel()
	kayit_pencere.title("KAYIT")
	kayit_pencere.geometry("300x300+100+100")
	kayit_pencere_yeni_kayit = Button(kayit_pencere, text="Kayıt penceresi için Yeni kayit butonu")
	kayit_pencere_yeni_kayit.pack(side="left")


yeni_kayit = Button(text="Yeni kayit", command=kayit)# kayit Butonu
yeni_kayit.pack(side="left")

kayit_getir = Button(text="kayit Getir")# kayit getirme butonu
kayit_getir.pack()

duzenle = Button(text="duzenle") #kayit duzenleme butonu
duzenle.pack(side="right")
cikis = Button(text="ÇIKIŞ") #Sistemden çıkş butonu
cikis.pack(side="bottom")
mainloop()
