# Entscheidungsvorlage USP III: Empfehlungen aus eigenen Urteilen

_Stand 24.10.2026, 2. Fassung nach Zweitprüfung ([pruefungen/USP-III-Codex-Zweitpruefung.md](pruefungen/USP-III-Codex-Zweitpruefung.md)). Entwurf zur Abstimmung mit Arjen. Die Punkte in Abschnitt 7 sind in Abschnitt 8 entschieden._

Grundlagen:
- [USP.md](USP.md)
- [RECHERCHE-EMPFEHLUNG.md](RECHERCHE-EMPFEHLUNG.md)
- unabhängige Prüfung: [pruefungen/USP-III-Codex-Pruefung.md](pruefungen/USP-III-Codex-Pruefung.md)

Alle Zahlen in dieser Vorlage sind **zu testende Entwurfswerte** und nicht belegt.

## Was sich gegenüber der ersten Recherche ändert

Die Prüfung hat recht, in diesen Punkten war mein erster Vorschlag falsch oder zu weitgehend:

1. **Die OCLC-Studie trägt keine Rangfolge.** Sie hatte 30 Teilnehmer und untersuchte mehrere Medien. Stimmung wurde vor allem für Musik genannt. Ob Stimmung, Thema, Figuren und Anspruch für Buchleser verständlich, häufig beantwortet und aussagekräftig sind, müssen wir selbst prüfen.
2. **Die 10-%-Regel für frühe Abbrüche entfällt.** Weder Schwelle noch Faktor waren belegt. Neu wird der gelesene Anteil gespeichert und je Merkmal bewertet (siehe Ebene 1).
3. **Ein Abbruch mit 5 Sternen wurde zwangsläufig negativ.** Das war falsch. „Hat mich erreicht“ und „nicht zu Ende gelesen“ werden jetzt getrennt erfasst.
4. **Die Formel war nicht konsistent.** Die Gewichte standen nur im Zähler, dadurch konnte das Ergebnis den Wertebereich verlassen. Korrigiert in Abschnitt 3.
5. **Eigene Empfehlungen geringer gewichten ist kein Gebot der Forschung.** Schnabel et al. verlangen, dass man die verzerrte Auswahl berücksichtigt, keinen pauschalen Abschlag. Deine stärkere Rückkopplung bleibt möglich, aber gezielt (siehe Ebene 4).

## 1. Vier Ebenen, die getrennt gespeichert werden

| Ebene | Was | Beispiele | Wer liefert es |
|---|---|---|---|
| **1. Beobachtung** | was passiert ist, ohne Wertung | Status (gelesen, pausiert, abgebrochen), Beginn und Ende, gelesener Anteil, Abbruchseite, Wiederlesen, Herkunft (App-Empfehlung, Schaufenster, selbst) | App, aus Einträgen |
| **2. Buchbeschreibung** | wie das Buch ist, unabhängig vom eigenen Gefallen | Genre, Thema, Länge, Tempo, Stimmung des Buchs (z. B. „düster“), Anspruch | Katalogdaten, optional der Leser (siehe Abschnitt 5) |
| **3. Persönliches Urteil** | was es *mir* bedeutet hat | Hat mich erreicht, was mochte ich, was hat mich gestört, Mehr von dieser Person, Was möchte ich künftig seltener | nur der Leser, alles optional |
| **4. Empfehlungsfeedback** | ob die Annahme der App stimmte | Hat die Empfehlung gepasst: Ja, Teilweise, Nein, plus vorhandene Gründe | nur bei App-Empfehlungen, optional |

