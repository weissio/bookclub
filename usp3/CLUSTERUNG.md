# USP III: Bewertungen zu passenden Büchern verbinden

Stand: 24.10.2026. Grundlage: lokales Repository bis `540f013`. Arbeitsgrundlage für die Umsetzung; kein Nachweis einer Empfehlungswirkung. Die bestehende Bewertungsansicht wird nicht um einen Pflichtfragebogen erweitert.

## 1. Das Ziel messbar machen

Empfohlen werden sollen neue Bücher, die die Person anschließend mit 4 oder 5 Lichtern bewertet. Die Schwelle ist eine operative Definition von „gut“ anhand der beschlossenen Beschriftung, keine psychologische Naturkonstante. Ein mit 4–5 Lichtern bewerteter Abbruch ist ebenfalls positives Gefallen; der Abbruch bleibt zusätzlich als eigenes Ereignis erhalten.

Primär messen wir den Anteil mit 4–5 Lichtern unter den bewerteten, nachweislich aus einer Empfehlung begonnenen Büchern. Dazu müssen immer Bewertungsabdeckung, Zahl der begonnenen Bücher, negative Urteile, Abbrüche und Ausschlussverletzungen stehen. Sonst kann ein System gut aussehen, das nur wenige ohnehin sichere Bücher empfiehlt oder dessen enttäuschte Leser keine Bewertung abgeben. Fehlende Bewertungen werden nicht als schlechte Bewertungen eingesetzt.

Die beiliegende Auswertung berechnet diese Größen pro Variante sowie den Mittelwert der Trefferanteile pro bewertender Person. Sie bewertet noch keinen Algorithmus: Dafür fehlen echte Beobachtungen und ein fairer Vergleich.

## 2. Psychologische Grundlage und Konsequenz

| Befund | Grenze der Evidenz | Konsequenz für Bookclub |
|---|---|---|
| Koopman (2015), Befragung von 343 Personen: Vorliebe für traurige Bücher hängt unter anderem mit Sinnsuche und dem Wunsch nach emotionalem Erleben zusammen. | Zusammenhang; keine geprüfte Empfehlungsregel. | Traurigkeit und düstere Atmosphäre sind Beschreibungen, keine Minuspunkte. Persönliches Gefallen separat lernen. |
| Cho et al. (2024), offene Befragung von 76 Personen: Verbindung, Sicherheit, Eskapismus und Bewältigung hängen mit Lesesituation und gewünschten Bucheigenschaften zusammen. | Qualitativ, besonders im Kontext pandemiebedingten Stresses; hier Abstract geprüft. | Dauerhafte Vorlieben von situativen Wünschen trennen. Aus Pausen weder Ablehnung noch psychischen Zustand ableiten. |
| Mikkonen & Vakkari (2019): 80 Personen suchten Romane; mehrere literarische Orientierungen waren je nach Suchaufgabe unterschiedlich relevant. | Interessantheitsurteile bei Katalogsuche, keine späteren Buchbewertungen. | Sprachliche, immersive und inhaltliche Anziehung getrennt abbilden. Keine festen Lesertypen daraus machen. |
| MINER (2022) modelliert mehrere Interessen für Nachrichtenempfehlungen. | Andere Domäne und andere Signale als Buchbewertungen. | Mehrere Geschmacksgruppen sind ein technischer Kandidat, kein belegter Vorteil für Bookclub. Gegen eine einfachere Nachbarschaftsmethode testen. |

Wir führen keine Persönlichkeitsdiagnostik ein. Die App soll Bücher verbinden, die jemand auf ähnliche Weise mag. Sie muss dafür nicht behaupten, jemand sei „der empathische Lesertyp“.

## 3. Welche Eigenschaften tragen einen Vergleich?

Ein Katalogmerkmal braucht `dimension`, `value_id`, `source`, `confidence`, `work_id`, gegebenenfalls `edition_id`. Für sicherheitsrelevante Ausschlüsse muss zusätzlich bekannt sein, ob die Dimension geprüft wurde: „nicht vorhanden“ und „nicht erfasst“ sind verschieden.

