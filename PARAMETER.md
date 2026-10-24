# Parameter-Katalog

_Entwurf vom 10.10.2026 – **teilweise bestätigt** (Genre-Liste, Lieblingsautor, Ort der Statistiken; siehe [ENTSCHEIDUNGEN.md](ENTSCHEIDUNGEN.md)), Rest noch offen. Grundlage: Arjens Vorgaben (Genre fehlt, Statistiken gewünscht) und [RECHERCHE.md](RECHERCHE.md)._

**Quelle:** `ISBN` = automatisch aus Buchdatenbank (DNB, ergänzend Google Books/Open Library), korrigierbar · `Nutzer` = gibt der Nutzer ein · `berechnet` = ergibt sich aus anderen Angaben

**Pflicht** heißt: ohne diese Angabe kann ein Buch nicht in die Bibliothek. Alles andere ist freiwillig.

## 1. Das Buch

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| ISBN | ISBN | – | fehlt bei Büchern vor 1970, dann Handeingabe |
| Titel, Untertitel | ISBN | ja | |
| Autor(en) | ISBN | ja | Grundlage für Autorenstatistik |
| Übersetzer | ISBN | – | |
| Verlag, Erscheinungsjahr | ISBN | – | |
| Seitenzahl | ISBN | – | Grundlage für Seitenstatistik |
| Sprache | ISBN | – | |
| Reihe und Band | ISBN / Nutzer | – | in Datenbanken oft lückenhaft |
| Sachgruppe, Schlagwörter | ISBN | – | DNB-Daten; taugen als Vorschlag, ersetzen aber kein Genre (zu prüfen) |
| Coverbild | ISBN / Nutzer | – | Standardcover oder eigenes Foto |

## 2. Einordnung

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| **Genre** | Nutzer | ja | ein Hauptgenre aus fester Liste (siehe unten), nötig für Kategoriesuche und Statistik |
| Nebengenre | Nutzer | – | zweites Genre aus derselben Liste |
| Fiktion / Sachbuch | berechnet | – | ergibt sich aus dem Genre |
| Zielgruppe | Nutzer | – | Erwachsene, Jugend, Kinder |
| Themen | Nutzer | – | frei, z. B. „Romantasy“, „Cozy Crime“, „Küste“ |
| Eigene Regale | Nutzer | – | freie Sammlungen |
| Lieblingsautor | Nutzer | – | wird manuell festgelegt, nicht berechnet |

**Feste Genre-Liste (16, von Arjen bestätigt):** Roman / Gegenwart · Krimi & Thriller · Fantasy · Science-Fiction · Liebesroman · Historischer Roman · Horror · Jugendbuch · Kinderbuch · Klassiker · Lyrik & Drama · Comic & Graphic Novel · Biografie & Erinnerungen · Sachbuch · Ratgeber · Reise & Natur

## 3. Mein Exemplar

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| Besitzstatus | Nutzer | ja | besitze · Wunschliste · verliehen · verkauft/abgegeben |
| Format | Nutzer | – | Hardcover, Taschenbuch, Klappenbroschur, E-Book, Hörbuch |
| Besonderheiten | Nutzer | – | Sonderausgabe, Farbschnitt, signiert, Erstausgabe |
| Zustand | Nutzer | – | |
| Standort zu Hause | Nutzer | – | |
| Herkunft | Nutzer | – | gekauft, geschenkt, getauscht, geerbt |
| Kaufdatum, Preis | Nutzer | – | privat; nur für eigene Statistik |
| Verliehen an, seit | Nutzer | – | später |

## 4. Lesen

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| Lesestand | Nutzer | ja | ungelesen · am Lesen · gelesen · abgebrochen |
| Begonnen am, beendet am | Nutzer | – | Datum vorschlagen, nicht erzwingen |
| Aktuelle Seite | Nutzer | – | |
| Lesedauer | berechnet | – | aus Beginn und Ende |
| Abgebrochen bei Seite, Grund | Nutzer | – | |
| Lesedurchgänge | berechnet | – | jedes Wiederlesen ein eigener Eintrag mit eigener Karte |

## 5. Meine Karte (Bewertung)

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| Hat mich erreicht | Nutzer | – | 0,5 bis 5 Sterne |
| Gefühl | Nutzer | – | mehrere aus fester Liste |
| Lesefluss | Nutzer | – | 5 Stufen: zäh … nicht weglegbar |
| Sprache / Schreibstil | Nutzer | – | 5 Stufen: holprig … jeder Satz sitzt |
| Tempo | Nutzer | – | ruhig · ausgewogen · rasant |
| Stark / hat gehakt | Nutzer | – | je Aspekt: Sprache, Figuren, Spannung, Atmosphäre, Idee, Humor, Tiefgang, Dialoge, Weltenbau, Ende |
| Wirkt nach | Nutzer | – | |
| Wieder lesen | Nutzer | – | |
| Mehr von dieser Autorin | Nutzer | – | indirekte Autorenbewertung |

