# Designer 1: Apple-Design-Award-Handwerk

Meine Haltung: native iOS-Bausteine (Navigationsleiste, Systemmaterial, Tab-Leiste, gruppierte Flächen) bleiben unangetastet. Jedes Konzept bekommt **genau eine präzise Idee**, die es unverwechselbar macht. Alle Bücher, Namen und Zahlen sind erfundene Beispieldaten.

## Recherche: Vorbilder und was ich daraus nehme

| Vorbild | URL | Was ich übernehme |
|---|---|---|
| Flighty (ADA 2023, Interaction) | https://en.wikipedia.org/wiki/Flighty · https://blakecrosley.com/de/guides/design/flighty | Daten werden zu einem Bild (Route mit Flugzeug statt Prozentzahl). Große, ruhige Ziffern für die eine Zahl, die zählt. Zeigt nur, was gerade relevant ist. |
| Halide Mark II (Lux Optics) | https://www.lux.camera/pro-camera-action-introducing-halide-mark-ii/ | Instrument-Rad mit Skala, das sich mit dem Daumen ziehen lässt. „Stay out of the way“. Alle häufigen Bedienelemente liegen in der Daumenzone, seltene wandern nach oben. |
| Gentler Streak (ADA 2024, Social Impact) | https://developer.apple.com/design/awards/2024/ | Ein ermutigender Ton statt Druck, Fortschritt ohne harten Vergleich. Daraus kommen „heute +23“ statt Streak und „Beiseitegelegt“ statt „Abgebrochen“. |
| Crouton (ADA 2024, Interaction) | https://developer.apple.com/design/awards/2024/ · https://www.macstories.net/reviews/crouton-review-an-elegant-modern-recipe-manager-and-cooking-aid/ | Die eine Handlung, die man jetzt braucht, steht allein und groß auf dem Schirm (Kochmodus mit einem Schritt). Übertragen heißt das: Seite eintragen ohne Umweg. |
| Mercury Weather | https://www.macstories.net/reviews/mercury-weather-a-crystal-clear-design-for-every-apple-device/ | Farbe trägt Information, die Kacheln sind klar gegliedert und die Typografie ist auf einen Blick lesbar. |
| Things 3 (Cultured Code, ADA 2017) | https://apps.apple.com/app/id904244226 | Ein einziger schwebender „Magic Plus“-Knopf im Daumenbereich statt mehrerer Hinzufügen-Wege. Zurückhaltendes Weiß, ein Akzent. |

---

## Konzept A: „Buchschnitt“

**Datei:** `konzept-a.html` / `konzept-a.png`

**Idee:** Jedes Buch, das du gerade liest, erscheint als sein Schnitt: der Seitenblock von der Seite gesehen, oben und unten die Deckel in der Farbe des Einbands. Gelesene Seiten sind nachgedunkelt, das Lesebändchen hängt genau an deiner Seite heraus. Die Bände tragen dieselbe Idee als **Farbschnitt**, also als eingefärbte Papierkante auf einer sonst ganz nativen, hellen iOS-Kachel.

Die Welt ist kühles Porzellan-Grau mit Systemweiß und einem Ultramarin-Akzent. Es gibt kein Creme, kein Holz und keine Serifen. Die Schrift ist Hanken Grotesk mit Tabellenziffern.

- **Vorbilder:** Flighty (Fortschritt als Bild), Things 3 (ein Plus, ruhiges Weiß), Mercury Weather (Farbe als Information). URLs siehe oben.
- **1 und 5 aktuelle Bücher:** Bei einem Buch steht eine einzige Karte da, die Bände rücken nach oben. Bei 2 Büchern siehst du 2 Karten. Ab 3 Büchern werden die Karten kompakt (Titel und Schnitt in einer Zeile, ca. 64 pt). Die Reihenfolge legst du über „Reihenfolge“ selbst fest. Ab 4 Büchern zeigt die Startseite 3 Bücher, das vierte und fünfte erreichst du über „+2 weitere“.
- **Wo wird erfasst?** Ein einziger Plus-Knopf unten rechts im Daumenbereich. Tippen öffnet den Scanner im Mehrfachmodus (Schübe), lange drücken bietet ISBN tippen oder Erfassen von Hand an. Sonst gibt es nirgends ein Plus.
- **Skalierung auf 1.000 Bücher:** Auf der Startseite stehen nur Zähler in den 6 Kacheln. Der Schnitt zeigt Seiten eines Buches, nicht die Menge der Bücher. Nichts wächst mit dem Bestand.
- **Sympathisches Element:** Das Lesebändchen in der Einbandfarbe und der nachgedunkelte, „gebrauchte“ Teil des Schnitts. Man sieht dem Buch an, dass man darin wohnt.
- **Risiko:** Die Seitenlinien sind feine Muster. In der echten App müssen sie als Bild in @2x/@3x kommen, sonst flimmern sie oder wirken wie ein Strichcode. Außerdem liegt die Kachel-Ebene nah am iOS-Standard. Trägt der Farbschnitt allein genug Eigenart?

