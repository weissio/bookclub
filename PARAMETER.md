# Parameter-Katalog

_Entwurf vom 10.10.2026 – **noch nicht bestätigt**. Grundlage: Arjens Vorgaben (Genre fehlt, Statistiken gewünscht) und [RECHERCHE.md](RECHERCHE.md)._

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

**Vorschlag feste Genre-Liste (16):** Roman / Gegenwart · Krimi & Thriller · Fantasy · Science-Fiction · Liebesroman · Historischer Roman · Horror · Jugendbuch · Kinderbuch · Klassiker · Lyrik & Drama · Comic & Graphic Novel · Biografie & Erinnerungen · Sachbuch · Ratgeber · Reise & Natur

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

| Statistik | braucht |
|---|---|
| Gelesene Bücher gesamt, pro Jahr, pro Monat | Lesestand, beendet am |
| Gelesene Seiten | Seitenzahl, Lesestand |
| Anzahl verschiedener Autoren | Autor |
| **Lieblingsautor** | Autor, Sterne (Regel offen, siehe Fragen) |
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

1. Ist die Genre-Liste so passend? Was fehlt, was ist zu viel?
2. Lieblingsautor: der mit den meisten gelesenen Büchern oder der mit der besten Durchschnittsbewertung (ab mindestens zwei Büchern)?
3. Wo leben die Statistiken? Die Startseite soll keine Zähler zeigen. Vorschlag: ein eigener Band „Mein Lesejahr“ im Regal.
4. Dürfen ausgewählte Statistiken (z. B. Lieblingsgenre) später freiwillig ins Schaufenster?
