# USP III – Zweitprüfung der Entscheidungsvorlage

Stand: 24. Oktober 2026. Geprüfte Vorlage: lokales `ENTSCHEIDUNGSVORLAGE-USP3.md`. Empfehlungen dieser Prüfung sind unbeschlossen. Das Repository wurde nicht verändert.

## Gesamturteil

Die vier Ebenen, die Behandlung fehlender Werte und die Trennung von Gesamturteil und Abbruch beheben die zentralen Probleme der ersten Fassung. Als Grundlage zur Entscheidung ist die Vorlage deutlich besser. Vor einer algorithmischen Umsetzung bleiben einige semantische Regeln und die Datenqualität zu präzisieren. Kein weiteres vollständiges Neuschreiben der Recherche ist erforderlich.

## 1. Formel: korrekt, Interpretation noch offen

`Σ(wᵢ · yᵢ) / (λ + Σwᵢ)` bleibt im Bereich −1 bis +1, wenn `wᵢ ≥ 0`, `λ ≥ 0`, `|yᵢ| ≤ 1` und der Nenner positiv ist. Ein strikt positives λ stellt auch bei fehlenden Beobachtungen einen definierten Wert sicher. Dieser rechnerische Startwert darf in der Oberfläche dennoch nicht mit einer ausdrücklich neutralen Meinung verwechselt werden: Evidenzmenge separat speichern.

Die angegebenen Beispiele sind rechnerisch korrekt: −5/8 = −0,625 und −3,5/9,5 ≈ −0,368. Diese Werte sind keine Wahrscheinlichkeiten und kein Nachweis einer bereits kalibrierten Grenze für „passt eher nicht“.

Der schwache Sternübertrag setzt weiterhin 2,5 als rechnerischen Nullpunkt. Bei einer Skala von 0,5 bis 5 ist das nicht der geometrische Mittelpunkt. Das macht die Formel nicht falsch, erfordert aber eine bewusste Festlegung, welche Bewertung welche Bedeutung hat. Auch als Testmodell muss eindeutig sein, ob Sterne persönliche Wirkung oder Gefallen ausdrücken und wie beides mit „mehr davon“ zusammenhängt.

Mehrere Antworten zum selben Buch sind keine voneinander unabhängigen Bücher. Gesamturteil, „Mehr von dieser Person“ und ein Abbruchgrund dürfen zu einer begrenzten Evidenz je Werk und Merkmal zusammengeführt werden. Erneutes Bearbeiten ersetzt die bisherige Antwort; es erzeugt keine zusätzliche Beobachtung.

## 2. Autorenbeispiel passt noch nicht zur eigenen Zuordnungsregel

Die Tabelle ordnet Gründe gezielt Tempo, Thema, Sprache oder Länge zu. Das Rechenbeispiel gibt dagegen fünf Abbrüchen bei Autor XY jeweils −1 auf den Autor, ohne Gründe oder ausdrückliche Autorenablehnung anzugeben.

Das muss präzisiert werden:

- Fünf ausdrückliche Antworten „Mehr von XY: Nein“ dürfen ein deutlich negatives Autorensignal bilden.
- Wiederholte, konsistent werkbezogene Ablehnungen können vorsichtiger auf den Autor übertragen werden, wenn diese Verallgemeinerung als Modellannahme ausgewiesen ist.
- Fünf Abbrüche allein ergeben nicht automatisch fünf starke Autorenablehnungen. Die vorhandenen positiven Wirkungsurteile und Gründe bleiben relevant.

Das ursprüngliche Nutzerziel, wiederholte Fehlpassungen bei einem Autor ernst zu nehmen, bleibt bestehen. Zu klären ist die Evidenz, die genau dieses Autorenmerkmal verändert, und wie wiederholte Abbrüche mit positiven Urteilen zusammengeführt werden.

## 3. Unbekannte unangenehme Inhalte nicht auf ähnliche Bücher übertragen

Abschnitt 2 sagt zutreffend: Bei „inhaltlich unangenehm“ ohne konkrete Angabe nur diesen Titel berücksichtigen. Abschnitt 4 erklärt anschließend pauschal, der Titel und ähnliche Inhalte fielen aus den nächsten Empfehlungen.

Konsistente Regel:

