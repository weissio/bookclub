# Designer 2 · Gemütliche Spiele – Runde 2

Designschule: Oberflächen gemütlicher Spiele. Besitz und Ordnung sollen sich zufrieden und ruhig anfühlen, mit liebevoll gezeichneten Dingen und klaren, rundlichen Spiel-Menüs. Es gibt keine Punkte, keine Streaks, keine Figur und keine Spielmechanik. Alle Bücher, Namen und Zahlen sind Beispieldaten.

## Recherche: Vorbilder

| Vorbild | URL | Was ich übernehme |
|---|---|---|
| Unpacking (Witch Beam) | https://www.unpackinggame.com/ | Die Wohnung zeigt, wer jemand ist, ganz ohne Figur. Bücher im Regal erzählen das Leben. Daraus kommen das Zimmer als Ort in A und das Wort „Einräumen“. |
| Animal Crossing: Museum und Critterpedia | https://nookipedia.com/wiki/Critterpedia | Die Sammlung wird als Ausstellung gezeigt, mit Vitrinen und Namensschildern. Aus den runden Menüs mit gestrichelter Innenkante entsteht B. |
| Stardew Valley | https://www.stardewvalley.net/ | Die Werkzeugleiste unten am Bildschirm (Hotbar) zeigt, was man gerade in der Hand hat. Daraus entsteht in B die „Tasche“ für „Am Lesen“ im Daumenbereich. |
| Wilmot’s Warehouse | https://en.wikipedia.org/wiki/Wilmot%27s_Warehouse | Ordnung macht von selbst zufrieden, ohne Wertung. Dinge werden nach Farbe und Gefühl gruppiert. Daraus kommen die farbigen Rücken und die freie Ordnung in den Bänden. |
| A Short Hike | https://ashorthike.com/ | Kleine, warme Welt mit großen, lesbaren Schildern und ohne Zeitdruck. Daraus kommen die dunklen Namensschilder mit Spitze in A. |
| Spiritfarer (Thunder Lotus) | https://thunderlotusgames.com/spiritfarer/ | Ein Ort, an dem man sich um Dinge kümmert und Abschied ohne Groll gehört dazu. Daraus kommt der Ton „Beiseitegelegt · ohne Groll“. |

Beide Konzepte verzichten bewusst auf das Motiv aus „Licht an“ (Lampe, Lichtkegel, aufgeschlagene Bücher). Sie vermeiden auch Cremepapier mit Serifen, Holzbrett, Terrakotta sowie Inter und DM Sans. Schriften: M PLUS Rounded 1c (A), Baloo 2 und Nunito (B).

---

## Konzept A: „Meine Leseecke“

**Idee:** Die Bibliothek ist ein kleines gezeichnetes Zimmer im Querschnitt, wie in Unpacking. Jeder Band ist ein Gegenstand an seinem Platz: das große Regal (Gelesen), der Stapel neben dem Sessel (Wartet), die Fensterbank (Wunschliste), der Karton (Beiseite), das Wandbrett (Eigene Regale) und das Bild an der Wand (Rückblick). Die Bücher „am Lesen“ liegen oben auf einem Tablett, jedes mit einem senffarbenen Lesezeichen, das die Seite trägt.

- **Vorbilder:** Unpacking, A Short Hike, Wilmot’s Warehouse (URLs oben)
- **Flächenanteil „Am Lesen“:** 18,7 % des Bildschirms mit 2 Büchern, 28,0 % mit 4 Büchern (gemessen per Playwright). Mit 5 Büchern sind es etwa 34 %; ab dem 5. Buch wird das Tablett deshalb innen scrollbar statt höher.
- **Bibliotheks-Einstiege:** 6 Orte im Zimmer, jeder mit großem Namensschild (≥ 44 pt). Dazu kommt „Einräumen“ als einziger Erfassungsweg.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. **Das Zimmer statt eines Rasters:** Das Regal ist Teil des Selbst (Belk), und Räume verraten Persönlichkeit (Gosling). Ein Zimmer fühlt sich nach Ankommen an, nicht nach Verwaltung. Introvertierte zeigen sich hier über Dinge, nicht über die eigene Person.
2. **Ungelesenes als Stapel neben dem Sessel, Abgebrochenes im Karton „Beiseite“:** Beides ist eine freundliche, alltägliche Rahmung ohne Schuld. Der Stapel wartet in Griffnähe, und was im Karton liegt, ist nicht weggeworfen. Es gibt keine Zahl im Alarmton und kein „noch X“.
3. **Das Lesezeichen als Knopf:** Die Seitenzahl sitzt auf einem Gegenstand, den jeder Leser kennt. „S. 142“ beschreibt einen Zustand, keine Leistung. Es gibt keine Prozente, keinen Balken und kein Ziel (Calm Technology, „du kannst“ statt „du musst“).

