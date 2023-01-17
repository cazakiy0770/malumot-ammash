class malu: 
    def init(self, ism, fml, ty, tel, mail): 
        self.ism = ism 
        self.fml= fml 
        self.ty=ty 
        self.mail=mail 
        self.tel=mail 
 #       self.hy=hy 
    print("malumot keritasizmi! agar malumot keritsangiz ha deb yozimg yoki malumotkirinmasangiz yo'q deb yozing ") 
    qwert = input("javobingiz;") 
    if qwert == "ha": 
        def mu_ke(): 
            ism = input("ism kiritin;") 
            fml = input("familiya keriting;") 
            ty = int(input("tug'ilgan yil;")) 
            hy = int(input("hozirgi yil;")) 
            while True:                 
                mail = input("gmail lingizni kirgizing;") 
                mail_id = mail[-1:-10] 
                if mail_id != "@gmail.com": 
                    print("@gmail.com bilan tugashi kerak") 
                else: 
                    print("gmail qabul qilindi")                         
            while True:#tel_len==13 and tel_len=="+9989": 
                tel = int(input("telefon raqamingizni keritingb")) 
                tel_len=len(tel) 
                tel_id=tel[0:4] 
                b=str(tel_id)                
                if tel_len>=13: 
                    print("telefon raqamingiz 13 ta xonadan kam") 
                elif tel_len==13: 
                    a=str(+9989) 
                if b == a: 
                    print("tellefon raqamingiz qabul qilindi") 
                else: 
                   print("raqamingiz 13 xonadan ko'p") 
             
            print("malumot keritildi") 
            print("malumotni ko'rishni hoxlaysanmi ha yoki yo'q") 
            asa = input("javobingiz;")     
            if asa == "ha": 
                def malum(self): 
                    javob = hy - self.ty 
                    return f"ismi {self.ism} {self.fml} javob" 
            else: 
                    print("raxmat sog'bo'lining") 
                 
    else: 
        print("malumot olmoqchi mesiz ha yoki yo'q") 
        isd = input("javobingiz;") 
        if isd == "ha": 
            print("bizda malumot yo'q") 
        else: 
            print("bizda malumot yo'q") 
         
qw = malu('ism', 'fml', 'ty','mail','tel')