- Den abgebrochenen Titel nicht wiederholt empfehlen, sofern keine bewusste Wiederaufnahme erfolgt.
- Ohne bekanntes störendes Merkmal keine dauerhafte Inhaltsablehnung auf andere Bücher übertragen.
- Bei konkreter Angabe wie „detaillierte Gewaltdarstellung“ kann dieses Merkmal berücksichtigt werden, soweit es bei Kandidaten bekannt ist.
- „Seltener“ senkt eine Priorität; „Nicht empfehlen“ ist ein ausdrücklich gesetzter Ausschluss. Diese beiden Bedienhandlungen nicht gleich behandeln.

Ebenso ist „Erwartung nicht erfüllt“ ein mögliches Empfehlungsproblem, aber kein automatischer Nachweis einer falschen Algorithmusannahme. Erwartungen können auch aus Cover, Klappentext oder externen Empfehlungen stammen. Das separate Passungsfeedback hilft bei der Zuordnung.

## 4. Variante C muss Empfehlungen verändern, nicht bloß Formulierungen

„Fehlerspeicher je Begründung, der künftige Begründungen abschwächt“ ist mehrdeutig. Falls nur Erklärungstexte seltener erscheinen, bleibt die Auswahl unverändert und der Fehler wird lediglich anders beschrieben.

Vorschlag: C korrigiert die betroffene Annahme in der Kandidatenbewertung. Die sichtbare Erklärung wird anschließend aus den tatsächlich verwendeten Auswahlfaktoren abgeleitet. Auch nicht angezeigte Modellmerkmale können relevante Fehlannahmen enthalten; eine Verbesserung darf sich nicht auf die zwei sichtbaren Gründe beschränken.

A/B/C sind zunächst unterschiedliche Modellvarianten, nicht drei gleichzeitig wechselnde Regeln pro Nutzer. Vor einer belastbaren Auswertung gemeinsame Ausgangsdaten, klare Zielgrößen und den zeitlichen Verlauf festlegen. Solange es noch keine Nutzerbasis gibt, zuerst synthetische Widerspruchsfälle und kleine qualitative Bedienversuche; daraus keinen statistischen Gewinner behaupten.

## 5. Open Library: die offene Feldfrage ist beantwortet

Die offizielle Dokumentation und das Work-Schema enthalten:

| Inhalt | Work-Feld | Hinweis |
|---|---|---|
| Themen | `subjects` | Freie beziehungsweise importierte Sachangaben; nicht ausschließlich Genre |
| Inhaltliche Ortsbezüge | `subject_places` | Nicht mit dem Erscheinungsort verwechseln |
| Inhaltliche Zeitbezüge | `subject_times` | Nicht mit Erscheinungsjahr verwechseln |
| Personenbezüge | `subject_people` | Nicht automatisch eine vollständige Figurenliste |

Die Felder können fehlen. Ein Ortsbezug kann ein Thema des Buches statt des einzigen Handlungsschauplatzes sein. Eine Felddefinition belegt daher Verfügbarkeit im Schema, keine vollständige Abdeckung deutscher Romane und keine geprüfte Richtigkeit jedes Werts.

Für die neue Integration empfiehlt Open Library Search beziehungsweise Work-/Edition-Endpunkte. Die generische Books API dokumentiert die genannten Felder ebenfalls, ist inzwischen aber als Legacy gekennzeichnet. Werksinformationen und Ausgabeninformationen getrennt behandeln; die ISBN identifiziert die Ausgabe.

