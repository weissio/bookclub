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

**Sympathisches Element:** die Lampe mit Zugkette. Ein Zug am Kettchen schaltet zwischen Abend- und Tagesansicht um (statt eines Schalters in den Einstellungen). Dazu kommen kleine Zeilen unter den Zahlen: „haben Zeit“, „irgendwann“.

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

---

## Prototyp, Runde 2: Startseite nach Variante 3 (24.10.2026)

Arjens Vorgaben: höchstens 5 Bücher am Lesen, die Reihenfolge lässt sich priorisieren, Priorität 1 liegt aufgeschlagen im Licht, die übrigen stehen als kleine Balken daneben. Der Rest folgt V3. Datei: `LichtAn.dc.html`, Screens in `screens2/` (01 bis 22). Der Playwright-Durchlauf auf Port 8810 lief ohne Konsolenfehler.

**Aufteilung.** „Am Lesen“ nimmt mit 1 bis 5 Büchern immer 26,9 % der Fläche ein (y 140–367). Links liegt das offene Buch mit Seitenzahl, darunter Titel und „Seite eintragen“. Rechts stehen bis zu vier Balken, je 44 pt hoch. Darunter folgt „Im Regal“ als Liste mit Cover-Fächern (Gelesen, Ungelesen im Regal, Wunschliste, Weitere Bände), danach einmal „Neue Bücher auspacken“.

**Balken.** Jeder Balken hat zwei Tippflächen von mindestens 44 pt. Der Titel (bis zu zwei Zeilen, danach „…“) legt das Buch ins Licht. Die Zahl mit dem Lesebändchen rechts öffnet „Seite eintragen“ für genau dieses Buch, ohne die Reihenfolge zu ändern. Die Zahl steht damit an derselben Stelle wie die Seitenzahl im offenen Buch: Zahl heißt Seite.

**Priorisieren.** Es gibt zwei Wege:
- Schnell: ein Tipp auf einen Titel holt das Buch nach vorn, das bisherige rückt an die erste Balkenstelle. So wechselt man abends das Buch, wie man es auf dem Nachttisch tut.
- Genau: „Reihenfolge“ öffnet ein Sheet mit Rang 1 bis 5 und je einem Pfeil „eine Stelle nach vorn“ (44 pt).

Ziehen per Drag habe ich bewusst weggelassen: Es ist einhändig unzuverlässig und für ältere Leser schwer.

**Grenze 5.** Will man ein sechstes Buch anfangen („Jetzt anfangen zu lesen“ auf der Buchseite eines ungelesenen Buchs), kommt keine Fehlermeldung. Stattdessen erscheint ein ruhiges Sheet: „Fünf Bücher liegen schon offen. Damit ‚Ein Jahr auf See‘ ins Licht kann, darf eines davon zurück ins Regal. Sein Lesebändchen bleibt, wo es ist.“ Darunter stehen die fünf Bücher mit „zurücklegen“ und unten „Doch noch warten lassen“. Das zurückgelegte Buch steht wieder bei Ungelesen, die Seite bleibt gemerkt. Das neue Buch kommt ans Ende („Neues Buch an Platz 5.“). Arjens Regel: Ein neu angefangenes Buch kommt immer ans Ende; nur wenn keins offen ist, liegt es im Licht. Hochstufen macht man selbst („Liegt jetzt an Platz 4.“, Screen 14b).

**Rückmeldungen** stehen in einer Zeile unter der Überschrift: „Eingetragen: Seite 71.“, „Liegt jetzt im Licht.“, „Zurückgelegt, Bändchen bleibt.“, „3 Neue bei Ungelesen.“

**Prototyp-Schalter** („P“ unten rechts): Abend oder Tag, 1, 2, 3 oder 5 Bücher. In der App schaltet die Zugkette der Lampe zwischen Abend und Tag um.

