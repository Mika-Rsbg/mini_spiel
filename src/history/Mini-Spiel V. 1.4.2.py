import sys
from random import randint



class activities():
    leben = 200
    energie = 500
    strecke_schatz = 100
    nahrung = 15
    random1 = 0
    random2 = 0
    runden_gewartet = 0
    runden_gewartet2 = 0
    gefundene_monster = 0
    jn = 'nein'
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
        print('Brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr!')
        print('Monster gefunden!')
        print('Willst du kämpfen?  Wenn NEIN -3 Leben!   Wenn JA -5/+10 Leben!')
        jn = input('Ja oder Nein:   ')
        if jn == 'Ja':
            player.kämpfen()
    def kämpfen(self):
        print('coming soon')
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



player.schatz()
#kämpfen