Regeln:
- **Eine fehlende Angabe ist keine Bewertung.** Eine unbeantwortete Frage zählt nicht als „neutral“ und nicht als „negativ“. „Keine Belege“ wird getrennt von einer ausdrücklich neutralen Antwort gespeichert, die Zahl der Belege je Merkmal steht immer dabei.
- **Ein Buch ist eine Beobachtung.** Gesamturteil, „Mehr von dieser Person“ und Abbruchgrund zum selben Werk werden je Merkmal zu einer begrenzten Evidenz zusammengeführt. Wer eine Antwort ändert, ersetzt sie und erzeugt keine zusätzliche Beobachtung.
- **„Das Buch ist ruhig“ (Ebene 2) heißt nicht „ich mag ruhige Bücher“ (Ebene 3).** Eine Vorliebe entsteht stark nur aus einer ausdrücklichen Angabe („Tempo: mochte ich“ oder „zu langsam“). Aus der Gesamtbewertung allein entsteht höchstens ein schwacher Hinweis auf die vorhandenen Merkmale.
- **Gelesener Anteil:** Ein früher Abbruch sagt etwas über Einstieg, Stil und Sprache, aber nichts über Ende oder Figurenentwicklung. Merkmale, die man erst später im Buch beurteilen kann, bekommen aus frühen Abbrüchen kein Signal. Welche Merkmale das sind, wird festgelegt, eine Prozentschwelle gibt es nicht.
- **Pause ist geschmacksneutral.** Ein angegebener Grund wie „Gerade nicht die Stimmung“ wirkt höchstens kurzfristig.
- **Lesedauer ist kein Geschmackssignal.** Bei gedruckten Büchern gibt es nur Kalendertage, keine tatsächliche Lesezeit.

## 2. Bewertungsansicht (Vorschlag für den Prototyp)

Sichtbar sind nur zwei freiwillige Bereiche:
1. **Hat mich erreicht:** vorhandene Bewertung, für gelesene und abgebrochene Bücher gleich.
2. **Was hat für dich funktioniert, was nicht?** Wenige Aspekte, jeweils eindeutig als „mochte ich“ oder „störte mich“ markiert, ohne verstecktes Umschalten durch mehrfaches Tippen.
   - Romane: Sprache, Figuren, Handlung, Atmosphäre, Thema
   - Sachbücher: passende eigene Begriffe (z. B. Verständlichkeit, Tiefe, Thema)

**Genauer beschreiben** (aufklappbar, freiwillig):
- Tempo des Buchs (ruhig, ausgewogen, rasant) und für mich (zu langsam, passend, zu schnell)
- Stimmung des Buchs, getrennt von meiner Reaktion
- Anspruch
- Mehr von dieser Person?
- Was möchtest du künftig seltener?

Die eigene Lesart (Freitext) bleibt daneben. Die bisherige ausführliche Karte bleibt als „Genauer beschreiben“ erhalten. Sie dient auch USP I und USP II und wird nicht für den Algorithmus gestrichen. Doppelungen werden entfernt.

**Beim Abbruch** erscheinen die bestätigten Abbruchgründe statt einer zweiten Schwächen-Frage. Im Hintergrund werden sie auf dieselben Aspekte abgebildet. Nichts wird doppelt abgefragt.

| Abbruchgrund | wirkt auf |
|---|---|
| Stil/Sprache | Sprache (dieses Werk; Übersetzung möglich) |
| Tempo | Tempo, optional präzisiert: zu langsam oder zu schnell |
| Thema | Thema |
| Figuren | Figuren |
| Zu lang | Länge |
| Zu schwer | Anspruch |
| Nicht mein Genre | Genre (bei Mischgenres unsicher) |
| Inhaltlich unangenehm | ohne Angabe nur dieser Titel (wird nicht wieder empfohlen). Nur mit konkreter Angabe, etwa „detaillierte Gewaltdarstellung“, wirkt es auf dieses Merkmal, soweit es bei Kandidaten bekannt ist |
| Erwartung nicht erfüllt | möglicher Hinweis auf eine unpassende Empfehlung, aber kein Beweis, denn Erwartungen entstehen auch durch Cover, Klappentext oder fremde Tipps. Zuordnung nur über das Passungsfeedback (Ebene 4) |
| Anderes | kein Merkmal |

**Bei einem Buch, das über eine App-Empfehlung kam:** freiwillig ein Tipp „Hat die Empfehlung gepasst?“ mit Ja, Teilweise oder Nein. Bei „Nein“ werden die vorhandenen Gründe genutzt, es gibt keinen zweiten Fragebogen. Ob dieser Zusatz bleibt, entscheidet ein Test.