**Offene Fragen an Arjen**
1. Soll ein Tipp auf den Titel im Balken das Buch ins Licht holen, oder soll er die Buchseite öffnen? Im zweiten Fall bliebe das Priorisieren nur über „Reihenfolge“.
2. Ist der Ton beim sechsten Buch richtig, und soll „zurücklegen“ das Buch zu Ungelesen schicken oder in einen eigenen Zustand „pausiert“?
3. (Entschieden: Neue Bücher kommen ans Ende.)

---

## Prototyp, Runde 3: Weitere Bände (24.10.2026)

Arjens Festlegungen: Abgebrochen bekommt Begründung und Bewertung, Pausiert bekommt eine Begründung, Aktiv nimmt mehr als 5 Bücher auf. Die Startseite ist unverändert; nur die Zählung lautet bei mehr als fünf Büchern „5 von 7 aktiv“. Screens in `screens3/` (01 bis 15), Playwright auf Port 8810, keine Konsolenfehler. Im Prototyp-Schalter gibt es zusätzlich „7“.

**Weitere Bände** ist in zwei Gruppen geteilt:
- Lesen: Aktiv, Pausiert, Abgebrochen
- Ordnen: Eigene Regale, Verliehen, Rückblick

**Aktiv:** Alle laufenden Bücher, gruppiert in „Auf der Startseite“ (Platz 1 bis 5) und „Nur in Aktiv“ (ab Platz 6). Ein Pfeil rückt ein Buch eine Stelle nach vorn; rutscht es auf Platz 5, liegt es auf der Startseite. Ein neues Buch wird nicht mehr blockiert, sondern kommt ans Ende: „Liegt in Aktiv an Platz 8.“ Das Sheet „Fünf Bücher liegen schon offen“ ist entfallen.

**Buchseite eines aktiven Buchs:** zwei Knöpfe, „Pausieren“ und „Abbrechen …“.

**Pausieren** (Sheet, alles freiwillig): Gründe als Mehrfachauswahl, ein optionales Freitextfeld und der Knopf „Pausieren“. Das Lesebändchen bleibt. Im Band „Pausiert“ hat jede Zeile den Knopf „Wieder aufnehmen“; das Buch kommt dann in Aktiv ans Ende („Wieder aktiv, in Aktiv an Platz 7.“).

**Abbrechen** (Sheet):
- Gründe als Mehrfachauswahl
- „Bis hierhin: Hat es dich erreicht?“ mit 0 bis 5 Lichtern, dieselbe Skala wie beim gelesenen Buch, ohne Eigenschaften
- „Noch einmal etwas von [Autor]?“ mit Ja / Vielleicht / Eher nicht
- optionaler Freitext
- Knopf „Bei Seite 12 abbrechen“

Der Band „Abgebrochen“ zeigt je Buch Seite, Gründe und Lichter, die Buchseite den ganzen Eintrag.

**Für den Empfehlungs-Algorithmus** entsteht je Abbruch ein strukturierter Datensatz: Gründe (feste Schlüssel), Lichter (0 bis 5), „noch einmal vom Autor“ (ja / vielleicht / nein), Seite und Anteil gelesen, dazu Autor und Genre aus den Buchdaten. Die Frage nach dem Autor macht das Beispiel „5 Abbrüche von XY“ direkt messbar, auch schon bei einem einzigen Abbruch.

### Vorgeschlagene Grundliste (Arjen bitte bestätigen)

**Abbrechen** (Mehrfachauswahl):
1. Stil, Sprache
2. Tempo
3. Thema
4. Figuren
5. Zu lang
6. Zu schwer
7. Erwartung nicht erfüllt
8. Nicht mein Genre
9. Inhaltlich unangenehm
10. Anderes

„Nicht jetzt“ steht bewusst nicht in dieser Liste. Wer „nicht jetzt“ meint, sollte pausieren, sonst verfälscht es die Empfehlungen.

**Pausieren** (Mehrfachauswahl, freiwillig):
1. Gerade nicht die Stimmung
2. Zu schwer für jetzt
3. Ein anderes Buch drängt
4. Keine Zeit
5. Will es in Ruhe lesen
6. Anderes

**Offen:** Soll ein abgebrochenes Buch im Schaufenster zeigbar sein? (Der Schalter ist derzeit vorhanden.)

