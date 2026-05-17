# zestaw klas
class Silnik:
    def start(self): print("Silnik: start")
    def stop(self):  print("Silnik: stop")

class Pompa:
    def on(self):  print("Paliwo: pompowanie")
    def off(self):   print("Paliwo: wyłączone")

class Zaplon:
    def on(self):    print("Zapłon: włączony")
    def off(self):   print("Zapłon: wyłączony")

class Fasada:
    # inicjalizowanie klas
    def __int__(self):
        self._silnik=Silnik()
        self._pompa=Pompa()
        self._zaplon=Zaplon()

    def start(self):
        self._silnik.start()
        self._pompa.on()
        self._zaplon.on()

    def stop(self):
        self._silnik.stop()
        self._pompa.off()
        self._zaplon.off()
# klient
auto = Fasada()
auto.start()
auto.stop()