Quellen: [Work-Schema](https://openlibrary.org/type/work), [API-Dokumentation](https://openlibrary.org/dev/docs/api/books), [Search API](https://openlibrary.org/dev/docs/api/search).

## 6. Datenquellen: drei Präzisierungen

### Katalogdaten sind eine Ausgangsbasis, keine Vollständigkeitsgarantie

Autor, Titel und Sprache lassen sich grundsätzlich bibliografisch beziehen. Seitenzahl hängt von der Ausgabe ab und kann fehlen. Thema, Ort und Zeit sind nicht für jeden Titel gleichermaßen erschlossen. Die Zuordnung aus Katalogkategorien zu den eigenen 16 Genres bleibt eine eigene, zu prüfende Verarbeitung.

Die offizielle Google-Books-Referenz dokumentiert unter anderem `authors`, `language`, `pageCount`, `categories` und `description`. Sie dokumentiert damit keine lückenlose oder fehlerfreie Verfügbarkeit dieser Eigenschaften. Die Quellenliste sollte die aktuelle API-Referenz statt einer alten Ruby-Client-Dokumentation verwenden. [Google Books: Volume](https://developers.google.com/books/docs/v1/reference/volumes)

### Fünf Leserangaben sind keine automatische Wahrheit

Eine Mindestzahl kann eine vorläufige Freigaberegel sein. Zusätzlich Anzahl unabhängiger Personen und Verteilung berücksichtigen: Fünf sehr unterschiedliche Tempoantworten sind etwas anderes als fünf übereinstimmende. Aggregierte Buchbeschreibung nicht mit individueller Vorliebe verwechseln. Weder eine Mehrheit noch redaktionelle Pflege machen subjektive Merkmale vollkommen objektiv.

### Hardcover: konkrete Verbotsformulierung noch belegen

Die in dieser Prüfung zugängliche Getting-Started-Dokumentation bestätigt Beta-Status und Einschränkungen für die Nutzung fremder Nutzerdaten. Die konkrete Formulierung „kommerziellen Produkten sind Vibes ausdrücklich verboten“ konnte auf der geprüften Seite nicht bestätigt werden. Daraus folgt keine Erlaubnis für Bookclub; die Einschränkungen sind weiterhin ernst zu nehmen. Für eine eindeutige Behauptung in der Vorlage jedoch die konkrete Passage mit Version beziehungsweise Datum nachtragen oder die Aussage auf „für unsere geplante Nutzung derzeit nicht gesichert“ begrenzen. [Hardcover API-Dokumentation](https://docs.hardcover.app/api/getting-started/)

StoryGraphs API-Anfrage steht auf der geprüften offiziellen Roadmap weiterhin auf „Long-term“. Die Quelle trägt damit, StoryGraph derzeit nicht als gesicherte öffentliche Integrationsquelle einzuplanen. [Roadmap](https://roadmap.thestorygraph.com/features/posts/an-api)

## 7. Empfehlungen für die sechs Entscheidungen – weiterhin unbeschlossen

1. **Bewertungsansicht:** Zwei freiwillige Einstiegsbereiche plus persönliche Lesart; Details auf Nachfrage. Aspekt allein ist noch keine präzise Vorliebe: „Figuren störten mich“ liefert weniger Vergleichsinformation als beispielsweise „zu viele wechselnde Perspektiven“. Nicht sofort zusätzliche Pflichtfragen daraus machen.
2. **Rückkopplung:** A/B/C als überprüfbare Alternativen beibehalten, C inhaltlich präzisieren. Kein Multiplikator wird als bereits bewährt bezeichnet.
3. **Merkmalsquellen:** Katalogdaten plus kleiner geprüfter Startkatalog; Open Library kann Themen sowie Orts- und Zeitbezüge ergänzen. Abdeckung und Normalisierung zuerst an echten Zielgruppentiteln prüfen.
4. **Schaufenster:** Öffentliche strukturierte Buchbeschreibungen als mögliche Ergänzung. Eine private Bewertung wird nicht deshalb zur öffentlichen Buchbeschreibung, weil sie dasselbe Werk betrifft. Nutzung für den gemeinsamen Katalog verständlich getrennt von der sichtbaren Schaufensterauswahl erklären.
5. **Nachfrage beim Lesebeginn:** Nur kontextuell, wenn eine App-Empfehlung tatsächlich infrage kommt. Startet die Person direkt aus der Empfehlung, Herkunft protokollieren und eine Korrektur ermöglichen; das ist eine beobachtete Route, kein Beweis für Motivation. Die ausdrückliche Bestätigung bleibt freiwillig und nur eine weitere Herkunftsangabe.
6. **Erklärung:** Tatsächliche Gründe kurz anzeigen und Korrektur anbieten. Eine kompakte Datenlückenanzeige mit aufrufbaren Details ist nutzerfreundlicher als ein langer Warnkatalog unter jeder Empfehlung. Nicht behaupten, wie schnell oder sicher ein unbekanntes Merkmal sei.

## Ergebnis für die weitere Abstimmung

Die Grundstruktur ist geeignet, um die sechs Produktentscheidungen mit dem Nutzer zu besprechen. Vor Implementierung sind insbesondere Autorenbeispiel, Verallgemeinerung unangenehmer Inhalte, Bedeutung von Variante C und Herkunft der Daten zu bereinigen. Es sind keine neuen generischen Fragebögen und keine weitere pauschale Kriterienliste nötig.
