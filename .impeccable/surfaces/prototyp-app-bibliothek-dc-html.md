---
version: 1
slug: "prototyp-app-bibliothek-dc-html"
primary_target: "prototyp/app/Bibliothek.dc.html"
related_targets: []
---

# Surface brief: Bibliothek (App-Prototyp)

Scope: Startseite „Bibliothek“, aufgeschlagener Band (Liste), Buchseite, Sheet „Seite eintragen“, Sheet „Buch erfassen“, Band „Statistiken“. Mode: Operate. Platform: iOS conventions.

Audience and job: Leser:innen zu Hause, einhändig; häufigste Aufgaben: weiterlesen und Seite eintragen, einen Band öffnen und ein Buch finden, ein Buch erfassen, die eigenen Worte zu einem Buch lesen.

Constraints: Owner pinned materials (Buchleinen, Prägung, Vorsatzpapier) but delegated all design authority; Wärme aus Material und Stimme; einfach, nicht kleinteilig, nicht verklickbar. Previous critique 19/40: shelf used as precise control, missing „Seite eintragen“, overloaded book page, broken platform conventions, contrast failures.

Decision round: owner delegated authority to the design team (24.10.2026); the assigned direction is built without a decision page. Challenger verdicts below.

Grounded list (by resonance): 1 Buchleinen, Goldprägung und Vorsatzpapier (owner-pinned material) · 2 handgeschriebene Empfehlungskärtchen der Buchhandlung · 3 Die Regenbogen-Reihe: eine Taschenbuchreihe, deren Rücken im Regal ein Farbspektrum bilden (Tradition der deutschen Reihengestaltung der 1960er) · 4 die gelbe Klassiker-Reihe im Heftformat · 5 kleine Hardcover mit Buntpapier und aufgeklebtem Titelschild · 6 Zettelkatalog der Stadtbibliothek · 7 Lesesaal.

Challenger verdicts:
- data-sublime barcode field: declined. Kept discipline: total palette commitment, nothing outside the defined spectrum.
- botanical folio: declined (competitive on nothing). Kept discipline: one fixed scale and shared baseline for every cover across all screens.
- labanotation score: declined. Kept discipline: length encodes real quantity (spine fill encodes the book count).
- design annual plate section: declined. Kept discipline: one UI face throughout, the display face only for book-world moments.
- boarding pass and gate board: declined. Kept discipline: a change stays marked until noticed (a just-finished book keeps its mark until opened).
- zoo guide map: declined. Kept discipline: colour fields own whole regions (an opened volume's header is its colour).

## Direction contract

THESIS: Die Bibliothek ist eine Reihe. Jede Liste ist ein Band mit eigener Farbe aus einem festen Spektrum, liegend gestapelt; zusammen ergeben die Rücken ein Regenbogenregal. Verweigert: das Raster aus gleich großen Karten und die stehende Rückenreihe als Zielübung.

OWN-WORLD: Weißer Grund, Tinte #1F1D1A. Sieben gesättigte Leinenfarben in Spektrumsreihenfolge (Rot, Orange, Ocker, Grün, Petrol, Blau, Violett), feine Leinenstruktur, eine helle Prägelinie je Rücken. Systemschrift für alles Bedienbare; EB Garamond nur für Bandnamen, Buchtitel und die eigenen Worte. Native Leiste, gruppierte Listen.

STORY: Man sieht sofort, wo man liest, trägt mit einem Tippen die Seite ein, öffnet einen Band über die volle Zeilenbreite und findet die eigenen Worte zuoberst auf der Buchseite. Die App spricht leise in ganzen Sätzen.

FIRST VIEWPORT: Großer Titel „Bibliothek“. Darunter Karte „Weiterlesen“ (Cover, Titel, Seite 142 von 312, Fortschritt, Knopf „Seite eintragen“). Dann der Stapel: sieben liegende Rücken, je 358 × 56 pt, 6 pt Abstand, leicht versetzt, Name links, Anzahl rechts. Unten über der Tab-Leiste der Knopf „Buch erfassen“ im Daumenbereich.

FORM: Regenbogen-Reihe als Stapel liegender Bände, Position 3 der eigenen Liste. seed:4dac831833509680

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

Signature interaction: Tippen auf einen Rücken öffnet den Band; dessen Kopf übernimmt die Leinenfarbe des Rückens als ganze Fläche (150 ms Einblenden, kein 3D).

Unresolved: Dark Mode (folgt), Android-Variante, endgültige Bereichsnamen.
