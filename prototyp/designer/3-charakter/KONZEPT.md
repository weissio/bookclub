# Designschule 3: Charakter und Sympathie

Zwei Startseiten für die Bibliothek. Die Wärme kommt aus gezeichneten Gegenständen, die man bedient, und aus einer Sprache mit leisem Humor. Es gibt keinen Lärm, keine Zähler-Jagd und kein Maskottchen mit Gesicht. Die Illustrationen sind von Hand als SVG gezeichnet. Bücher und Personen sind erfunden und als Beispieldaten markiert.

## Recherche: Vorbilder und was ich daraus nehme

| Vorbild | Quelle | Was ich nehme |
|---|---|---|
| (Not Boring) Weather, Andy Works | https://apps.apple.com/app/id1531063436 · https://www.tapsmart.com/apps/not-boring-weather-fun-alternative-weather-watchers/ | Eine riesige Zahl als Held der Seite und dicke, greifbare 3D-Objekte, die man anfasst, statt Daten zu lesen. Daraus wird in Konzept B die große Seitenzahl. |
| Airbnb-Redesign 2025, dimensionale Icons | https://www.itsnicethat.com/articles/airbnb-app-redesign-140525 | Icons als kleine Gegenstände mit Licht, Volumen und „fun details“, die man entdeckt. Weiche, runde Formen. Daraus entstehen die Band-Gegenstände in Konzept A. |
| Duolingo: Formensprache | https://blog.duolingo.com/shape-language-duolingos-art-style/ | Wenige, klug gesetzte Grundformen, klare Silhouetten, Freiraum um jede Figur und ein überzeichnetes Detail für den Humor, etwa die Brille auf der Stütze oder das Buch, das als Zelt daliegt. |
| Tiimo (App Store Award 2025) | https://www.tiimoapp.com/resource-hub/tiimo-winner-2025-app-store-awards | „Gentle, inviting, easy to trust“: weiche Pastellflächen und Ruhe trotz Farbe, gebaut für Menschen mit wenig Reizbudget. Das prägt Farbklima und Zurückhaltung in Konzept B. |
| Finch | https://screensdesign.com/showcase/finch-self-care-pet | Ein Gegenüber, das sympathisch ist, ohne zu fordern. Ich übernehme die Haltung („kein Schuldgefühl“), aber nicht das Haustier mit Energiebalken. Die Bücherstütze verlangt nichts. |
| Arc (The Browser Company) | https://www.inverse.com/input/design/the-browser-company-arc-design-interview | „The room matters, too“: Der Raum um den Inhalt ist Teil des Erlebnisses. In Konzept A ist die Startseite ein abendliches Zimmer mit Lichtkegel. |
| Partiful | https://ixd.prattsi.org/2025/02/design-critique-partiful/ | Jedes Ereignis bekommt sein eigenes Poster in eigener Farbe, die Beschriftung ist alltagsnah und augenzwinkernd. In Konzept B bekommt jedes aktuelle Buch ein farbiges Poster. |

Einschränkung: Die Quellen beschreiben die Screens nur in Worten. Bilder der Apps konnte ich hier nicht ansehen.

---

## Konzept A: „Licht an“

**Idee:** Die Startseite ist ein Zimmer am Abend: Eine Pendelleuchte wirft ihr Licht auf die Bücher, die gerade offen liegen. Die Seitenzahl steht groß auf der aufgeschlagenen Seite. Darunter, im Halbdunkel, stehen die Bände als kleine beleuchtete Gegenstände: ein Stapel (Gelesen), Bücher mit Anhänger (Ungelesen), eine Buchladentüte (Wunschliste), ein umgedreht abgelegtes Buch (Abgebrochen), eine Kiste (Regale) und ein Paket zum Auspacken (Erfassen).

- Datei: `konzept-a.html`, Bild: `konzept-a.png`
- Schrift: Nunito (rund, warm). Farben: Tintenblau, Lampengelb, kein Creme-Grund.
- Vorbilder: Airbnb 2025 (Icons als Gegenstände), Arc („the room matters“), Duolingo (Silhouette, ein überzeichnetes Detail).

**1 und 5 aktuelle Bücher:** Bei einem Buch liegt es groß und mittig im Lichtkegel, die Überschrift lautet „Ein Buch liegt offen.“ Ab drei Büchern liegt das zuletzt gelesene aufgeschlagen im Licht. Die anderen bilden daneben einen kleinen Stapel geschlossener Bücher (höchstens 4 Rücken, Seitenzahl am Rücken). Ein Tipp auf den Stapel tauscht das offene Buch. Die Reihenfolge legt man selbst fest. Die Fläche wächst also nicht.

