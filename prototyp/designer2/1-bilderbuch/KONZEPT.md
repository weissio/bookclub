# Bilderbuch-Illustration als Oberfläche – Runde 2

Designschule: Erzählende Illustration, die zugleich Bedienung ist. Jedes Bild ist ein Einstieg, jedes Ding tut etwas, der Humor ist leise. Beide Konzepte sind Tagesbilder (Licht an war Nacht), mit dicker, gleichmäßiger Tuschelinie und flachen Farben wie bei Mitgutsch und Berner. Es gibt keine Pendelleuchte und keine aufgeschlagenen Bücher als Hauptmotiv.

## Vorbilder (beide Konzepte)

| Vorbild | URL | Was ich daraus nehme |
|---|---|---|
| Ali Mitgutsch, Wimmelbücher | https://en.wikipedia.org/wiki/Ali_Mitgutsch | Der Querschnitt durch Häuser und Orte, bei dem jedes Zimmer eine eigene kleine Geschichte hat. Ich nehme davon nur wenige große Zimmer statt Gewimmel. |
| Rotraut Susanne Berner, Wimmelbücher (Gerstenberg) | https://perlentaucher.de/buch/rotraut-susanne-berner/winter-wimmelbuch.html | Gleich dicke Konturen, flache Farben ohne Verlauf und ein Ort, den man immer wieder betritt |
| Jon Klassen, „I Want My Hat Back“ | https://www.penguinrandomhouse.com/books/214488/i-want-my-hat-back-by-jon-klassen/ | Trockener Humor über ein Detail, etwa den kleinen Hut auf einem wartenden Buch. Die Figuren haben Punktaugen und wenig Mimik. |
| Oliver Jeffers, „Stuck“ | https://www.penguinrandomhouse.com/books/310267/stuck-by-oliver-jeffers-illustrated-by-oliver-jeffers | Dinge an unerwarteten Orten, zum Beispiel Bücher als Früchte im Baum oder als Drachenschwanz. Die Logik ist absurd, aber freundlich. |
| Wolf Erlbruch, „Ente, Tod und Tulpe“ | https://en.wikipedia.org/wiki/Duck,_Death_and_the_Tulip | Ein schweres Thema wird sanft erzählt, hier das Abbrechen. Viel Leerraum um wenige Dinge. |
| Beatrice Alemagna, „The Wonderful Fluffy Little Squishy“ | https://enchantedlion.com/all-books/the-wonderful-fluffy-little-squishy | Kräftige Farbe als Wärme, die nicht kitschig wird |

---

## Konzept A: Das Bücherhaus

**Idee:** Die Bibliothek ist ein Haus im Querschnitt, und jeder Band ist ein Zimmer, in dem Bücher etwas tun. Gelesene stehen in der Stube, ungelesene sitzen im Wartezimmer auf der Bank, abgebrochene schlafen sich im Bett aus, und Wunschbücher fliegen mit Papierflügeln zum Dachboden. Oben im Hausflur liegen die offenen Bücher als ruhige Zeilen, jede mit ihrem Knopf „S. 142 eintragen“.

