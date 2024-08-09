import sys
from random import randint

wiederholungen = 0

def monsterz():
    gegner_willen = randint(1, 11)
    gegner_willenz = randint(1, 11)
    gegner_willend = randint(1, 11)
    gegner_willenv = randint(1, 11)
    player_willen = randint(1, 10)
    player_willenz = randint(1, 10)
    player_willend = randint(1, 10)
    player_willenv = randint(1, 10)
    while wiederholungen == 17:
        print(randint(1, 10)),print(randint(1, 10)),print(randint(1, 10)),print(randint(1, 10))
        wiederholungen = wiederholungen + 1
    print(gegner_willen),print(gegner_willenz),print(gegner_willend),print(gegner_willenv)
    print(player_willen),print(player_willenz),print(player_willend),print(player_willenv)
    if player_willen >= gegner_willen:
        print('1. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
    else:
        print('1. Du verlierst')
        player.zaehlen = player.zaehlen -1
    if player_willenz >= gegner_willenz:
        print('2. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
    else:
        print('2. Du verlierst')
        player.zaehlen = player.zaehlen -1
    if player_willend >= gegner_willend:
        print('3. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
    else:
        print('3. Du verlierst')
        player.zaehlen = player.zaehlen -1
    if player_willenv >= gegner_willenv:
        print('4. Du gewinnst')
        player.zaehlen = player.zaehlen + 1
    else:
        print('4. Du verlierst')
        player.zaehlen = player.zaehlen -1
    wiederholungen = 0

        
class activities():
    leben = 200
    energie = 500
    strecke_schatz = 100
    nahrung = 15
    random1 = 0
    runden_gewartet = 0
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
            self.energie + 1
            self.leben + 1
        else:
            print('Sie haben keine Nahrung mehr.')
    def tier_gefunden(self):
        print('Sie haben ein Tier gefunden!!')
        eingabe = input('Möchten sie das Tier töten? Ja oder Nein')
        if eingabe == 'Ja' or 'ja':
            self.energie - 3
            print(self.energie)
            self.nahrung + 5
            print(self.nahrung)
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
        if self.zaehlen << 0:
            self.leben = self.leben - 5
            self.energie = self.energie - 5
            self.zaehlen = 0
            print('Du hast verlohren!')
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
        player.monster_gefunden()
    if not player.random1 == player.runden_gewartet:
        player.runden_gewartet = player.runden_gewartet + 1
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



player.schatz()
#kämpfen