**Erfassen:** an genau einer Stelle, dem Paket „Neue Bücher auspacken“ unten rechts im Daumenbereich. Das Paket passt zum Schub-Verhalten: Man scannt mehrere Bücher hintereinander und packt sie dann gemeinsam aus. Oben gibt es kein Plus.

**1.000 Bücher:** Es ändert sich nur die Zahl unter dem Gegenstand. Das Raster aus acht Gegenständen bleibt fest, Listen entstehen erst im jeweiligen Band.

**Sympathisches Element:** die Lampe mit Zugkette. Ein Zug am Kettchen schaltet zwischen Abend- und Tagesansicht um (statt eines Schalters in den Einstellungen). Dazu kommen kleine Zeilen unter den Zahlen: „haben Zeit“, „irgendwann“, „ohne Groll“.

**Risiko:** Die dunkle Abendwelt passt nicht zu jeder Tageszeit, deshalb ist die Tagesvariante Pflicht. Außerdem sind die Gegenstände klein: Sie müssen bei großer Systemschrift als Liste mit Icon umbrechen, sonst werden die Beschriftungen eng. Acht kleine Illustrationen sind Aufwand und müssen stilistisch streng bleiben, sonst wirken sie wie Clipart.

---

## Konzept B: „Die Bücherstütze“

**Idee:** Oben steht ein farbiges Poster pro aktuellem Buch, darauf ein dickes 3D-Buch und die riesige Seitenzahl. Ein einziger großer Knopf führt zu „Seite eintragen“. Darunter steht dein Regal als Reihe weicher, knetartiger Bände. Gehalten wird es von einer schweren Bücherstütze mit Lesebrille, die die Gesamtzahl trägt und beim Antippen die Statistik öffnet. Zwischen den Bänden und der Stütze ist eine Lücke frei: „Noch Platz“. Dort erfasst man neue Bücher.

- Datei: `konzept-b.html`, Bild: `konzept-b.png`
- Schrift: Bricolage Grotesque (eigenwillig, breit, mit Charakter). Farben: helles Salbei, Kobalt, Senf, Flieder, Rosa, Tanne.
- Vorbilder: Not Boring Weather (riesige Zahl, greifbare Objekte), Partiful (Poster je Ereignis), Tiimo (sanfte Pastellruhe), Finch (Sympathie ohne Forderung).

**1 und 5 aktuelle Bücher:** Bei einem Buch gibt es ein Poster ohne Seitenpunkte und ohne angeschnittenes Nachbarposter. Bei 2 bis 5 Büchern blättert man waagerecht, das nächste Poster lugt rechts hervor, und oben zeigen Punkte die Position (höchstens 5). Jedes Buch behält seine Posterfarbe, so erkennt man es wieder.

**Erfassen:** nur in der Lücke „Noch Platz“ vor der Stütze. Die Logik ist physisch: Neue Bücher kommen dorthin, wo im Regal Platz ist. Auch hier gibt es kein zweites Plus.

**1.000 Bücher:** Die Reihe hat feste Breiten, die Bände werden nicht dicker. Nur die Zahlen auf den Etiketten ändern sich, und die Stütze trägt „1.000“. Die Lücke bleibt immer gleich groß. Sie ist eine Aktion und kein Füllstand.

**Sympathisches Element:** die Bücherstütze mit Brille. Sie hat kein Gesicht und spricht nicht. Sie hält das Regal zusammen und „weiß“ die Statistik. Dazu kommen Gegenstände, die sich wie echte Bücher verhalten: Das abgebrochene Buch liegt quer obendrauf („beiseitegelegt“), und die Wunschliste ist in Geschenkpapier eingepackt, weil man sie noch nicht besitzt.

**Risiko:** Die senkrechte Schrift auf den Bänden ist bei großer Systemschrift schwer lesbar. Ab einer bestimmten Textgröße braucht es deshalb eine waagerechte Variante (Bände als liegender Stapel). Das kräftige Kobalt des Knopfs und die Pastellflächen können verspielter wirken, als ältere Leser mögen, deshalb muss das im Kansei-Test geprüft werden. Die Stütze darf nie Sprechblasen oder Launen bekommen, sonst kippt sie ins Maskottchen.

---

## Was die beiden Konzepte grundsätzlich trennt

| | A „Licht an“ | B „Die Bücherstütze“ |
|---|---|---|
| Welt | Zimmer am Abend, Licht als Ordnung | Tageslicht, Knet-Objekte, Poster |
| Am Lesen | aufgeschlagene Bücher, Zahl auf der Seite | ein Poster je Buch, Riesenzahl wie bei Not Boring |
| Bände | Gegenstände im Raster (Stapel, Tüte, Kiste …) | Bände in einer Reihe, gehalten von der Stütze |
| Erfassen | Paket „auspacken“ | Lücke „Noch Platz“ |
| Statistik | Gegenstand „Rückblick“ und Vermerk | die Bücherstütze selbst |
| Charakter | Lampe mit Zugkette | Stütze mit Brille |