## 3. Gedämpfte Zusammenfassung (konsistent)

Für jedes Merkmal *f* (z. B. „Tempo ruhig“, „Autor XY“, „Thema Meer“):

```
Vorliebe(f) = Σ (wᵢ · yᵢ) / (λ + Σ wᵢ)
```

- Gezählt werden nur Beobachtungen, die **für dieses Merkmal tatsächlich etwas aussagen**.
- **yᵢ** ist die Richtung und Stärke, zwischen −1 und +1.
  - ausdrücklich „mochte ich“: +1
  - „störte mich“ oder ein passender Abbruchgrund: −1
  - nur die Gesamtbewertung, auf die vorhandenen Merkmale des Buchs übertragen: schwach, z. B. (Lichter − 3) / 2 × 0,3 (aktualisiert, siehe Nachtrag 3)
- **wᵢ** ist das begrenzte Gewicht: Zuverlässigkeit der Angabe × Herkunftsfaktor, gedeckelt.
- **λ** ist die Dämpfung, ein neutraler Startwert, z. B. 3.
- Bedingungen: wᵢ ≥ 0, λ > 0, |yᵢ| ≤ 1. Bei keinerlei Belegen ergibt die Formel 0. Diese 0 bedeutet „keine Belege“ und wird in der Oberfläche nie als neutrale Meinung gezeigt.
- **Lichter-Skala (aktualisiert):** Es gibt 1 bis 5 Lichter mit der Mitte 3 („okay“). Kodiert wird mit (Lichter − 3) / 2, das ergibt −1, −0,5, 0, +0,5 und +1. Das ist eine Modellentscheidung; die Wortstufen beweisen keine gleich großen Abstände. „Keine Bewertung“ ist `null`, nicht 0 und nicht drei Lichter.

Eigenschaften:
- Weil alle |yᵢ| ≤ 1 sind, bleibt die Vorliebe immer zwischen −1 und +1, auch bei vielen stark gewichteten Beobachtungen.
- Wenige Beobachtungen bleiben nah bei 0. Ein einzelner Abbruch kippt keinen Autor.
- Die Werte sind **keine Wahrscheinlichkeiten**. Eine Grenze für „passt eher nicht“ ist noch nicht kalibriert.

**Dein Autorenbeispiel, präzisiert.** Welche Evidenz das Merkmal „Autor XY“ verändert:
- **Ausdrücklich:** 5 Werke mit „Mehr von XY: Nein“ (je y = −1, w = 1) ergeben −5 / (3 + 5) = **−0,63**, ein deutliches Autorensignal.
- **Nur Abbrüche, ohne Gründe und ohne Autorenantwort:** Jeder Abbruch zählt als schwacher, ausdrücklich als Modellannahme markierter Übertrag auf den Autor (Entwurf: w = 0,3). Das ergibt −1,5 / (3 + 1,5) = **−0,33**. Wiederholte Fehlpassungen werden also ernst genommen, aber nicht als fünf starke Ablehnungen gezählt.
- **Abbrüche mit Gründen:** Sie wirken zuerst auf das genannte Merkmal (Tempo, Thema …). Nur „Stil/Sprache“ über mehrere Werke darf vorsichtig auf den Autor übertragen werden, denn eine Übersetzung kann die Ursache sein.
- **Positive Urteile zählen mit:** Ein Werk von XY mit 5 Sternen und „Mehr von XY: Ja“ (y = +1, w = 1,5) zieht den ersten Fall auf −3,5 / 9,5 = **−0,37**.

## 4. Empfehlungsfehler getrennt lernen (deine stärkere Rückkopplung)

Für jede Empfehlung wird gespeichert: wann angezeigt, mit welchen Begründungen, in welcher Version, und was danach geschah (vorgemerkt, begonnen, laut Nutzer wegen dieser Empfehlung begonnen, gelesen, pausiert oder abgebrochen, Passung Ja/Teilweise/Nein). Mehrere Anzeigen derselben Empfehlung zählen nicht als mehrere Urteile. Dass ein Buch nach einer Anzeige begonnen wurde, beweist noch nicht, dass die Empfehlung der Grund war. Deshalb gibt es beim Beginnen eine freiwillige Bestätigung.

