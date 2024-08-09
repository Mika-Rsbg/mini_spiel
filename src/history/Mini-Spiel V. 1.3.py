import sys
import time
from random import randint

def monsterz():
    gegner_willen = randint(1, 11)
    gegner_willenz = randint(1, 11)
    gegner_willend = randint(1, 11)
    gegner_willenv = randint(1, 11)
    player_willen = randint(1, 10)
    player_willenz = randint(1, 10)
    player_willend = randint(1, 10)
    player_willenv = randint(1, 10)
    wiederholungen = 0
    while not wiederholungen == 17:
        printausgang = []
        b = randint(1, 9)
        printausgang.append(b)
        c = randint(1, 9)
        printausgang.append(c)
        d = randint(1, 9)
        printausgang.append(d)
        e = randint(1, 9)
        printausgang.append(e)
        print(printausgang)
        wiederholungen = wiederholungen + 1
        time.sleep(0.2)
    print('-------------------------------------')
    kampfzahlen = []
    kampfzahleneins = []
    kampfzahlen.append(gegner_willen)
    kampfzahlen.append(gegner_willenz)
    kampfzahlen.append(gegner_willend)
    kampfzahlen.append(gegner_willenv)
    kampfzahleneins.append(player_willen)
    kampfzahleneins.append(player_willenz)
    kampfzahleneins.append(player_willend)
    kampfzahleneins.append(player_willenv)
    print('Gegner: %s' %kampfzahlen)
    print('Du: %s' %kampfzahleneins)
    if player_willen >= gegner_willen:
        print('1. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
        time.sleep(0.5)
    else:
        print('1. Du verlierst')
        player.zaehlen = player.zaehlen -1
        time.sleep(0.5)
    if player_willenz >= gegner_willenz:
        print('2. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
        time.sleep(0.5)
    else:
        print('2. Du verlierst')
        player.zaehlen = player.zaehlen -1
        time.sleep(0.5)
    if player_willend >= gegner_willend:
        print('3. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
        time.sleep(0.5)
    else:
        print('3. Du verlierst')
        player.zaehlen = player.zaehlen -1
        time.sleep(0.5)
    if player_willenv >= gegner_willenv:
        print('4. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
        time.sleep(0.5)
    else:
        print('4. Du verlierst')
        player.zaehlen = player.zaehlen -1
        time.sleep(0.5)

class activities():
    leben = 200
    energie = 200
    strecke_schatz = 100
    nahrung = 15
    random1 = 0
    random2 = 0
    runden_gewartet = 0
    runden_gewartet2 = 0
    gefundene_monster = 0
    jn = 'nein'
    zaehlen = 0
    def gehen(self):
        if self.energie >= 5:
            self.energie = self.energie - 5
            self.strecke_schatz = self.strecke_schatz - 1
        else:
            print('Sie haben zu wenig Energie um zu laufen. Essen sie um mehr Energie zu bekommen.')
    def essen(self):
        if self.nahrung >= 1:
            self.nahrung - 1
            self.energie + 2
            self.leben + 1
        else:
            print('Sie haben keine Nahrung mehr.')
    def tier_gefunden(self):
        print('Sie haben ein Tier gefunden!!')
        eingabe = input('Möchten sie das Tier töten? Ja oder Nein:    ')
        if eingabe == 'Ja' or 'ja':
            self.energie = self.energie - 3
            self.nahrung = self.nahrung + 5
            print('Du hast das Tier bezwungen!')
            print('-------------------------------------')
        else:
            print('Das Tier ist weggelaufen und hat sich versteckt!')
    def monster_gefunden(self):
        self.gefundene_monster = self.gefundene_monster + 1
        print('Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr!')
        print('Monster gefunden!')
        print('Willst du kämpfen?  Wenn NEIN -3 Leben!   Wenn JA -5/+10 Leben!')
        jn = input('Ja oder Nein:   ')
        if jn == 'Ja':
            self.kämpfen()
        if jn == 'ja':
            self.kämpfen()
        if jn == 'Nein':
            self.leben = self.leben - 3
        if jn == 'nein':
            self.leben = self.leben - 3
    def kämpfen(self):
        monsterz()
        if self.zaehlen >= 0:
            self.leben = self.leben +10
            self.energie = self.energie - 5
            self.zaehlen = 0
            print('Du hast gewonnen!')
            time.sleep(2)
            print('-------------------------------------')
        if self.zaehlen << 0:
            self.leben = self.leben - 5
            self.energie = self.energie - 5
            self.zaehlen = 0
            print('Du hast verlohren!')
            time.sleep(2)
            print('-------------------------------------')
    def schatz(self):
        print('Sie haben gewohnen!')
        if input('Möchten sie das Spiel neu starten?  ') == 'Ja' or 'ja':
            self.neustart()
        else:
            sys.exit()
    def neustart(self):
        self.leben = 200
        self.energie = 500
        self.strecke_schatz = 100
        self.nahrung = 15

player = activities()

while player.strecke_schatz > 0:
    print('Was möchten sie tun?')
    print('W/w für gehen     E/e für essen     Q/q für kämpfen')
    print('Leben: %s' %player.leben)
    print('Energie: %s' %player.energie)
    print('Essen: %s' %player.nahrung)
    print('Strecke bis zum Schatz: %s' %player.strecke_schatz)
    print('-------------------------------------')
    if player.random1 == 0:
        player.random1 = randint(3, 8)
    if player.random1 == player.runden_gewartet:
        player.random1 = 0
        player.runden_gewartet = 0
        player.runden_gewartet2 = player.runden_gewartet2 - 1
        player.monster_gefunden()
    if not player.random1 == player.runden_gewartet:
        player.runden_gewartet = player.runden_gewartet + 1
        if player.random2 == 0:
            player.random2 = randint(3, 8)
        if player.random2 == player.runden_gewartet2:
            player.random2 = 0
            player.runden_gewartet2 = 0
            player.tier_gefunden()
        if not player.random2 == player.runden_gewartet2:
            player.runden_gewartet2 = player.runden_gewartet2 + 1
            eingabe = input('Eingabe:    ')
    if eingabe == 'ä':
        continue
    if eingabe == 'stop':
        break
    if eingabe == 'Stop':
        break
    if eingabe == 'w':
        player.gehen()
    if eingabe == 'W':
        player.gehen()
    if eingabe == 'e':
        player.essen()
    if eingabe == 'E':
        player.essen()
    if eingabe == 'q':
        player.kämpfen()
    if eingabe == 'Q':
        player.kämpfen()

if player.strecke_schatz == 0:
    player.schatz()
else:
    sys.exit