---

## Prototyp, Runde 4: Höchstens 5 aktiv, kein Band „Aktiv“ (24.10.2026)

Arjens Entscheidung: Aktiv sind genau die bis zu 5 Bücher der Startseite. Einen Band „Aktiv“ gibt es nicht mehr; was in Runde 3 dazu steht, gilt nicht mehr. Screens in `screens4/` (01 bis 16), Playwright auf Port 8810, keine Konsolenfehler.

- **Startseite:** zählt „· n von 5“. Die Reihenfolge erreicht man über „Reihenfolge“. Im Sheet öffnet ein Tipp auf den Titel die Buchseite mit „Pausieren“ und „Abbrechen …“.
- **Weitere Bände:** Pausiert und Abgebrochen (Gruppe Lesen), Eigene Regale, Verliehen und Rückblick (Gruppe Ordnen).
- **Sechstes Buch** („Jetzt anfangen zu lesen“ bei 5 aktiven) und **Wieder aufnehmen** bei 5 aktiven führen zum selben Sheet „Platz machen“:
  1. „Fünf Bücher liegen schon offen. Damit ‚…‘ dazukommen kann, macht eines davon Pause. Sein Lesebändchen bleibt, wo es ist. Das neue kommt ans Ende.“ Darauf folgen die 5 Bücher mit „pausieren“.
  2. Das gewählte Buch steht oben (mit „ändern“), darunter „Magst du sagen, warum? Freiwillig.“ mit den Pausegründen, Freitext und dem Knopf „Pausieren und Neues dazunehmen“.
  3. Rückmeldung: „Pausiert. Das neue liegt an Platz 5.“
- Mit weniger als 5 aktiven Büchern gibt es keine Frage: „Wieder am Lesen, an Platz 4.“
- Die Kopfzeile des Sheets heißt „Doch nicht“, damit sie nicht mit „Abbrechen“ (Buch abbrechen) verwechselt wird.
- **Prototyp-Schalter:** 1, 2, 3 oder 5 Bücher.
- **Schaufenster (Arjen, 24.10.2026):** Das Schaufenster zeigt eigene Empfehlungen mit eigenen Worten. Bei gelesenen Büchern bleibt der Schalter, wie er ist; die Rückfrage beginnt mit „Hier steht deine Empfehlung mit deinen Worten.“ Bei abgebrochenen Büchern steht nur noch ein kleiner Schalter ganz unten mit dem Satz „Das Schaufenster ist für Empfehlungen gedacht. Zeigen ist trotzdem möglich.“ Er ist standardmäßig aus und fragt ebenfalls nach. Screens 17 bis 20.
- **Arjen, 24.10.2026:** Abbruch- und Pausegründe sind bestätigt. Die frühere wertende Formulierung beim Abbrechen ist überall entfernt; der Band „Abgebrochen“ heißt im Untertitel „Mit Grund und Lichtern“, die Rückmeldung lautet „Abgebrochen bei Seite 12.“ Ein Tipp auf den Titel in einem Balken öffnet die Buchseite und holt das Buch **nicht** ins Licht. Die Reihenfolge ändert sich nur über „Reihenfolge“, ein Tipp auf die Zahl trägt die Seite ein. Neue Screens: 00a bis 00c, 03b.

---

## Prototyp, Runde 5: Bewertungsansicht (24.10.2026)

Grundlage: ENTSCHEIDUNGSVORLAGE-USP3.md, Abschnitte 2 und 8. Screens in `screens5/` (00 bis 18), Playwright auf Port 8810, keine Konsolenfehler.

