# Bibliothek – Prototyp des Designer-Teams

Klickbarer iPhone-Prototyp (390 × 844 pt) im claude.ai-Design-Canvas, Seite „App (Designer-Team)“. `Bibliothek.dc.html` ist die Kopie aus dem Canvas.

## Idee

Die Bibliothek ist eine Reihe: sieben liegende Bände in festen Leinenfarben (Rot bis Violett), zusammen ein Regenbogenregal. Wärme kommt aus Material (Buchleinen, eine Goldprägung je Rücken, Vorsatzpapier unter dem Bandkopf) und aus der Stimme (ganze Sätze, „du“). Bedienelemente in Systemschrift, EB Garamond nur für Bandnamen, Buchtitel und eigene Worte.

## Korrekturrunde 24.10.2026

Nach Abschlussprüfung (Impeccable) und iOS-Prüfung:

- Leinen und Prägung als Bilder statt CSS-Verläufen; Vorsatzpapier als ruhiger Sepia-Marmor
- feste Navigationsleiste auf Band-, Buch- und Statistikseite, Titel erscheint beim Scrollen
- „Buch erfassen“ als oberste Reihe des Stapels, sichtbar ohne Scrollen; zusätzlich „+“ oben rechts
- Etikett „Weiterlesen“ entfernt
- alle Rücken volle Breite mit kleinem festem Versatz; Bandnamen dürfen umbrechen (große Schrift)
- Regalbrett unter dem letzten Band
- „Ganze Karte“ und Detailzeilen mit Pfeil zum Aufklappen
- Rückmeldung nach dem Eintragen direkt unter dem Knopf statt zeitgesteuerter Einblendung
- Sheet „Seite eintragen“ mit Abbrechen / Sichern oben; Sichern gesperrt, solange das Feld leer ist
- gewählter Tab mit gefülltem Symbol; erneutes Tippen auf „Bibliothek“ führt zurück zur Startseite
- eine Textfarbe (Tinte) für Textknöpfe, heller Schalter im Aus-Zustand
- Suchfeld 44 pt hoch mit Löschknopf; noch nicht gebaute Schritte öffnen einen Hinweis „Kommt bald“

Zweite Prüfrunde (unabhängige Abschlussprüfung): Urteil „nachbessern“, alle acht früheren Punkte erledigt. Eingearbeitet:

- Cover als Leinen mit Prägelinie, Farben nur noch aus dunklen Tönen der sieben Bandfarben
- „Neues Buch erfassen“ als ungefärbter Leinenrücken oben auf dem Stapel statt gestrichelter Box
- Anzahl und Pfeil der Rücken bündig rechts; Versatz nur noch links
- Rückmeldung nach dem Eintragen ersetzt die Zeile „… Seiten bis zum Ende“, nichts verschiebt sich mehr
- Griff oben an den Sheets; dunkle Prägelinie für Ocker als eigenes Bild statt Filter

Hinweis der Prüfung, noch nicht entschieden: Sterne erscheinen überall; wenn sie „wie sehr hat es mich erreicht“ bedeuten, sollte das einmal erklärt werden.

## Runde 3: nach psychologischer Beratung (24.10.2026)

- Ganze Startseite als Rückwand eines Regals (warmes Rohpapier als Bild), Leinenfarben leicht entsättigt, Buch- und Bandseiten auf warmem Buchpapier statt Weiß
- Ex-Libris statt „Bibliothek“: „Aus der Bücherei von Mara“ und „Bücherei am Fenster“ (Beispielnamen)
- Begrüßung als Satz: „Guten Abend. Das Lesebändchen liegt noch auf Seite 142.“ Rückmeldung nach dem Eintragen ersetzt diesen Satz
- Aktuelles Buch liegt obenauf mit Lesebändchen und „S. 142“; Tippen aufs Bändchen trägt die Seite ein. Kein Balken, keine Prozente
- „Ein Buch dazustellen“ als einziger Erfassen-Einstieg (Rohleinenband oben); Plus oben rechts entfernt
- Rücken werden mit der Anzahl dicker, Zahl eingeprägt, keine Pfeile
- Zettel mit einem Satz aus der eigenen Lesart am Regalbrett; Druckvermerk statt Statistikblock
- Knöpfe aus Leinen statt schwarzer Pillen
- Neue Bilder: `assets/make_raum.py` (Rückwand, Buchpapier, Regalbrett, Lesebändchen)

Offen: Band- und Buchseiten noch in Listenoptik, Patina der Bände, Android-Variante, endgültige Bereichsnamen.

## Dateien

- `assets/make_textures.py` – erzeugt `linen.png`, `praegung.png`, `vorsatz.png` prozedural (keine Fremdbilder)
- `flow.js` – Playwright-Durchlauf, erzeugt die Bilder in `.impeccable/review/`