- Dateien: `konzept-a.html` (mit `#4` für 4 Bücher), `konzept-a.png`, `konzept-a-4buecher.png`
- **Flächenanteil „Am Lesen“:** 25,9 % bei 2 Büchern, 32,1 % bei 4 Büchern (gemessen an 844 px). Bei 4 Büchern werden die Zeilen auf 54 px verdichtet, und das Haus wird flacher, statt nach unten wegzurutschen.
- **Bibliotheks-Einstiege:** 6 Zimmer (Wunschliste, Gelesen, Ungelesen, Eigene Regale, Abgebrochen, Rückblick als Gartenschild) und dazu genau eine Tür zum Erfassen. In Licht an waren es 8 Kacheln.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. *Ein Haus statt eines Rasters:* Besitz ist erweitertes Selbst (Belk), und Räume verraten ihre Bewohner (Gosling). „Aus der Bücherei von Mira Kessler“ über einem Haus, in dem die Bücher wohnen, macht die Sammlung zu einem Ort, an dem man ankommt. Wer die App öffnet, kommt nach Hause und betritt kein Werkzeug.
2. *Ungelesen als Wartezimmer mit freundlichen Gesichtern („61 haben Zeit“):* Der SuB schwankt zwischen Schuld und Humor. Wartende, gemütliche Bücher (eines schläft, eines trägt Hut) machen aus der Schuld ein Schmunzeln und stellen keine Forderung. Das entspricht der Calm Technology und dem Ansatz „du kannst“ statt „du musst“.
3. *Abgebrochen als Bett („6 ruhen sich aus“):* „Beiseitegelegt“ statt „gescheitert“. Wie bei Erlbruch wird ein unbequemes Thema sanft erzählt. Das Buch darf wieder aufstehen.

Ergänzend gilt: Neue Bücher kommen durch die Haustür, das passt zum Ankommen. Die Hausnummer zeigt den Bestand (240) und wird zur leisen Statistik ohne Kennzahlenkachel.

**Nutzerfreundlichkeit**
- Häufigste Handlung: Der gelbe Knopf rechts in der Buchzeile („S. 142 eintragen“, 94 × 60 pt, bei 4 Büchern 94 × 46 pt) wird einmal getippt. Danach öffnet sich ein Zahlenfeld mit der zuletzt eingetragenen Seite. Er liegt im Daumenbereich der rechten Hand.
- Erfassen geschieht nur an der gelben Haustür „Neue Bücher erfassen“ in der Mitte des Erdgeschosses. Es gibt kein zweites Plus.
- Jedes Zimmer ist als Ganzes tippbar (mindestens 88 × 116 pt). Die Beschriftung steht als echter Text auf einem hellen Schild (Kontrast ≥ 9 : 1). Bei großer Systemschrift wachsen die Schilder, die Illustration skaliert mit `meet` darüber und wird nur kleiner, nie abgeschnitten.

**Skalierung auf 1.000 Bücher:** Die Illustrationen sind fest und zeigen zum Beispiel immer dasselbe Regal in der Stube. Wachsen dürfen nur die Zahlen auf den Schildern und die Hausnummer. Ab dem ersten Eigenen Regal mit Inhalt beschriften sich die Kisten mit den Namen der drei größten Sammlungen.

**Risiko:** Das Haus kann in Richtung Kinderbuch kippen, besonders durch die Gesichter auf den Büchern. Gegenmittel sind wenige Punktaugen (Klassen-Reduktion) und kein Maskottchen. Ein Kansei-Test sollte das Paar „wertig–kitschig“ prüfen. Außerdem verlangt jede neue Kategorie ein neues Zimmer, das Haus ist also weniger erweiterbar als ein Raster.

---

## Konzept B: Der Lesegarten

**Idee:** Die Bibliothek ist ein Garten, in dem Bücher wachsen, ruhen und fliegen. Gelesenes hängt als Früchte im Baum, Ungelesenes steckt keimend im Beet, Abgebrochenes macht Pause in der Hängematte, Wunschbücher fliegen als Drachenschwanz, und neue Bücher kommen per Schubkarre, also in Schüben. Die offenen Bücher liegen vorne „auf der Bank“ als Kacheln mit großem Eintragen-Knopf.