**Was gebaut ist**
- Die Lichter beantworten jetzt überall „Wie hat es dir gefallen?“ (1 gar nicht, 2 eher nicht, 3 okay, 4 gut, 5 sehr gut). Die alte Bezeichnung ist aus dem Prototyp entfernt; im Rückblick heißt es „Am besten gefallen“.
- **Sheet „Bewertung“**, direkt nach „Zu Ende gelesen“ (Seite eintragen → „Ende“) oder „Fertig gelesen“ auf der Buchseite. Das Buch ist sofort gelesen; „Später“ schließt ohne Angaben. Der Inhalt von oben nach unten:
  1. Gefallen (fünf Lichter, nochmals tippen löscht)
  2. „Was hat funktioniert, was hat gestört?“: je Aspekt zwei getrennte Knöpfe „mochte ich“ und „störte mich“, also kein Umschalten durch Mehrfachtippen. Romane: Sprache, Figuren, Handlung, Atmosphäre, Thema. Sachbücher: Verständlichkeit, Tiefe, Thema.
  3. Meine Lesart (Freitext)
  4. „Genauer beschreiben“ (zugeklappt, zeigt „3 von 6 angegeben“): Tempo des Buchs, Tempo für mich, Stimmung, Anspruch, „Mehr von [Autorin]?“, „Was möchtest du künftig seltener?“
- **Abbruch:** dasselbe Sheet, Titel „Abbrechen“. „Woran lag es?“ mit den bestätigten Gründen ersetzt „funktioniert/gestört“. Gefallen bleibt, „Genauer beschreiben“ auch. Der Knopf heißt „Bei Seite 38 abbrechen“; „Zurück“ bricht nichts ab.
- **Buchseite:** Die Karte „Wie hat es dir gefallen?“ zeigt Lichter und Wort, darunter knappe Zeilen: Mochte ich, Störte mich, Woran es lag, Genauer, Mehr davon?, Seltener. Mit „Bearbeiten“ öffnet sich dasselbe Sheet vorbefüllt. Ohne Angaben steht dort „Bewerten“.

**Ehrliche Einschätzung beim Durchspielen**

*Leicht, unter 30 Sekunden:*
- Gefallen ist ein Tipp.
- Zwei, drei Aspekte sind drei Tipps; die Wörter „mochte ich“ und „störte mich“ sind sofort klar.
- Der Speicher-Knopf ist immer erreichbar.
- Der schnelle Weg (Lichter, drei Aspekte, Speichern) braucht 5 Tipps und etwa 10 Sekunden.
- Beim Abbruch fühlen sich die Gründe natürlicher an als die Aspekte, weil man ohnehin gerade über den Grund nachdenkt.

*Lohnend, aber schon Arbeit:*
- Die Lesart als Freitext ist der persönlichste Teil, aber die einzige Stelle, die Tippen auf der Tastatur verlangt. Gut, dass sie leer bleiben darf.

*Wirkte beim Durchspielen unnötig oder doppelt:*
- **„Tempo des Buchs“ neben „Tempo für mich“**: Beim Ausfüllen gibt man fast immer nur eins an, meist „für mich“. Das Buchtempo kann ein Katalogmerkmal werden, statt eine Leserfrage zu sein.
- **„Stimmung des Buchs“**: sechs Wörter, schwer zu entscheiden, fühlt sich wie eine Prüfung an. Das ist eher ein Katalog- oder Schaufenster-Merkmal.
- **„Anspruch“** überschneidet sich beim Abbruch mit dem Grund „Zu schwer“. Nicht doppelt, aber man fragt sich, wo man es angeben soll.
- **„Was möchtest du künftig seltener?“** ist beim Abbruch sinnvoll, bei einem gefallenen Buch fast immer leer. Vorschlag: nur zeigen, wenn Gefallen höchstens 2 ist oder es ein Abbruch ist.
- **„Mehr von [Autorin]?“** ist stark und leicht. Ich würde es aus „Genauer beschreiben“ herausholen und sichtbar machen.
- Bei **Sachbüchern** passen drei Aspekte; „Thema“ wirkt dort doppelt zum Buchthema selbst, „Nutzen“ wäre vielleicht treffender (zu prüfen).

