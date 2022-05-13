balans=1000
from playsound import playsound
from gtts import gTTS
import os
import time
playsound("C:/Users/user/Music/ATM/qarsilama.mp3")
while True:
    playsound("C:/Users/user/Music/ATM/emeliyyatlar.mp3")
    emeliyyat=input("1-Balansı artırmaq\n2-Balansdan çıxarış etmək\n3-Balansı göstərmək\nİcra etmək istədiyiniz əməliyyatın nömrəsini daxil edin:")
    if emeliyyat=="1":
        playsound("C:/Users/user/Music/ATM/birnomrəozek.mp3")
        daxil=int(input("Balansa əlavə etmək istədiyiniz miqdarı daxil edin:"))
        balans=balans+daxil
        artdi=gTTS(text=str(daxil)+"manat balansa elave olundu,yekun balans"+str(balans)+"manatdir",lang="tr")
        artdi.save("artdi.mp3")
        os.system("artdi.mp3")
        print("Balans artırıldı")
    elif emeliyyat=="2":
        playsound("C:/Users/user/Music/ATM/ikinomreozek.mp3")
        xaric=int(input("Balansdan çıxartmaq istədiyiniz miqdarı daxil edin:"))
        if xaric<=balans:
            balans=balans-xaric
            azaldi=gTTS(text=str(xaric)+"manat negdleşdirildi,yekun balans"+str(balans)+"manatdır",lang="tr")
            azaldi.save("azaldi.mp3")
            os.system("azaldi.mp3")
            print("Pulunuz nəğdləşdirildi")
        else:
            playsound("C:/Users/user/Music/ATM/ikixeta.mp3")
            print("Balansda bu qədər pul yoxdur,yenidən cəhd edə bilərsiniz")
    elif emeliyyat=="3":
        manimani=gTTS("Balansiniz"+str(balans)+"manatdir",lang="tr")
        manimani.save("manimani.mp3")
        os.system("manimani.mp3")
        print("Balansınız:", balans)
    time.sleep(10)
    playsound("C:/Users/user/Music/ATM/secim.mp3")
    secim=input("Yenə əməliyyatlara davam etmək istəyirsiniz?\nDavam etmək üçün B,sonlandırmaq üçün X yə basın:")
    if secim=="X":
        playsound("C:/Users/user/Music/ATM/tesekkur.mp3")
        print("Xidmətlərimizdən istifadə üçün təşəkkür edirik,yenə gözləyirik")
        break