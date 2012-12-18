# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
import os
import urllib2
import datetime
import smtplib
import webbrowser
try:
    pencere = Tk()
    pencere.title("Robot Yönetim v3.0")
    pencere.geometry("300x300")


    def albumol():
        global albumpen
        global giris8
        albumpen = Toplevel()
        albumpen.title("Albüm oluştur")
        giris8 = Entry(albumpen)
        giris8.insert(END,"Albüm Adı")
        giris8.pack()
        buton35 = Button(albumpen,text="Tamam",command=albumolustur)
        buton35.pack()
    def albumolustur():
        try:
            os.chdir("fotolar")
        except:
            pass
        os.mkdir(giris8.get())
        albumpen.destroy()
    def fotogez():
        fotolar = Toplevel()
        try:
            os.chdir("fotolar")
        except:
            pass
        fotolis = os.listdir(os.curdir)
        fotogorliste = Listbox(fotolar)
        fotogorliste.pack()
        for i in fotolis:
            fotogorliste.insert(END,i)
        def gosterici(event):
            os.system(u"nautilus %s" %fotogorliste.get(ACTIVE))
        fotogorliste.bind("<Double-Button-1>", gosterici)
        
        


    def fotoyon():
        fotopen = Toplevel()
        fotopen.title("Fotoğraf Yönetim Paneli")
        buton33 = Button(fotopen,text=u"Fotoğraf Albümü oluştur",command=albumol)
        buton34 = Button(fotopen,text="Fotoğraf Albümlerini gez",command=fotogez)
        buton33.pack()
        buton34.pack()

    def kayit():
        global bugun
        kayitpen = Toplevel()
        kayitpen.title("Kayıtlar")
        if os.path.isdir("kayit"):
            pass
        else:
            os.mkdir("kayit")
            pass
        bugunt = datetime.date.today()
        buguna = str(bugunt)
        bugun = buguna + ".txt"
        buton29=Button(kayitpen,text=u"Kayıt ekle",command=kayitekle)
        buton30 = Button(kayitpen,text=u"Kayıtları gözden geçir",command=kayitgozana)
        buton29.pack()
        buton30.pack()
    def kayitekle():
        global kayiteklepen
        global text1get
        global giris6get
        global giris6
        global text1
        kayiteklepen = Toplevel()
        kayiteklepen.title("Kayıt Ekle")
        giris6 = Entry(kayiteklepen)
        giris6.pack()
        giris6.insert(END,u"Başlığı yazınız")
        text1 = Text(kayiteklepen,font = "TimesNewRoman 13")
        text1.pack()
        buton31 = Button(kayiteklepen,text="Ekle",command = kaydagec)
        buton31.pack()
    def kaydagec():
        os.chdir("kayit")
        kayitdosyaw=open(bugun,"w")
        kayitdosyaw.write(giris6.get())
        kayitdosyaw.write("\n")
        kayitdosyaw.write("\n")
        kayitdosyaw.write(unicode(text1.get(1.0,END)))
        giris6.delete(0,END)
        kayitdosyaw.close()
        kayiteklepen.destroy()
    def kayitgozana():
        global kayitgozpen
        kayitgozpen = Toplevel()
        kayitgozpen.title("Kayıtları Düzenle")
        global giris7
        global giris8
        global giris9
        try:
            os.chdir("kayit")
        except:
            pass
        giris7 = Entry(kayitgozpen)
        giris7.pack()
        giris7.insert(END,u"Tarih")
        giris8 = Entry(kayitgozpen)
        giris8.pack()
        giris8.insert(END,u"Ay")
        giris9 = Entry(kayitgozpen)
        giris9.pack()
        giris9.insert(END,u"Gün")
        buton32 = Button(kayitgozpen, text="Git",command=kayitac)
        buton32.pack()
    def kayitac():
        global kaydabakpen
        global tarih
        global text2
        tarih = "%s-%s-%s" %(giris7.get(),giris8.get(),giris9.get())
        kayitdosyawr = open(tarih + ".txt")
        kaydabakpen = Toplevel()
        kaydabakpen.title("Kayıt açıldı")
        text2 = Text(kaydabakpen,font = "TimesNewRoman 13")
        text2.pack()
        oku = kayitdosyawr.read()
        text2.insert(END,oku)
        buton33 = Button(kaydabakpen,text="Kaydet",command=kaydikaydet)
        buton33.pack()
    def kaydikaydet():
        kayitdosyawri=open(tarih + ".txt","w")
        kayitdosyawri.write(text2.get(1.0,END))
        kaydabakpen.destroy()
        
    buton28 = Button(text=u"Kayıtlar",command=kayit)
    buton28.pack(side=TOP,anchor=NW)



    def programlar():
        penpro = Toplevel()
        penpro.title("Programlar")
        penpro.geometry("200x200")
        def sunu():
            os.system("libreoffice --impress %U")
        def programses():
            os.system("gnome-sound-recorder")
        def programpy():
            os.system("idle")
        def youtube():
            webbrowser.open("http://www.youtube.com")
        def internet():
            os.system("chromium-browser")

        buton3 = Button(penpro, text ="Ses kaydet",command=programses)
        buton3.pack(side=TOP,anchor=NW)
        buton4 = Button(penpro, text ="Python ile robot programla",command=programpy)
        buton4.pack(side=TOP,anchor=NW)
        buton6 = Button(penpro, text="Youtube", command=youtube)
        buton6.pack(side=TOP,anchor=NW)
        buton7 = Button(penpro, text = u"İnternet", command = internet)
        buton7.pack(side=TOP,anchor=NW)
        buton14 = Button(penpro, text = "Sunu hazırla",command = sunu)
        buton14.pack(side=TOP,anchor=NW)
    buton2 = Button(text="Programlar",command=programlar)
    buton2.pack(side=TOP,anchor=NW)
    def ekip():
        ekipanapen = Toplevel()
        ekipanapen.title(u"Ekip ayarları")
        ekipdosya = open("ekip.txt")
        ekipliste = ekipdosya.readlines()
        ekipgorliste = Listbox(ekipanapen)
        ekipgorliste.pack()
        for i in ekipliste:
            ekipgorliste.insert(END,i)
        def yeni():
            global giris1
            global eklepen
            eklepen = Toplevel()
            eklepen.title("Ekle")
            giris1 = Entry(eklepen)
            giris1.pack()
            buton9 = Button(eklepen, text="Ekle",command = ekle)
            buton9.pack()
        def ekle():
            ekipgorliste.insert(END,giris1.get())
            ekledef = giris1.get() + "\n"
            ekipliste.append(ekledef)
            giris1.delete(0,END)
            eklepen.destroy()
        def sil():
            a = ekipgorliste.get(ACTIVE)
            ekipliste.remove(a)
            ekipgorliste.delete(ACTIVE)
        def kaydet():
            ekipdosya.close()
            ekipkaydosya = open("ekip.txt","w")
            ekipkaydosya.writelines(ekipliste)
            ekipanapen.destroy()
        def iptal():
            soru = showwarning("Uyarı",
                                u"Değişiklikleri kaydetmediniz",
                                detail = "Kaydetmek ister misiniz?",
                                type = OKCANCEL)
            if soru == "ok":
                kaydet()
            if soru == "cancel":
                ekipanapen.destroy()
                
        buton10 = Button(ekipanapen,text="Ekle",command = yeni)
        buton10.pack(side=LEFT)
        buton11 = Button(ekipanapen,text="Sil",command = sil)
        buton11.pack(side=LEFT)
        buton12 = Button(ekipanapen,text="Kaydet",command=kaydet)
        buton12.pack(side=LEFT)
        buton13 = Button(ekipanapen,text="İptal",command=iptal)
        buton13.pack(side=LEFT)
    buton8 = Button(text="Ekibi Düzenle",command = ekip)
    buton8.pack(side=TOP,anchor=NW)

    def olay():
        global olaypen
        olaypen = Toplevel()
        olaypen.title=("Olay oluştur")
        bilgilabel = Label(olaypen,text=u"Lütfen oluşturacağınız olayı seçin")
        bilgilabel.pack()
        buton15 = Button(olaypen,text=u"FLL yarışması",command=fll)
        buton15.pack(side=TOP,anchor=NW)
        buton16 = Button(olaypen,text=u"Gösteri",command=show)
        buton16.pack(side=TOP,anchor=NW)
    olaysave= open("olaysave.txt","a")
    def fll():
        global entry2
        global entry3
        global fllanapen
        fllanapen = Toplevel()
        fllanapen.title("Fll yarışması oluştur")
        entry2 = Entry(fllanapen)
        entry2.insert(END,u"Yarışmanın adını yazınız")
        entry2.pack()
        entry3=Entry(fllanapen)
        entry3.pack()
        entry3.insert(END,u"İlk yarışma Tarihi")
        buton18 = Button(fllanapen,text=u"Oluştur",command = fllolustur)
        buton18.pack()
    def fllolustur():
        flliste=[]
        adsave = entry2.get() + "\n"
        tarihsave = entry3.get() + "\n"
        flliste.append(adsave)
        flliste.append(tarihsave)
        flldosya = open("fllana.txt","w")
        flldosya.writelines(flliste)
        olaysavewr = "FLL yarışması:" + adsave
        olaysave.write(olaysavewr)
        flldosya.close()
        fllanapen.destroy()
        olaysave.close()

        

    def show():
        if os.path.isdir("gosteri"):
            pass
        else:
            os.mkdir("gosteri")
        os.chdir("gosteri")
        showanadosya = open("show.txt","w")
        showanadosya.close()
        os.chdir(os.pardir)
        olaysave.write("gosteri \n")
        olaypen.destroy()
        olaysave.close()
    buton17 = Button(text=u"Olay oluştur",command=olay)
    buton17.pack(side=TOP,anchor=NW)

    def olayac():
        olayacpen=Toplevel()
        olayacpen.title("Olay aç...")
        olaysave.close()
        olaysave2 = open("olaysave.txt")
        olayliste = olaysave2.readline()
        olay = Button(olayacpen,text=olayliste,command=fllana)
        if olayliste == "gosteri \n":
            os.system("explorer C:\\Documents and Settings\\MehmetAlkan\\Desktop\\robot\\gosteri")
            pencere.destroy()
        else:
             olay.pack()
    def fllana():
        fllpen = Toplevel()
        fllpen.title("FLL yarışması")
        flldosya = open("fllana.txt","r")
        fllliste = flldosya.readlines()
        yaradi = fllliste[0]
        yartarih = fllliste[1]
        labelad = Label(fllpen,text=yaradi)
        labelad.pack()
        labeltarih= Label(fllpen,text=yartarih)
        labeltarih.pack()
        def ac():
            os.system("explorer C:\\Documents and Settings\\MehmetAlkan\\Desktop\\robot\\fll")

        def fllliste():
            flllistepen = Toplevel()
            flllistepen.title(u"Yapılacaklar")
            yapdosya = open("yap.txt")
            yapliste = yapdosya.readlines()
            yapgorliste = Listbox(flllistepen)
            yapgorliste.pack()
            for i in yapliste:
                yapgorliste.insert(END,i)
            def fllyeni():
                global giris5
                global flleklepen
                flleklepen = Toplevel()
                flleklepen.title("Ekle")
                giris5 = Entry(flleklepen)
                giris5.pack()
                buton21 = Button(flleklepen, text="Ekle",command = fllekle)
                buton21.pack()
            def fllekle():
                yapgorliste.insert(END,giris5.get())
                ekledeffll = giris5.get() + "\n"
                yapliste.append(ekledeffll)
                giris5.delete(0,END)
                flleklepen.destroy()
            def fllsil():
                b = yapgorliste.get(ACTIVE)
                yapliste.remove(b)
                yapgorliste.delete(ACTIVE)
            def fllkaydet():
                yapdosya.close()
                yapkaydosya = open("yap.txt","w")
                yapkaydosya.writelines(yapliste)
                flllistepen.destroy()
            def flliptal():
                soru2 = showwarning("Uyarı",
                                    u"Değişiklikleri kaydetmediniz",
                                    detail = "Kaydetmek ister misiniz?",
                                    type = OKCANCEL)
                if soru2 == "ok":
                    fllkaydet()
                if soru2 == "cancel":
                    flllistepen.destroy()
                    
            buton22 = Button(flllistepen,text="Ekle",command = fllyeni)
            buton22.pack(side=LEFT)
            buton23 = Button(flllistepen,text="Sil",command = fllsil)
            buton23.pack(side=LEFT)
            buton24 = Button(flllistepen,text="Kaydet",command=fllkaydet)
            buton24.pack(side=LEFT)
            buton25 = Button(flllistepen,text="İptal",command=flliptal)
            buton25.pack(side=LEFT)
        
            
        buton20 = Button(fllpen,text=u"Çalışma dizinini aç",command=ac)
        buton20.pack()
        buton26 = Button(fllpen,text=u"Yapılacaklar listesi",command=fllliste)
        buton26.pack()


    buton19 = Button(text="Olay aç...",command = olayac)
    buton19.pack(side=TOP,anchor=NW)

    def reset():
        soru3 = showwarning("Uyarı","Bu komut yaptığınız her şeyi silecek",
                            type=OKCANCEL)
        if soru3 == "ok":
            os.system("rm gosteri")
            os.system("rm ekip.txt")
            os.system("rm kayit")
            olaysave.close()
            os.system("rm olaysave.txt")
            os.system("rm fllana.txt")
            os.system("rm yap.txt")
            showinfo("Reset","Resetleme işlemi bitti")
            dosya1 = open("ekip.txt","w")
            dosya2 = open("yap.txt","w")
            os.system("mkdir fotolar")
        pencere.destroy()
        if soru3 == "cancel":
            pencere.destroy()

    buton27 = Button(text="Reset",command=reset)
    buton27.pack(side=TOP,anchor=NW)
    buton34 = Button(text=u"Fotoğraflar",command=fotoyon)
    buton34.pack(side=TOP,anchor=NW)
    kayitbuton = Button(text=u"Gönder")
    kayitbuton.pack(side=TOP,anchor=NW) 
    mainloop()
except:
    import tkMessageBox
    showerror("Hata","Program bir hata ile karşılaştı ve kapanacak.")
        