---

## Konzept B: „Lesepult“

**Datei:** `konzept-b.html` / `konzept-b.png`

**Idee:** Die Startseite ist zweigeteilt wie ein Möbel. Oben steht das Regal: die Bände als Leinenrücken mit Goldprägung, gleich breit, weit weg vom Daumen, weil man dort selten tippt. Unten liegt das Pult in der Daumenzone mit dem aktuellen Buch, einer großen Seitenzahl und einem **Seitenrad** nach dem Vorbild der Halide-Kamera: ziehen, loslassen, gespeichert. Die heute gelesenen Seiten leuchten auf der Skala golden.

Die Welt ist ein Nachtblau, das an Leinen erinnert, mit Gold. Es gibt kein Schwarz-Neon. Barlow / Barlow Semi Condensed wirkt wie die gravierte Beschriftung eines Instruments.

- **Vorbilder:** Halide (Rad, Daumenzone, Instrumentenschrift), Flighty (eine große Zahl), Crouton (eine Handlung allein im Fokus), Gentler Streak („heute +23“ statt Streak). URLs siehe oben. Ausgangspunkt war Arjens Wunsch nach Leinenrücken mit Goldprägung.
- **1 und 5 aktuelle Bücher:** Bei einem Buch entfällt der Umschalter, und der Titel steht als Zeile über der Zahl. Bei 2 bis 3 Büchern gibt es Umschalt-Chips, bei 4 bis 5 Büchern 3 Chips und dazu „+2“, das ein Auswahlblatt öffnet. Das Pult zeigt immer genau ein Buch, deshalb bleibt die Höhe konstant.
- **Wo wird erfasst?** Am Ende des Regals steht ein leerer, gestrichelter Platz „Erfassen“. Logisch ist das der Ort, an den ein neues Buch gestellt wird. Er liegt bewusst oben, weil man in Schüben erfasst und das selten tut. Das Häufige (Seite eintragen) liegt unten.
- **Skalierung auf 1.000 Bücher:** Das Regal hat immer genau 6 Rücken mit fester Breite. Die Rückenhöhen sind gestaltet und hängen nicht von der Anzahl ab. Nur die geprägte Zahl ändert sich. Eigene Regale verbergen sich hinter einem Rücken.
- **Sympathisches Element:** Das goldene Stück der Skala „heute +23“. Es zeigt, was du heute gelesen hast, ohne Ziel, Streak oder Wertung. Dazu kommen die Prägung auf den Rücken und das Gefühl, an einem Pult zu sitzen.
- **Risiko:** Das Rad kann zu fein sein, wenn man 80 Seiten auf einmal einträgt. Dafür braucht es ein schnelles Schwungrad und das Tippen auf die große Zahl für die Eingabe per Tastatur. Der dunkle Grund und das Gold liegen nahe an „edel“ und könnten mit Schmuck-Ästhetik verwechselt werden. Die Leinentextur muss als Bild kommen.

---

## Was die beiden grundverschieden macht

| | A Buchschnitt | B Lesepult |
|---|---|---|
| Welt | hell, Systemmaterial, Porzellan | dunkel, Leinen, Gold |
| Präzise Idee | Datenvisualisierung (Schnitt + Bändchen) | Bedienelement (Seitenrad) |
| Seite eintragen | Knopf „S. 214“ öffnet Eingabe | direkt ziehen, ohne Blatt |
| Bände | Kacheln mit Farbschnitt | Buchrücken im Regal |
| Erfassen | schwebendes Plus (Daumen) | leerer Regalplatz (oben, selten) |
| Ordnung | Lesen oben, Bestand unten | Bestand oben, Lesen unten (Daumenlogik) |
