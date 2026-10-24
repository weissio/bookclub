# Protokoll: Kandidatenpool aus dem DNB-Katalog (Ausgangsbücher a01–a10)

Erstellt am 24.10.2026. Ausgabe: `kandidaten-aus-arjen.json` (60 Einträge, d01–d60). Alle Kandidaten stammen aus SRU-Antworten der DNB (`https://services.dnb.de/sru/dnb`, recordSchema MARC21-xml). Es wurden keine Titel nach eigenem Urteil hinzugefügt oder weggelassen; alle Auswahl- und Ausschlussregeln sind unten festgelegt und wurden maschinell angewandt.

## 1. GND-Schlagwörter der Ausgangsbücher

Abfrage je Buch: `query=num=<ISBN>`. Ausgewertet: MARC 650, 651, 689 (GND-Sachschlagwörter) und 082 (Sachgruppe).

| ID | Titel | IDN | Sachgruppe (082) | GND-Schlagwörter (650/651/689) |
|---|---|---|---|---|
| a01 | Offene See | 1200364155 | 820 / B | **keine** |
| a02 | Die Eleganz des Igels | 986852554 | 840 / B | Paris, Concierge, Doppelleben, Bewohner, Zwischenmenschliche Beziehung |
| a03 | Acht Berge | 1130167798 | 850 / B | **keine** |
| a04 | Der Buchspazierer | 1207330817 | 830 / B | **keine** |
| a05 | Das Gewicht der Worte | 119689227X | 830 / B | **keine** |
| a06 | Strandgut | 1347122842 | 820 / B | **keine** |
| a07 | Das Café ohne Namen | 1270835084 | 830 / B | **keine** |
| a08 | Der Schatten des Windes | 967934273 | 860 / B | Barcelona, Buch, Autor, Verschollenheit, Geschichte 1945-1956, Junge, Faszination |
| a09 | Herr Lehmann | 961410949 | 830 / B | Berlin-Kreuzberg, Sonderling, Identitätsfindung, Geschichte 1989 |
| a10 | Das kleine Haus am Sonnenhang | 1306104424 | 830 / B | **keine** |

Hinweis a09: Die ISBN-Suche lieferte 2 Treffer (zusätzlich „Die Lehmann-Trilogie“); verwendet wurde nur der Datensatz mit der passenden ISBN (961410949).

**Problem:** Für 7 von 10 Büchern (a01, a03, a04, a05, a06, a07, a10) enthält der DNB-Datensatz keine GND-Sachschlagwörter, nur Gattungsangaben (655: „Fiktionale Darstellung“, „Erzählende Literatur: Gegenwartsliteratur ab 1945“). Die DNB erschließt neuere Belletristik meist nicht inhaltlich; die Verlagsstichwörter in 653 (nur in MARC21plus sichtbar) sind keine GND-Schlagwörter. **Ersatzregel:** Für diese 7 Bücher wurden die `thema`-Werte aus `arjen-buecher.json` in gleichlautende GND-Begriffe übertragen (Meer & Küste → Meer, Küste; Natur & Landschaft → Natur, Landschaft; Erwachsenwerden; Freundschaft; Berge; Familie; Bücher & Lesen → Buch, Lesen; Philosophie & Sinn → Philosophie, Sinn; Kunst & Musik → Kunst, Musik; Alter; Großstadt; Gesellschaft & Politik → Gesellschaft, Politik; Dorf & Provinz → Dorf). Diese Suchen beruhen also auf den redaktionellen Merkmalen der Eingabe, nicht auf GND-Erschließung.

## 2. SRU-Syntax

- Indizes laut `operation=explain`: `sw` (Schlagwörter), `sgt` (Sachgruppe), `spr` (Sprachencode), `mat` (Materialart). `sgt=B` = Belletristik.
- Jeder Suche wurde `and sgt=B and spr=ger and mat=books` angehängt (deutschsprachig, gedruckte Bücher; Hörbücher und Online-Ressourcen sind dadurch ausgeschlossen). `maximumRecords=30`.
- Mehrwortbegriffe in Anführungszeichen (`sw="Zwischenmenschliche Beziehung"`). Ohne Anführungszeichen wird der Ausdruck anders zerlegt.
- Die DNB liefert keine Relevanzsortierung: die Treffer sind etwa nach Erscheinungsjahr absteigend sortiert. „Rang in Abfrage“ ist die Position in dieser Antwort.
- Der Index `sw` passt auch auf Datensätze, deren Schlagwörter nicht vom Ausgangsbuch stammen. Bei Einzelbegriffen kommen deshalb thematisch beliebige Romane in den Pool (z. B. Fantasy oder Thriller bei `sw=Buch`).
- Kombinationen aus zwei Begriffen ergaben bei Belletristik fast immer 0–10 Treffer, Einzelbegriffe 20–4000.

## 3. Vorab-Tests (nur Trefferzahl, keine Kandidaten daraus)

Zur Wahl der Abfragen wurden folgende Abfragen nur gezählt (alle mit `and sgt=B and spr=ger and mat=books`, sofern nicht anders angegeben):

| Abfrage | Treffer |
|---|---|
| `sw=Freundschaft and sw=Berge and sgt=B (ohne spr/mat)` | 1 |
| `sw=Freundschaft and sw=Gebirge and sgt=B (ohne spr/mat)` | 1 |
| `sw=Freundschaft and sw=Berg and sgt=B (ohne spr/mat)` | 0 |
| `sw=Freundschaft and sgt=B (ohne spr/mat)` | 1348 |
| `sw=Freundschaft and sgt=B and spr=ger (ohne mat)` | 1040 |
| `sw=Freundschaft and sgt=B and mat=books (ohne spr)` | 880 |
| `sw=Concierge and sgt=B (ohne spr/mat)` | 11 |
| `sw=Küste and sw=Erwachsenwerden and sgt=B (ohne spr/mat)` | 0 |
| `sw=Meer and sw=Erwachsenwerden and sgt=B (ohne spr/mat)` | 3 |
| `sw=Meer and sw=Erwachsenwerden` | 2 |
| `sw=Küste and sw=Natur` | 0 |
| `sw=Meer and sw=Natur` | 1 |
| `sw=Meer and sw=Landschaft` | 1 |
| `sw=Küste and sw=Landschaft` | 0 |
| `sw=Natur and sw=Erwachsenwerden` | 0 |
| `sw=Concierge` | 6 |
| `sw=Concierge and sw=Paris` | 5 |
| `sw=Concierge and sw=Bewohner` | 5 |
| `sw=Paris and sw=Zwischenmenschliche Beziehung (ohne Anführungszeichen)` | 17 |
| `sw=Freundschaft and sw=Gebirge` | 0 |
| `sw=Freundschaft and sw=Alpen` | 0 |
| `sw=Freundschaft and sw=Berge` | 0 |
| `sw=Berge and sw=Familie` | 1 |
| `sw=Freundschaft and sw=Familie` | 37 |
| `sw=Freundschaft and sw=Buch` | 0 |
| `sw=Freundschaft and sw=Lesen` | 0 |
| `sw=Buch and sw=Lesen` | 1 |
| `sw=Lesen and sw=Buch and sw=Freundschaft` | 0 |
| `sw=Philosophie and sw=Buch` | 1 |
| `sw=Philosophie and sw=Lesen` | 0 |
| `sw=Philosophie and sw=Sinn` | 4 |
| `sw=Sinn and sw=Buch` | 0 |
| `sw=Lesen and sw=Sinn` | 0 |
| `sw=Küste and sw=Alter` | 0 |
| `sw=Meer and sw=Kunst` | 7 |
| `sw=Meer and sw=Musik` | 1 |
| `sw=Meer and sw=Alter` | 6 |
| `sw=Küste and sw=Kunst` | 1 |
| `sw=Küste and sw=Musik` | 0 |
| `sw=Kunst and sw=Alter` | 0 |
| `sw=Großstadt and sw=Gesellschaft` | 0 |
| `sw=Großstadt and sw=Politik` | 0 |
| `sw=Gesellschaft and sw=Politik` | 5 |
| `sw=Buch and sw=Verschollenheit` | 10 |
| `sw=Barcelona and sw=Buch` | 10 |
| `sw=Barcelona and sw=Verschollenheit` | 10 |
| `sw=Verschollenheit and sw=Autor` | 10 |
| `sw=Berlin-Kreuzberg and sw=Sonderling` | 6 |
| `sw=Berlin-Kreuzberg and sw=Identitätsfindung` | 1 |
| `sw=Sonderling and sw=Identitätsfindung` | 1 |
| `sw=Berlin-Kreuzberg and sw="Geschichte 1989"` | 1 |
| `sw=Dorf and sw=Philosophie` | 3 |
| `sw=Dorf and sw=Buch` | 1 |
| `sw=Dorf and sw=Lesen` | 0 |
| `sw=Dorf and sw=Sinn` | 1 |
| `Einzelbegriffe: Meer 297 · Küste 141 · Natur 77 · Landschaft 214 · Erwachsenwerden 290 · Freundschaft 584 · Berge 20 · Familie 4142 · Buch 655 · Lesen 27 · Philosophie 879 · Sinn 296 · Kunst 354 · Musik 119 · Alter 556 · Großstadt 122 · Gesellschaft 359 · Politik 219 · Dorf 1400` | je Begriff |
| `Einzelbegriffe: Paris 1084 · Concierge 6 · Doppelleben 209 · Bewohner 116 · "Zwischenmenschliche Beziehung" 168 · Barcelona 119 · Autor 78 · Verschollenheit 26 · Junge 3688 · Faszination 102 · Berlin-Kreuzberg 29 · Sonderling 62 · Identitätsfindung 738` | je Begriff |

## 4. Regel für die Abfragen je Buch

- **Q1:** die Zwei-Begriff-Kombination mit den meisten Treffern unter den getesteten Kombinationen des Buches.
- **Q2** (nur ausgewertet, wenn Q1 weniger als 8 passende Treffer lieferte): der spezifischste Einzelbegriff des Buches (wenigste Treffer, mindestens 8), der nicht schon als Q2 eines früheren Buches verwendet wurde.
- Passende Treffer werden in DNB-Reihenfolge übernommen, zuerst aus Q1, dann aus Q2.

## 5. Durchgeführte Abfragen

