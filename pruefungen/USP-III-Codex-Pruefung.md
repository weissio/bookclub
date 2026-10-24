# USP III – unabhängige Prüfung der Recherche und des Modells

24. Oktober 2026. Grundlage: vom Nutzer übergebene Datei `RECHERCHE-EMPFEHLUNG.md`, Stand 24.10.2026. Diese Prüfung ist ein Vorschlag zur Diskussion, keine beschlossene Änderung der Produktanforderungen. Das Bookclub-Repository wurde nicht verändert.

## Urteil

Die Recherche bietet eine brauchbare Grundlage für die Gestaltung eines kleinen Bewertungssystems. Sie trennt viele Praxisbeobachtungen sinnvoll von wissenschaftlichen Ergebnissen. Der vorgeschlagene Algorithmus sollte in dieser Form aber noch nicht implementiert werden: Er vermischt Buchbeschreibung, persönliches Gefallen, Abbruch und Unsicherheit. Außerdem normalisiert seine Formel die unterschiedlich gewichteten Rückmeldungen nicht konsistent.

Der Produktwunsch bleibt sinnvoll: Wenn ein Leser ein Buch aufgrund einer App-Empfehlung beginnt und anschließend eine Fehlpassung meldet, soll das System sichtbar und gezielt daraus lernen. Daraus folgt noch kein allgemein gültiger Multiplikator für sämtliche Eigenschaften des Buchs.

Prüfumfang: Das gesamte übergebene Dokument wurde gelesen. Die zentralen Schlussfolgerungen wurden gegen ausgewählte Originalquellen geprüft, insbesondere OCLC/ALISE, Netflix, Jellybooks, Schnabel et al., Chaney et al. und Li et al. Weitere Angaben wurden mit offiziellen StoryGraph- und DNB-Informationen sowie dem GroupLens-Autorenbeitrag abgeglichen. Dies ist keine vollständige Replikation und keine vollständige Einzelprüfung aller 34 Quellen.

## 1. Was die Belege tatsächlich tragen

### Appeal Factors: hilfreiches Gerüst, keine validierte Rangfolge für Buchleser

