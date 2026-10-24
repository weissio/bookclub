# Designschule Papier, Scherenschnitt und Collage: zwei Startseiten

Gebaut wird nur aus flachen, geschnittenen Farbflächen (SVG, CSS-clip-path). Die Tiefe entsteht durch weiche, kurze Schichtschatten (Papier liegt auf Papier). Es gibt keine Fotos, keine Fake-Texturen, keine Verläufe und keine harten Versatz-Schatten. Alle Daten sind Beispieldaten und als solche markiert.

## Vorbilder (für beide Konzepte)

| Vorbild | URL | Was ich übernehme |
|---|---|---|
| Henri Matisse, *Jazz* und die Scherenschnitte | https://www.moma.org/audio/playlist/6/304 | Mutige, unvermischte Farbflächen und organische Schnittformen (Blatt, Stern, Alge) als Ornament. Die Farbe trägt die Gliederung, Linien sind nicht nötig. |
| Eric Carle | https://www.carle.org/about-eric-carle | Kindliche Direktheit und Wärme durch einfache, gerissene oder geschnittene Formen. Jedes Ding hat *eine* Farbe. |
| Lotte Reiniger, *Die Abenteuer des Prinzen Achmed* (1926) | https://en.wikipedia.org/wiki/The_Adventures_of_Prince_Achmed | Dunkle Silhouetten vor farbigem Grund: Fenster, Bogen und Treppengiebel werden als Schattenriss gelesen. |
| Tearaway (Media Molecule) | https://blog.playstation.com/?p=190010 | Eine ganze begehbare Welt aus Papier, in der Orte auch Bedienelemente sind. Daher kommt das „Viertel“ in Konzept A. |
| Robert Sabuda, Pop-up-Bücher | https://www.readingrockets.org/books/interviews/sabuda | Fächer und Ebenen, die sich aus der Fläche heben. Leichte Tiefe ohne 3D-Effekt. Daher kommt das ausgeschnittene Regal mit Fachschatten in Konzept B. |
| Owen Gildersleeve | https://theinspirationgrid.com/handcrafted-worlds-layered-papercut-art-by-owen-gildersleeve/ | Geschichtete Papierlandschaften mit sauberem Schnitt und kleinen Schatten. Daran orientiert sich das Maß für die Schichtschatten. |

---

## Konzept A: „Papierviertel“

**Idee:** Die Bibliothek ist ein kleines Viertel aus geschnittenen Papierhäusern. Jeder Band ist ein Haus mit eigener Silhouette (Giebel, Bogen, Sternfenster, Treppengiebel). Oben liegt auf einem petrolfarbenen Fensterbrett, was gerade aufgeschlagen ist.

- Dateien: `konzept-a.html`, `konzept-a.png` (2 Bücher), `konzept-a-4buecher.html`, `konzept-a-4buecher.png`
- **Flächenanteil „Am Lesen“:** 228 px von 844 px, das sind **27 %**. Der Wert ist bei 1 bis 5 Büchern gleich, weil das Fensterbrett eine feste Höhe hat und die Bücher schmaler werden.
- **Bibliotheks-Einstiege:** 4 Häuser (Gelesen 148, Wartet im Regal 61, Wunschliste 23, Eigene Regale 5) und 2 Wegweiser (Beiseitegelegt, Rückblick), zusammen **6**. Dazu kommt „Buch erfassen“ als Aktion.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. **Die Bibliothek als Ort mit Adresse („Kirschweg 7“, „Dein Viertel“) statt als Raster.** Belk sieht Besitz als erweitertes Selbst, Gosling zeigt, dass Räume ihre Bewohner verraten. Ein Viertel kann man „bewohnen“, Kacheln kann man nur bedienen. Das löst Arjens Kritik am App-Raster.
2. **„Wartet im Regal“ als Haus mit offenem Fenster und Büchern darin, Beiseitegelegt nur als Wegweiser am Rand.** Der SuB wird so zu einem freundlich wartenden Haus und nicht zu einer Schuldzahl. Abgebrochenes bleibt erreichbar, ohne aufzufallen („ohne Groll“). Das entspricht Ankommen statt Leisten.
3. **„Aufgeschlagen“ statt „Fortschritt“: nur „bei Seite 142“, kein Balken, keine Prozente.** Ruhe ohne Druck (Calm Technology, Walters „du kannst“). Die Seitenzahl ist eine Erinnerung und kein Ziel.

**Nutzerfreundlichkeit**
- Häufigste Handlung: Man tippt bei dem Buch auf den gelben Streifen „Seite eintragen“ (48 pt hoch, bei 4 Büchern 52 pt mit Seitenzahl). Danach öffnet sich das Seiten-Sheet. Das ist ein Tippen, und alles liegt im oberen Drittel. Mit dem Daumen ist das gerade noch erreichbar. Bei 4 Büchern sitzen die Knöpfe auf derselben Höhe.
- Erfassen gibt es **nur** an einer Stelle: der Papierstreifen „Buch erfassen · Scan · ISBN · von Hand“ unten am Viertel, gut im Daumenbereich. Ein Plus in der Kopfzeile gibt es nicht.
- Kontrast: Weiß auf Petrol ca. 8,9 : 1, Tinte auf Senf ca. 11 : 1, Weiß auf Kobalt ca. 7,6 : 1, Weiß auf Grün ca. 6,3 : 1, Tinte auf Rosa ca. 6,8 : 1.
- Große Systemschrift: Die Hausbeschriftung ist zweizeilig und darf auf drei Zeilen wachsen. Die Häuser wachsen dabei nach oben in den „Himmel“. Bei sehr großer Schrift gehen die Wegweiser in eine zweite Reihe.