## 6. Eigene Worte

| Parameter | Quelle | Pflicht | Hinweis |
|---|---|---|---|
| Meine Lesart | Nutzer | – | freigebbar fürs Schaufenster |
| Für wen | Nutzer | – | freigebbar |
| Zitate mit Seite | Nutzer | – | freigebbar |
| Private Notizen | Nutzer | – | nie öffentlich |

## 7. Statistiken (alle berechnet, privat)

**Wo sie stehen (von Arjen festgelegt):** ein paar Zeilen kurze Zusammenfassung unter dem Regal; ausführlichere Statistiken in einem eigenen Band im Regal. Welche Zeilen in die Kurzfassung kommen, ist noch offen.

| Statistik | braucht |
|---|---|
| Gelesene Bücher gesamt, pro Jahr, pro Monat | Lesestand, beendet am |
| Gelesene Seiten | Seitenzahl, Lesestand |
| Anzahl verschiedener Autoren | Autor |
| **Meistgelesener Autor** | Autor, Lesestand (der Lieblingsautor wird stattdessen manuell gesetzt) |
| **Lieblingsgenre**, Verteilung nach Genre | Genre |
| Durchschnittliche Bewertung, Verteilung der Sterne | Sterne |
| Durchschnittliche Lesedauer, schnellstes und längstes Buch | Beginn, Ende |
| Bibliotheksgröße: besessen, ungelesen, Wunschliste | Besitzstatus, Lesestand |
| Ältestes ungelesenes Buch im Regal | Kaufdatum |
| Abbruchquote | Lesestand |
| Formate, Sprachen, Übersetzungen | Format, Sprache, Übersetzer |
| Häufigste Gefühle, häufigste Stärken | Karte |
| Wiedergelesene Bücher | Lesedurchgänge |
| Erscheinungsjahre, Verlage | ISBN-Daten |
| Wert der Bibliothek | Preis (nur wenn eingetragen) |

## Offene Fragen

1. Welche zwei bis vier Angaben gehören in die Kurzfassung unter dem Regal?
2. Name des Statistik-Bandes.
3. Dürfen ausgewählte Statistiken (z. B. Lieblingsgenre) später freiwillig ins Schaufenster?

## Am Lesen (24.10.2026, bestätigt)
- Höchstens 5 Bücher gleichzeitig am Lesen.
- Reihenfolge priorisierbar (1 bis 5).
- Priorität 1 erscheint auf der Startseite als aufgeschlagenes Buch mit Seitenzahl.
- Priorität 2 bis 5 erscheinen als kleine Balken mit Seitenzahl neben dem offenen Buch.
- Ein neu angefangenes Buch kommt ans Ende der Reihenfolge, wenn bereits ein Buch offen ist. Nach vorn holt man es selbst (bestätigt 24.10.2026).

## Lesezustände unter „Weitere Bände“ (24.10.2026, bestätigt)
- **Am Lesen (aktiv):** höchstens 5 Bücher gleichzeitig, genau die 5 Plätze der Startseite. Es gibt keinen eigenen Band „Aktiv“. Wer ein 6. Buch anfängt, wird ruhig gefragt, welches der 5 pausiert werden soll (bestätigt 24.10.2026, nach Recherche: rund ein Drittel liest nur ein Buch, die Mehrheit der engagierten Leser liest 2–5 parallel).
- **Pausiert:** mit Begründung (optional), jederzeit wieder auf aktiv setzbar.
- **Abgebrochen:** mit Begründung und mit Bewertung (ersetzt den früheren Vorschlag „abgebrochene Bücher bekommen keine Sterne“).

## Passende Bücher finden (Algorithmus, später)
Einfluss haben Begründung und Bewertung abgebrochener Bücher zusammen mit den Buchdaten (Autor, Genre usw.) und den gelesenen, bewerteten Büchern.

Beispiel (Arjen): Wurden 5 Bücher von Autor XY abgebrochen und gibt es kein positiv bewertetes, gelesenes Buch von XY, passt der Leser eher nicht zu XY.

Daraus folgt: Abbrüche und Pausen müssen mit Grund, Datum und Seite gespeichert werden, nicht nur als Status.

## Gründe (bestätigt 24.10.2026)
- **Abbrechen:** Stil/Sprache, Tempo, Thema, Figuren, Zu lang, Zu schwer, Erwartung nicht erfüllt, Nicht mein Genre, Inhaltlich unangenehm, Anderes (+ Freitext optional)
- **Pausieren:** Gerade nicht die Stimmung, Zu schwer für jetzt, Ein anderes Buch drängt, Keine Zeit, Will es in Ruhe lesen, Anderes (+ Freitext optional)
- **Offen für den Empfehlungsalgorithmus:** Gelesene und abgebrochene Bücher erhalten dieselben Kriterien zum Ausfüllen, jeweils optional.