---

## Prototyp „Licht an“ (gewählt am 24.10.2026)

Datei: `LichtAn.dc.html` (Format des claude.ai-Design-Canvas, 390 × 844). Klickdurchlauf und Screenshots in `screens/` (01 bis 27). Der Durchlauf lief ohne Konsolenfehler. Alle Bücher, Personen und Zahlen sind Beispieldaten.

**Startseite**
- Abend: Lichtkegel der Pendelleuchte. Tag: Fensterlicht fällt schräg ins Zimmer, die Lampe ist aus, die Akzente sind tintenblau statt lampengelb.
- Umschalten: in der App über die Zugkette an der Lampe. Im Prototyp gibt es zusätzlich den kleinen „P“-Knopf unten rechts für Tageszeit und Bücherzahl.
- 1 Buch: Es liegt groß und mittig im Licht. 2 Bücher: Sie liegen nebeneinander. 3 bis 5 Bücher: Eines liegt aufgeschlagen im Licht, die anderen liegen daneben als kleiner Stapel geschlossener Bücher mit Seitenzahl. Antippen legt ein Buch ins Licht. Die Fläche wächst nicht mit.
- Die Seitenzahl steht auf der aufgeschlagenen Seite. Kein Balken, keine Prozente.

**Seite eintragen**
- Ein Sheet mit großer Seitenzahl auf einem Papierblatt samt Lesebändchen. Dazu gibt es −/+, Sprünge um +5, +10 und +20, ein eigenes Ziffernfeld (Tasten 50 pt) und „Ende“ für die letzte Seite.
- Der Hauptknopf liegt im Daumenbereich und sagt, was passiert: „Bändchen auf Seite 152 legen“.
- Rückmeldung: Die zweite Kopfzeile wird für den Moment zu „Bändchen jetzt auf S. 152.“, und die Zahl im Buch ändert sich. Nichts springt, nichts blinkt.

**Band „Gelesen“**
- Kopf mit dem Band-Gegenstand. Darunter eine Suche (44 pt) und die Sortierung „Nach Jahr / Nach Lichtern / A bis Z“. Die Liste ist nach Jahren gruppiert und zeigt kleine Buchrücken.
- Die Bewertung erscheint als fünf kleine Lichter. Am Ende steht „… und 139 weitere“.

**Buchseite**
- Ganz oben steht „Meine Lesart“ als Papierkarte mit Lesebändchen und „Weiterschreiben“.
- Darunter „Hat mich erreicht“ mit fünf Glühbirnen und einem Wort („mitten ins Herz“), getrennt von den Eigenschaften (Lesefluss, Sprache, Tempo, Stark).
- Danach folgen Zitat mit Seite, „Mein Exemplar“ und „Leseverlauf“.
- Der Schalter „Im Schaufenster zeigen“ steht standardmäßig auf aus. Beim Einschalten fragt ein Sheet nach und sagt genau, was sichtbar wird und was privat bleibt.

**Neue Bücher auspacken**
- Drei Wege: Scannen, ISBN eintippen, von Hand.
- Scannen ist als Platzhalter gestaltet: Kamera, dann „Im Karton · 3“, dann die Wahl „Ungelesen / Wunschliste“, dann „3 Bücher ins Regal stellen“. Danach zählt der Band hoch, und die Kopfzeile meldet „3 Neue bei Ungelesen.“
- ISBN und „von Hand“ sind reine Platzhalter.

**Tabs**
- Bibliothek ist gebaut. Schaufenster, Entdecken und Ich sind illustrierte Platzhalter.

**Bewusst weggelassen:** Streaks, Ziele, Prozentbalken, Push-Hinweise, Konfetti, ein zweites Plus. Animationen gibt es nur als Überblendung (150 ms) und als Sheet-Einschub (200 ms). Unter „Bewegung reduzieren“ entfallen beide.

**Offene Fragen an den Auftraggeber**
1. Soll die Bewertung „Lichter“ heißen (Glühbirnen) oder neutral bleiben (Punkte)?
2. Soll die Tageszeit der Uhr folgen, dem Systemmodus (hell/dunkel) oder nur der Zugkette?
3. Gehört „Verliehen“ schon jetzt ins Raster, oder soll der Platz frei bleiben, bis die Funktion kommt?
4. Ist ab 5 aktuellen Büchern Schluss, oder soll der Stapel ab dem sechsten Buch zu „+2“ zusammenfallen?