**Skalierung auf 1.000 Bücher:** Nur die Zahlen auf den Schildern ändern sich. Häuser, Fenster und Höhen bleiben fest, nichts wächst linear. Eigene Regale öffnen sich als eigene Straße.

**Risiko:** Die Häuser-Metapher kann ins Niedliche kippen, wenn weitere Deko dazukommt (Wolken, Bäume, Figuren). Strenge Regel: höchstens eine Form pro Haus. Bei 5 Büchern werden die Titel im Fensterbrett auf 2 Zeilen gekürzt.

---

## Konzept B: „Jazz-Regal“

**Idee:** Ein einziges, aus Ultramarin geschnittenes Regal auf Zitronenpapier. Die Fächer sind große Matisse-Farbflächen mit je einer Schnittform. Die Bücher am Lesen liegen als einzelne Papierbänder darüber, ein Band pro Buch.

- Dateien: `konzept-b.html`, `konzept-b.png` (2 Bücher), `konzept-b-4buecher.html`, `konzept-b-4buecher.png`
- **Flächenanteil „Am Lesen“:** bei 2 Büchern 165 px, also **20 %**. Bei 4 Büchern 261 px, also **31 %**. Bei 5 Büchern sind es etwa 34 %, die Bänder werden dafür auf 50 px verdichtet. Das Regal gibt die Höhe ab: Die Fächer schrumpfen, die Einstiege bleiben.
- **Bibliotheks-Einstiege:** 3 große Fächer (Gelesen, Wartet im Regal, Wunschliste) und 3 Schubladen (Eigene Regale, Beiseitegelegt, Rückblick), zusammen **6**. Dazu kommt das leere Fach „Buch erfassen“.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. **Das ganze Regal ist ein Gegenstand, das „Shelfie“ als Startseite.** Introvertierte zeigen sich über Dinge (Gosling, Shelfie-Studien). Ein einziger, kräftiger Korpus wirkt wie *mein* Möbel und nicht wie ein Menü. Die großen Farbfelder geben Wärme ohne Kitsch.
2. **Erfassen als Lücke im Regal, durch die das Grundpapier scheint.** Die leere Stelle lädt ein, ohne zu drängen (Ma, Leerraum mit Bedeutung). Das neue Buch „füllt die Lücke“. Das gibt Sinn und erklärt, warum es dort steht und nicht oben.
3. **„Wartet im Regal · ganz ohne Eile“ und die Wunschliste mit gelbem Stern auf Schwarz.** Ungelesenes wartet freundlich. Wünsche bekommen das hellste Zeichen, aber keine Zahl, die drängt. Die Stimme der Buchhändlerin spricht nur in Nebensätzen.

**Nutzerfreundlichkeit**
- Häufigste Handlung: Am rechten Ende jedes Bandes ist eine ultramarinblaue Lasche „Seite eintragen“ (104 × 64 pt, bei 4 Büchern 104 × 54 pt). Ein Tippen genügt. Alle Laschen liegen rechts in einer Spalte, also für Rechtshänder in der Daumenzone. Die zuletzt eingetragene Seite steht im Band („bei S. 142“), damit sie nicht doppelt erscheint.
- Erfassen gibt es **nur** im Lückenfach „Buch erfassen · Scan · ISBN · von Hand“. Es liegt im unteren Drittel und ist mit einer Hand gut erreichbar.
- Kontrast: Weiß auf Ultramarin ca. 10 : 1, Weiß auf Koralle ca. 4,6 : 1 (nur große Schrift ab 17 px fett), Tinte auf Rosa ca. 12 : 1, Weiß auf Nachtschwarz ca. 17 : 1, Tinte auf Zitrone ca. 14 : 1. Die Fließschrift ist Atkinson Hyperlegible, gebaut für Lesbarkeit.
- Große Systemschrift: Die Bänder werden höher, die Fächer geben Höhe ab. Die Nebensätze („ganz ohne Eile“) fallen zuerst weg, Zahl und Name bleiben.

**Skalierung auf 1.000 Bücher:** Die Fächer haben eine feste Geometrie, nur die Zahl ändert sich. „Zuletzt: Nachtzug“ zeigt immer genau einen Titel. Eigene Regale liegen in der Schublade, egal ob es 5 oder 50 sind.

**Risiko:** Zitronengelb als Grund ist mutig und kann am Abend laut wirken. Eine gedämpfte Abendvariante (Zitrone → Safranocker) müsste getestet werden. Bei 5 Büchern wird das Regal flach. Die großen Fächer sind dann nur noch etwa 80 pt hoch, das ist noch tippbar, aber weniger „Ort“.