| Vergleichsdimension | Mögliche Buchmerkmale, nur soweit belegt | Bestehendes persönliches Signal |
|---|---|---|
| Spannung und Erzählbewegung | Tempo, Handlungsschwerpunkt, Spannungsaufbau | Handlung mochte/störte; Tempo zu langsam/passend/zu schnell |
| Figuren und Beziehungen | Figurenfokus, Perspektiven, Beziehungsthemen | Figuren mochte/störte |
| Sprache und Zugänglichkeit | sprachliche Gestaltung, Verständlichkeit, erzählerische Komplexität | Sprache mochte/störte; bei Sachbüchern Verständlichkeit |
| Atmosphäre und emotionaler Ton | z. B. bedrückend, hoffnungsvoll, humorvoll; keine Wertung | Atmosphäre mochte/störte |
| Thema und Erkenntnis | konkrete Themen; bei Sachbüchern Tiefe und Aufbereitung | Thema mochte/störte; Sachbuch-Tiefe |

Diese Dimensionen sind ein Entwurf zur Beschreibung von Büchern, keine validierte psychologische Skala. Genre, Autor, Länge und Sprache bleiben zusätzliche Katalogmerkmale. Genre und Thema werden getrennt gezählt; Synonyme dürfen keine künstlichen Mehrfachtreffer erzeugen. Autor allein soll keine Geschmacksgruppe erzeugen. Übersetzungsabhängige Sprache gehört zur Ausgabe.

**Entscheidende Zuordnung:** „Figuren mochte ich“ ist ein Urteil über dieses Buch. Erst mit einer belegten Beschreibung der Figuren lässt sich vorsichtig auf Kandidaten übertragen. Ohne diese Beschreibung bleiben Werkbezug und positives Aspekturteil erhalten; „moralisch ambivalente Figuren gefallen dir“ wäre erfunden. Ebenso bedeutet „Tempo passend“ ohne bekanntes Buchtempo noch keine Vorliebe für ruhiges Erzählen.

## 4. Clusterung: mehrere Gruppen innerhalb einer Person

Startpunkt ist der einzelne positiv bewertete Titel. Wir gruppieren **die bewerteten Bücher einer Person**, nicht Menschen nach Alter oder Geschlecht. Ein Buch kann mehreren Geschmacksnachbarschaften angehören.

Beispiel: Eine Person bewertet zwei ruhige, sprachlich geprägte Familienromane und zwei schnelle, handlungsgetriebene Thriller gut. Ein neuer Familienroman darf zur ersten Gruppe passen, ohne dass die schnelle Thriller-Vorliebe dagegenspricht. Ein mittelmäßig passender Durchschnitt aus beiden Gruppen erhält keinen Bonus.

Für die erste Implementierung werden zwei nachvollziehbare Verfahren gegenübergestellt:

1. **Einfache Vergleichsvariante:** Kandidaten anhand ihrer Ähnlichkeit zu einzelnen gut bewerteten Büchern ordnen. Noch keine expliziten Cluster.
2. **Cluster-Variante:** Aus denselben positiven Büchern mehrere, gegebenenfalls überlappende Nachbarschaften bilden. Kandidaten nach ihrer besten passenden Gruppe bewerten. Weitere Gruppenzugehörigkeiten nicht blind aufsummieren.

Für beide gelten identische Regeln:

- Keine feste Vorgabe „jeder Mensch hat fünf Geschmacksgruppen“. Bei wenig Evidenz bleiben einzelne Ankerbücher bestehen.
- Ähnlichkeit aus belegten gemeinsamen Eigenschaften berechnen. Fehlende Angaben gelten weder als Übereinstimmung noch als Widerspruch; die Abdeckung wird separat ausgewiesen. Ein zufälliger Treffer bei ansonsten fehlenden Daten darf keine starke Passung ergeben.
- Ausdrücklich positiv bewertete Aspekte stärker berücksichtigen als bloß vorhandene Buchmerkmale. Die Gesamtbewertung allein erlaubt nur schwachen Übertrag; das begrenzt falsche Zuschreibungen.
- Negative Aspekte zuerst am bewerteten Buch und an den tatsächlich beschriebenen Eigenschaften verankern. Ein einzelner langsamer Thriller darf die ruhigen Familienromane nicht automatisch abwerten. Ausdrückliche allgemeine Wünsche wie „ruhiges Tempo seltener“ wirken dagegen gruppenübergreifend.
- Ein Urteil pro Person und Werk; Bearbeitung ersetzt es. Mehrere ISBN, wiederholtes Anzeigen und mehrere Fragen erzeugen keine zusätzlichen unabhängigen Bewertungen.
- Ohne ausreichend Merkmale oder positive Anker keine scheinpräzise persönliche Passung. Dann nachvollziehbar auf einzelne bekannte Bücher oder freiwillige Auswahl zurückgreifen.

