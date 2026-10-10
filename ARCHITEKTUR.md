# Architektur

_Bestätigt von Arjen am 10.10.2026. Bereichsnamen sind Platzhalter._

## Aufbau

```
Bookclub
│
├── 1  Meine Bibliothek            (privat · Startseite der App)
│   ├── Am Lesen                    Bücher, die gerade offen sind
│   ├── Gelesen                     mit Karte: Bewertung, Lesart, Zitate
│   ├── Ungelesen im Regal          besessen, noch nicht gelesen
│   ├── Wunschliste                 noch nicht besessen
│   ├── Abgebrochen                 mit Seite und Grund
│   ├── Eigene Regale               frei angelegte Sammlungen
│   ├── Verliehen                   an wen, seit wann        (später)
│   └── + Neues Buch erfassen       Scan · ISBN · von Hand
│
├── 2  Mein Schaufenster            (öffentlich · nur was freigegeben ist)
│   ├── Gestalten                   Name, Ort, Beschreibung, Aussehen
│   ├── Ausgestellte Bücher         mit eigenen Kärtchen
│   ├── Sichtbarkeit                privat · nur per Link · auffindbar
│   └── Angebote                    Verleih, Verkauf           (später)
│
├── 3  Entdecken
│   ├── In der Nähe                 Schaufenster im Umkreis
│   ├── Ein Buch suchen             Leserstimmen aus Schaufenstern
│   ├── Kategorien
│   └── Gemerkte Schaufenster
│
├── 4  Ich                          Pseudonym, Privatsphäre, Export, Einstellungen
│
└── später: Begegnungen             Buchclubs, Events, Anfragen
```

## Die Buchseite

Kein eigenes Modul, aber das zentrale Element: Jedes Buch hat genau eine Buchseite, egal aus welcher Liste es geöffnet wird.

- Karte: Bewertung und eigene Worte
- Exemplar: Ausgabe, Zustand, Standort
- Zitate
- Leseverlauf, auch bei mehrmaligem Lesen
- Schalter „im Schaufenster zeigen“

## Grundsätze

- **Startseite ist die Bibliothek.** Erfassen ist eine Aktion darin, kein Einstieg.
- **Ungelesen im Regal und Wunschliste sind getrennt:** das eine besitzt man, das andere nicht.
- **Kein Feed, keine Benachrichtigungen, keine Follower, keine Zähler auf der Startseite.** Die App drängt nicht.
- **Vier Hauptbereiche** in der Navigation. Begegnungen kommen später als fünfter dazu.

## App-Grundsätze für Bedienung und Leistung

_Von Arjen vorgegeben am 10.10.2026._

- **Tippflächen** mindestens 44 × 44 Punkt; Listeneinträge über die ganze Zeile antippbar.
- **Animationen nur als Antwort auf ein Tippen**, kurz (höchstens etwa 200 ms) und einfach (Einblenden statt 3D-Bewegung). Keine dauerhaft laufenden Animationen.
- **Texturen** (Leinen, Marmorpapier, Papier) in der echten App als fertige Bilder, nicht als live berechnete Grafikfilter. Keine Ebenen über dem ganzen Bildschirm, die beim Scrollen neu berechnet werden.
- Bei „Bewegung reduzieren“ im System entfallen Animationen ganz.

## Umfang je Schritt

| Schritt | Umfang |
|---|---|
| 1 | Meine Bibliothek, Buchseite, Ich |
| 2 | Mein Schaufenster, Entdecken |
| später | Verliehen, Angebote, Begegnungen |