| Buch | Abfrage | Treffer gesamt | geliefert | ausgewertet | URL |
|---|---|---|---|---|---|
| a01 | `sw=Meer and sw=Erwachsenwerden and sgt=B and spr=ger and mat=books` | 2 | 2 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DMeer%20and%20sw%3DErwachsenwerden%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a01 | `sw=Natur and sgt=B and spr=ger and mat=books` | 77 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DNatur%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a02 | `sw=Paris and sw="Zwischenmenschliche Beziehung" and sgt=B and spr=ger and mat=books` | 17 | 17 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DParis%20and%20sw%3D%22Zwischenmenschliche%20Beziehung%22%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a02 | `sw=Bewohner and sgt=B and spr=ger and mat=books` | 116 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBewohner%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a03 | `sw=Freundschaft and sw=Familie and sgt=B and spr=ger and mat=books` | 37 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DFreundschaft%20and%20sw%3DFamilie%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a03 | `sw=Berge and sgt=B and spr=ger and mat=books` | 20 | 20 | nein (Q1 ≥ 8 passend) | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBerge%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a04 | `sw=Buch and sw=Lesen and sgt=B and spr=ger and mat=books` | 1 | 1 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBuch%20and%20sw%3DLesen%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a04 | `sw=Lesen and sgt=B and spr=ger and mat=books` | 27 | 27 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DLesen%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a05 | `sw=Philosophie and sw=Sinn and sgt=B and spr=ger and mat=books` | 4 | 4 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DPhilosophie%20and%20sw%3DSinn%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a05 | `sw=Sinn and sgt=B and spr=ger and mat=books` | 296 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DSinn%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a06 | `sw=Meer and sw=Kunst and sgt=B and spr=ger and mat=books` | 7 | 7 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DMeer%20and%20sw%3DKunst%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a06 | `sw=Musik and sgt=B and spr=ger and mat=books` | 119 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DMusik%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a07 | `sw=Gesellschaft and sw=Politik and sgt=B and spr=ger and mat=books` | 5 | 5 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DGesellschaft%20and%20sw%3DPolitik%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a07 | `sw=Großstadt and sgt=B and spr=ger and mat=books` | 122 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DGro%C3%9Fstadt%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a08 | `sw=Buch and sw=Verschollenheit and sgt=B and spr=ger and mat=books` | 10 | 10 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBuch%20and%20sw%3DVerschollenheit%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a08 | `sw=Verschollenheit and sgt=B and spr=ger and mat=books` | 26 | 26 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DVerschollenheit%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a09 | `sw=Berlin-Kreuzberg and sw=Sonderling and sgt=B and spr=ger and mat=books` | 6 | 6 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBerlin-Kreuzberg%20and%20sw%3DSonderling%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a09 | `sw=Berlin-Kreuzberg and sgt=B and spr=ger and mat=books` | 29 | 29 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBerlin-Kreuzberg%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a10 | `sw=Dorf and sw=Philosophie and sgt=B and spr=ger and mat=books` | 3 | 3 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DDorf%20and%20sw%3DPhilosophie%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |
| a10 | `sw=Buch and sgt=B and spr=ger and mat=books` | 655 | 30 | ja | https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=sw%3DBuch%20and%20sgt%3DB%20and%20spr%3Dger%20and%20mat%3Dbooks&recordSchema=MARC21-xml&maximumRecords=30 |

## 6. Ausschlussregeln (maschinell angewandt)

1. Keine gedruckte Textausgabe (Leader/007): entfällt praktisch durch `mat=books`.
2. Sprache (041 $a) nicht ausschließlich `ger`: zweisprachige Ausgaben sind ausgeschlossen.
3. ISBN eines Ausgangsbuchs.
4. Kein Verfasser in 100 (Anthologien und Sammelwerke).
5. Verfasser eines Ausgangsbuchs (GND-Nummer oder Name: Myers, Barbery, Cognetti, Henn, Mercier/Bieri, Seethaler, Ruiz Zafón, Regener, Capus).
6. Keine erzählende Prosa: 655 enthält Anthologie, Lyrik, Bildband, Pressendruck, Kinder-/Bilderbücher, Zweisprachige Ausgabe, Kommentar, Aufsatzsammlung oder Geschenkbücher. Ebenfalls ausgeschlossen: weder 655 (Erzählende Literatur, Belletristische Darstellung, Historische Romane, Krimis, Romanhafte Biographien) noch Titel/Zusatz (Roman, Erzählung, Novelle) zeigen erzählende Prosa an.
7. Dublette: dasselbe Werk (gleicher Verfasser und normalisierter Titel oder Einheitstitel 240) kam schon weiter oben vor. Der erste Treffer bleibt; Neuauflagen, Taschenbuch-, Lizenz- und Sonderausgaben fallen weg.
8. Doppelung im Pool: das Werk ist bereits über ein anderes Ausgangsbuch im Pool.
9. Obergrenze: höchstens 8 je Ausgangsbuch und 60 insgesamt. Die passenden Treffer von 10 Büchern hätten die 60 überschritten. Damit kein Buch bevorzugt wird, wurde **reihum** zugeteilt (Rang 1 jedes Buches, dann Rang 2 usw.). So wurde die Grenze von 60 bei **6 Kandidaten je Buch** erreicht. Alle weiteren passenden Treffer sind unten als „Obergrenze erreicht“ vermerkt.

## 7. Kandidaten je Ausgangsbuch

- **a01** (Offene See): d01 Michael Gantenberg – Zwischen allen Wolken (Q1 Rang 1); d11 Henry David Thoreau – Vom Glück, in der Natur zu sein (Q2 Rang 1); d21 Josephine Laloi – Hochzeit in Jakobswalde (Q2 Rang 4); d31 John Lewis-Stempel – Mein Jahr als Jäger und Sammler (Q2 Rang 5); d41 Ada Dorian – Betrunkene Bäume (Q2 Rang 8); d51 Andreas Maier – Bullau (Q2 Rang 11)
- **a02** (Die Eleganz des Igels): d02 Anna Gavalda – Zusammen ist man weniger allein (Q1 Rang 2); d12 Djuna Barnes – Nachtgewächs (Q1 Rang 6); d22 Mazarine Pingeot – Die erste Metro (Q1 Rang 14); d32 Joachim B. Schmidt – In Küstennähe (Q2 Rang 1); d42 Ralf Thenior – Ja, mach nur einen Plan (Q2 Rang 2); d52 Jenny Erpenbeck – Heimsuchung (Q2 Rang 3)
- **a03** (Acht Berge): d03 Julia Kröhn – Die Tochter des Ketzers (Q1 Rang 1); d13 Cecelia Ahern – Zwischen Himmel und Liebe (Q1 Rang 2); d23 Kat Eryn Rubik – Superposition (Q1 Rang 3); d33 Rebecca Maly – Ein Haus am Kahu River (Q1 Rang 4); d43 Sarah Schmidt – Eine Tonne für Frau Scholz (Q1 Rang 5); d53 Gernot Gricksch – Die heldenhaften Jahre der Kirschkernspuckerbande (Q1 Rang 6)
- **a04** (Der Buchspazierer): d04 Alan Bennett – Die souveräne Leserin (Q2 Rang 3); d14 Frédérique Deghelt – Frühstück mit Proust (Q2 Rang 4); d24 Sam Savage – Firmin (Q2 Rang 5); d34 Giwi Margwelaschwili – Der Kantakt (Q2 Rang 9); d44 A. J. Jacobs – Britannica & ich (Q2 Rang 12); d54 Karen Joy Fowler – Der Jane-Austen-Club (Q2 Rang 13)
- **a05** (Das Gewicht der Worte): d05 Francesc Miralles – Daniel und die Sehnsucht nach dem Glück (Q1 Rang 1); d15 Jörg Hannemann – Abstand (Q1 Rang 2); d25 Michael Eichhammer – Solo für Anna (Q1 Rang 4); d35 Paulo Coelho – Veronika beschließt zu sterben (Q2 Rang 1); d45 Thees Uhlmann – Sophia, der Tod und ich (Q2 Rang 3); d55 Nicholas Sparks – Bis zum letzten Tag (Q2 Rang 6)
- **a06** (Strandgut): d06 Tracy Chevalier – Das Mädchen mit dem Perlenohrring (Q1 Rang 1); d16 Avas. Gold – Magnolien Mädchen (Q2 Rang 5); d26 Edith Maria Engelhard – Der Komponist (Q2 Rang 6); d36 Schoppmann Herbert – Error six in India (Q2 Rang 7); d46 Dieter David Seuthe – Frankfurt verboten (Q2 Rang 8); d56 Tonia S. Pöppler – Liebe laut! (Q2 Rang 9)
- **a07** (Das Café ohne Namen): d07 Cesare Pavese – Der Genosse (Q1 Rang 1); d17 Ivan Klíma – Stunde der Stille (Q1 Rang 3); d27 Jonathan Coe – Klassentreffen (Q1 Rang 4); d37 Wilhelm Genazino – Ein Regenschirm für diesen Tag (Q2 Rang 1); d47 Banana Yoshimoto – Kitchen (Q2 Rang 2); d57 Jackie Thomae – Momente der Klarheit (Q2 Rang 3)
- **a08** (Der Schatten des Windes): d08 Susanne Amtsberg – Das Dach der Seligen (Q2 Rang 1); d18 Klaus Merz – Los (Q2 Rang 3); d28 Werner Köhler – Drei Tage im Paradies (Q2 Rang 5); d38 Kim Echlin – In der Mitte des Flusses (Q2 Rang 6); d48 Joseph Gelinek – Die 10. Symphonie (Q2 Rang 7); d58 Petra Hůlová – Endstation Taiga (Q2 Rang 8)
- **a09** (Herr Lehmann): d09 Gerhard Falkner – Apollokalypse (Q2 Rang 3); d19 Wolfgang Haberl – Niemand sagt was (Q2 Rang 4); d29 Serap Pilevneli – Pflegefall (Q2 Rang 5); d39 Deniz Utlu – Die Ungehaltenen (Q2 Rang 6); d49 Susann Rehlein – Auch die Liebe hat drei Seiten (Q2 Rang 8); d59 Sebastian Lehmann – Sebastian oder: das Leben ist nur ein Schluck aus der Flasche der Geschichte (Q2 Rang 10)
- **a10** (Das kleine Haus am Sonnenhang): d10 Angela Huth – Meeresleuchten (Q1 Rang 1); d20 David Christoph Seybold – Die Gelehrten-Verstaigerung (Q2 Rang 1); d30 Sébastien Pérez – Die Hexen von Venedig (Q2 Rang 2); d40 Theodor Fontane – Irrungen, Wirrungen (Q2 Rang 3); d50 Danielle Valentine – Two sides to every murder (Q2 Rang 4); d60 Ray Bradbury – Fahrenheit 451 (Q2 Rang 7)