Gruppenzahl, Ähnlichkeitsschwelle, Mindestabdeckung und Gewichte werden erst an den Vergleichsfällen untersucht. Ein komplexeres Clustering wird nur übernommen, wenn es gegenüber der einfachen Methode erkennbar hilft.

## 5. Signalverarbeitung vor jeder Auswahl

1. Aktuelle Urteile je Werk laden; Informationen aus der Zukunft ausschließen.
2. Explizite Ausschlüsse prüfen, bereits gelesene/begonnene Werke und doppelte Ausgaben entfernen, soweit keine bewusste Wiederlesesuche vorliegt.
3. Kandidatenmerkmale einschließlich Herkunft und Lücken laden.
4. Passung zu den persönlichen Geschmacksgruppen ermitteln; begründete Ablehnungen und „seltener“ berücksichtigen.
5. Gezielt korrigierte Fehlannahmen aus eigenen Empfehlungen berücksichtigen. Ein eigener Empfehlungsfehler darf nicht zugleich mehrfach als Abbruch, schlechtes Gefallen und separater Fehler vervielfacht werden.
6. Bestgeeignete Kandidaten auswählen. Abwechslung unter gut passenden Kandidaten; keine starre Quote, die schlecht passende Bücher erzwingt.
7. Begründung aus tatsächlich verwendeten Merkmalen und passenden Ankerbüchern bilden. Auswahl, Datenstand und Version protokollieren.

Die Zwischenwerte sind Rangwerte, keine Wahrscheinlichkeiten für 4–5 Lichter. Eine Erfolgswahrscheinlichkeit darf erst nach Kalibrierung an zurückgehaltenen echten Urteilen erscheinen.

Die historische Sternformel im Abschnitt 3 der bestehenden Vorlage ist nicht mehr aktuell: Bei beschlossener Mitte 3 lautet eine einfache symmetrische Ausgangscodierung `(Lichter - 3) / 2`. Sie liefert −1, −0,5, 0, +0,5, +1. Auch das bleibt eine Modellentscheidung; die verbalen Stufen beweisen keine gleich großen Abstände. „Keine Bewertung“ bleibt `null`, nicht 0 oder drei Lichter.

## 6. Ein verbleibendes Problem der Datenbindung

Der aktuelle Prototyp speichert Ausschlüsse unter allgemeinen Texten wie `dieses Genre`, `dieses Thema`, `solche Länge`, `diesen Ton`. Das genügt für die Oberfläche, aber noch nicht für Empfehlungen.

Stattdessen muss die gespeicherte Handlung beispielsweise so aussehen:

```json
{
  "action": "never",
  "dimension": "content",
  "value_id": "graphic_violence",
  "source_work_id": "work-123",
  "scope": "global",
  "explicit": true
}
```

Bei mehreren Themen muss die Person erkennen und wählen können, welches gemeint ist. Kein stiller Ausschluss sämtlicher Themen eines geliebten Buchs. „Solche Länge“ braucht einen sichtbaren, definierten Bereich. Ein unbestimmter Abbruchgrund „Thema“ begründet keinen solchen allgemeinen Ausschluss.

Fehlt der betreffende Kandidatenwert, ist die Einhaltung eines harten Ausschlusses ungeklärt. Für den Start solche Kandidaten nicht in die als passend gefilterte Auswahl aufnehmen, bis die betreffende Dimension geprüft ist; bei zu wenig Auswahl die Lücke erklären. Unbekannt darf nicht als „enthält das nicht“ gelten. Der Ausschluss wird dadurch nicht still gelockert.

## 7. Die Fälle, die vor einer Leserprüfung bestehen müssen