- Dateien: `konzept-b.html` (mit `#4` für 4 Bücher), `konzept-b.png`, `konzept-b-4buecher.png`
- **Flächenanteil „Am Lesen“:** 22,2 % bei 2 Büchern, 32,8 % bei 4 Büchern. Bei 4 Büchern werden die Kacheln flacher, und der Drachen sinkt vom Himmel auf das Schuppendach. Wenige offene Bücher bedeuten also mehr Himmel.
- **Bibliotheks-Einstiege:** 6 Steckschilder (Wunschliste, Gelesen, Abgebrochen, Eigene Regale, Rückblick, Ungelesen) und dazu genau eine Schubkarre zum Erfassen.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. *Ungelesen als Beet („61 haben Zeit“):* Ungelesenes steht für Möglichkeit (Antibibliothek). Ein Keimling drängt nicht, er wächst, wenn es Zeit ist. Das ist die stärkste Form von „ungelesene Bücher warten freundlich“.
2. *Gelesenes als Baum mit Früchten:* Gelesenes ist Ernte und Erinnerung (Normans reflektive Ebene), keine Leistung. Es gibt keine Zahl, die steigt, nur einen Baum, der da ist. Das Regal wird ruhig als Teil des eigenen Lebens erzählt.
3. *Die Bank als Ort für das Aktuelle:* Lesen heißt im Bild sitzen und nicht leisten. Die Kacheln liegen wie Bücher auf der Gartenbank. Daraus folgen Ankommen statt Fortschrittsbalken, keine Prozente und keine Ziele.

Ergänzend gilt: Die Schubkarre greift den belegten Erfassungsrhythmus auf (Schübe, CLZ und BookBuddy). Der Rückblick ist ein Baumstumpf mit Jahresringen, also Chronik statt Dashboard.

**Nutzerfreundlichkeit**
- Häufigste Handlung: der gelbe Balken „S. 142 eintragen“ über die volle Kachelbreite (155 × 46 pt, bei 4 Büchern 155 × 44 pt) wird einmal getippt. Mit dem Daumen ist er in beiden Spalten gut erreichbar.
- Erfassen geschieht nur über das gelbe Schild „Neue Bücher erfassen“ an der Schubkarre, unten in der Mitte. Das ist die beste Daumenzone.
- Alle Einstiege sind echte Textschilder mit mindestens 44 pt Höhe. Die Illustration liegt dahinter und ist nicht selbst Tippziel. Dadurch gibt es keine Mehrdeutigkeit, wenn Bilder sich überlappen. Bei großer Systemschrift brechen die Kacheltitel bis auf drei Zeilen um.

**Skalierung auf 1.000 Bücher:** Baum, Beet und Drachenschwanz haben eine feste Anzahl Dinge. Wachsen dürfen nur die Zahlen auf den Schildern. Bei 5 offenen Büchern bekommt die Bank 3 + 2 Kacheln mit etwa 88 pt Höhe, das sind rund 33 %. Der Garten schiebt sich dann bis unter den Drachen.

**Risiko:** Die Szene ist dichter als das Haus, und die Schilder liegen frei im Bild. Bei sehr großer Systemschrift können sie sich überlappen, dann braucht es einen Rückfall auf eine zweispaltige Schilderreihe. Die Gartenmetapher („Abgebrochen in der Hängematte“) ist außerdem stärker erklärungsbedürftig als ein Zimmer.

---

## Was beide Konzepte gegenüber „Licht an“ lösen
- „Am Lesen“ belegt höchstens ein Drittel der Fläche (22–33 % statt etwa 45 %). Es funktioniert mit 1 bis 5 Büchern, und Eintragen braucht immer ein Tippen.
- Statt 8 kleiner Kacheln gibt es 6 große, benannte Orte in einem zusammenhängenden Bild und einen einzigen Erfassungsweg.
- Kontrast: Text in `#26232F` bzw. `#22302A` auf hellen Schildern ≥ 9 : 1, Nebentext ≥ 7 : 1.
- Schriften: A nutzt Bricolage Grotesque und Atkinson Hyperlegible (für Sehschwäche entwickelt). B nutzt Grandstander (nur Überschriften) und Lexend. Keine davon steht auf der Verbotsliste.
- Beispieldaten sind gekennzeichnet („BEISPIEL“, erfundene Titel und Namen).

Render-Skript: `render.js` (eigener Server auf Port 8801, misst den Flächenanteil mit).
