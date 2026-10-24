# Entscheidungen

Getrennt nach Herkunft, damit klar ist, was feststeht und was nur vorgeschlagen wurde.

## Von Arjen entschieden

| Datum | Entscheidung |
|---|---|
| 10.10.2026 | Kein lokaler Bücherverleih als Kern. Fokus: eigene Bibliothek mit eigener Bewertung und Erfassung. |
| 10.10.2026 | Profil ≠ Schaufenster. Das Profil enthält Bibliothek und Daten (privat), das Schaufenster wird komplett selbst freigegeben. |
| 10.10.2026 | Das Schaufenster ist eine eigene öffentliche Bibliothek: eigener Name, Ortsangabe freiwillig (Dorf, Stadt oder frei gewählt), weitere Angaben wie Lieblingskategorien möglich. |
| 10.10.2026 | Verleih und/oder Kauf finden im Schaufenster statt. |
| 10.10.2026 | Zielgruppe ausdrücklich auch Introvertierte: anonym oder pseudonym, Gleichgesinnte über Bücher finden. |
| 10.10.2026 | Später denkbar: Schaufenster veranstalten Events und Buchclubs. Wird gemeinsam entwickelt und bewertet. |
| 10.10.2026 | Reihenfolge: Schritt 1 Bibliothek (USP in der Buchpflege), Schritt 2 Schaufenster. |
| 10.10.2026 | Keine Umfrage. Der USP soll aus der Community selbst entstehen. |
| 10.10.2026 | Ziel: Bedarf wecken, gelesene Bücher in eigenen Worten zu beschreiben. Wer gut beschreibt, kann damit beliebt werden. |
| 10.10.2026 | Entdecken über drei Wege: Region (freiwilliger Standort, Suche im Umkreis von X km), Buchsuche (welche Schaufenster haben das Buch gelesen, bewertet, ausgestellt) und Kategorien. |
| 10.10.2026 | Erfassung per ISBN. Als Bild wahlweise Standardcover oder eigenes Foto. |
| 10.10.2026 | Bewertung ist das Kernelement der Bibliothek. Mehr als „gut / mittel / schlecht“: was war gut, Schreibstil, wie gut ließ es sich lesen (ohne Pausen usw.). Buch und Autor. |
| 10.10.2026 | Eigene Interpretationen und Worte zum Buch, wie in einer Buchhandlung. |
| 10.10.2026 | Arbeitsweise: Karpathy-Guidelines, Stand im Repo dokumentieren, regelmäßig zu GitHub pushen. Keine eigenständigen Entscheidungen ohne Abstimmung. |
| 10.10.2026 | Die App braucht eine klare Struktur statt direktem Einstieg in den Scan. Architektur gemäß [ARCHITEKTUR.md](ARCHITEKTUR.md) bestätigt: Startseite ist die Bibliothek, vier Hauptbereiche, „Ungelesen im Regal“ und „Wunschliste“ getrennt. Bereichsnamen bleiben vorerst Platzhalter. |
| 10.10.2026 | Designrichtung: malerisch, natürlich, introvertiert – keine 08/15-KI-Struktur. „Malerisch“ in zweifacher Bedeutung: gemalte Designs aus Buchwelten oder eine malerische Stimmung. |
| 10.10.2026 | Stilrichtung C „Vorsatzpapier und Buchrücken“ gewählt: marmoriertes Vorsatzpapier, Listen als Buchrücken in Leinen mit Goldprägung, „Neues Buch erfassen“ als Lücke im Regal. |
| 10.10.2026 | Es ist eine App: nutzerfreundlich beim Tippen, wenig Animation, damit nichts ruckelt. Ausformuliert in [ARCHITEKTUR.md](ARCHITEKTUR.md), Abschnitt „App-Grundsätze“. |
| 10.10.2026 | Design der Demos reicht vorerst. Vorrang hat, die richtigen Parameter zu finden. Genre muss enthalten sein. Statistiken gewünscht (z. B. gelesene Bücher, Anzahl Autoren, Lieblingsautor). Entwurf in [PARAMETER.md](PARAMETER.md). |
| 10.10.2026 | Genre-Liste mit 16 Einträgen bestätigt (siehe [PARAMETER.md](PARAMETER.md)). |
| 10.10.2026 | Lieblingsautor wird manuell festgelegt. Berechnet wird stattdessen der meistgelesene Autor. |
| 10.10.2026 | Statistiken: einige Zeilen kurze Zusammenfassung unter dem Regal, tiefere Statistiken in einem eigenen Band. Inhalt der Kurzfassung noch offen. Ersetzt den Grundsatz „keine Zähler auf der Startseite“. |
| 24.10.2026 | Statistik-Band heißt „Statistiken“. Inhalte: meistgelesene Autoren, meistgelesene Genres, bestbewertete Autoren, bestbewertete Genres, bestbewertete Bücher (Top 3). Ob Kurzfassung oder Band: noch offen. |
| 24.10.2026 | Aufbau (Am Lesen, Gelesen, Ungelesen …) und Hauptbereiche (Bibliothek, Schaufenster, Entdecken, Ich) passen. Das GUI ist zu kleinteilig und überfüllt, man kann sich leicht verklicken. Ein Design- und Usability-Experte soll hinzugezogen werden: optisch einfach, maximal benutzerfreundlich, Wärme eines Buchclubs, sympathische Elemente, einzigartig. |
| 24.10.2026 | Design-Experte: Impeccable (Open Source) als Designer, iOS-Plugin „Mobile App Design“ als Zweitprüfer. Erste Kritik: 19/40. **Volle Entscheidungshoheit über Gestaltung und Umfang der Überarbeitung liegt beim Designer-Team.** Wärme soll aus Material und Stimme kommen. Produktentscheidungen (Struktur, Parameter, Statistik-Inhalte) bleiben bestehen. |

