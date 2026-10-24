# Briefing für die Designer: Startseite „Bibliothek“

Du bist ein unabhängiger App-Designer. Andere Designer arbeiten parallel an derselben Aufgabe, ihre Entwürfe siehst du nicht. Gesucht ist **deine** Handschrift. Der Auftraggeber (Arjen, CEO) hat bisherige Entwürfe als „0815“, „KI-Slop“ und „immer 2–3 ähnliche Modelle, null neue Inspiration“ abgelehnt.

## Produkt
Lies: `/home/claude/bookclub/PRODUCT.md`, `/home/claude/bookclub/ARCHITEKTUR.md`.
Kurz: deutsche iPhone-App, private Heimbibliothek für gedruckte Bücher. Erfassen per ISBN, Bände (Listen):
- Am Lesen
- Gelesen
- Ungelesen im Regal
- Wunschliste
- Abgebrochen
- Eigene Regale
- Statistiken

Dazu Bewertung mit eigenen Worten. Später kommt ein freiwilliges, pseudonymes „Schaufenster“. Tab-Leiste: Bibliothek · Schaufenster · Entdecken · Ich. Die Zielgruppe schließt introvertierte Leser ein. Die App soll die Wärme eines Buchclubs haben, sympathische Elemente, einzigartig sein und einfach und nicht kleinteilig wirken.

## Belegte Grundlagen (lesen!)
- Leserpsychologie: `/home/claude/bookclub/.impeccable/psychologie/leserpsychologie.md`
- Leseverhalten und Startseiten anderer Apps: `/home/claude/bookclub/.impeccable/psychologie/leseverhalten.md`

Harte Fakten für die Startseite:
- 1 bis 5 Bücher gleichzeitig „am Lesen“.
- Seite eintragen ist die häufigste Handlung.
- Bücher werden in Schüben erfasst (großer Import, dann gelegentlich).
- Der Bestand reicht von 10 bis Tausende Bücher. Nichts darf linear mit der Anzahl wachsen.
- Keine fremden Inhalte, kein Feed, keine Streaks.

## Was Arjen bisher abgelehnt hat
- Generischer iOS-Look: großer fetter Titel, schwarze Pillen-Knöpfe, Listen wie Einstellungen.
- Ein Viertel der Fläche nur Dekoration (Begrüßung, Zitat-Zettel, Druckvermerk).
- Doppelte Aktionen (zwei „+“).
- Cremepapier + Serifenschrift + Holzbrett = Buch-Kostüm.
- Logik ohne Grund: z. B. „Buch dazustellen“ ganz oben, Rücken, die mit der Anzahl dicker werden.
- Mehrere Varianten, die nur Umstellungen desselben Baukastens sind.

Gemocht hat Arjen bisher: die Idee der Bände als Buchrücken in Leinenfarben mit Goldprägung, als Ausgangspunkt. Das ist aber nicht bindend. Du darfst eine völlig andere Welt vorschlagen.

## Regeln
- Es ist eine App: Tippziele ≥ 44 pt, kaum Animation (kein Ruckeln), Bedienung mit einer Hand.
- Texturen nur als Bilder, nicht als Live-Filter. Du kannst keine Bilder erzeugen, also arbeite mit CSS, SVG und Typografie.
- Echte Beispieldaten auf Deutsch, als Beispiel erkennbar.
- Vermeide die KI-Standards:
  - warmer Cremegrund + kontrastreiche Serifen + Terrakotta-Akzent
  - Schwarz + Neon
  - Haarlinien-Editorial mit Mono-Labels
  - flache Sättigung mit harten Versatz-Schatten
  - Fraunces, Playfair, Cormorant, Lora, Inter-als-Display, DM Sans, Space Grotesk
  - Wenn man deinen Stil aus der Kategorie „Buch-App“ erraten kann, ist er gescheitert.

## Auftrag
1. **Recherche** (WebSearch/WebFetch): Suche 4–6 echte Vorbilder aus deiner Designschule, also echte Apps, Gestaltungen oder Objekte, mit URL. Begründe jeweils, was du daraus nimmst.
2. **Entwerfe 2 grundverschiedene Startseiten-Konzepte** (erster Bildschirm, 390 × 844 pt, iPhone) mit deiner Handschrift. Sie dürfen sich nicht nur in der Anordnung unterscheiden.
3. Je Konzept eine **statische HTML-Datei** (inline CSS, Google Fonts erlaubt, kein JavaScript nötig), Rahmen exakt 390 × 844 px. Statusleiste: 54 px oben frei lassen. Home-Indikator: 34 px unten. Zeige 2 Bücher „am Lesen“ und eine Bibliothek mit etwa 240 Büchern.
4. **Rendere** jede Datei als PNG mit Playwright (Node, `require('playwright')` funktioniert, `chromium.launch()` ohne Optionen, Viewport 390 × 844, deviceScaleFactor 2). Schau dir dein PNG mit dem Read-Tool an und verbessere, bis es deinem Anspruch genügt (höchstens 2 Runden).
5. Schreibe `KONZEPT.md`. Pro Konzept: Name, Idee in 2 Sätzen, Vorbilder mit URL, Antworten auf
   - Wie geht es mit 1 und mit 5 aktuellen Büchern?
   - Wo wird erfasst?
   - Wie skaliert es auf 1.000 Bücher?
   - Was ist das sympathische Element?
   - Welches Risiko gibt es?

Ablage: nur in deinem Ordner (siehe Auftrag), sonst nichts anfassen.