## 8. Ausschlüsse je Treffer

Alle gelieferten Treffer, die nicht in den Pool kamen, mit Grund.


**a01 Q1** (`sw=Meer and sw=Erwachsenwerden and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 998735051 | Gantenberg, Michael | Zwischen allen Wolken Roman | 2010 | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q1 Rang 1) |

**a01 Q2** (`sw=Natur and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 1265700451 | Dominguez, Fernando | Los niños descubren América del Sur cuentos infantiles | 2022 | nicht (nur) deutschsprachig: 041=['ger', 'spa'] |
| 3 | 1246538946 | Barrett, Andrea | Schiffsfieber Roman | [2022] | keine erzählende Prosa (655: Erzählende Literatur: Anthologien) |
| 6 | 1237829739 | Stockmann, Ingrid Ursula | Rettermaxe in Oppidum | (21. Juli 2021) | keine erzählende Prosa (655: Erzählende Literatur; Jugendbücher ab 12 Jahre; Bilderbücher) |
| 7 | 1171244371 | Lewis-Stempel, John | Mein Jahr als Jäger und Sammler was es wirklich heißt, von der Natur z | 2019 | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q2 Rang 5) |
| 9 | 1148312625 | Spilling-Nöker, Christa | Geh aus, mein Herz, und suche Freud … vom Staunen & Hoffen | [2018] | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 10 | 1116097745 | Dorian, Ada | Betrunkene Bäume Roman | [2017] | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q2 Rang 8) |
| 12 | 1098324803 | Doerr, Anthony | Der Muschelsammler Erzählungen | 2017 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur; Erzählende Literatur: Gegenwartsliteratur ab 1945) |
| 13 | 1079743847 | Behrens, Katja | Roman von einem Feld | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 1051512816 | Schnetzler, Kaspar | Das Modell | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 15 | 1028141319 | Döblin, Alfred | Berge, Meere und Giganten Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 1032760117 | – | Canto do mato = Gesang des Dickichts | 2013 | nicht (nur) deutschsprachig: 041=['ger', 'por'] |
| 17 | 1035385287 | Rosegger, Peter | Rosegger für uns Zeitloses und Aktuelles aus seiner Zeitschrift "Heimg | 2013 | keine erzählende Prosa (655: Anthologie) |
| 18 | 1011687186 | Winter, Jan | Der Duft des Mangobaums Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 19 | 1184300445 | Vahldiek, Carola | Lichtblicke für Auge und Seele | 2012 | keine erzählende Prosa (655: Bildband; Anthologie) |
| 20 | 102638365X | Weber, Andreas | Minima Animalia ein Stundenbuch der Natur | 2012 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur: Anthologien) |
| 21 | 1022398245 | Thoreau, Henry David | Vom Glück, in der Natur zu sein | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q2 Rang 1) |
| 22 | 1016910789 | Thiel, Elisa | Gespräche mit dem Wind | [2011?] | keine erzählende Prosa (655: Bildband) |
| 23 | 1011791692 | – | Zwischenzeiten | 2011 | kein Verfasser (Sammelwerk/Anthologie) |
| 24 | 1002362008 | Winter, Jan | Der Duft des Mangobaums Roman | 2010 | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q2 Rang 18) |
| 25 | 1003243495 | – | Der Maulwurf unter dem Fußballplatz Kinder der 3ten Klassen der Grunds | 2010 | kein Verfasser (Sammelwerk/Anthologie) |
| 26 | 1002118344 | Yaşar Kemal | Die Hähne des Morgenrots | 2010 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 1000210243 | – | Jahreszeiten Haiku, Tanka | 2010 | kein Verfasser (Sammelwerk/Anthologie) |
| 28 | 1002359694 | Thoreau, Henry David | Vom Glück durch die Natur zu gehen | 2010 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 29 | 993929699 | – | Bäume | 2009 | kein Verfasser (Sammelwerk/Anthologie) |
| 30 | 99333928X | Behrens, Katja | Roman von einem Feld | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a01_q2 Rang 13) |

**a02 Q1** (`sw=Paris and sw="Zwischenmenschliche Beziehung" and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1008777749 | Barbery, Muriel | Die Eleganz des Igels Roman | 2011 | Autor eines Ausgangsbuchs |
| 3 | 994170076 | Barbery, Muriel | Die Eleganz des Igels Roman | 2009 | Autor eines Ausgangsbuchs |
| 4 | 994170696 | Barbery, Muriel | Die Eleganz des Igels Roman | 2009 | Autor eines Ausgangsbuchs |
| 5 | 993487998 | Barbery, Muriel | Die Eleganz des Igels Roman | 2009 | Autor eines Ausgangsbuchs |
| 7 | 986852554 | Barbery, Muriel | Die Eleganz des Igels Roman | 2008 | Ausgangsbuch |
| 8 | 988838753 | Gavalda, Anna | Zusammen ist man weniger allein | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 9 | 986634719 | Gavalda, Anna | Zusammen ist man weniger allein Roman | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 10 | 987010077 | Gavalda, Anna | Zusammen ist man weniger allein Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 11 | 980174538 | Gavalda, Anna | Zusammen ist man weniger allein Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 12 | 972783989 | Gavalda, Anna | Zusammen ist man weniger allein Roman | 2005 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 13 | 975981889 | Gavalda, Anna | Zusammen ist man weniger allein Roman | 2005 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 2) |
| 15 | 952815524 | Barnes, Djuna | Nachtgewächs Roman | 1998 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 6) |
| 16 | 870772708 | Barnes, Djuna | Nachtgewächs Roman | 1987 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 6) |
| 17 | 450233502 | Barnes, Djuna | Nachtgewächs Roman | 1959 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q1 Rang 6) |

**a02 Q2** (`sw=Bewohner and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 4 | 1100369597 | Tremain, Rose | Der weite Weg nach Hause Roman | 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 5 | 1081638532 | Sternberg, Emma | Fünf am Meer Roman | 06/2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 6 | 1063908205 | Reinker, Ulrike | Brehm 46 Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 7 | 107033409X | Kincaid, Greg | Ein Hund zu Weihnachten Roman | November 2105 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 8 | 1067536000 | Joens, Nicole | Tal der Tausendnebel | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 9 | 1034597957 | Vanderbeke, Birgit | Die Frau mit dem Hund Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 10 | 105084761X | Scheuermann, Silke | Die Häuser der anderen Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 11 | 104522975X | Breuer, Guido M. | Die Maiskolbenmörder ein Eifel-Krimi | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 1055025308 | Pettersson, Elsa | Eine Liebe auf Gotland Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 1050262786 | Jirgl, Reinhard | Nichts von euch auf Erden Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 1032879777 | Feyerabend, Joachim | Gesichter im Nebel Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 15 | 1038074967 | Koller-Fanconi, Mariolina | Ich, das alte Haus in Cavaglia eine Geschichte aus dem Puschlav | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 1023791595 | Schmidt, Joachim B. | In Küstennähe Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 1) |
| 17 | 1034157248 | Fitz, Anke | Klingel geht nicht, rufen Sie laut Dingdong! die Abenteuer einer uners | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 18 | 1044607920 | Joens, Nicole | Tal der Tausend Nebel Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 8) |
| 19 | 1017747806 | Sebastián, Javier | Der Radfahrer von Tschernobyl Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 20 | 1022326554 | Nicholson, William | Der verborgene Zauber des ganz normalen Lebens Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 21 | 1038290376 | Wittstock, Joachim | Die blaue Kugel Erzählungen über Hermannstädter Gebäude und ihre Bewoh | 2012 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur: Anthologien) |
| 22 | 102221120X | Vanderbeke, Birgit | Die Frau mit dem Hund Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 9) |
| 23 | 1022181033 | Scheuermann, Silke | Die Häuser der anderen Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 10) |
| 24 | 1021808067 | Kincaid, Greg | Ein Hund zu Weihnachten | 2012 | keine erzählende Prosa (655: Belletristische Darstellung; Kinderbücher bis 11 Jahre) |
| 25 | 1028558260 | Kincaid, Greg | Ein Hund zu Weihnachten | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 7) |
| 26 | 1017292574 | Pettersson, Elsa | Eine Liebe auf Gotland Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 12) |
| 27 | 1021755710 | Seidenauer, Gudrun | Hausroman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 28 | 1021807788 | De Paolis, Federica | Ich höre dir zu Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 29 | 1022211994 | Jordan, Noemi | Insel der schwarzen Perlen Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 30 | 1026986427 | Thenior, Ralf | Ja, mach nur einen Plan Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a02_q2 Rang 2) |