| Fall | Erwartetes Verhalten |
|---|---|
| Zwei gut bewertete, unterschiedliche Lesewelten | Beide bleiben repräsentiert; keine erzwungene Durchschnittsvorliebe. |
| Ruhiger Roman 5, langsamer Thriller 1 mit konkreter Kritik | Keine automatische globale Ablehnung ruhigen Erzählens. |
| Düsteres Buch 5 | Düster nicht als negativ behandeln. |
| Buch 5, aber detaillierte Gewalt ausdrücklich ausgeschlossen | Ausschluss gewinnt auch gegen hohe Gesamtpassung. |
| Gewalt ausgeschlossen, Kandidatenangabe fehlt | Nicht als gewaltfrei empfehlen. |
| Abbruch 5 mit „keine Zeit“ | Positives Gefallen bleibt; kein automatischer Autorenmalus. |
| Pause ohne Urteil | Geschmacksprofil unverändert. |
| Figuren mochte, Figurenmerkmale fehlen | Keine erfundene Vorliebe für einen bestimmten Figurentyp. |
| Kandidat mit nur einem bekannten Merkmal | Geringe Abdeckung sichtbar; keine starke Erklärung. |
| Bewertung nachträglich geändert | Alte Evidenz ersetzt; Empfehlung neu berechnen. |
| Gleicher Titel, zwei ISBN | Ein Werk, keine doppelte Evidenz oder doppelte Empfehlung. |
| Eigenempfehlung scheitert an Tempo | Betroffene Tempoannahme korrigieren, nicht pauschal Autor und Themen. |

Diese Fälle prüfen Logik, nicht tatsächliches Gefallen. Für die Umsetzung sind sie Abnahmekriterien; sie wurden hier nicht als Algorithmustests ausgeführt.

## 8. Nachweisen, dass die Bücher anschließend gefallen

**Zuerst:** eine kleine reale, redaktionell beschriebene Titelauswahl mit unterschiedlichen Lesewelten. Merkmale vor Kenntnis der individuellen Bewertung erfassen; sonst verrät die Beschreibung schon das Ergebnis. Unterschiedliche beschreibende Personen an einer Teilmenge vergleichen. Kein auf perfekte synthetische Cluster zugeschnittener Katalog.

**Rückblickend:** Bewertungen je Person zeitlich trennen. Nur ältere Urteile zum Lernen verwenden, spätere zurückhalten. Popularität innerhalb desselben Kandidatenbestands, Genre/Autor, einzelne positive Nachbarn und die Cluster-Variante vergleichen. Fehlende Urteile nicht als negatives Training behandeln. Nicht bewertete Kandidaten sind keine bekannten Misserfolge; Offline-Rangmetriken über den bewerteten Teil nur entsprechend eingeschränkt interpretieren.

**Mit Lesern:** Erst Verständnis und Korrekturmöglichkeiten prüfen. Danach Varianten mit gleichem Katalog und vergleichbaren Bedingungen zuweisen, vorzugsweise pro Person, damit sich Profile nicht gegenseitig verändern. Angezeigte, begonnene und bewertete Bücher getrennt erfassen. Fehlende Antworten und Beobachtungsdauer ausweisen. Als erste Einstellung kann ein 60-Tage-Fenster dienen; das ist frei gewählt und muss für lange Bücher ergänzt werden.

**Entscheidung:** Clusterung nur beibehalten, wenn spätere Bewertungen im Vergleich zur einfacheren Methode besser ausfallen, ohne Ausschlüsse zu verletzen oder den Anteil bewerteter Bücher stark zu senken. Bei kleinen Fallzahlen keine Siegerbehauptung. Leserinteresse, Klicks und Vormerkungen ersetzen das spätere Gefallen nicht. Ein guter rückblickender Wert beweist noch keine Wirkung bei neuen Empfehlungen.

## Quellen

- Koopman (2015): [Why do we read sad books?](https://www.sciencedirect.com/science/article/pii/S0304422X15000534), Abstract und zugängliche Ausschnitte geprüft.
- Cho et al. (2024): [Reading When Stressed](https://www.journals.uchicago.edu/doi/abs/10.1086/730461), Abstract geprüft.
- Mikkonen & Vakkari (2019): [The role of readers’ literary preferences in predicting success in fiction search](https://doi.org/10.1108/JD-01-2019-0005), Verlagsauszug und Ergebnisabschnitte geprüft.
- Li et al. (2022): [MINER](https://aclanthology.org/2022.findings-acl.29/), Abstract geprüft; ausschließlich als technischer Vergleich, keine Buch-Evidenz.
- Shani & Gunawardana (2009): [Evaluating Recommender Systems](https://www.microsoft.com/en-us/research/publication/evaluating-recommender-systems/), Überblick zu Offline-Vergleichen, Nutzerversuchen und Online-Auswertung; keine Begründung unserer konkreten Schwellen.