## Vorschläge von Claude – noch nicht bestätigt

| Datum | Vorschlag | Status |
|---|---|---|
| 10.10.2026 | Drei Erfassungstiefen: 1 nur scannen und Lesestand, 2 Bewertung und Gedanken nach dem Lesen, 3 Sammler-Details zum Exemplar | offen |
| 10.10.2026 | Exemplar statt Titel erfassen (Ausgabe, Farbschnitt, signiert, Zustand, Standort zu Hause) | offen |
| 10.10.2026 | Bewertung trennt „Wie sehr hat es mich erreicht“ (Sterne, halbe Schritte) von beschreibenden Dimensionen: Lesefluss, Sprache, Tempo, Stärken/Schwächen, Nachhall, Wiederlesen | offen |
| 10.10.2026 | Autor nicht direkt bewerten, sondern „Mehr von dieser Autorin lesen?“ plus automatische Zusammenfassung auf einer Autorenseite | offen |
| 10.10.2026 | Abgebrochene Bücher bekommen keine Sterne, nur Seite und Grund | offen |
| 10.10.2026 | Gemeinsame feste Genre-Liste zusätzlich zu freien eigenen Regalen (nötig für die Kategoriesuche) | offen |
| 10.10.2026 | Umkreissuche über Ortsmittelpunkt oder PLZ mit gerundeten Entfernungen, damit sich kein Wohnort eingrenzen lässt | offen |
| 10.10.2026 | Beliebtheitssignal „hat mich zum Buch gebracht“ statt Likes und Followerzahlen | offen |
| 10.10.2026 | Datenmodell erlaubt mehrere Schaufenster pro Nutzer, Oberfläche im MVP nur eines | offen |
| 10.10.2026 | Deutsche Nationalbibliothek als Hauptquelle für Buchdaten, Google Books und Open Library ergänzend | offen |
| 10.10.2026 | Gestaltung als Karteikarte: Schreibmaschine für Fragen, Handschrift für Antworten, Stempel für den Lesestand | offen |