**Nutzerfreundlichkeit**
- **Seite eintragen:** Ein Tipp auf das Lesezeichen „S. 142“ öffnet ein kleines Blatt mit Zahlenrad, vorbelegt mit der letzten Seite.
- **Erfassen:** Nur über „Einräumen“ oben rechts (Mehrfachscan, ISBN, Hand). Es gibt kein zweites Plus.
- **Bedienung:** Alle Ziele sind ≥ 44 pt, und die Texte auf den dunklen Schildern haben einen Kontrast über 10 : 1. Bei großer Systemschrift brechen die Schilder zweizeilig um. Das Zimmer bleibt dabei unten verankert, oben fällt nur Wand weg.

**Skalierung auf 1.000 Bücher:** Das Zimmer bleibt gleich groß, nur die Zahlen auf den Schildern ändern sich. Die Bände öffnen eigene Listen mit Suche. Nichts wächst linear mit dem Bestand.

**Risiko:** Sechs Schilder in einer Zeichnung können bei sehr großer Schrift eng werden. Fallback ist eine reine Schilderreihe ohne Szene. Die Illustration muss außerdem für Hell und Dunkel gezeichnet werden. „Einräumen“ liegt oben und ist damit weniger daumennah, was zum seltenen Erfassen in Schüben passt.

Dateien: `konzept-a.html`, `konzept-a.png`, `konzept-a-4buecher.html`, `konzept-a-4buecher.png`

---

## Konzept B: „Miras Sammlung“

**Idee:** Die Bibliothek ist eine kleine Ausstellung, wie das Museum in Animal Crossing. Vier große Vitrinen mit je einem liebevollen Ausstellungsstück stehen für Gelesen, Wartet, Wunschliste und Beiseitegelegt, darunter liegen zwei flache Fächer für Eigene Regale und Rückblick. „Am Lesen“ ist die **Tasche** unten am Daumen, wie die Hotbar in Stardew Valley: Sie hat immer dieselbe Höhe, egal ob 1 oder 5 Bücher darin liegen.

- **Vorbilder:** Animal Crossing (Museum, Critterpedia), Stardew Valley (Hotbar), Spiritfarer (URLs oben)
- **Flächenanteil „Am Lesen“:** 17,1 % des Bildschirms, konstant bei 1 bis 5 Büchern (gemessen per Playwright)
- **Bibliotheks-Einstiege:** 4 große Vitrinen und 2 flache Fächer, also 6 Einstiege. Dazu kommt „Einräumen“ als einziger Erfassungsweg.

**Psychologische Begründung der 3 wichtigsten Entscheidungen**
1. **Die Tasche unten:** Was man gerade liest, trägt man bei sich. Es ist ein Begleiter und nicht die Hauptsache des Bildschirms. So steht die Bibliothek als Ganzes im Vordergrund und es entsteht kein Leistungsdruck. Die feste Höhe sorgt für Ruhe, weil sich nichts verschiebt, wenn ein Buch dazukommt.
2. **Vitrinen mit Ausstellungsstücken:** Im Museum bedeutet Sammeln Bewahren und eine Auswahl mit selbst gesetztem Wert (Pearce). Das gepresste Blatt auf dem Gelesen-Stapel steht für „Erinnerungen statt Abzeichen“.
3. **Sprache der Dinge:** „haben Zeit“ mit Teetasse, „ohne Groll“ mit Kieselstein, Wunschzettel an der Leine. Ungelesenes wartet freundlich, Abbrechen ist erlaubt, und es gibt keine Zähler, die mahnen.

**Nutzerfreundlichkeit**
- **Seite eintragen:** Ein Tipp auf ein Buch in der Tasche öffnet das Seitenblatt, direkt im Daumenbereich und mit einer Hand bedienbar.
- **Erfassen:** Nur über „Einräumen“ oben rechts. Es gibt kein zweites Plus.
- **Anzeige je nach Anzahl:** Bei 1 bis 2 Büchern zeigt jedes Fach Umschlag, Titel und Seite. Bei 3 bis 5 Büchern zeigt es nur Umschlag und Seite. Die Fächer sind mindestens 64 × 92 pt groß. Alle Texte erreichen mindestens 4,5 : 1.

**Skalierung auf 1.000 Bücher:** Die Vitrinen zeigen feste Stücke und Zahlen. Die Bände öffnen Listen mit Suche und Sortierung. Die Startseite bleibt unverändert.

**Risiko:** Ab 3 Büchern stehen in der Tasche keine Titel mehr, die Bücher sind nur am Umschlag erkennbar. Mit echten Verlagscovern funktioniert das gut, bei Bildschirmleser-Labels auch, bei großer Systemschrift muss es geprüft werden. Als Notlösung zeigt langes Drücken den Titel. Die Vitrinen ähneln außerdem dem Kachel-Raster einer App, und den Unterschied macht nur die Qualität der Zeichnungen.

Dateien: `konzept-b.html`, `konzept-b.png`, `konzept-b-4buecher.html`, `konzept-b-4buecher.png`

---

`render.js` erzeugt die Varianten mit 4 Büchern, rendert alles über Port 8802 und misst den Flächenanteil.
