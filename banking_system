class Ucet:
    def __init__(self, meno, suma=0):
        self.meno = meno
        self.suma = int(suma)

    def __str__(self):      #returns string representation of acc name and amount
        return f'{self.meno} ––> {self.suma}'

    def stav(self):         #returns accout balance
#        print('stav uctu je ', self.suma)
        return self.suma

    def vklad(self, suma):  #deposit
        self.suma += suma

    def vyber(self, suma):  #withdrawal
        if abs(suma) > abs(self.suma):  #check if enough balance is available, if not withdraw all from account
            novy = self.suma
            self.suma = 0
            print('nedostatok prostriedkov, vyberam vsetko ', self.suma)
            return abs(suma)
        else:
            self.suma -= abs(suma)
            print('novy zostatok ', self.suma)
            return abs(suma)

class UcetHeslo(Ucet):      #adding password feature to base class
    def __init__(self, meno, heslo, suma=0):
        super().__init__(meno, suma)
        self.heslo = heslo

    def vklad(self, suma):
        zadaj = str(input(f'zadaj heslo {self.meno}:'))     #prompting for passwd
        if zadaj == self.heslo:
            super().vklad(suma)

    def vyber(self, suma):
        zadaj = str(input(f'zadaj heslo {self.meno}:'))     #prompting for passwd
        if zadaj == self.heslo:
            return super().vyber(suma)

mbank = UcetHeslo('mbank', 'gigi')
csob = Ucet('csob', 100)
tatra = UcetHeslo('tatra', 'gogo', 17)
sporo = Ucet('sporo', 50)
mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
csob.vyber(-5)
spolu = 0
for ucet in mbank, csob, tatra, sporo:
    print(ucet)
    spolu += ucet.stav()
print('spolu = ', spolu)
