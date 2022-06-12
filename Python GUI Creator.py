from tkinter import *
from tkinter import messagebox

pen = Tk()
pen.title('Python GUI Creator')
pen.geometry('750x500')

def nnk():
    nnkp = Tk()
    nnkp.title('Python GUI Creator - Nedir ? Nasıl Kullanılır ?')
    nnkp.geometry('320x300')
    
    nnky = Label(nnkp, text="Python GUI Creator Kod Yazmadan Arayüzlü\nProgram Oluşturmanızı Sağlar. Kullanmak İçin\nSadece İstediğiniz Butonu Seçin Ve Ordaki\nButonda Yazan Kod Eklenecektir.\n\nCoded By M Talha - MuhammedTr768")
    nnky.pack()
    

    nnkp.mainloop()

def basla():
    def olsf():
        def ltime():
            intvar = int(yigir.get())
            tmdl = open(f"{filename}.py", "a", encoding="utf-8")
            tmdl.write(f"\ntime.sleep(intvar)")
            tmdl.close()
        def labeldznle():
            def olsdzn():
                labelopen = open(f"{filename}.py", "a", encoding="utf-8")
                labelopen.write(f'\n{dad.get()}["text"] = f"{istefrs.get()}"')
                labelopen.close()
            pena = Tk()
            pena.title('Label Düzenleme Kodu Ekle')
            pena.geometry('300x300')
            
            lgrn = Label(pena, text="Yazı Gir (Değişken Girecekseniz, {} içerisine yazın entry ise değişkenin sonuna .get() getirin)")
            lgrn.pack()
            istefrs = Entry(pena, width=20)
            istefrs.pack()
            btnsnnd = Button(pena, text="Ekle", width=14, command=olsdzn)
            btnsnnd.pack()
            
            
            pena.mainloop()
        def entryunt():
            entryus = open(f"{filename}.py", "a", encoding="utf-8")
            entryus.write(f"\n{dad.get()} = Entry({dad2.get()}, width={uzunlukgir.get()})\n{dad.get()}.place(x={xayar.get()},y={yayarknm.get()})")
            entryus.close()
        def funccalis():
            funcalisdeg = open(f"{filename}.py", "a", encoding="utf-8")
            funcalisdeg.write(f'\n{yigir.get}()')
            funcalisdeg.close()
        def kkefun():
            def olskkef():
                kkeolh = open(f"{filename}.py", "a", encoding="utf-8")
                kkeolh.write(f"\n{giriskke.get()}")
                kkeolh.close()
                messagebox.showinfo("Python GUI Creator", "Kod Eklendi")
            kkep = Tk()
            kkep.title('Kendin Kod Yaz')
            kkep.geometry('320x300')
            
            hgkkefun = Label(kkep, text="Kod Ekleme Bölümüne hoşgeldiniz", font="Arial 13")
            hgkkefun.pack()
            
            kkeblg = Label(kkep, text="Yazmak İstediğiniz Kodu Girin:")
            kkeblg.pack()
            giriskke = Entry(kkep, width=15)
            giriskke.pack()
            
            olsbtnkke = Button(kkep, text="Ekle", width=7, command=olskkef)
            olsbtnkke.pack()
        def dcaldi():
            dcalkodgir = open(f"{filename}.py", "a", encoding="utf-8")
            dcalkodgir.write(f"\n{dad.get()}")
            dcalkodgir.close()
            messagebox.showinfo("Python GUI Creator", "Kod Eklendi")
        def hzrpack():
            userekle = open(f"{filename}.py", "a", encoding="utf-8")
            userekle.write('\nusermttgui = os.getcwd()[9:12]')
            userekle.close()
        def codeview():
            codepen = Tk()
            codepen.title('Kod Penceresi')
            codepen.geometry('500x500')
            
            kodlar = Label(codepen, text="")
            kodlar.pack()
            kodlarr = open(f"{filename}.py", "r", encoding="utf-8")
            kodoku = kodlarr.read()
            kodlar["text"] = kodoku
            codepen.mainloop()
        def buttol():
            butolyaz = open(f"{filename}.py", "a", encoding="utf-8")
            butolyaz.write(f"\n{dad.get()} = Button({dad2.get()}, text='{yigir.get()}', width={uzunlukgir.get()}, command={bient.get()})\n{dad.get()}.place(x={xayar.get()},y={yayarknm.get()})")
            butolyaz.close()
        def defol():
            def degolstr():
                defolusum = open(f"{filename}.py", "a", encoding="utf-8")
                defolusum.write(f'\n{dadgirisyap.get()} = {dyazgiris.get()}')
                defolusum.close()
                messagebox.showinfo("Python GUI Creator", "Değişken Eklendi")
            depen = Tk()
            depen.title('Değişken Penceresi')
            depen.geometry('320x300')
            
            hgdepen = Label(depen, text="Değişken Penceresine\nHoşgeldiniz", font="Arial 13")
            hgdepen.pack()
            
            dadgirinizltfn = Label(depen, text="Oluşturmak İstediğiniz Değişken Adı Girin:")
            dadgirinizltfn.pack()
            dadgirisyap = Entry(depen, width=15)
            dadgirisyap.pack()
            
            dyazgir = Label(depen, text="Değişkenin İçerisine Yazmak İstediğinizi Girin")
            dyazgir.pack()
            
            dyazgiris = Entry(depen, width=15)
            dyazgiris.pack()
            
            btnoldudeg = Button(depen, text="Ekle", command=degolstr)
            btnoldudeg.pack()
            
            depen.mainloop()
        def funcol():
            def newlabel():
                def butonprf():
                    pgcr = open(f"{filename}.py", "a", encoding="utf-8")
                    pgcr.write(f'\n    {entdeg.get()} = Label({newvar.get()}, text="{sjent.get()}")\n{entdeg.place({xyten.get()})}')
                prf = Tk()
                prf.title('Label Oluştur')
                prf.geometry('400x380')
                
                dgirkc = Label(prf, text="Değişken Gir")
                dgirkc.pack()
                entdeg = Entry(prf, width=20)
                entdeg.pack()
                labgirisbl = Label(prf, text="Yazı Gir")
                labgirisbl.pack()
                sjent = Entry(prf, width=20)
                sjent.pack()
                yskn = Label(prf, text="Hangi Pencerede Olacak ? (Değişken Gir)")
                yskn.pack()
                newvar = Entry(prf, width=20)
                newvar.pack()
                xygirlab = Label(prf, text="X ve Y Gir. Örn(x=90,y=90)")
                xygirlab.pack()
                xyten = Entry(prf, width=20)
                xyten.pack()
                
                butonewl = Button(prf, text="Ekle", command=butonprf)
                butonewl.pack()
                
                prf.mainloop()
            def newlab():
                def funcpenlab():
                    yazisl = open(f"{filename}.py", "a", encoding="utf-8")
                    yazisl.write(f'\n    {bsfrentry.get()}["text"] = f"{yaznetry.get()}"')
                    yazisl.close()
                penlab = Tk()
                penlab.title('Label Değiştir')
                penlab.geometry('400x380')
                
                deggirad = Label(penlab, text="Değişken Girin")
                deggirad.pack()
                bsfrentry = Entry(penlab, width=20)
                bsfrentry.pack()
                
                labelblgsi = Label(penlab, text='Label Girin. (Bir Değişken Gireceksen, Değişkeni {} İçerisine Yaz\n entry ise sonuna .get() getir)')
                yaznetry = Entry(penlab, width=20)
                labelblgsi.pack()
                yaznetry.pack()
                didbtn = Button(penlab, text="Ekle", width=13, command=funcpenlab)
                didbtn.pack()
                
                
                penlab.mainloop()
            def funcbuyu():
                funcicineyaz = open(f"{filename}.py", "a", encoding="utf-8")
                funcicineyaz.write(f'\n    {funcget.get()}')
                funcicineyaz.close()
            def funcdog():
                sfuncdog = open(f"{filename}.py", "a", encoding="utf-8")
                sfuncdog.write(f'\ndef {funcgiris.get()}():')
                sfuncdog.close()
                funcadgirlab.pack_forget()
                olsbutfunc.pack_forget()
                funcgiris.pack_forget()
                funcgiry.pack()
                funcget.pack()
                butyazfunc.pack()
                newlabeldeg.place(x=5,y=50)
                newlabelols.place(x=640,y=50)
                messagebox.showinfo('Python GUI Creator', 'Fonksiyon Oluşturuldu. İçerisine Yazın')
            funcpne = Tk()
            funcpne.title('Fonksiyon Penceresi')
            funcpne.geometry('750x500')
            
            hgfunc = Label(funcpne, text="Fonksiyon Penceresine\nHoşgeldiniz", font="Arial 13")
            hgfunc.pack()
            
            funcadgirlab = Label(funcpne, text="Fonksiyon Ad Gir:")
            funcadgirlab.pack()
            funcgiris = Entry(funcpne, width=20)
            funcgiris.pack()
            funcgiry = Label(funcpne, text="Fonksiyonun İçine Yaz:")
            funcget = Entry(funcpne, width=20)
            olsbutfunc = Button(funcpne, text="Fonksiyon Oluştur", width=16, command=funcdog)
            olsbutfunc.pack()
            butyazfunc = Button(funcpne, text="Fonksiyonun İçine Yaz", width=16, command=funcbuyu)
            newlabeldeg = Button(funcpne, text="Label Değiştir", width=15, command=newlab)
            newlabelols = Button(funcpne, text="Yeni Label Oluştur", width=15, command=newlabel)
            
            funcpne.mainloop()
        def modyuk():
            exmod = open(f"{filename}.py", "a", encoding="utf-8")
            exmod.write(f"\nimport {yigir.get()}")
            exmod.close()
        def bayarla():
            bayar = open(f"{filename}.py", "a", encoding="utf-8")
            bayar.write(f"\n{dad.get()}.title('{yigir.get()}')")
            bayar.close()
        def pboyls():
            pboygir = open(f"{filename}.py", "a", encoding="utf-8")
            pboygir.write(f"\n{dad.get()}.geometry('{yigir.get()}')")
            pboygir.close()
        def penols():
            pnols = open(f"{filename}.py", "a", encoding="utf-8")
            pnols.write(f"\n{dad.get()} = Tk()")
            pnols.close()
        def loop():
            loopcmd = open(f"{filename}.py", "a", encoding="utf-8")
            loopcmd.write(f"\n{dad.get()}.mainloop()")
            loopcmd.close()
        def yolu():
            yoluol = open(f"{filename}.py", "a", encoding="utf-8")
            yoluol.write(f"\n{dad.get()} = Label({dad2.get()}, text='{yigir.get()}')\n{dad.get()}.place(x={xayar.get()},y={yayarknm.get()})")
            yoluol.close()
        filename = aa.get()
        soru1.pack_forget()
        aa.pack_forget()
        olst.pack_forget()
        yaz = open(f"{filename}.py", "w")
        yaz.write('from tkinter import *\nfrom tkinter import messagebox\n')
        yaz.close()
        onm = Label(pen, text="Programınıza Eklemek İstediklerinizi\nSeçin", font="Arial 15")
        onm.pack()
        dadgir = Label(pen, text="Değişken Adı Gir:")
        dadgir.pack()
        dad = Entry(pen, width=15)
        dad.pack()
        yigirbl = Label(pen, text="Yazı Girin:")
        yigirbl.pack()
        yigir = Entry(pen, width=15)
        yigir.pack()
        dad2gir = Label(pen, text="Hangi Pencerede Olacak (2.Değişken) Gir:")
        dad2gir.pack()
        dad2 = Entry(pen, width=15)
        dad2.pack()
        bifunc = Label(pen, text="Butonlar İçin Fonksiyon Seç")
        bifunc.pack()
        bient = Entry(pen, width=15)
        bient.pack()
        uzsec = Label(pen, text="Uzunluk Gir")
        uzsec.pack()
        uzunlukgir = Entry(pen, width=15)
        uzunlukgir.pack()
        blgxy = Label(pen, text="Konum Ayarla (X)")
        blgxy.pack()
        xayar = Entry(pen, width=15)
        xayar.pack()
        blgyknm = Label(pen, text="Konum Ayarla (Y)")
        blgyknm.pack()
        yayarknm = Entry(pen, width=15)
        yayarknm.pack()
        yolst = Button(pen, text="Yazı oluştur", width=15, command=yolu)
        yolst.place(x=5,y=50)
        ploop = Button(pen, text="Pencereyi Loop'a Koy", width=16, command=loop)
        ploop.place(x=5,y=75)
        pdeg = Button(pen, text="Pencere Oluştur", width=15, command=penols)
        pdeg.place(x=5,y=100)
        pboyols = Button(pen, text="Pencere Boyutunu Ayarla", width=18, command=pboyls)
        pboyols.place(x=5,y=125)
        bayarsor = Button(pen, text="Pencere Başlığı Gir", width=16, command=bayarla)
        bayarsor.place(x=5,y=150)
        exmocs = Button(pen, text="Modül Yükle", width=15, command=modyuk)
        exmocs.place(x=5,y=175)
        funcols = Button(pen, text="Fonksiyon Oluştur", width=15, command=funcol)
        funcols.place(x=5,y=200)
        degoo = Button(pen, text="Değişken Oluştur", width=15, command=defol)
        degoo.place(x=5,y=225)
        butolla = Button(pen, text="Buton Oluştur", width=15, command=buttol)
        butolla.place(x=5,y=250)
        kodview = Button(pen, text="Kodları Göster", width=15, command=codeview)
        kodview.place(x=635,y=225)
        hazirpack = Button(pen, text="Username Değişkeni Ekle", width=18, command=hzrpack)
        hazirpack.place(x=615,y=200)
        dcalstr = Button(pen, text="Değişken Çalıştır", width=15, command=dcaldi)
        dcalstr.place(x=635,y=175)
        kke = Button(pen, text="Kendin Kod Ekle", width=15, command=kkefun)
        kke.place(x=635,y=150)
        funcalist = Button(pen, text="Fonksiyon Çalıştır", width=15, command=funccalis)
        funcalist.place(x=635,y=125)
        entryolst = Button(pen, text="Entry Oluştur", width=15, command=entryunt)
        entryolst.place(x=635,y=100)
        labeldzn = Button(pen, text="Label'ı Düzenleme", width=15, command=labeldznle)
        labeldzn.place(x=635,y=75)
        bkmtcmd = Button(pen, text="Bekletme Kodu (time mdl gerek)", width=24, command=ltime)
        bkmtcmd.place(x=577,y=50)
        
    hgl.pack_forget()
    btnsor.place_forget()
    btnbas.place_forget()
    csoon.place_forget()
    soru1 = Label(pen, text="Oluşturmak İstediğiniz Dosya Adı (uzantısız)")
    soru1.pack()
    aa = Entry(pen, width=15)
    aa.pack()
    olst = Button(pen, text="Oluştur", width=10, command=olsf)
    olst.pack()

hgl = Label(pen, text="Python GUI Creator", font="Arial 15 bold")
hgl.pack(pady=5)

btnsor = Button(pen, text="Nedir ? Nasıl Kullanılır ?", width=17, height=1, command=nnk)
btnsor.place(x=200,y=45)

btnbas = Button(pen, text="Başla", width=17, height=1, command=basla)
btnbas.place(x=395,y=45)

csoon = Label(pen, text="Çok Yakında:\nModül Komutları Kodsuz\nKaranlık Tema\nHata Tespiti\nKodsuz Konsol Programı Oluşturma\nÖrnek Programlar\nAlgoritma Oluşturma\nProgramın Kodlarını Kaydet\nFonksiyon Penceresine Yeni Özellikler")
csoon.place(x=275,y=180)

cbymtt = Label(pen, text="Coded by M Talha - MuhammedTr768", font="Arial 7")
cbymtt.place(x=0,y=483)



pen.mainloop()
