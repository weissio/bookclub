# „Licht an“: drei Varianten

Stand 24.10.2026, nach Arjens Rückmeldung: „Am Lesen“ soll höchstens ein Drittel einnehmen, und es soll weniger, aber größere Einstiege in die Bibliothek geben.

Alle drei Varianten spielen in derselben Welt: Abend, Pendelleuchte, Nunito, Tintenblau und Lampengelb. Erfassen gibt es überall genau einmal, als Zeile „Neue Bücher auspacken“ über dem Vermerk. Die Szene speist sich aus den eigenen Büchern: Rücken, Cover-Fächer und Lesebändchen tragen die Farben der Bücher des Nutzers (hier Beispieldaten). Die Zahl der gezeigten Rücken ist fest, sie wächst also nicht mit dem Bestand.

Gemessen ist der Abschnitt „Am Lesen“ (Überschrift bis Unterkante) bei 390 × 844 mit Playwright. Kopf und Lampe kommen in allen Varianten mit 74 pt dazu.

| Variante | Am Lesen, 2 Bücher | Am Lesen, 4 Bücher | Einstiege in die Bibliothek |
|---|---|---|---|
| V1 Leselicht-Leiste | 21,4 % | 21,4 % | 4 große Fächer (+ Auspacken) |
| V2 Regalbretter | 17,1 % | 31,3 % | 4 Regalbretter (+ Auspacken) |
| V3 Ein Buch im Licht | 21,3 % | 27,7 % | 4 Zeilen mit Cover-Fächer (+ Auspacken) |

## V1 – Leselicht-Leiste (`v1.html`, `v1.png`, `v1-4buecher.png`)
„Am Lesen“ ist eine waagerechte Leiste kleiner aufgeschlagener Bücher mit Seitenzahl, darunter je ein Knopf „Eintragen“. Ab drei Büchern wischt man, die Höhe bleibt gleich. Die Bibliothek besteht aus vier großen Fächern im 2×2-Raster: Gelesen, Ungelesen im Regal, Wunschliste und „Weitere Bände“ (Abgebrochen, Eigene Regale, Verliehen, Rückblick als Liste). Am Fuß jedes Fachs steht eine Reihe Rücken in den echten Farben der Bücher darin.

## V2 – Regalbretter (`v2.html`, `v2.png`, `v2-4buecher.png`)
„Am Lesen“ ist eine ruhige Liste: Jedes Buch hat eine Zeile mit Rücken in seiner Farbe, Titel und einem großen Seitenknopf „S. 142“. Ein Tipp auf den Knopf öffnet „Seite eintragen“. Die Bibliothek besteht aus vier breiten Regalbrettern (Gelesen, Ungelesen im Regal, Wunschliste, Weitere Bände), auf denen die eigenen Rücken stehen. Das ist am nächsten an einem echten Regal und am leichtesten zu lesen. Weil die Liste mit jedem Buch wächst, ist bei 4 Büchern die Grenze von einem Drittel fast erreicht.

## V3 – Ein Buch im Licht (`v3.html`, `v3.png`, `v3-4buecher.png`)
Nur ein Buch liegt im Lichtkegel, als Pult mit Cover, Titel, „Lesebändchen auf Seite 142“ und einem großen gelben Knopf „Seite eintragen“. Die anderen aktuellen Bücher sind kleine Chips „Daneben“; ein Tipp legt eines ins Licht. Die Bibliothek ist eine geordnete Liste aus vier großen Zeilen mit einem Fächer aus drei echten Covern, Name, einer kurzen Zeile und der Zahl. Diese Variante wirkt am „erwachsensten“ und hat die klarste Hierarchie: ein Hauptknopf, vier Einstiege.

## Empfehlung des Designers
V3 für die Startseite: Sie hat einen fast konstanten Anteil (21 bis 28 %), genau eine starke Handlung und eine Liste, die wie ein Inhaltsverzeichnis gelesen wird. Aus V2 würde ich die Regalbretter als Kopf der jeweiligen Bandseite übernehmen.

`gen_var.py` erzeugt alle sechs Ansichten neu.