Der OCLC-Bericht hat 30 Teilnehmer, die über Universitätsverteiler und persönliche Netzwerke rekrutiert wurden. Untersucht wurden mehrere Medien. Stimmung, Schauplatz und Komplexität waren zudem bereits Schwerpunkte der Interviewfragen. Stimmung wurde besonders für Musik genannt; einige Teilnehmer konnten leichter unerwünschte Stimmungen benennen. Die Nennungshäufigkeiten belegen deshalb keine allgemeine Prioritätenliste für die Kriterien einer Buch-App. Auch „Nutzer können generell leichter sagen, was sie meiden“ wäre weitergehend als der berichtete Befund. Der Bericht wurde 2016 veröffentlicht; 2015 bezeichnet das Förderprojekt. [Originalbericht](https://www.oclc.org/content/dam/research/grants/reports/2015/lee2015.pdf)

Konsequenz: Stimmung, Thema, Figuren und Anspruch sind plausible Kandidaten. Welche davon für Bookclub zugleich verständlich, häufig beantwortet und vorhersagekräftig sind, muss noch geprüft werden.

### Einfachere Rückmeldungen: plausibel, aber keine garantierte Ausfüllquote

Netflix berichtet aus eigenen Tests eine Steigerung der Bewertungsaktivität um 200 Prozent beim Wechsel zu Daumen. Der Bericht thematisiert auch Missverständnisse über die Bedeutung von Sternen. Er isoliert daher nicht lediglich die Anzahl der Antwortoptionen und beweist keine optimale Zahl von Bookclub-Fragen. [Netflix, 2017](https://about.netflix.com/en/news/goodbye-stars-hello-thumbs)

Die Book-Riot-Aussage zur Nutzung von Ja/Nein-Fragen ist eine journalistische Beobachtung, keine veröffentlichte Ausfüllstatistik. Die Formulierung „je einfacher, desto mehr Antworten“ sollte als Designhypothese und nicht als universelles Gesetz stehen bleiben.

### Früher Abbruch: die 10-Prozent-Regel ist nicht belegt

Jellybooks beschreibt Abschlussraten in seinem Testleseverfahren und betrachtet Leser, die tatsächlich Lesedaten übermitteln. Das ist keine allgemeine Quote für gekaufte Bücher oder bewusst erklärte Abbrüche. Aus der Häufigkeit früher Ausstiege folgt weder eine Schwelle bei zehn Prozent noch der Faktor 0,7. Ein früher Abbruch kann eine sehr eindeutige Stil- oder Inhaltsablehnung enthalten. [Jellybooks: Completion Rate](https://www.jellybooks.de/about/jellybooks-radar/completion-rate?locale=en)

Konsequenz: Gelesenen Anteil speichern. Wie viel er über eine bestimmte Eigenschaft aussagen kann, getrennt betrachten: Über den Einstieg und den früh erlebten Stil kann ein Urteil informiert sein; über das Ende oder die gesamte Figurenentwicklung nicht.

### Eigene Empfehlungen: Auswahlverzerrung ist kein pauschales Verbot stärkerer Korrektur

Schnabel et al. behandeln verzerrte Beobachtungswahrscheinlichkeiten. Die inverse Gewichtung hängt davon ab, mit welcher Wahrscheinlichkeit eine Bewertung beobachtet wird; sie lautet nicht allgemein „eigene Empfehlungen geringer gewichten“. Daraus folgt weder ein generelles Verbot noch eine Bestätigung von 1,5/2. [Recommendations as Treatments](https://arxiv.org/html/1602.05352)

Chaney et al. demonstrieren mögliche Rückkopplungsprobleme anhand von Simulationen. Das stützt die Notwendigkeit, die vom System selbst beeinflusste Auswahl zu berücksichtigen; es ist kein direkter Wirksamkeitsnachweis für Bookclub. [Originalarbeit](https://arxiv.org/abs/1710.11214)

Li et al. untersuchen einen Nachrichten-Bandit mit Klickfeedback. Die Ergebnisse begründen keinen festen Anteil von 20 Prozent Erkundung und keine stärkere Gewichtung von Buchabbrüchen. [Originalarbeit](https://arxiv.org/pdf/1003.0146)

## 2. Die wichtigsten Probleme im vorgeschlagenen Modell

### A. „Das Buch ist ruhig“ bedeutet nicht „Ich mag ruhige Bücher“

Die Kriterien 2 bis 5 beschreiben vor allem das Buch. Selbst eine positive Gesamtbewertung verrät nicht eindeutig, welche seiner Eigenschaften gefallen haben. Ein Leser kann einen ruhigen Roman trotz seines Tempos lieben – wegen der Figuren. Ein anderer bricht einen ruhigen Roman wegen der Sprache ab, ohne langsames Erzählen abzulehnen.

Für den Anfang darf Gesamtgefallen schwache Hinweise auf vorhandene Buchmerkmale liefern. Eine ausdrücklich benannte Stärke oder Schwäche ist aber spezifischer und sollte gezielter wirken. Nicht jede Eigenschaft eines geliebten Buchs wird automatisch zur Vorliebe, nicht jede Eigenschaft eines abgebrochenen Buchs zum Ausschluss.

### B. Abbruch ist kein universelles negatives Gesamturteil

Im Vorschlag wird das Signal eines bewerteten abgebrochenen Buchs auf höchstens −0,2 begrenzt. Ein Abbruch mit fünf Sternen wird dadurch dennoch negativ. Das widerspricht einer getrennten Erfassung von persönlicher Wirkung und Leseausgang.

Beispiel: Ein Buch hat die Person stark erreicht, ist ihr emotional aber zu belastend zum Weiterlesen. Die Wirkung darf positiv bleiben; der Wunsch nach weniger belastenden Inhalten wird zusätzlich erfasst. Beides muss nicht in eine einzige negative Zahl gepresst werden.

Ohne Bewertung oder Grund bleibt ein Abbruch zunächst ein Hinweis auf Nichtfortsetzung dieses Titels. Eine starke Verallgemeinerung auf Autor, Genre oder Tempo ist dann unsicher. Der Nutzerwunsch nach starker Korrektur bei eigenen Fehlvorschlägen lässt sich separat erfüllen.

### C. Die Normalisierung berücksichtigt Gewichte nur im Zähler

Die vorgeschlagene Formel lautet:

`Merkmalspräferenz = Σ(Gewicht × Signal) / (Anzahl + 3)`

Bei zehn empfohlenen Büchern mit Signal +1 und Gewicht 1,5 ergibt das 15/13 = 1,154. Obwohl die Einzelsignale im Bereich bis +1 liegen, verlässt das Ergebnis diesen Bereich. Mit vielen negativen, doppelt gewichteten Signalen ist dasselbe auf der negativen Seite möglich. Es ist damit keine auf diesen Bereich begrenzte, gedämpfte Mittelung.

Eine konsistente mögliche Alternative mit neutralem Prior ist:

`Merkmalspräferenz = Σ(wᵢ × yᵢ) / (λ + Σwᵢ)`

Dabei gelten nur tatsächlich informative Beobachtungen für dieses Merkmal. `yᵢ` bezeichnet die Richtung und Stärke der Evidenz, `wᵢ` deren begrenztes Gewicht einschließlich Zuverlässigkeit; `λ` ist eine noch zu prüfende Dämpfung. Das ist ein mathematisch konsistenter Entwurf, kein validierter Empfehlungsalgorithmus. Die Herkunft der Gewichte und die Abbildung von Sternen auf Signale müssen weiterhin definiert werden. Eine unbeantwortete Frage ist keine Nullbewertung.

### D. Abbruchgründe dürfen nicht mechanisch ganze Autoren verurteilen

„Stil/Sprache“ kann Werk, Übersetzung oder Autor betreffen. „Nicht mein Genre“ bei einem Mischgenre identifiziert nicht automatisch das unerwünschte Teilgenre. „Zu schwer“ kann Themenwissen, Erzählstruktur oder aktuelle Lebenssituation betreffen.

Vorschlag: Explizit benannte Gründe zuerst dem konkreten Titel und der betroffenen Eigenschaft zuordnen. Eine Verallgemeinerung auf den Autor wächst vorsichtig über mehrere Werke und wird durch „Mehr von dieser Person?“ ergänzt. Eine direkte Antwort „Nein“ ist dafür aussagekräftiger als ein pauschaler Stil-Rückschluss.

### E. Lesedauer ist kein verlässlicher Ersatz für Gefallen

Bei gedruckten Büchern erfasst die App nur eingetragene Daten. Kalendertage zwischen Beginn und Ende enthalten Arbeit, Krankheit, parallel gelesene Bücher und vergessene Einträge. „Seiten pro Tag“ ist deshalb zunächst eine Kalenderkennzahl, nicht tatsächliche Lesegeschwindigkeit oder Begeisterung.

Vorschlag: Pause und langsame Fertigstellung im MVP nicht als negatives Geschmackssignal verwenden. Explizites Wiederlesen kann ein separates positives Indiz sein, ersetzt aber ebenfalls kein Urteil.

## 3. Prüfung der sieben Kriterien

| Vorgeschlagen | Empfehlung | Begründung |
|---|---|---|
| Hat mich erreicht | Behalten | Persönliches Gesamturteil; gleiche Bedeutung bei gelesen und abgebrochen. Keine automatische Überschreibung durch Status. |
| Getragen von: genau eins aus vier | Ändern | Schwerpunkt des Buchs und das, was der Person gefallen hat, sind verschieden. „Genau eins“ erzwingt häufig falsche Eindeutigkeit. Für Sachbücher passen Handlung und Figuren oft nicht. |
| Tempo | Optional behalten | Neutrale Buchbeschreibung; „zu langsam“ ist eine andere Aussage als „ruhig“. |
| Stimmung | Optional behalten, Vokabular trennen | „Düster“ beschreibt die Buchstimmung; „enttäuscht“ das persönliche Urteil. Die vorhandene Gefühlsliste ist kein unveränderter Ersatz. |
| Anspruch | Optional behalten | Verständlich benennen, nicht als objektives Qualitätsurteil. Beim Abbruch nur für den gelesenen Teil. |
| Mehr von dieser Autorin? | Optional behalten | Direktes Autorensignal mit „weiß nicht“ beziehungsweise Überspringen. |
| Nichts mehr davon? | Kontextbezogen neu formulieren | „Was möchtest du künftig seltener?“ mit konkretem Merkmal. Keine unklare pauschale Ablehnung und kein automatisches dauerhaftes Verbot. |

Die bestehende differenzierte Bewertung ist außerdem Teil von USP I und II. Sie allein für eine kleinere Algorithmuseingabe zu streichen, würde einen anderen Produktnutzen beschneiden. Zunächst hinter „Genauer beschreiben“ weiter anbieten und Doppelungen entfernen.

## 4. Vorschlag für eine schlanke erste Bewertungsansicht

Nicht sieben Fragen gleichzeitig zeigen. Zuerst zwei kurze, freiwillige Bereiche:

1. **„Hat mich erreicht“** – vorhandene Bewertung mit klar erklärter Bedeutung.
2. **„Was hat für dich funktioniert – oder nicht?“** – wenige Aspekte, nach Auswahl eindeutig als „mochte ich“ oder „störte mich“ markierbar. Keine versteckte Umschaltung durch wiederholtes Tippen. Zunächst beispielsweise Sprache, Figuren, Handlung, Atmosphäre und Thema; bei Sachbüchern passende Begriffe statt einer erzwungenen Romanstruktur. Eine kleine Auswahlgrenze wäre zu testen, nicht als wissenschaftlich begründete Zahl zu behaupten.

„Genauer beschreiben“ öffnet zusätzliche freiwillige Angaben: Tempo, Stimmung, Anspruch und „Mehr von dieser Person?“. Die persönliche Lesart bleibt daneben als eigener freier Text erhalten.

Bei **Abbruch** erscheinen die bereits bestätigten Abbruchgründe anstelle einer doppelten Frage nach Schwächen. Entsprechende Merkmale werden im Hintergrund gleich kodiert. „Tempo“ kann auf Wunsch zu „zu langsam/zu schnell“ präzisiert werden. Der Nutzer muss eine Information nicht zweimal eingeben. Ein Merkmal wie „Figuren“ allein beschreibt zunächst nur den betroffenen Aspekt, keine präzise generalisierbare Vorliebe.

Bei einer **nachvollziehbar übernommenen App-Empfehlung** kann zusätzlich ein freiwilliger Ein-Tipp-Hinweis erscheinen: „Hat die Empfehlung zu dir gepasst?“ mit „Ja“, „Teilweise“, „Nein“. Bei „Nein“ werden vorhandene Gründe genutzt; kein zweiter Fragebogen. Falls selbst dieser Zusatz zu viel ist, sollte er testweise entfallen. Die Passung einer Empfehlung ist dennoch getrennt von Buchqualität und Leseausgang zu modellieren.

## 5. Empfohlene Rückkopplung: zwei getrennte Lernaufgaben

### Geschmack verstehen

Lernt aus ausdrücklichem Gesamturteil, konkreten Stärken/Schwächen, Autorenvorliebe und verfügbaren Buchmerkmalen. Hier bleibt die Verallgemeinerung vorsichtig, fehlende Angaben werden nicht als Ablehnung gelesen, widersprüchliche Signale bleiben möglich.

### Eigene Empfehlungsannahmen korrigieren

Die App speichert Empfehlung, Zeitpunkt, Modellversion, gezeigte Begründungen und den späteren Verlauf. Sie unterscheidet:

- angezeigt;
- vorgemerkt;
- begonnen;
- laut Nutzer aufgrund dieser Empfehlung begonnen;
- gelesen, pausiert oder abgebrochen;
- ausdrücklich als passend oder unpassend bewertet.

Ein Klick oder ein Lesestart nach einer Anzeige beweist die Ursache nicht. Eine freiwillige Bestätigung beim Beginnen kann die Zuordnung verbessern. Mehrere Anzeigen derselben Empfehlung werden nicht als mehrere unabhängige Urteile gezählt.

Wird eine klar als passend ausgesprochene Empfehlung übernommen und mit einer relevanten negativen Begründung abgebrochen, darf die App ihre damalige Annahme stärker, aber begrenzt korrigieren. Das erfüllt den gewünschten Schwerpunkt, ohne alle Buchmerkmale doppelt negativ zu zählen.

Beispiel: Empfohlen wurde „wegen der ruhigen, atmosphärischen Erzählweise“. Der Leser meldet „zu langsam“. Dann ist die Annahme über gewünschtes Tempo zu prüfen. Meldet er „inhaltlich unangenehm“, steht zunächst eine andere Eigenschaft im Mittelpunkt. Dieselbe persönliche Reaktion sollte den Titel trotzdem aus unmittelbaren Wiederholungsempfehlungen entfernen.

Faktor 1,5/2 bleibt eine mögliche Testkonfiguration, nicht der feststehende Standard. Vergleich gegen Gewicht 1, gegen gezielte Korrektur nur relevanter Eigenschaften und gegen getrennte Empfehlungsrückmeldung. Exploration bedeutet passende, abwechslungsreiche Alternativen; sie muss ausdrücklich genannte Ausschlüsse respektieren. Eine klare negative Rückmeldung wird bei „zum Ausprobieren“ nicht ignoriert.

## 6. Der größte noch offene Engpass: Merkmale unbekannter Bücher

Selbst perfekte Nutzerbewertungen ermöglichen keinen Vergleich nach Stimmung oder Tempo, wenn Kandidaten diese Merkmale nicht besitzen. DNB-Inhaltserschließung beschreibt Themen über Schlagwörter, Sachgruppen und weitere Klassifikationen. Daraus entsteht nicht automatisch ein verlässlicher Katalog von Stimmung, Erzähltempo oder Anspruch. [DNB: Inhaltserschließung](https://blog.dnb.de/literatur-unter-der-lupe-3/)

Jedes Kandidatenmerkmal braucht daher eine Herkunft und einen Unsicherheitsstatus: redaktionell geprüft, strukturierte öffentliche Nutzerangabe, bibliografische Quelle oder geschätztes Merkmal. Fehlend bleibt fehlend. Eine Schätzung aus Klappentexten darf nicht als gesicherte Leseeigenschaft ausgegeben werden.

Für einen prüfbaren Anfang empfehle ich einen überschaubaren Kandidatenkatalog mit nachvollziehbaren Merkmalen. Nutzer müssen nicht für jedes Buch einen vollständigen Merkmalsdatensatz liefern. Die Empfehlungen verwenden zunächst nur die belegbar vorhandenen Dimensionen und benennen ihre Grenzen.

Private Daten anderer Personen und veröffentlichte Schaufensterinhalte sind getrennte Quellen. Inhaltsbasierte Personalisierung kann öffentliche Katalogdaten verwenden. Kollaborative Verfahren und die Frage, ob lokal oder auf einem Server gerechnet wird, sind unterschiedliche Architekturentscheidungen.

## 7. Antworten auf die sechs Entscheidungsfragen

1. **Sieben Kriterien?** Als Kandidatenpool brauchbar; als immer sichtbarer Fragebogen nicht übernehmen. Zwei freiwillige Einstiegsbereiche, weitere Angaben auf Wunsch. Buchmerkmale und persönliches Urteil sauber trennen.
2. **Faktor 1,5/2?** Nicht beschließen, bevor Attribution, Merkmalszuordnung und konsistente Normalisierung geklärt sind. Als begrenzte Testvariante möglich. Explorative Bücher liefern ebenfalls verwertbares Feedback, aber ein erwarteter Erkundungsfehlschlag ist kein gleich großer Fehler einer sicheren Passungsaussage.
3. **Herkunft der Merkmale?** Bibliografische Daten für das, was sie tatsächlich liefern; gezielte redaktionelle Ergänzung für einen Anfangskatalog; später strukturierte öffentliche Angaben mit Herkunft und Unsicherheit. DNB-Schlagwörter nicht mit Stimmung und Tempo gleichsetzen.
4. **Fremde Schaufenster?** Öffentliche strukturierte Angaben können den Katalog bereichern. Die eigenen Urteile bleiben individuell. Lokale Berechnung und fremde Merkmalsdaten schließen sich nicht aus. Noch keine pauschale Nutzung privater Daten unterstellen.
5. **Pause?** Im MVP geschmacksneutral. Explizit genannter aktueller Kontext darf kurzfristig helfen, wird aber nicht stillschweigend zur dauerhaften Abneigung.
6. **Alternde Bewertungen?** Zunächst keine automatische Entwertung allein nach Alter. Neue Bewertungen und Wiederlesen ergänzen oder korrigieren das Profil. Ein späterer Zeitfaktor sollte gegen eine Variante ohne Verfall getestet werden.

## 8. Woran ein erster Versuch gemessen werden sollte

Zwei Fragen getrennt testen:

- **Nutzerfreundlichkeit:** Welche Bereiche werden beantwortet oder übersprungen? Wie lange dauert die Eingabe? Werden Buchbeschreibung, Gefallen und Abbruch verstanden? Sind die Antworten später noch nachvollziehbar?
- **Empfehlungsqualität:** Werden Vorschläge tatsächlich übernommen? Wie werden sie anschließend beurteilt? Welche begründeten Fehlpassungen wiederholen sich? Bleiben die Vorschläge abwechslungsreich?

Mit zunächst getrennten Testfällen prüfen: positiver Abbruch, früher klar begründeter Abbruch, Pause wegen Zeitmangel, widersprüchliche Bücher desselben Autors, fehlende Bewertungen, fehlende Kandidatenmerkmale und wiederholte Anzeige derselben Empfehlung. Ein abgeschlossener Titel ist nicht automatisch ein Erfolg, ein Abbruch nicht automatisch eine schlechte Empfehlung.

Die Kriterien müssen ihren zusätzlichen Nutzen gegenüber einem einfachen Ausgangsmodell zeigen. Eingabeaufwand allein und Klickrate allein reichen als Erfolgskriterium nicht aus. Bei späteren Auswertungen muss die Beeinflussung der Titelauswahl durch die eigenen Empfehlungen berücksichtigt werden.

## Nächster fachlicher Abstimmungspunkt für Claude

Bitte eine überarbeitete Entscheidungsvorlage erstellen, die (a) Beobachtung, Buchbeschreibung, persönliches Urteil und Empfehlungsfehler trennt, (b) eine konsistente gedämpfte Aggregation erklärt, (c) auf die unbelegte 10-Prozent-Regel verzichtet und (d) für jedes Kandidatenmerkmal eine tatsächlich verfügbare Datenquelle benennt. Zahlen für Gewichte, Auswahlgrenzen und Exploration bleiben klar als zu testende Entwurfswerte markiert. Noch keine dieser Empfehlungen als vom Nutzer beschlossen in das Entscheidungsprotokoll übernehmen.
