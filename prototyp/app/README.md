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

Offen: Dark Mode, Android-Variante, endgültige Bereichsnamen.

## Dateien

- `assets/make_textures.py` – erzeugt `linen.png`, `praegung.png`, `vorsatz.png` prozedural (keine Fremdbilder)
- `flow.js` – Playwright-Durchlauf, erzeugt die Bilder in `.impeccable/review/`
