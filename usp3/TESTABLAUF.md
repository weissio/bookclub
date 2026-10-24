# Erster Algorithmustest mit Arjens eigenen Büchern

Arjen gibt die Bücher vor und beurteilt selbst, ob die Empfehlungen passen. Das ist ein erster qualitativer Test mit einer Person. Er sagt etwas über die Plausibilität aus, beweist aber keine Überlegenheit einer Variante.

## Ablauf
1. **Arjen liefert seine Bücher.** Am besten 15–30 Titel, gemischt aus guten und schlechten, gelesenen und abgebrochenen. Die Vorlage ist `meine-buecher-vorlage.csv`.
   - Pflicht: Titel, Autor, Status, Lichter
   - alles andere freiwillig, wie im Bewertungsbogen
2. **Merkmale erfassen (Claude).** Für Arjens Bücher und für die Kandidaten werden Genre, Thema, Tempo, Ton, Fokus, Sprache, Länge und Inhalt erfasst.
   - Jedes Merkmal bekommt eine Quelle: DNB, Verlagstext oder Rezension.
   - Ein Merkmal ohne Beleg bleibt leer.
   - Die Kandidatenmerkmale werden **ohne Kenntnis** von Arjens Bewertungen erfasst.
3. **Kandidaten.** Grundlage sind die 48 Titel aus `startkatalog-vorschlag.md`, ergänzt nach Bedarf. Bücher, die Arjen schon kennt, werden markiert und fallen heraus.
4. **Drei Varianten** liefern je 5 Empfehlungen: nachbar, cluster und nur F1.
   - Die Empfehlungen werden **gemischt und ohne Variantenname** vorgelegt, damit das Urteil nicht beeinflusst wird.
   - Jede Empfehlung zeigt ihre Begründung.
5. **Arjen beurteilt jede Empfehlung:**
   - „Würde ich lesen?“: Ja · Vielleicht · Nein
   - „Passt die Begründung?“: Ja · Teilweise · Nein
   - optional ein Satz, warum
6. **Auswertung.** Erst danach wird aufgedeckt, welche Empfehlung aus welcher Variante kam.
   - Die Ergebnisse werden je Variante getrennt gezählt.
   - Später, wenn Arjen Bücher davon tatsächlich gelesen hat, folgen echte Lichter. Erst diese zählen für `auswertung.py`.

## Grenzen
- Eine Person und eine Momentaufnahme. Wie gut die Merkmalserfassung ist, prägt das Ergebnis stark.
- „Würde ich lesen“ ist nicht dasselbe wie späteres Gefallen. Es dient nur als frühes Signal.