**Was korrigiert wird:** die Annahme, mit der die App das Buch begründet hat.
- Beispiel: Die App empfiehlt „wegen der ruhigen, atmosphärischen Erzählweise“, und der Leser bricht mit „Tempo: zu langsam“ ab. Dann bekommt die Tempo-Annahme eine **stärkere, gedeckelte** Korrektur.
- Bricht er dagegen mit „inhaltlich unangenehm“ ab, wird das Tempo nicht belastet. Der **Titel** wird nicht wieder empfohlen, außer man nimmt ihn bewusst wieder auf. Ohne Angabe, was gestört hat, wird nichts auf andere Bücher übertragen.
- **„Seltener“ und „Nicht empfehlen“ sind zwei verschiedene Handlungen.** „Seltener“ senkt die Priorität eines Merkmals. „Nicht empfehlen“ ist ein ausdrücklich gesetzter Ausschluss.

**Testvarianten für die Stärke** (nichts davon beschlossen):

| Variante | Regel |
|---|---|
| A | Gewicht 1 wie jede andere Rückmeldung |
| B | ×1,5 bei gelesen, ×2 bei Abbruch, aber nur auf die Merkmale, mit denen die Empfehlung begründet war |
| C | Ein getrennter Fehlerspeicher korrigiert die betroffene Annahme direkt in der Bewertung der Kandidaten, also in der Auswahl selbst und nicht nur in den Erklärungstexten. Das gilt auch für Merkmale, die nicht als Grund angezeigt wurden. Die sichtbare Erklärung wird danach aus den tatsächlich verwendeten Auswahlfaktoren abgeleitet. |

A, B und C sind Modellvarianten, nicht drei Regeln, die pro Nutzer gleichzeitig wechseln. Vor einer Auswertung werden gemeinsame Ausgangsdaten, Zielgrößen und Zeitraum festgelegt. Solange es keine Nutzer gibt, wird mit erfundenen Widerspruchsfällen und kleinen Bedienversuchen geprüft. Ein statistischer Sieger wird daraus nicht behauptet.

**Ausprobieren (Exploration):**
- Ein Teil der Empfehlungen bietet bewusst Abwechslung und ist als „zum Ausprobieren“ markiert. Der Anteil ist ein Testwert, die 20 % aus der ersten Recherche sind nicht belegt.
- Ausdrückliche „seltener“-Wünsche werden auch hier respektiert.
- Ein klares Nein bei einem solchen Buch wird nicht ignoriert. Es gilt aber nicht als gleich großer Fehler wie bei einer sicheren Empfehlung.

## 5. Woher die Merkmale fremder Bücher kommen (größter Engpass)

Damit die App ein Buch empfehlen kann, das der Leser noch nicht kennt, braucht dieses Buch selbst Merkmale. Jedes Merkmal bekommt eine **Herkunft** und einen **Status**: redaktionell geprüft, bibliografisch, Leserangaben (mit Anzahl), geschätzt oder fehlt. Fehlt bleibt fehlt. Eine Schätzung aus dem Klappentext wird nie als gesicherte Eigenschaft gezeigt.

