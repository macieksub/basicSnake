import pygame
from pygame import Vector2
import sys
import random

class Snake:
    def __init__(self):
        self.cialo = [Vector2(10,10), Vector2(9,10)]
        self.kierunek = Vector2(1, 0)
        self.wynik = 0
        self.nowy_blok = False

    def rysuj_snake(self):
        aa = True
        for blok in self.cialo:
            x_poz = int(blok.x * rozmiar_pola)
            y_poz = int(blok.y * rozmiar_pola)
            blok_rect = pygame.Rect(x_poz + 1, y_poz + 1, rozmiar_pola -2, rozmiar_pola - 2)
            if aa == True:
                pygame.draw.rect(obraz, (100, 30, 80), blok_rect)
                aa = False
            else:
                pygame.draw.rect(obraz, (183, 111, 122), blok_rect)

    def ruch_snake(self):
        self.sprawdz_kolizje()
        if self.nowy_blok == True:
            cialo_kopia = self.cialo[:]
            cialo_kopia.insert(0, cialo_kopia[0] + self.kierunek)
            self.nowy_blok = False
        else :
            cialo_kopia = self.cialo[:-1]
            cialo_kopia.insert(0, cialo_kopia[0] + self.kierunek)
        if cialo_kopia[0].x >= ilosc_pol:
            cialo_kopia[0].x = 0
        elif cialo_kopia[0].y >= ilosc_pol:
            cialo_kopia[0].y = 0
        elif cialo_kopia[0].x < 0:
            cialo_kopia[0].x = ilosc_pol
        elif cialo_kopia[0].y < 0:
            cialo_kopia[0].y = ilosc_pol
        self.cialo = cialo_kopia[:]

    def klawisze(self):
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if zdarzenie.type == pygame.USEREVENT:
                self.ruch_snake()
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_UP:
                    if self.kierunek != Vector2(0, 1):
                        self.kierunek = Vector2(0, -1)
                elif zdarzenie.key == pygame.K_DOWN:
                    if self.kierunek != Vector2(0, -1):
                        self.kierunek = Vector2(0, 1)
                elif zdarzenie.key == pygame.K_LEFT:
                    if self.kierunek != Vector2(1, 0):
                        self.kierunek = Vector2(-1, 0)
                elif zdarzenie.key == pygame.K_RIGHT:
                    if self.kierunek != Vector2(-1, 0):
                        self.kierunek = Vector2(1, 0)

    def sprawdz_kolizje(self):
        for blok in self.cialo[1:]:
            if blok == self.cialo[0]:
                self.koniec_gry()

    def koniec_gry(self):
        bb = True
        while bb:
            obraz.fill(pygame.Color("black"))
            mess1 = czcionka2.render("Koniec gry!", True,(255,0,0))
            mess2 = czcionka1.render("nacisnij spacje", True,(255,255,0))
            obraz.blit(mess1, [320, 200])
            obraz.blit(mess2, [320, 250])
            pygame.display.update()
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if zdarzenie.type == pygame.KEYDOWN:
                    if zdarzenie.key == pygame.K_SPACE:
                        self.cialo = [Vector2(10,10), Vector2(9,10)]
                        self.wynik = 0
                        bb = False
                    elif zdarzenie.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

class Owoc:
    def __init__(self):
        self.losowa_pozycja()
        #self.jablko = pygame.image.load(r"D:\python\pygame\snake\apple.png").convert_alpha()

    def rysuj_owoc(self):
        owoc_rect = pygame.Rect(int(self.x * rozmiar_pola), int(self.y * rozmiar_pola), rozmiar_pola, rozmiar_pola)
        #obraz.blit(self.jablko,owoc_rect)
        pygame.draw.rect(obraz, (126,166,114), owoc_rect)

    def losowa_pozycja(self):
        self.x = random.randint(0, ilosc_pol - 1)
        self.y = random.randint(0, ilosc_pol - 1)
        self.pozycja = Vector2(self.x, self.y)


def rysuj_podloze(obraz):
    obraz.fill(pygame.Color(175,215,70))
    for y in range(ilosc_pol):
        for x in range(ilosc_pol):
            trawa = pygame.Rect(int(x * rozmiar_pola), int(y * rozmiar_pola), rozmiar_pola, rozmiar_pola)
            if (x + y) % 2 == 0:
                pygame.draw.rect(obraz,(167, 209, 61), trawa)

rozmiar_pola = 40
ilosc_pol = 20

pygame.init()
pygame.display.set_caption("Snake")
obraz = pygame.display.set_mode((rozmiar_pola * ilosc_pol, rozmiar_pola * ilosc_pol))
zegar = pygame.time.Clock()

owoc = Owoc()
snake = Snake()

pygame.time.set_timer(pygame.USEREVENT, 150)
czcionka1 = pygame.font.SysFont("monospace",16)
czcionka2 = pygame.font.SysFont("Helvetica",36)

def main():
    while True:
        snake.klawisze()
        rysuj_podloze(obraz)
        owoc.rysuj_owoc()
        snake.rysuj_snake()
        if snake.cialo[0] == owoc.pozycja:
            snake.nowy_blok = True
            snake.wynik += 1
            owoc.losowa_pozycja()
        tekst = czcionka1.render("Wynik {0}".format(snake.wynik), 1, (0,0,0))
        obraz.blit(tekst, (5,10))
        pygame.display.update()
        zegar.tick(60)

main()
