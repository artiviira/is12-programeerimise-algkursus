str = ("sooja saia sisu")
print (str.capitalize())
print (str.center(20,"-"))
print (str.count("a", 0, 100))
print (str.encode('UTF-8','strict'))
abc = (str.encode("UTF-8","strict"))
print (abc.decode('UTF-8','strict'))
print (str.endswith("sisu"))
print (str.endswith("sisu",20))
print (str.endswith("saia",2,10))
abc = ("sooja sa\tia sisu")
print (abc.expandtabs(0))
print (abc.expandtabs(16))
print (str.find("ai",1))
print (str.find("ja",1))
abc = ("{} saia {}")
print (abc.format("sooja","sisu"))
print (str.index("ai",1))
print (str.index("ja",1))
abc = ("asdasd56")
cba =("as asd7")
aaa = ("123123")
print (abc.isalnum())#true kui on tyhik
print (cba.isalnum())
print (abc.isalpha())#true kui seal on täht
print (cba.isalpha())
print (abc.isdigit())
print (aaa.isdigit())#k6ik on numbrid
print (abc.islower())#k6ik v2ikeste t2htedega
print (cba.islower())
print (abc.isspace())#true kui on tyhik sees
print (cba.isspace())
print (abc.istitle())#true kui seal on tiitlip2rane string
print (cba.istitle())
print (abc.isupper())#true kui on k6ik suured t2hed
print (cba.isupper())
märk = ("_")
sõna = ("kas","sa","kus","kes")
print (märk.join(sõna))
print (str.ljust(40, "@"))
aja = ("AdaAJIUjhJ")
print (aja.lower())
jama = ("aaaaaaa0bbbaa fgjhf0hgh")
print (jama.lstrip("a"))
print (jama.partition("0"))
print (str.replace("a", "b",3))#a muudetav, b muutuja, 3 mitu esimest.
print (str.rfind("ja",0,10))
print (str.rindex("saia"))#erinev sellest str.index-ist see polest et index leiab mitmes s6na see aga mitmes t2ht
print (str.rjust(25,"%"))
print (jama.rpartition("0"))
print (jama.rstrip("a"))
print (("1 2 3 4").rsplit(None,1))
print (("1 2 3 4").split())
print (("ab c\nde fg\rkl\r\n").splitlines())
print (("asfasfas").startswith("a",0,20))
print (("aasdasd").strip("a"))
print (("asdffsJHGasdj").swapcase())#v2ike suureks suur v2ikeseks
print (("asd asd farw asd").title())

print (("assaf awrsaf asdoiqewr qwr").translate('a'))#ei t66ta
print(("asdHGhg").upper())
print(("kjashd asdff sdfsdfsdf sd asd").zfill(100))#zfill ehk zerofill
print (("12412412").isnumeric())
print (("jh123123jh").isnumeric())
print (("sdgsdgs").isdecimal())
print (("jh123123jh").isdecimal())