| Merkmal | tatsächlich verfügbare Quelle | Belastbarkeit |
|---|---|---|
| Autor, Titel, Sprache, Übersetzung, Erscheinungsjahr | DNB (SRU, frei), Google Books | hoch |
| Länge | Seitenzahl aus DNB oder Google Books (`pageCount`) | gut, hängt aber von der Ausgabe ab und kann fehlen |
| Genre (eigene 16) | Zuordnung aus DNB-Sachgruppe und Google `categories`, mit Prüfung | mittel. Die Zuordnung zu unseren 16 Genres ist eine eigene Verarbeitung, die geprüft werden muss |
| Thema, Ort, Zeit, Personen | DNB-Inhaltserschließung (GND-Schlagwörter, Sachgruppen); Open Library Work-Felder `subjects`, `subject_places`, `subject_times`, `subject_people` | mittel. Die Felder können fehlen. Ein Ortsbezug ist ein Thema, nicht unbedingt der Schauplatz. Sie beschreiben Inhalte, nicht das Leseerlebnis. Abdeckung deutscher Titel zuerst an echten Zielgruppentiteln prüfen |
| Klappentext | Google Books `description` | nur als Quelle für eine markierte Schätzung |
| **Tempo, Stimmung, Anspruch** | **keine freie, verlässliche Quelle gefunden** | siehe unten |

Zu Tempo, Stimmung und Anspruch:
- **StoryGraph** hat diese Daten, aber keine öffentliche Schnittstelle. Eine Anfrage steht dort seit März 2021 auf „Long-term“.
- **Hardcover** hat eine Schnittstelle im Beta-Status mit Einschränkungen für die Nutzung von Daten anderer Nutzer. Meine Abfrage vom 24.10. gab eine Zusammenfassung der Seite zurück, kein wörtliches Zitat, und darin ausdrücklich auch „Vibes“. Die Zweitprüfung konnte diese Formulierung auf der Seite nicht bestätigen. Stand: **für unsere geplante Nutzung derzeit nicht gesichert.** Vor jeder Nutzung muss die konkrete Passage mit Datum belegt werden.
- **DNB-Schlagwörter** beschreiben Themen, aber nicht Tempo oder Stimmung.

**Folge für den Start:**
1. Empfehlungen beruhen zuerst auf dem, was belastbar vorliegt: Autor, Genre, Thema, Länge, Sprache sowie die eigenen Urteile mit ihren ausdrücklichen Vorlieben.
2. Tempo, Stimmung und Anspruch gibt es für fremde Bücher nur dort, wo sie vorliegen: aus einem kleinen redaktionell gepflegten Startkatalog oder später aus strukturierten Angaben anderer Leser in Bookclub. Eine Mindestzahl (Entwurf: 5) ist nur eine vorläufige Freigaberegel. Zusätzlich zählen die Anzahl unabhängiger Personen und die Übereinstimmung: Fünf gleiche Tempoangaben sagen mehr als fünf verschiedene. Subjektive Merkmale werden weder durch eine Mehrheit noch durch Redaktion objektiv.
   Open Library: für neue Anbindungen die Search- sowie Work- und Edition-Endpunkte nutzen (die allgemeine Books API gilt als Legacy). Werk und Ausgabe getrennt behandeln, denn die ISBN bezeichnet die Ausgabe.
3. Jede Empfehlung nennt kurz ihre tatsächlichen Gründe. Datenlücken sind kompakt markiert und auf Antippen einsehbar, statt als lange Warnliste unter jeder Empfehlung zu stehen. Die App behauptet nichts über ein unbekanntes Merkmal.

Datenschutz: Die eigenen Urteile bleiben persönlich. Ob öffentliche Schaufenster-Angaben Buchmerkmale ergänzen dürfen, ist eine eigene Entscheidung (siehe Abschnitt 7, Frage 4). Ob lokal oder auf einem Server gerechnet wird, ist wieder eine andere.

## 6. Zu testende Entwurfswerte

| Wert | Entwurf | Prüfen gegen |
|---|---|---|
| Dämpfung λ | 3 | 1 und 5 |
| Schwacher Übertrag der Gesamtbewertung auf Buchmerkmale | × 0,3 | 0 (gar nicht) |
| Gewicht für ausdrückliche Antwort zum Autor | 1,5 | 1 |
| Rückkopplung auf eigene Empfehlungen | Varianten A, B, C | untereinander |
| Anteil „zum Ausprobieren“ | offen | 0 % und niedrige Werte |
| Mindestzahl Leserangaben für ein Merkmal | 5 | 3 und 10 |

