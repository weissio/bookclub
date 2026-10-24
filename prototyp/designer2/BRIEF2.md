# Briefing Runde 2: Startseite „Bibliothek“ in der kreativen Richtung von „Licht an“

Lies zuerst das Grundbriefing `/home/claude/bookclub/prototyp/designer/BRIEF.md` mit Produkt, Belegen, Regeln und KI-Standards, die zu vermeiden sind. Es gilt weiter. Hier steht, was sich geändert hat.

## Was der Auftraggeber (Arjen) gewählt hat und warum
Aus acht Entwürfen von vier Designern hat ihm **„Licht an“** am besten gefallen. Das Bild liegt unter `/home/claude/bookclub/prototyp/designer/3-charakter/konzept-a.png`, schau es dir an. Sein Urteil: „erweckt zum ersten Mal Kreativität mit Kompaktheit“. Die anderen Entwürfe waren ihm „zu kühl, sehen mehr aus wie Kennzahlen und statistische Systeme“.

**Wichtig:** Er will nicht genau diesen Entwurf, sondern **mehrere neue Ideen mit dieser Art von Kreativität**. Gemeint ist eine illustrierte, warme, sympathische Welt mit Charakter, die trotzdem kompakt ist. Kopiere „Licht an“ nicht: keine Pendelleuchte, keine aufgeschlagenen Bücher im Lichtkegel als Hauptmotiv.

## Seine Kritik an „Licht an“, die du lösen musst
1. **Zu großer Fokus auf „gerade gelesen“.** Dort nimmt es fast die Hälfte der Ansicht ein. Neu darf „Am Lesen“ samt „Seite eintragen“ höchstens etwa **ein Viertel bis ein Drittel des ersten Bildschirms** einnehmen. Es muss mit 1 bis 5 Büchern funktionieren, und „Seite eintragen“ bleibt mit einem Tippen erreichbar.
2. **Zu viele kleine Regal-Bausteine.** In „Licht an“ waren es acht kleine Icon-Kacheln. Neu sind es **weniger, größere, klar benannte Einstiege** in die Bibliothek. Sie sollen sich wie ein Ort anfühlen, nicht wie ein App-Raster.

## Was jetzt im Vordergrund steht
- **Psychologische Faktoren:** Lies `/home/claude/bookclub/.impeccable/psychologie/leserpsychologie.md` und `/home/claude/bookclub/.impeccable/psychologie/beratung-stilmittel.md`. Wichtig sind: das Regal als Teil des Selbst, Ankommen statt Leisten, ungelesene Bücher warten freundlich, Introvertierte zeigen sich über Dinge, Ruhe ohne Druck. Benenne für jede Gestaltungsentscheidung den psychologischen Grund.
- **Nutzerfreundlichkeit:**
  - eine Hand
  - Tippziele ≥ 44 pt
  - Beschriftungen lesbar und eindeutig
  - die häufigste Handlung (Seite eintragen) ist mit einem Tippen erreichbar
  - es gibt nur einen Weg zum Erfassen
  - keine Doppelungen
  - lesbar auch bei großer Systemschrift
  - Kontrast mindestens 4,5 : 1 für Text

## Auftrag
1. **Recherche:** 4 bis 6 echte Vorbilder aus deiner Designschule mit URL.
2. **Zwei grundverschiedene Startseiten-Konzepte** (erster Bildschirm, 390 × 844, iPhone). Dazu je eine zweite Ansicht derselben Startseite mit **4 Büchern am Lesen**, damit man sieht, dass nichts verstopft.
3. Statisches HTML (inline CSS, SVG-Illustrationen selbst gezeichnet, Google Fonts erlaubt). Rahmen 390 × 844 px, oben 54 px Statusleiste, unten 34 px Home-Indikator. Daten: 2 bzw. 4 Bücher am Lesen, etwa 240 Bücher in der Bibliothek, als Beispieldaten erkennbar.
4. Rendern mit Playwright (`require('playwright')`, `chromium.launch()`, Viewport 390 × 844, deviceScaleFactor 2). Arbeite **nur in deinem eigenen Ordner**, verwende einen eigenen Port und starte keine Skripte anderer Ordner. Schau die PNGs mit dem Read-Tool an und verbessere sie, höchstens 2 Runden.
5. `KONZEPT.md` mit folgenden Angaben pro Konzept:
   - Name und Idee in 2 Sätzen
   - Vorbilder mit URL
   - Flächenanteil von „Am Lesen“ in Prozent
   - Anzahl der Bibliotheks-Einstiege
   - psychologische Begründung der 3 wichtigsten Entscheidungen
   - Nutzerfreundlichkeit: wie die häufigste Handlung abläuft und wo erfasst wird
   - Skalierung auf 1.000 Bücher
   - Risiko

Dateinamen: `konzept-a.html`, `konzept-a.png`, `konzept-a-4buecher.png`, `konzept-b.html`, `konzept-b.png`, `konzept-b-4buecher.png`, `KONZEPT.md`. Für die Ansicht mit 4 Büchern darfst du eine zweite HTML-Datei anlegen.