**a03 Q1** (`sw=Freundschaft and sw=Familie and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 7 | 1019698950 | Cauley, Harry | Bridie und Finn die Geschichte einer Freundschaft ; Roman | [2012] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 8 | 1017293287 | Hustvedt, Siri | Was ich liebte Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 9 | 1017386951 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 10 | 1011557185 | Jergović, Miljenko | Wolga, Wolga Roman | 2011 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 11 | 998736090 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2010 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 12 | 988666758 | Cauley, Harry | Bridie und Finn die Geschichte einer Freundschaft ; Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 7) |
| 13 | 996356851 | Kröhn, Julia | Die Tochter des Ketzers Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 1) |
| 14 | 99389674X | Kulbach-Fricke, Karina | Die Tuchhändlerin von Köln Roman | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 15 | 994179251 | Baydar, Oya | Verlorene Worte | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 991651537 | Hustvedt, Siri | Was ich liebte Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 17 | 996359680 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 18 | 988747456 | Baydar, Oya | Verlorene Worte Roman | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 15) |
| 19 | 987464329 | Hustvedt, Siri | Was ich liebte Roman | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 20 | 984394028 | Kröhn, Julia | Die Tochter des Ketzers Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 1) |
| 21 | 98237223X | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 22 | 982602472 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 23 | 976599759 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 24 | 981058515 | Ahern, Cecelia | Zwischen Himmel und Liebe Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 2) |
| 25 | 975617095 | Hustvedt, Siri | Was ich liebte Roman | 2005 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 26 | 969401868 | Hustvedt, Siri | Was ich liebte Roman | 2004 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 27 | 971258813 | Hustvedt, Siri | Was ich liebte Roman | 2004 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 28 | 968308694 | Hustvedt, Siri | Was ich liebte Roman | 2003 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 29 | 966085485 | Hustvedt, Siri | Was ich liebte Roman | 2003 | Dublette (anderes Erscheinen desselben Werks, bereits als a03_q1 Rang 8) |
| 30 | 964041642 | Fredriksson, Marianne | Sofia und Anders Roman | 2002 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

**a03 Q2** (`sw=Berge and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1243004975 | Binder, Hannes | Sherlock Holmes - das letzte Problem | 2022 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 2 | 1070259225 | Augstburger, Urs | Kleine Fluchten Roman | [2015] | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 3 | 1059877988 | Jesenko, Herbert | Bergerlebnisse - in den Karawanken und anderswo | © 2014 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 4 | 1044919256 | – | Die Berge Gedichte | 2014 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 5 | 1045299138 | – | Gipfel - Col - Valle Berggeschichten | 2014 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 6 | 1018010823 | – | Die Berge Gedichte | 2012 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 7 | 1011877678 | Monteagudo, David | Ende Roman | 2012 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 8 | 1011636204 | – | Gedichte für Bergfreunde | 2012 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 9 | 102180729X | Bach, Leah | Sanfter Mond über Usambara Roman | 2012 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 10 | 1011167611 | – | Der andere Horizont Kraft und Inspiration aus den Bergen | 2011 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 11 | 1001885783 | Orontes, Peter | Der Seelenhändler historischer Kriminalroman | 2011 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 12 | 1012252191 | – | Erlebnis Bergjagd die besten Geschichten | 2011 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 13 | 1003493785 | Orontes, Peter | Der Seelenhändler | [2010?] | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 14 | 998736864 | – | Über allen Gipfeln eine literarische Reise durchs Gebirge | 2010 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 15 | 991424719 | Orontes, Peter | Der Seelenhändler historischer Kriminalroman | 2009 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 16 | 988523213 | – | Sehnsucht nach den Bergen Schriftstellerinnen im Gebirge | 2008 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 17 | 989186520 | – | Weihnachten in den Bergen die schönsten Geschichten | 2008 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 18 | 986697532 | – | Die schönsten Berggeschichten | 2007 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 19 | 931161320 | – | Das Meer, der Berg, die Wüste Begegnung mit der Ewigkeit | 1993 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |
| 20 | 871387603 | Gregorius | Zwischen Epos und Drama: Ein unbekannter Streit der Töchter Gottes Ers | 1987 | Q2 nicht ausgewertet (Q1 lieferte ≥8 passende Treffer) |

**a04 Q1** (`sw=Buch and sw=Lesen and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1100179119 | Hesse, Heiko | Till Eulenspiegel in Brandenburg  Schelmengeschichten aus Berlin und B | [2016] | keine erzählende Prosa (655: Erzählende Literatur) |

**a04 Q2** (`sw=Lesen and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1100179119 | Hesse, Heiko | Till Eulenspiegel in Brandenburg  Schelmengeschichten aus Berlin und B | [2016] | keine erzählende Prosa (655: Erzählende Literatur) |
| 2 | 1136380981 | – | Das Zweite Polnische Lesebuch Stufen A2 B1 Zweisprachig mit Polnisch-d | 2014 | nicht (nur) deutschsprachig: 041=['ger', 'pol'] |
| 6 | 1018191577 | – | Macht Lesen sexy? Und wenn nicht: was macht es dann? | 2011 | kein Verfasser (Sammelwerk/Anthologie) |
| 7 | 1001932188 | Deghelt, Frédérique | Frühstück mit Proust Roman | 2010 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 4) |
| 8 | 1007773049 | – | Lesealltag | 2010 | kein Verfasser (Sammelwerk/Anthologie) |
| 10 | 994484348 | Bennett, Alan | Die souveräne Leserin | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 3) |
| 11 | 994179227 | Savage, Sam | Firmin ein Rattenleben ; Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 5) |
| 14 | 988630109 | Bennett, Alan | Die souveräne Leserin | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 3) |
| 15 | 993504299 | Bennett, Alan | Die souveräne Leserin | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 3) |
| 16 | 984249796 | Kaufman, Jennifer | Die Tagträumerin Roman | 2008 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 17 | 988848333 | Savage, Sam | Firmin ein Rattenleben ; Roman | 2008 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 5) |
| 18 | 988403374 | Weinrich, Harald | Vom Leben und Lesen der Tiere ein Bestiarium | 2008 | keine erzählende Prosa (655: Bildband; Anthologie; Bildband) |
| 19 | 986930695 | Holl, Norbert Heinrich | Von Leuten, die bei Tisch lesen | 2008 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 20 | 982510675 | Fowler, Karen Joy | Der Jane-Austen-Club Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 13) |
| 21 | 979906091 | Jacobs, A. J. | Britannica & ich von einem, der auszog, der klügste Mensch der Welt zu | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 12) |
| 22 | 979906784 | Kaufman, Jennifer | Die Tagträumerin Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 16) |
| 23 | 977237257 | Blixen, Tania | Die unsterbliche Geschichte | 2006 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 24 | 974161748 | Fowler, Karen Joy | Der Jane-Austen-Club Roman | 2005 | Dublette (anderes Erscheinen desselben Werks, bereits als a04_q2 Rang 13) |
| 25 | 959544879 | Gourio, Jean-Marie | Die Bibliothekarin Roman | 2000 | nicht (nur) deutschsprachig: 041=['ger', 'fre'] |
| 26 | 950786810 | Sefchovich, Sara | Die Herrin der Träume Roman | 1997 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 361772416 | Traven, B. | Der Marsch ins Reich der Caoba ein Kriegsmarsch | 1933 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

**a05 Q1** (`sw=Philosophie and sw=Sinn and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 3 | 1002413079 | Miralles, Francesc | Daniel und die Sehnsucht nach dem Glück Roman | 2010 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q1 Rang 1) |

**a05 Q2** (`sw=Sinn and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 1379671329 | Kasuga, Mitsuko | Akane Immigrantin und Dichterin : die Tanka von Mitsuko Kasuga, eine j | 2025 | nicht (nur) deutschsprachig: 041=['eng', 'ger', 'jpn'] |
| 4 | 1274359678 | – | Mittelhochdeutsche Sangsprüche des 13. Jahrhunderts Mittelhochdeutsch/ | 2024 | nicht (nur) deutschsprachig: 041=['ger', 'gmh'] |
| 5 | 1231378891 | Coelho, Paulo | Veronika beschließt zu sterben Roman | 2022 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 1) |
| 7 | 1212123972 | Marthaler, Roland | Kunst und Künstler vom Talent zum Genie : 6 Vorträge und 1 Schauspiel | [2020] | keine erzählende Prosa (655: Aufsatzsammlung) |
| 8 | 1216760020 | Sepherēs, Giōrgos | Sechs Nächte auf der Akropolis Roman | 2020 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 9 | 1183599277 | Bjerg, Bov | Auerhaus Roman | 2019 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 10 | 1220442771 | Engin-Deniz, Helga | Die Wegbereiterin | [2019] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 11 | 1170498450 | Peters, Christoph | Mitsukos Restaurant Roman | Mai 2019 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 1166179680 | Jensen, Anna | Der Tag an dem ich eine Million manifestierte | 2018 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 1148312625 | Spilling-Nöker, Christa | Geh aus, mein Herz, und suche Freud … vom Staunen & Hoffen | [2018] | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 14 | 1132074819 | Spark, Muriel | Memento Mori Roman | [2018] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 15 | 1119167795 | Bjerg, Bov | Auerhaus Roman | 2017 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 9) |
| 16 | 1147601658 | Armanski, Gerhard | Bittere Liebe. Medeia und die Argonauten | 11.2017 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 17 | 1120516285 | Wellm, Alfred | Morisco Roman | 2017 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 18 | 1131178718 | Uhlmann, Thees | Sophia, der Tod und ich Roman | 2017 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 3) |
| 19 | 1119257115 | Coelho, Paulo | Veronika beschließt zu sterben Roman | 2017 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 1) |
| 20 | 1136965041 | Schrey, Gisela | Versuche Gedichte einer 80-Jährigen | [2017] | keine erzählende Prosa (655: Lyrik, Dramatik) |
| 21 | 1106266005 | Bjerg, Bov | Auerhaus Roman | 2016 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 9) |
| 22 | 1113118261 | Röhrs, Frauke | Beinahe Roman | 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 23 | 1077572565 | Sparks, Nicholas | Bis zum letzten Tag Roman = The choice | 3/2016 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 6) |
| 24 | 1081110392 | Bielmann, David | Freedom Bar Roman | 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 25 | 1106898788 | Wieczorek, Rainer | Kreis und Quadrat eine Melancholie | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 26 | 1099451051 | Jecker Lambreva, Evelina | Nicht mehr Roman | 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 1128679027 | Brauner, Ernst | Struldbrugs eine Chronik aus den ersten Jahrzehnten des dritten Jahrta | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 28 | 1091079439 | Bremer, Lu | Täuschung ein Leben | 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 29 | 1070325465 | Bjerg, Bov | Auerhaus Roman | 2015 | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 9) |
| 30 | 1081461225 | Bjerg, Bov | Auerhaus Roman | [2015?] | Dublette (anderes Erscheinen desselben Werks, bereits als a05_q2 Rang 9) |