Gemessen werden zwei Dinge getrennt:
- **Nutzerfreundlichkeit:** Was wird beantwortet, was übersprungen, wie lange dauert es, wird es verstanden?
- **Empfehlungsqualität:** Wird übernommen? Wie wird danach geurteilt? Wiederholen sich Fehlpassungen? Bleibt es abwechslungsreich?

Testfälle:
- positiver Abbruch
- früher, klar begründeter Abbruch
- Pause wegen Zeitmangel
- widersprüchliche Bücher derselben Person
- fehlende Bewertungen
- fehlende Merkmale beim Kandidaten
- dieselbe Empfehlung mehrfach angezeigt

## 7. Zu entscheiden (Arjen)

1. **Bewertungsansicht:** Sichtbar sind nur „Hat mich erreicht“ und „Was hat funktioniert, was nicht“, alles Weitere unter „Genauer beschreiben“. Passt das?
2. **Rückkopplung:** Testen wir A, B und C gegeneinander, statt jetzt 1,5/2 festzulegen?
3. **Merkmalsquellen:** Start mit belastbaren Katalogdaten und einem kleinen redaktionell gepflegten Startkatalog für Tempo, Stimmung und Anspruch, dazu später Angaben anderer Leser?
4. **Schaufenster-Daten:** Dürfen öffentliche, strukturierte Angaben aus Schaufenstern Buchmerkmale ergänzen (nicht persönliche Urteile)?
5. **Herkunft beim Lesebeginn:** Wird ein Buch direkt aus einer Empfehlung heraus begonnen, wird nur dieser Weg festgehalten. Das zeigt den Weg, nicht den Beweggrund, und lässt sich korrigieren. Nachgefragt wird nur, wenn eine Empfehlung tatsächlich infrage kommt, freiwillig und nicht bei jedem Lesestart.
6. **Erklärung:** Soll jede Empfehlung ihre tatsächlichen Gründe kurz zeigen, Datenlücken auf Antippen und „stimmt nicht“ zur Korrektur?
7. **Bedeutung der Sterne:** Stehen die Sterne („Hat mich erreicht“) für die persönliche Wirkung oder für Gefallen? Und wie hängen sie mit „Mehr davon“ zusammen? Daraus folgt, welcher Sternwert als Nullpunkt gilt.
8. **„Seltener“ vs. „Nicht empfehlen“:** Bieten wir beide getrennt an?

## Quellen (zusätzlich zu den in der Recherche genannten)