*Offene Fragen an Arjen:*
1. Soll „Mehr davon?“ aus „Genauer“ nach oben wandern?
2. Soll „Seltener“ nur bei niedrigem Gefallen oder Abbruch erscheinen?
3. Gehören Tempo des Buchs und Stimmung in den Katalog statt in die Bewertung?
- **Entschieden (24.10.2026), umgesetzt:** „Mehr von [Person]?“ steht direkt unter dem Gefallen und wird mit einem Tipp beantwortet: Ja / Nein / weiß nicht. „Genauer beschreiben“ enthält nur noch „Tempo für mich“. „Seltener“ erscheint dort nur bei 1–2 Lichtern oder beim Abbruch. Tempo des Buchs, Stimmung und Anspruch sind entfallen und gehören in den Katalog. Beim Abbruchgrund „Tempo“ erscheint direkt darunter „Tempo war … zu langsam / zu schnell“. „Tempo für mich“ unter „Genauer“ ist dann ausgeblendet, damit nichts doppelt gefragt wird. Screens in screens5/ neu erzeugt.
- **Nachtrag 2 (externe Prüfung), umgesetzt:**
  - Unter jedem Licht steht die Stufe: gar nicht, eher nicht, okay, gut, sehr gut.
  - Neu ist „Künftig weniger davon?“: Genre, Thema, Länge, Ton, je mit zwei getrennten Knöpfen „seltener“ und „nicht empfehlen“, dazu eine kurze Erklärung, dass „seltener“ nur senkt und „nicht empfehlen“ ausschließt. Das ist bei 1–2 Lichtern und beim Abbruch hervorgehoben, sonst steht es unter „Genauer beschreiben“; die zugeklappte Zeile zeigt die Zahl der Angaben.
  - Gespeichert wird nur Sichtbares: Wer „Tempo“ abwählt, löscht auch „zu langsam/zu schnell“. Gründe werden nur beim Abbruch gespeichert, Aspekte nur beim gelesenen Buch.
  - Geprüfte Fälle (screens5/):
    - 10b–10e: 2 Lichter, „seltener“, dann 5 Lichter. Die Angabe bleibt unter „Genauer“ sichtbar und wird gespeichert.
    - 12–12c: „Tempo“ an, „zu langsam“, „Tempo“ ab. Die Angabe ist weg und taucht beim erneuten Anwählen nicht wieder auf.
    - 13–14: „nicht empfehlen“ gespeichert und auf der Buchseite gezeigt.
  - Die 10 Sekunden stammen aus internem Durchspielen; ob es für echte Leser schnell und verständlich ist, muss ein Test zeigen.
- **Datenbindung der Ausschlüsse (CLUSTERUNG.md, Abschnitt 6), umgesetzt:**
  - Jedes Beispielbuch zeigt auf der Buchseite „Merkmale · aus dem Katalog“: Genre, 1–3 Themen, Ton, Längenbereich (unter 350 / 350 bis 500 / über 500 Seiten) und, wo passend, einen Inhalt wie „detaillierte Gewaltdarstellung“.
  - „Künftig weniger davon?“ listet genau diese Werte einzeln, je mit „seltener“ und „nicht empfehlen“. Es gibt keinen Sammelausschluss aller Themen.
  - Gespeichert wird `{action: 'seltener'|'never', dimension, value_id, label, source_work_id, scope: 'global', explicit: true}`. Der Abbruchgrund „Thema“ erzeugt keinen Ausschluss.
  - Auf der Buchseite stehen die Einträge unter „Künftig weniger, für alle Empfehlungen“, z. B. „Seltener: Thema Meer“, jeweils mit „entfernen“.
  - Geprüft in screens5/10b–10f (wählen, speichern, sehen, entfernen) und 13–14 (Abbruch mit „Thema Verlust: seltener“ und „Ton ruhig: nicht empfehlen“).
- **Wording und Platz (24.10.2026):** Die Aspekt-Knöpfe heißen „gefiel mir“ / „gefiel mir nicht“, auf der Buchseite „Gefiel mir“ / „Gefiel mir nicht“. Nichts gewählt heißt keine Aussage. „Künftig weniger davon?“ ist auch bei 1–2 Lichtern und beim Abbruch zugeklappt: eine dezent hervorgehobene Zeile mit „Merkmal wählen“ bzw. der Zahl der Angaben (screens5/10a, 13b).