**a06 Q1** (`sw=Meer and sw=Kunst and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 994484445 | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |
| 3 | 977257290 | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |
| 4 | 96947993X | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring Roman | 2004 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |
| 5 | 967412242 | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring Roman | 2003 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |
| 6 | 961569328 | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring | 2001 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |
| 7 | 958627290 | Chevalier, Tracy | Das Mädchen mit dem Perlenohrring | 2000 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q1 Rang 1) |

**a06 Q2** (`sw=Musik and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1148138153 | Uhlich, Veronika | Märchen von Musik und Tanz zum Erzählen und Vorlesen | 2018 | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 2 | 1158611072 | Hanstein, Thomas | Wunder gibt es immer wieder 24 Herzensmelodien in neuem Licht | [2018] | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 3 | 1140931199 | Keup, Petra | Das Weltmusik Lesebuch aus Stille (er)schaffen mit Klang und Gesang | 2017 | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 4 | 1136155376 | Vlasova, Marina | Dežavju | 2017 | nicht (nur) deutschsprachig: 041=['rus', 'ger'] |
| 10 | 1070338931 | Roßbacher, Verena | Schwätzen und Schlachten Roman | Februar 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 11 | 1070832421 | Krausser, Helmut | Alles ist gut Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 1062502418 | Degens, Marc | Fuckin Sushi Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 1071474766 | Drenger, Shanghai | Minol-Pirols leben, und nicht leben lassen : Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 1069867225 | – | Musikgedichte | 2015 | kein Verfasser (Sammelwerk/Anthologie) |
| 15 | 106484488X | Schöpf, Alois | Platzkonzert Essay mit Erinnerung | [2015] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 1171763549 | Brandl, Ulrike J. | Setzen Sie sich Gereimtes und Ungereimtes | [2015] | keine erzählende Prosa (655: Lyrik) |
| 17 | 1063359856 | Kreisler, Fritz | Trotz des Tosens der Kanone Frontbericht eines Virtuosen | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 18 | 1045110353 | Bortlik, Wolfgang | Arme Ritter Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 19 | 1044552913 | Sulzer, Alain Claude | Aus den Fugen Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 20 | 1050508033 | Neft, Anselm | Helden in Schnabelschuhen Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 21 | 105119055X | Klug, Gereon | Low Fidelity Hans E. Plattes Briefe gegen den Mainstream + Bonüsse | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 22 | 105060539X | Krausser, Helmut | Melodien oder Nachträge zum quecksilbernen Zeitalter Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 23 | 105132999X | – | Musik ist die Sprache der Engel Anekdoten rund um die Musik | [2014] | kein Verfasser (Sammelwerk/Anthologie) |
| 24 | 1044553294 | Roßbacher, Verena | Schwätzen und schlachten Roman | 2014 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q2 Rang 10) |
| 25 | 1031440259 | Gotschy, Helmut | Der geschenkte Traum Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 26 | 1034177605 | Bokelberg, Nilz | Endlich gute Musik | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 1035787431 | Seuthe, Dieter David | Frankfurt verboten Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q2 Rang 8) |
| 28 | 1022335898 | Sulzer, Alain Claude | Aus den Fugen Roman | 2012 | Dublette (anderes Erscheinen desselben Werks, bereits als a06_q2 Rang 19) |
| 29 | 1022290886 | Mayer, Gina | Das Lied meiner Schwester Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 30 | 1026469546 | Plöger, Stefan | Der Klang der Hingabe | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

**a07 Q1** (`sw=Gesellschaft and sw=Politik and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 1185294724 | Pavese, Cesare | Der Genosse Roman | [2019] | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q1 Rang 1) |
| 5 | 957134991 | Pavese, Cesare | Der Genosse Roman | 1999 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q1 Rang 1) |

**a07 Q2** (`sw=Großstadt and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 4 | 1252816618 | Mezger, Daniel | Land spielen | [2022] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 5 | 127199626X | Genazino, Wilhelm | Leise singende Frauen Roman | 2022 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 6 | 1156552141 | Meyer, Clemens | Die stillen Trabanten Erzählungen | Januar 2019 | keine erzählende Prosa (655: Erzählende Literatur: Gegenwartsliteratur ab 1945) |
| 7 | 1153911523 | Kullmann, Katja | Fortschreitende Herzschmerzen bei milden 18 Grad eine Erzählung | [2018] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 8 | 1156227747 | Erpenbeck, Jenny | Wörterbuch | 2018 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 9 | 1117490475 | Meyer, Clemens | Die stillen Trabanten Erzählungen | [2017] | keine erzählende Prosa (655: Erzählende Literatur: Gegenwartsliteratur ab 1945) |
| 10 | 1096784351 | Liebenow, Flora Mailin | An den Finder | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 11 | 1079489320 | Köhlmeier, Michael | Das Mädchen mit dem Fingerhut Roman | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 1079808183 | Kraske, Michael | Vorhofflimmern | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 1060410788 | Gugić, Sandra | Astronauten Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 1067532315 | Zierhut, Anna | Carla kocht [Roman] | [2015] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 15 | 1050500172 | Haller, Christian | Der seltsame Fremde Roman | 2015 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 107056785X | Thomae, Jackie | Momente der Klarheit Roman | 2015 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 3) |
| 17 | 1050847776 | Meyer, Clemens | Im Stein Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 18 | 1050839196 | Lehmann, Sebastian | Kein Elch. Nirgends Geschichten von Zuhause und von weit weg | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 19 | 1034320319 | Genazino, Wilhelm | Leise singende Frauen Roman | 2014 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 5) |
| 20 | 1045641243 | Genazino, Wilhelm | Leise singende Frauen Roman | 2014 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 5) |
| 21 | 1056018046 | Letocha, Thomas | Oma Else kann's nicht lassen Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 22 | 1044715308 | Winter, Leonie | Unter Umständen verliebt Roman | 2014 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 23 | 1028105606 | Delius, Friedrich Christian | Adenauerplatz Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 24 | 1029100845 | Truschner, Peter | Das fünfunddreißigste Jahr Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 25 | 1028143265 | Haller, Christian | Der seltsame Fremde Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 15) |
| 26 | 1034383477 | Meyer, Clemens | Im Stein Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 17) |
| 27 | 1028147457 | Letocha, Thomas | Oma Else kann's nicht lassen Roman | 2013 | Dublette (anderes Erscheinen desselben Werks, bereits als a07_q2 Rang 21) |
| 28 | 1022506056 | Baum, Antonia | Vollkommen leblos, bestenfalls tot Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 29 | 1028317972 | Genazino, Wilhelm | Wenn wir Tiere wären Roman | 2013 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 30 | 1017526656 | Beckerhoff, Florian | Das Landei Roman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

**a08 Q1** (`sw=Buch and sw=Verschollenheit and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1017663777 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2012 | Autor eines Ausgangsbuchs |
| 2 | 1008351393 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2011 | Autor eines Ausgangsbuchs |
| 3 | 99078990X | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2008 | Autor eines Ausgangsbuchs |
| 4 | 982314159 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2007 | Autor eines Ausgangsbuchs |
| 5 | 987010298 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2007 | Autor eines Ausgangsbuchs |
| 6 | 979730643 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2006 | Autor eines Ausgangsbuchs |
| 7 | 975188593 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2005 | Autor eines Ausgangsbuchs |
| 8 | 97084977X | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | [2004?] | Autor eines Ausgangsbuchs |
| 9 | 971536244 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2004 | Autor eines Ausgangsbuchs |
| 10 | 967934273 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2003 | Ausgangsbuch |

**a08 Q2** (`sw=Verschollenheit and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 1017663777 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2012 | Autor eines Ausgangsbuchs |
| 4 | 1008351393 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2011 | Autor eines Ausgangsbuchs |
| 9 | 994944675 | Echlin, Kim | Der verschollene Liebhaber Roman | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 10 | 991841050 | Gelinek, Joseph | Die 10. Symphonie Thriller | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a08_q2 Rang 7) |
| 11 | 991522303 | Carvalho, Bernardo | In São Paulo geht die Sonne unter Roman | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 988534770 | Carvalho, Bernardo | Mongólia Roman | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 984042822 | Filastò, Nino | Das Eden-Alphabet Roman | 2008 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 99078990X | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2008 | Autor eines Ausgangsbuchs |
| 15 | 989298582 | Tambornino, Rico | Jakobs gestörtes Verhältnis zum Schnee Roman | 2008 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 982314159 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2007 | Autor eines Ausgangsbuchs |
| 17 | 987010298 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2007 | Autor eines Ausgangsbuchs |
| 18 | 97983810X | Degli Antoni, Piero | Eisesstille Thriller | 2007 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 19 | 982518730 | Carvalho, Bernardo | Mongólia Roman | 2007 | Dublette (anderes Erscheinen desselben Werks, bereits als a08_q2 Rang 12) |
| 20 | 977044203 | Filastò, Nino | Das Eden-Alphabet Roman | 2006 | Dublette (anderes Erscheinen desselben Werks, bereits als a08_q2 Rang 13) |
| 21 | 979730643 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2006 | Autor eines Ausgangsbuchs |
| 22 | 975188593 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2005 | Autor eines Ausgangsbuchs |
| 23 | 97084977X | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | [2004?] | Autor eines Ausgangsbuchs |
| 24 | 971536244 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2004 | Autor eines Ausgangsbuchs |
| 25 | 967934273 | Ruiz Zafón, Carlos | Der Schatten des Windes Roman | 2003 | Ausgangsbuch |
| 26 | 963918966 | Velikić, Dragan | Der Fall Bremen Roman | 2002 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

**a09 Q1** (`sw=Berlin-Kreuzberg and sw=Sonderling and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1380081777 | Regener, Sven | Der kleine Bruder Roman | Juni 2026 | Autor eines Ausgangsbuchs |
| 2 | 1380088550 | Regener, Sven | Herr Lehmann ein Roman | Juni 2026 | Autor eines Ausgangsbuchs |
| 3 | 998864552 | Regener, Sven | Der kleine Bruder Roman | 2010 | Autor eines Ausgangsbuchs |
| 4 | 993489168 | Regener, Sven | Der kleine Bruder Roman | 2009 | Autor eines Ausgangsbuchs |
| 5 | 988573245 | Regener, Sven | Der kleine Bruder Roman | 2008 | Autor eines Ausgangsbuchs |
| 6 | 991990366 | Regener, Sven | Der kleine Bruder Roman | 2008 | Autor eines Ausgangsbuchs |

**a09 Q2** (`sw=Berlin-Kreuzberg and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 1 | 1380081777 | Regener, Sven | Der kleine Bruder Roman | Juni 2026 | Autor eines Ausgangsbuchs |
| 2 | 1380088550 | Regener, Sven | Herr Lehmann ein Roman | Juni 2026 | Autor eines Ausgangsbuchs |
| 7 | 1034689010 | Bittermann, Klaus | Alles schick in Kreuzberg unter Touristen, Pennern, Gentrifzierten | 2013 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur: Anthologien; Erzählende Literatur) |
| 9 | 102250634X | Bittermann, Klaus | Möbel zu Hause, aber kein Geld für Alkohol Kreuzberger Szenen | 2013 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur) |
| 11 | 1018517995 | Rüster, Susanne | Der letzte Tanz Kreuzberg explosiv! ; Kriminalroman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 12 | 1021117811 | Mahler, Thomas | In der Schlange mein Jahr auf Hartz IV | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 13 | 1022454013 | Wachlin, Oliver G. | Kreuzberg Kriminalroman | 2012 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 14 | 1017058652 | Korfmann, Hans W. | Der Herr D. die Erlebnisse eines Neukreuzbergers | 2011 | keine erzählende Prosa (655: Anthologie) |
| 15 | 1010456598 | Lehmkuhl, Petra | Dürfen ist Pflicht Roman | 2011 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 16 | 1008781916 | Mahler, Thomas | In der Schlange mein Jahr auf Hartz IV | 2011 | Dublette (anderes Erscheinen desselben Werks, bereits als a09_q2 Rang 12) |
| 17 | 101195754X | Bittermann, Klaus | Möbel zu Hause, aber kein Geld für Alkohol Kreuzberger Szenen | 2011 | keine erzählende Prosa (655: Anthologie; Erzählende Literatur) |
| 18 | 1008477915 | Lehmann, Sebastian | Sebastian oder: das Leben ist nur ein Schluck aus der Flasche der Gesc | 2011 | Dublette (anderes Erscheinen desselben Werks, bereits als a09_q2 Rang 10) |
| 19 | 998096628 | Sönmez, Sila | Das Ghetto-Sex-Tagebuch Roman | 2010 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 20 | 998864552 | Regener, Sven | Der kleine Bruder Roman | 2010 | Autor eines Ausgangsbuchs |
| 21 | 998413518 | Rothmann, Ralf | Feuer brennt nicht Roman | 2010 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 22 | 998801658 | Sezgin, Hilal | Mihriban pfeift auf Gott Roman | 2010 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 23 | 993489168 | Regener, Sven | Der kleine Bruder Roman | 2009 | Autor eines Ausgangsbuchs |
| 24 | 99933798X | Rothmann, Ralf | Feuer brennt nicht Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a09_q2 Rang 21) |
| 25 | 991399420 | Rothmann, Ralf | Feuer brennt nicht Roman | 2009 | Dublette (anderes Erscheinen desselben Werks, bereits als a09_q2 Rang 21) |
| 26 | 994393334 | Ebertowski, Jürgen | Tränenpalast Kriminalroman | 2009 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 988573245 | Regener, Sven | Der kleine Bruder Roman | 2008 | Autor eines Ausgangsbuchs |
| 28 | 991990366 | Regener, Sven | Der kleine Bruder Roman | 2008 | Autor eines Ausgangsbuchs |
| 29 | 990887367 | Hoffmann, Gerhardt | Kreuzberger Geschichten Erzählungen aus dem Milieu | 2008 | keine erzählende Prosa (655: Anthologie) |