- [StoryGraph Roadmap: „An API“ (Status Long-term, seit 2021)](https://roadmap.thestorygraph.com/features/posts/an-api)
- [Hardcover: Getting Started with the API (Beta, Nutzungsbedingungen)](https://docs.hardcover.app/api/getting-started)
- [Google Books API: Volume-Referenz](https://developers.google.com/books/docs/v1/reference/volumes)
- [Open Library: Work-Schema](https://openlibrary.org/type/work) · [Books API (Legacy)](https://openlibrary.org/dev/docs/api/books) · [Search API](https://openlibrary.org/dev/docs/api/search)
- [DNB: Inhaltserschließung](https://blog.dnb.de/literatur-unter-der-lupe-3/)
- [Schnabel et al.: Recommendations as Treatments](https://arxiv.org/html/1602.05352)

## 8. Entscheidungen (Claude, im Auftrag von Arjen, 24.10.2026)

Arjen hat diese fachlichen Grundlagen an Claude delegiert. Alle Gewichte bleiben Testwerte.

1. **Bewertungsansicht:** Zwei freiwillige Bereiche:
   - „Wie hat es dir gefallen?“ (Sterne)
   - „Was hat funktioniert, was hat gestört?“

   Die eigene Lesart bleibt daneben. Alles Weitere steht unter „Genauer beschreiben“. Beim Abbruch ersetzen die Abbruchgründe die Frage nach dem Gestörten.
2. **Rückkopplung:** Start mit Variante C, also Korrektur der betroffenen Annahme in der Auswahl. A dient als Vergleich, B bleibt eine Testvariante. Kein Multiplikator ist festgelegt.
3. **Merkmalsquellen:** Katalogdaten (DNB, Google Books, Open Library) plus ein kleiner redaktionell gepflegter Startkatalog für Tempo, Stimmung und Anspruch. Leserangaben kommen später dazu, mit Anzahl und Übereinstimmung. Hardcover und StoryGraph sind nicht eingeplant.
4. **Schaufenster:** Öffentliche, strukturierte Buchbeschreibungen dürfen den Katalog ergänzen. Private Urteile bleiben getrennt. Die Nutzer bekommen das verständlich erklärt.
5. **Herkunft:** Wird ein Buch direkt aus einer Empfehlung begonnen, hält die App den Weg fest. Das ist korrigierbar. Nachgefragt wird nur im Zusammenhang und freiwillig.
6. **Erklärung:** Jede Empfehlung zeigt die tatsächlichen Gründe kurz, Datenlücken auf Antippen und „stimmt nicht“.
7. **Bedeutung der Sterne:** Die Sterne beantworten „**Wie hat dir das Buch gefallen?**“.
   - *Begründung:* Empfehlungen sollen vorhersagen, was gefällt. Ein Buch kann stark aufwühlen und trotzdem nicht gefallen, deshalb ist „Hat mich erreicht“ als Maßstab mehrdeutig.
   - Wirkung und Deutung haben ihren Platz in der eigenen Lesart.
   - „Mehr von dieser Person?“ bleibt eine eigene Frage.
   - Neutraler Punkt ist vorerst 3 Sterne („okay“). Das ist ein Testwert.
   - *Folge:* Die Bezeichnung „Hat mich erreicht“ im Prototyp wird ersetzt.
8. **„Seltener“ und „Nicht empfehlen“** werden getrennt angeboten. „Seltener“ senkt die Priorität, „Nicht empfehlen“ schließt aus.

**Nächster Schritt:** Eine konkrete Bewertungsansicht im Prototyp, durchgespielt an einem gelesenen und einem abgebrochenen Beispielbuch. Dabei zeigt sich, welche Angaben leichtfallen und welche unnötig sind.

### Nachtrag nach dem Durchspielen (Claude, 24.10.2026)

Der Designer hat die Bewertungsansicht im Prototyp an drei Büchern durchgespielt. Gefallen und Aspekte dauern etwa 10 Sekunden. Tempo, Stimmung und Anspruch des Buchs wirkten dabei unnötig. Daraus folgen drei Entscheidungen:

1. **„Mehr von dieser Person?“ wird sichtbar.** Die Frage steht klein unter dem Gefallen und ist mit einem Tipp beantwortet. Sie ist das direkteste Autorensignal und gehört deshalb nicht in den zugeklappten Bereich.
2. **„Seltener“ erscheint nur bei einer Bewertung von höchstens 2 Lichtern und beim Abbruch.** Bei Büchern, die gefallen haben, war die Frage überflüssig.
3. **Tempo, Stimmung und Anspruch des Buchs fallen aus der persönlichen Bewertung heraus.** Sie beschreiben das Buch und nicht das eigene Urteil. Deshalb gehören sie in den Katalog (Startkatalog, später öffentliche Beschreibungen aus dem Schaufenster). „Tempo für mich“ (zu langsam, passend, zu schnell) bleibt unter „Genauer beschreiben“, ebenso beim Abbruchgrund „Tempo“.

### Nachtrag 2 (Claude, 24.10.2026, nach externer Prüfung des Prototyps)

1. **Lichter-Stufen:** 1 „gar nicht“, 2 „eher nicht“, 3 „okay“, 4 „gut“, 5 „sehr gut“.
2. **„Nicht empfehlen“ wird ergänzt.** Es steht neben „Seltener“ als eigene, ausdrückliche Handlung und schließt das gewählte Merkmal aus. „Seltener“ senkt nur die Priorität.
3. **„Seltener“ und „Nicht empfehlen“ sind immer erreichbar.** Bei 1–2 Lichtern und beim Abbruch sind sie hervorgehoben. In allen anderen Fällen stehen sie unter „Genauer beschreiben“. Ein Buch kann gefallen, und trotzdem möchte man zum Beispiel Gewalt künftig seltener.
4. **Keine versteckt gespeicherten Angaben.** Eine Angabe wird nur gespeichert, wenn sie beim Speichern sichtbar ist. Abhängige Angaben werden mit ihrer Bedingung gelöscht: Wer den Abbruchgrund „Tempo“ abwählt, löscht auch „zu langsam/zu schnell“. Angaben bleiben sichtbar, wo sie liegen; „Genauer beschreiben“ zeigt beim Zuklappen die Zahl der Angaben.
5. **Grenzen:** Die 10 Sekunden stammen aus einem internen Durchspielen. Ob echte Leser die Fragen schnell und einheitlich verstehen, muss ein Test zeigen. Dass der Empfehlungsalgorithmus funktioniert, ist damit nicht nachgewiesen.

### Nachtrag 3 (Claude, 24.10.2026): Clusterung als Arbeitsgrundlage

[usp3/CLUSTERUNG.md](usp3/CLUSTERUNG.md) (ausgearbeitet von Codex) wird Arbeitsgrundlage für die Umsetzung:
- **Mehrere Geschmacksgruppen innerhalb einer Person.** Wer ruhige Familienromane und schnelle Thriller mag, bekommt kein verwischtes Durchschnittsprofil. Ein Kandidat wird nach seiner besten passenden Gruppe bewertet.
- **Vergleich zweier Verfahren:** einfache Nachbarschaft zu einzelnen gut bewerteten Büchern gegen Clusterung. Die Clusterung wird nur übernommen, wenn danach besser bewertete Bücher folgen, ohne Ausschlüsse zu verletzen und ohne dass weniger bewertet wird.
- **Zielgröße:** Anteil mit 4–5 Lichtern unter bewerteten, aus einer Empfehlung begonnenen Büchern. Daneben wird immer angegeben, wie viele Bücher überhaupt bewertet wurden, wie viele Urteile negativ waren, wie viele Abbrüche es gab und wie oft ein Ausschluss verletzt wurde.
- **„Düster“ und „traurig“ sind Beschreibungen, keine Minuspunkte** (Koopman 2015).
- **Nur belegte Verbindungen:** „Figuren mochte ich“ ohne beschriebene Figurenmerkmale erzeugt keine Vorliebe für einen Figurentyp.
- **Die 12 Abnahmefälle** aus Abschnitt 7 der Clusterung gelten für die Umsetzung.
- **Ausschlüsse an eindeutige Merkmale binden.** Gespeichert wird `{action, dimension, value_id, source_work_id, scope, explicit}` statt eines Textes wie „dieses Thema“. Die Person wählt sichtbar, welches Thema gemeint ist; „solche Länge“ bekommt einen sichtbaren Bereich. Fehlt bei einem Kandidaten der Wert zu einem harten Ausschluss, wird er nicht als passend empfohlen, denn „unbekannt“ heißt nicht „enthält das nicht“.

Die ausführbare Qualitätsauswertung (`auswertung.py`) liegt noch nicht im Repository, weil sie nicht mitgeschickt wurde.

### Nachtrag 4 (Claude, 24.10.2026)

- **Wortlaut der Aspekt-Knöpfe:** „gefiel mir“ und „gefiel mir nicht“ statt „mochte ich“ und „störte mich“. Arjen hatte „störte mich“ als unsauber empfunden. Der frühere Wortlaut war eine Gestaltungswahl und kein Studienergebnis. Belegt ist nur die Struktur: eine ausdrückliche positive oder negative Aussage je Aspekt, leer bedeutet „keine Aussage“. Es gibt keinen dritten Knopf „neutral“, weil das leere Feld diese Rolle bereits erfüllt.
- **„Künftig weniger davon?“** ist auch beim Abbruch und bei 1–2 Lichtern zugeklappt und als Zeile hervorgehoben. Der Grund: Der Bogen muss kurz bleiben.
- **Prüfen im Lesertest:** ob Leser die Knöpfe einheitlich verstehen.