**a10 Q1** (`sw=Dorf and sw=Philosophie and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 2 | 959030956 | Huth, Angela | Meeresleuchten Roman | 2000 | Dublette (anderes Erscheinen desselben Werks, bereits als a10_q1 Rang 1) |
| 3 | 954667913 | Huth, Angela | Meeresleuchten Roman | 1998 | Dublette (anderes Erscheinen desselben Werks, bereits als a10_q1 Rang 1) |

**a10 Q2** (`sw=Buch and sgt=B and spr=ger and mat=books`)

| Rang | IDN | Verfasser | Titel | Jahr | Grund |
|---|---|---|---|---|---|
| 5 | 1325501808 | – | Edward Gorey - Großmeister des Kuriosen | November 2024 | kein Verfasser (Sammelwerk/Anthologie) |
| 6 | 1336021209 | Riemer-Buddecke, Elke | E.T.A. Hoffmann - Porträts und Illustrationen | [2024] | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 8 | 128336591X | Am Ende, Matthias | 3000 Jahre altes Wissen für heute neu entdecken 1000 Sprüche mit 500 K | [2023] | keine erzählende Prosa (655: Anthologie) |
| 9 | 1300663324 | Frei, Peter Thomas | Jeschua - ich bin eine dichterische Übersetzung und Betrachtung des Ma | [2023] | keine erzählende Prosa (655: Kommentar) |
| 10 | 1259639193 | Ransmayr, Christoph | Unter einem Zuckerhimmel Balladen und Gedichte | [2022] | keine erzählende Prosa (655: Lyrik) |
| 11 | 1239077297 | Heeke, Rainer | Die Praktikantin, le Bookinist & de Boekenstad | 2021 | nicht (nur) deutschsprachig: 041=['ger', 'dut', 'eng'] |
| 12 | 1233893092 | Frei, Peter Thomas | Jeschua - vom Mut zur Wahrhaftigkeit eine dichterische Übersetzung und | [2021] | keine erzählende Prosa (655: Kommentar) |
| 13 | 1246984008 | Aeschbacher-Sinecká, Helena | Träume Gedichte und Aquarelle | [2021] | keine erzählende Prosa (655: Lyrik) |
| 14 | 1208021176 | Bradbury, Ray | Fahrenheit 451 Roman | 2020 | Dublette (anderes Erscheinen desselben Werks, bereits als a10_q2 Rang 7) |
| 15 | 1212039254 | Mohnnau, Ralph Günther | Tag um Tag faltet sich die Zeit 99 Haiku | 2020 | nicht (nur) deutschsprachig: 041=['ger', 'jpn'] |
| 16 | 1192776593 | Hennig, Falko | Alles nur geklaut Roman | [2019] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 17 | 118683076X | Bloesch, Hans | "Das Buch" ein Gemeinschaftsprojekt von 1902-1905 : Faksimile und Tran | 2019 | nicht (nur) deutschsprachig: 041=['ger', 'eng'] |
| 18 | 1201501725 | Omansen, Rudolf | George Grosz, Rudolf Omansen und ein Huhn wie es zur letzten Illustrat | 2019 | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 19 | 1148962972 | Voltaire | Candide oder Die beste Welt | 2018 | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 20 | 1141703793 | Kredel, Fritz | Das kleine Buch der Vögel und Nester | 2018 | keine erzählende Prosa (655: Geschenkbücher) |
| 21 | 1155772318 | Domínguez, Carlos María | Das Papierhaus Erzählung | 2018 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 22 | 117291964X | Cesaro, Ingo | Dass unsere Fantasie jubelt = Our fantasies rejoice | 2018 | nicht (nur) deutschsprachig: 041=['geo', 'ger', 'eng'] |
| 23 | 1201582210 | Strugalla, Johannes | Der gespiegelte Schmetterlingsflug = Le reflet d'un vol de papillon | [2018] | nicht (nur) deutschsprachig: 041=['ger', 'fre'] |
| 24 | 1168596335 | Brentano, Clemens | Eulenkind | Frühjahr 2018 | keine erzählende Prosa (655: Pressendruck) |
| 25 | 1159917752 | Roth, Tobias | Grotesken von Sabbioneta | 2018 | keine erzählende Prosa (655: Erzählende Literatur: Gegenwartsliteratur ab 1945) |
| 26 | 1147304955 | Hartlieb, Petra | Meine wundervolle Buchhandlung | 2018 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 27 | 1148673695 | Bischoff, Xandi | Psalmen destillieren alte Gebete neu lesen | [2018] | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 28 | 1148999760 | Morgenstern, Christian | Die Mitternachtsmaus Galgenlieder & Notturnos | 2017 | Gattung nicht als erzählende Prosa erkennbar (655 leer/abweichend) |
| 29 | 1070853089 | Montasser, Thomas | Ein ganz besonderes Jahr Roman | Januar 2016 | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |
| 30 | 1098441788 | Buch, Hans Christoph | Elf Arten, das Eis zu brechen Roman | [2016] | Obergrenze erreicht (8 je Ausgangsbuch bzw. 60 gesamt) |

## 9. Bibliografische Felder und `thema`

- `titel` (245 $a), `autor` (100 $a, invertiert), `isbn` (erste ISBN-13 aus 020), `jahr` (264/260 $c), `verlag` (264/260 $b), `seiten` (300 $a). Quelle jeweils `https://d-nb.info/<IDN>` des übernommenen Datensatzes, also der im Rang ersten Ausgabe. Das kann ein Taschenbuch- oder Neudruck sein, nicht unbedingt die deutsche Erstausgabe.
- `laenge` wird aus `seiten` berechnet (< 250 kurz, 250–450 mittel, > 450 lang).
- `genre`: „Krimi & Thriller“ bei 655 Krimis oder Thriller/Krimi im Titel; „Historischer Roman“ bei 655 Historische Romane oder Zusatz „historischer Roman“; „Biografie & Erinnerungen“ bei 655 Romanhafte Biographien; „Klassiker“ bei 655 „Hauptwerk vor 1945“; „Roman / Gegenwart“, wenn der Titel oder Zusatz Roman, Erzählung oder Novelle nennt. Sonst `null`.
- `thema`: GND-Schlagwörter (689/650/651) des Kandidaten, über eine feste Zuordnungstabelle auf die Schema-Liste abgebildet (höchstens 3, in Reihenfolge der Schlagwörter). Städte wie Paris, Berlin(-Kreuzberg), Wien, Madrid, Boston, Leipzig, Dortmund, Frankfurt und Santiago de Chile zählen als „Großstadt“. Chronologische Schlagwörter („Geschichte 19xx“) zählen als „Geschichte“. Personenbezeichnungen ohne Themenbezug (z. B. Redakteur, Ärztin, Geograf) werden nicht zugeordnet. Hat ein Kandidat keine zuordenbaren GND-Schlagwörter, ist `thema` = `null` (2 Fälle: d30, d40).
- Einzelfälle: d36 Verfasser laut DNB „Herbert, Schoppmann“ (auch 245 $c: „Schoppmann Herbert“), unverändert übernommen. d16 „Avas. Gold“ ist zugleich als Verfasser und Verlag erfasst.

## 10. Redaktionelle Merkmale (tempo, ton, fokus, sprache, inhalt)

Höchstens 3 Abrufe je Kandidat, in fester Reihenfolge: (1) Perlentaucher-Buchseite nach URL-Schema `/buch/<autor>/<titel>.html`, (2) de.wikipedia `<Titel>`, (3) de.wikipedia `<Titel>_(Roman)` oder, bei einer Begriffsklärungsseite, der dort verlinkte Romanartikel. Wikipedia antwortete mehrfach mit HTTP 429 (Rate-Limit). Diese Anfragen ohne Inhalt wurden einmal wiederholt und sind als „Wiederholung nach 429“ vermerkt. Ein Wert wurde nur gesetzt, wenn der Text ihn ausdrücklich stützt (Beleg unten). Sonst bleibt er `null`.

| ID | Abrufe (URL → Status) | gesetzte Felder | Beleg |
|---|---|---|---|
| d01 | https://www.perlentaucher.de/buch/michael-gantenberg/zwischen-allen-wolken.html → 404<br>https://de.wikipedia.org/wiki/Zwischen_allen_Wolken → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Zwischen_allen_Wolken_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d02 | https://www.perlentaucher.de/buch/anna-gavalda/zusammen-ist-man-weniger-allein.html → 200<br>https://de.wikipedia.org/wiki/Zusammen_ist_man_weniger_allein → 200 | ton=['humorvoll', 'warm'] | Klappentext „mit Charme und Witz“; FAZ: Umgang mit den Protagonisten mit „Güte“ und Ironie |
| d03 | https://www.perlentaucher.de/buch/julia-kroehn/die-tochter-des-ketzers.html → 404<br>https://de.wikipedia.org/wiki/Die_Tochter_des_Ketzers → 404<br>https://de.wikipedia.org/wiki/Die_Tochter_des_Ketzers_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d04 | https://www.perlentaucher.de/buch/alan-bennett/die-souveraene-leserin.html → 200<br>https://de.wikipedia.org/wiki/Die_souver%C3%A4ne_Leserin → 200 | ton=['humorvoll', 'warm'], fokus=ideen, sprache=schlicht | SZ „hinreißend komisch“, FR „ungemein liebevoll“, „Schlichtheit, Raffinesse“; „erforscht … die Natur des Lesens“ (Gedankenspiel) |
| d05 | https://www.perlentaucher.de/buch/francesc-miralles/daniel-und-die-sehnsucht-nach-dem-glueck.html → 404<br>https://de.wikipedia.org/wiki/Daniel_und_die_Sehnsucht_nach_dem_Gl%C3%BCck → 404<br>https://de.wikipedia.org/wiki/Daniel_und_die_Sehnsucht_nach_dem_Gl%C3%BCck_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d06 | https://www.perlentaucher.de/buch/tracy-chevalier/das-maedchen-mit-dem-perlenohrring.html → 404<br>https://de.wikipedia.org/wiki/Das_M%C3%A4dchen_mit_dem_Perlenohrring → 200<br>https://de.wikipedia.org/wiki/Das_M%C3%A4dchen_mit_dem_Perlenohrring_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d07 | https://www.perlentaucher.de/buch/cesare-pavese/der-genosse.html → 404<br>https://de.wikipedia.org/wiki/Der_Genosse → 404<br>https://de.wikipedia.org/wiki/Der_Genosse_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d08 | https://www.perlentaucher.de/buch/susanne-amtsberg/das-dach-der-seligen.html → 404<br>https://de.wikipedia.org/wiki/Das_Dach_der_Seligen → 404<br>https://de.wikipedia.org/wiki/Das_Dach_der_Seligen_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d09 | https://www.perlentaucher.de/buch/gerhard-falkner/apollokalypse.html → 200<br>https://de.wikipedia.org/wiki/Apollokalypse → 404<br>https://de.wikipedia.org/wiki/Apollokalypse_%28Roman%29 → 404 | tempo=rasant, ton=['humorvoll'], sprache=verspielt | Welt: „Alles läuft sehr hochtourig“; FAZ: „Verspielt, humorvoll, sprachgewandt“ |
| d10 | https://www.perlentaucher.de/buch/angela-huth/meeresleuchten.html → 404<br>https://de.wikipedia.org/wiki/Meeresleuchten → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Meeresleuchten_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d11 | https://www.perlentaucher.de/buch/henry-david-thoreau/vom-glueck-in-der-natur-zu-sein.html → 404<br>https://de.wikipedia.org/wiki/Vom_Gl%C3%BCck%2C_in_der_Natur_zu_sein → 404<br>https://de.wikipedia.org/wiki/Vom_Gl%C3%BCck%2C_in_der_Natur_zu_sein_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d12 | https://www.perlentaucher.de/buch/djuna-barnes/nachtgewaechs.html → 404<br>https://de.wikipedia.org/wiki/Nachtgew%C3%A4chs → 404<br>https://de.wikipedia.org/wiki/Nachtgew%C3%A4chs_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d13 | https://www.perlentaucher.de/buch/cecelia-ahern/zwischen-himmel-und-liebe.html → 404<br>https://de.wikipedia.org/wiki/Zwischen_Himmel_und_Liebe → 404<br>https://de.wikipedia.org/wiki/Zwischen_Himmel_und_Liebe_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d14 | https://www.perlentaucher.de/buch/frederique-deghelt/fruehstueck-mit-proust.html → 404<br>https://de.wikipedia.org/wiki/Fr%C3%BChst%C3%BCck_mit_Proust → 404<br>https://de.wikipedia.org/wiki/Fr%C3%BChst%C3%BCck_mit_Proust_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d15 | https://www.perlentaucher.de/buch/joerg-hannemann/abstand.html → 404<br>https://de.wikipedia.org/wiki/Abstand → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Abstand_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d16 | https://www.perlentaucher.de/buch/avas-gold/magnolien-maedchen.html → 404<br>https://de.wikipedia.org/wiki/Magnolien_M%C3%A4dchen → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Magnolien_M%C3%A4dchen_%28Roman%29 → 404 (Wiederholung nach 429) | – | keine verwertbare Quelle zum Werk gefunden |
| d17 | https://www.perlentaucher.de/buch/ivan-klima/stunde-der-stille.html → 200<br>https://de.wikipedia.org/wiki/Stunde_der_Stille → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Stunde_der_Stille_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d18 | https://www.perlentaucher.de/buch/klaus-merz/los.html → 200<br>https://de.wikipedia.org/wiki/Los → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Los_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d19 | https://www.perlentaucher.de/buch/wolfgang-haberl/niemand-sagt-was.html → 404<br>https://de.wikipedia.org/wiki/Niemand_sagt_was → 404<br>https://de.wikipedia.org/wiki/Niemand_sagt_was_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d20 | https://www.perlentaucher.de/buch/david-christoph-seybold/die-gelehrten-verstaigerung.html → 404<br>https://de.wikipedia.org/wiki/Die_Gelehrten-Verstaigerung → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Die_Gelehrten-Verstaigerung_%28Roman%29 → 404 (Wiederholung nach 429) | – | keine verwertbare Quelle zum Werk gefunden |
| d21 | https://www.perlentaucher.de/buch/josephine-laloi/hochzeit-in-jakobswalde.html → 404<br>https://de.wikipedia.org/wiki/Hochzeit_in_Jakobswalde → 404<br>https://de.wikipedia.org/wiki/Hochzeit_in_Jakobswalde_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d22 | https://www.perlentaucher.de/buch/mazarine-pingeot/die-erste-metro.html → 404<br>https://de.wikipedia.org/wiki/Die_erste_Metro → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Die_erste_Metro_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d23 | https://www.perlentaucher.de/buch/kat-eryn-rubik/superposition.html → 404<br>https://de.wikipedia.org/wiki/Superposition → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Superposition_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d24 | https://www.perlentaucher.de/buch/sam-savage/firmin.html → 404<br>https://de.wikipedia.org/wiki/Firmin → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Firmin_%28Roman%29 → 200 | ton=['heiter', 'melancholisch'] | Wikipedia: „ernste und melancholische Sprache … Es überwiegt jedoch ein launig-heiterer Ton“ |
| d25 | https://www.perlentaucher.de/buch/michael-eichhammer/solo-fuer-anna.html → 404<br>https://de.wikipedia.org/wiki/Solo_f%C3%BCr_Anna → 404<br>https://de.wikipedia.org/wiki/Solo_f%C3%BCr_Anna_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d26 | https://www.perlentaucher.de/buch/edith-maria-engelhard/der-komponist.html → 404<br>https://de.wikipedia.org/wiki/Der_Komponist → 404<br>https://de.wikipedia.org/wiki/Der_Komponist_%28Roman%29 → 404 (Wiederholung nach 429) | – | keine verwertbare Quelle zum Werk gefunden |
| d27 | https://www.perlentaucher.de/buch/jonathan-coe/klassentreffen.html → 200<br>https://de.wikipedia.org/wiki/Klassentreffen → 200 | – | keine verwertbare Quelle zum Werk gefunden |
| d28 | https://www.perlentaucher.de/buch/werner-koehler/drei-tage-im-paradies.html → 200<br>https://de.wikipedia.org/wiki/Drei_Tage_im_Paradies → 404<br>https://de.wikipedia.org/wiki/Drei_Tage_im_Paradies_%28Roman%29 → 404 (Wiederholung nach 429) | ton=['humorvoll'] | FAZ: „augenzwinkernd“, „ironisierte Geschichte“ |
| d29 | https://www.perlentaucher.de/buch/serap-pilevneli/pflegefall.html → 404<br>https://de.wikipedia.org/wiki/Pflegefall → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Pflegefall_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d30 | https://www.perlentaucher.de/buch/sebastien-perez/die-hexen-von-venedig.html → 404<br>https://de.wikipedia.org/wiki/Die_Hexen_von_Venedig → 404<br>https://de.wikipedia.org/wiki/Die_Hexen_von_Venedig_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d31 | https://www.perlentaucher.de/buch/john-lewis-stempel/mein-jahr-als-jaeger-und-sammler.html → 200<br>https://de.wikipedia.org/wiki/Mein_Jahr_als_J%C3%A4ger_und_Sammler → 404<br>https://de.wikipedia.org/wiki/Mein_Jahr_als_J%C3%A4ger_und_Sammler_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d32 | https://www.perlentaucher.de/buch/joachim-b-schmidt/in-kuestennaehe.html → 404<br>https://de.wikipedia.org/wiki/In_K%C3%BCstenn%C3%A4he → 404<br>https://de.wikipedia.org/wiki/In_K%C3%BCstenn%C3%A4he_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d33 | https://www.perlentaucher.de/buch/rebecca-maly/ein-haus-am-kahu-river.html → 404<br>https://de.wikipedia.org/wiki/Ein_Haus_am_Kahu_River → 404<br>https://de.wikipedia.org/wiki/Ein_Haus_am_Kahu_River_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d34 | https://www.perlentaucher.de/buch/giwi-margwelaschwili/der-kantakt.html → 200<br>https://de.wikipedia.org/wiki/Der_Kantakt → 404<br>https://de.wikipedia.org/wiki/Der_Kantakt_%28Roman%29 → 404 | ton=['humorvoll'], fokus=ideen, sprache=verspielt | FAZ: „witzigsten“, „versponnene“ Werk; „Metabuch“, „Ontotextologie“ |
| d35 | https://www.perlentaucher.de/buch/paulo-coelho/veronika-beschliesst-zu-sterben.html → 200<br>https://de.wikipedia.org/wiki/Veronika_beschlie%C3%9Ft_zu_sterben → 200 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Veronika_beschlie%C3%9Ft_zu_sterben_%28Roman%29 → 404 | fokus=ideen, inhalt=['suizid'] | Wikipedia: Roman „wie ein Lehrstück aufgebaut“ (Sinnsuche); Inhalt: Suizidversuch der Hauptfigur |
| d36 | https://www.perlentaucher.de/buch/schoppmann-herbert/error-six-in-india.html → 404<br>https://de.wikipedia.org/wiki/Error_six_in_India → 404<br>https://de.wikipedia.org/wiki/Error_six_in_India_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d37 | https://www.perlentaucher.de/buch/wilhelm-genazino/ein-regenschirm-fuer-diesen-tag.html → 200<br>https://de.wikipedia.org/wiki/Ein_Regenschirm_f%C3%BCr_diesen_Tag → 200 | tempo=ruhig, ton=['melancholisch', 'humorvoll'] | Kurier (zit. Wikipedia): „Leise ironisch … ohne Angst vor der Langsamkeit … Mit Action, mit Tempo hat dieser brillante Erzähler nichts am Schuh“, Melancholie; taz: „subtiler Humor“ |
| d38 | https://www.perlentaucher.de/buch/kim-echlin/in-der-mitte-des-flusses.html → 404<br>https://de.wikipedia.org/wiki/In_der_Mitte_des_Flusses → 404<br>https://de.wikipedia.org/wiki/In_der_Mitte_des_Flusses_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d39 | https://www.perlentaucher.de/buch/deniz-utlu/die-ungehaltenen.html → 404<br>https://de.wikipedia.org/wiki/Die_Ungehaltenen → 404<br>https://de.wikipedia.org/wiki/Die_Ungehaltenen_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d40 | https://www.perlentaucher.de/buch/theodor-fontane/irrungen-wirrungen.html → 404<br>https://de.wikipedia.org/wiki/Irrungen%2C_Wirrungen → 200 | – | keine verwertbare Quelle zum Werk gefunden |
| d41 | https://www.perlentaucher.de/buch/ada-dorian/betrunkene-baeume.html → 200<br>https://de.wikipedia.org/wiki/Betrunkene_B%C3%A4ume → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Betrunkene_B%C3%A4ume_%28Roman%29 → 404 (Wiederholung nach 429) | sprache=poetisch | Verlagstext: „Berührend und poetisch beschreibt Ada Dorian …“ |
| d42 | https://www.perlentaucher.de/buch/ralf-thenior/ja-mach-nur-einen-plan.html → 404<br>https://de.wikipedia.org/wiki/Ja%2C_mach_nur_einen_Plan → 404<br>https://de.wikipedia.org/wiki/Ja%2C_mach_nur_einen_Plan_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d43 | https://www.perlentaucher.de/buch/sarah-schmidt/eine-tonne-fuer-frau-scholz.html → 404<br>https://de.wikipedia.org/wiki/Eine_Tonne_f%C3%BCr_Frau_Scholz → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Eine_Tonne_f%C3%BCr_Frau_Scholz_%28Roman%29 → 404 (Wiederholung nach 429) | – | keine verwertbare Quelle zum Werk gefunden |
| d44 | https://www.perlentaucher.de/buch/a-j-jacobs/britannica-ich.html → 404<br>https://de.wikipedia.org/wiki/Britannica_%26_ich → 404<br>https://de.wikipedia.org/wiki/Britannica_%26_ich_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d45 | https://www.perlentaucher.de/buch/thees-uhlmann/sophia-der-tod-und-ich.html → 200<br>https://de.wikipedia.org/wiki/Sophia%2C_der_Tod_und_ich → 200 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Sophia%2C_der_Tod_und_ich_%28Roman%29 → 429 | ton=['humorvoll', 'melancholisch'] | FAZ: „amüsant“, „witzige Dialoge“, „im Grunde … die traurige Geschichte eines Enddreißigers“ |
| d46 | https://www.perlentaucher.de/buch/dieter-david-seuthe/frankfurt-verboten.html → 404<br>https://de.wikipedia.org/wiki/Frankfurt_verboten → 404<br>https://de.wikipedia.org/wiki/Frankfurt_verboten_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d47 | https://www.perlentaucher.de/buch/banana-yoshimoto/kitchen.html → 404<br>https://de.wikipedia.org/wiki/Kitchen → 200<br>https://de.wikipedia.org/wiki/Kitchen_%28Roman%29 → 200 | fokus=figuren | NYT (zit. Wikipedia): Fähigkeit, „die Herzen ihrer Charaktere zu durchdringen“ |
| d48 | https://www.perlentaucher.de/buch/joseph-gelinek/die-10-symphonie.html → 404<br>https://de.wikipedia.org/wiki/Die_10._Symphonie → 404<br>https://de.wikipedia.org/wiki/Die_10._Symphonie_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d49 | https://www.perlentaucher.de/buch/susann-rehlein/auch-die-liebe-hat-drei-seiten.html → 404<br>https://de.wikipedia.org/wiki/Auch_die_Liebe_hat_drei_Seiten → 404<br>https://de.wikipedia.org/wiki/Auch_die_Liebe_hat_drei_Seiten_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d50 | https://www.perlentaucher.de/buch/danielle-valentine/two-sides-to-every-murder.html → 404<br>https://de.wikipedia.org/wiki/Two_sides_to_every_murder → 404<br>https://de.wikipedia.org/wiki/Two_sides_to_every_murder_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d51 | https://www.perlentaucher.de/buch/andreas-maier/bullau.html → 404<br>https://de.wikipedia.org/wiki/Bullau → nicht dieses Werk<br>https://de.wikipedia.org/wiki/Bullau_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d52 | https://www.perlentaucher.de/buch/jenny-erpenbeck/heimsuchung.html → 200<br>https://de.wikipedia.org/wiki/Heimsuchung → 200<br>https://de.wikipedia.org/wiki/Heimsuchung_%28Roman%29 → 200 | sprache=poetisch | FAZ (zit. Wikipedia): „schlackenlose, poetisch beherrschte Sprachkunst“ |
| d53 | https://www.perlentaucher.de/buch/gernot-gricksch/die-heldenhaften-jahre-der-kirschkernspuckerbande.html → 404<br>https://de.wikipedia.org/wiki/Die_heldenhaften_Jahre_der_Kirschkernspuckerbande → 404<br>https://de.wikipedia.org/wiki/Die_heldenhaften_Jahre_der_Kirschkernspuckerbande_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d54 | https://www.perlentaucher.de/buch/karen-joy-fowler/der-jane-austen-club.html → 404<br>https://de.wikipedia.org/wiki/Der_Jane-Austen-Club → 200<br>https://de.wikipedia.org/wiki/Der_Jane-Austen-Club_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d55 | https://www.perlentaucher.de/buch/nicholas-sparks/bis-zum-letzten-tag.html → 404<br>https://de.wikipedia.org/wiki/Bis_zum_letzten_Tag → 404<br>https://de.wikipedia.org/wiki/Bis_zum_letzten_Tag_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d56 | https://www.perlentaucher.de/buch/tonia-s-poeppler/liebe-laut.html → 404<br>https://de.wikipedia.org/wiki/Liebe_laut%21 → 404<br>https://de.wikipedia.org/wiki/Liebe_laut%21_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d57 | https://www.perlentaucher.de/buch/jackie-thomae/momente-der-klarheit.html → 200<br>https://de.wikipedia.org/wiki/Momente_der_Klarheit → 404 (Wiederholung nach 429)<br>https://de.wikipedia.org/wiki/Momente_der_Klarheit_%28Roman%29 → 404 | ton=['humorvoll'], fokus=figuren | Zeit: „unfassbar unterhaltsam“, taz: „Witz und Timing“; FAZ: schaut „in die Köpfe ihrer Protagonisten“, taz: „psychologischer Blick“ auf das Ensemble |
| d58 | https://www.perlentaucher.de/buch/petra-hulova/endstation-taiga.html → 200<br>https://de.wikipedia.org/wiki/Endstation_Taiga → 404<br>https://de.wikipedia.org/wiki/Endstation_Taiga_%28Roman%29 → 404 (Wiederholung nach 429) | tempo=ruhig, sprache=poetisch | FR: „poetische und reflektorische Niveau“, „leiser, wie traumwandelnder … Erzählgang“ |
| d59 | https://www.perlentaucher.de/buch/sebastian-lehmann/sebastian-oder-das-leben-ist-nur-ein-schluck-aus-der-flasche-der-geschichte.html → 404<br>https://de.wikipedia.org/wiki/Sebastian_oder%3A_das_Leben_ist_nur_ein_Schluck_aus_der_Flasche_der_Geschichte → 404<br>https://de.wikipedia.org/wiki/Sebastian_oder%3A_das_Leben_ist_nur_ein_Schluck_aus_der_Flasche_der_Geschichte_%28Roman%29 → 404 | – | keine verwertbare Quelle zum Werk gefunden |
| d60 | https://www.perlentaucher.de/buch/ray-bradbury/fahrenheit-451.html → 404<br>https://de.wikipedia.org/wiki/Fahrenheit_451 → 200 | – | keine verwertbare Quelle zum Werk gefunden |

Unbrauchbare Treffer: d02 und d54 (Wikipedia-Artikel zur Verfilmung), d06 (Artikel zum Gemälde), d27 (Sachartikel „Klassentreffen“), d45 (Wikipedia-Artikel zur Verfilmung; die Rezeption dort betrifft den Film), d47 und d52 (zuerst Begriffsklärungen, danach Romanartikel abgerufen), d10, d15, d18, d23, d29, d51 (gleichnamiger Artikel zu anderem Gegenstand). Für d17, d18, d27 und d31 fanden sich Perlentaucher-Notizen, aber ohne eindeutige Aussage zu den kontrollierten Werten. Diese Felder bleiben `null`.

`inhalt` ist nur bei d35 gesetzt (`["suizid"]`, Suizidversuch als Handlungskern laut Wikipedia). Die Liste ist dort nicht auf weitere Punkte geprüft. In allen übrigen Fällen ist `inhalt` = `null` (nicht geprüft).

## 11. null-Anteile (60 Kandidaten)

| Feld | null | Anteil |
|---|---|---|
| titel | 0 | 0 % |
| autor | 0 | 0 % |
| isbn | 0 | 0 % |
| jahr | 0 | 0 % |
| verlag | 0 | 0 % |
| seiten | 0 | 0 % |
| genre | 12 | 20 % |
| thema | 2 | 3 % |
| tempo | 57 | 95 % |
| ton | 51 | 85 % |
| fokus | 55 | 92 % |
| sprache | 54 | 90 % |
| laenge | 0 | 0 % |
| inhalt | 59 | 98 % |
