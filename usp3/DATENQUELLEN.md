# Datenquellen und Kandidatenfindung (Recherche 24.10.2026)

**[belegt]** = so in der Quelle oder selbst gemessen; **[Einschätzung]** = eigene Folgerung. Nur öffentliche Preise und Konditionen.

Stichprobe: 120 ISBNs aus `katalog/*.json` (aktuelle Publikumsromane), abgefragt am 24.10.2026 über DNB-SRU [15] und Open Library [24]. Nicht repräsentativ, verzerrt auf lieferbare Verlagsromane.

## 1. VLB (MVB)

- **Felder:** Die REST-API v2 liefert Zusatztexte (`textContents`), eine Produktklassifikation (`subjects`) mit Thema-Codes und **Lesemotiven**, außerdem Schlagwörter (Verlags- und DNB-Schlagwörter), Zielgruppe und Alter (`audiences`) sowie Cover und Mediendateien. Formate JSON und ONIX 2.1/3.0, Stapelsuche bis 500 ISBNs. [belegt] [2]
- Zu den Zusatztexten zählen Hauptbeschreibung, Kurztext, Klappentext, Inhaltsverzeichnis, Leseprobe und Autorenporträt. [belegt] [5]
- **Lesemotive** sind ein Standard von MVB und Gruppe Nymphenburg mit zehn Motiven, etwa Entspannen, Eintauchen, Nervenkitzeln, Lachen und Leichtlesen. Seit Oktober 2021 stehen sie über das VLB der Branche zur Verfügung. [belegt] [12][13] Sie liegen fachlich am nächsten an „Ton/Stimmung“. [Einschätzung]
- **Füllgrad:** Laut Task-Force-Bericht von 2014 hatten 59 % aller Titel eine Hauptbeschreibung, bei Neuzugängen 70 %. Mindestens drei Schlagwörter: 43 % bzw. 46 %. [belegt] [6] Bei aktuellen Romanen liegt der Wert vermutlich höher (97 % MVB-Klappentexte in der Stichprobe, Abschnitt 3). [Einschätzung] [15]
- **Zugang:** Die API verlangt einen Token. Für Verlagsdaten ist ein VLB-Abonnement Voraussetzung. [belegt] [2] Software-Dienstleister erhalten den API-Vertrag und einen Entwicklungszugang kostenlos, ihre Kunden brauchen aber ein eigenes VLB-Abo oder einen Webshop-Vertrag. [belegt] [3][4]
- **Lizenz und Kosten (Webshop-Mustervertrag):** einfaches Nutzungsrecht nur für die im Vertrag genannte Website, Weitergabe an Dritte verboten, Vertragsstrafe 9.995 € je Verstoß, Einrichtungsgebühr 150 € zzgl. MwSt. Die Jahresgebühr richtet sich nach dem Vorjahresumsatz und einer Preisliste, die nicht veröffentlicht ist. [belegt] [1] Einen Vertragstyp für Lese- oder Empfehlungs-Apps ohne Shop gibt es öffentlich nicht. [belegt] [1][3]
- MVB erlaubt öffentlichen Bibliotheken Cover kostenlos per dynamischem Link, aber ohne lokale Speicherung. [belegt] [19]
- **Startup-Zugang:** möglich, aber nur über einen individuell verhandelten Vertrag. Die Webshop-Klauseln (eine Website, keine Weitergabe) passen nicht ohne Weiteres zu einer App. [Einschätzung] [1][3]

## 2. Thema (EDItEUR)

- Thema umfasst rund 3.000 Kategorien und etwa 1.000 gemeinsame Qualifier in sechs Gruppen. Die Codes werden kombiniert (Postkoordination). [belegt] [8] Die Qualifier-Gruppen sind Ort, Sprache, Zeit, Bildungszweck, Interessenalter/Sonderinteresse und Stil. [belegt] [11] Version 1.6 brachte 131 neue Kategorien und 411 Qualifier, u. a. mehr Liebesroman-Genres. [belegt] [10]
- **Belletristik:** FBA steht für moderne und zeitgenössische Belletristik, FFP für Polizeikrimi. FX-Codes erfassen erzählerische Themen, zum Beispiel FXQ für Vertreibung/Exil/Migration. Ort- und Zeit-Qualifier sind feinkörnig (z. B. 3MRBF = 2010–2019). [belegt] [8] Dazu kommen Trope-Codes wie FRLE (enemies to lovers) sowie FMJ (Cosy Fantasy) und FMT (Dark Fantasy). Empfohlen werden höchstens 4–5 Kategorien und 4–5 Qualifier pro Titel. [belegt] [9] FX darf nicht der Hauptcode sein. [belegt] [7]
- **Verbreitung in Deutschland:** Der Leitfaden des Börsenvereins sagt, Thema werde „flächendeckend im Handel eingesetzt“. Pflicht ist nur eine Kategorie pro Titel. [belegt] [7] Libri kürzt die Belletristik-Kategorien auf 90. [belegt] [8] Die DNB-Datensätze der Stichprobe enthielten keine Thema-Codes (0 von 40). [belegt] [15]
- **Für die Kandidatenfindung:** Thema taugt gut als Filter für Genre, Subgenre, Ort, Zeit und teilweise Thema (FX). Tempo und Ton bildet es nicht ab. Die Tiefe hängt vom Verlag ab. [Einschätzung] [7][9]

## 3. DNB-Inhaltstexte (MARC 856)

- **Verbreitung:** 116 von 120 Stichprobentiteln (97 %) haben in Feld 856 einen Link `Inhaltstext` mit Quelle `X:MVB` (Muster: `https://services.dnb.de/plus/idn/<IDN>/blurb/`). [belegt] [15] Bei älteren Titeln oder Kleinverlagen ist die Abdeckung vermutlich deutlich niedriger. [Einschätzung]
- **Rechte:** Die DNB stellt ihre bibliografischen Daten unter CC0. [belegt] [16] Die Inhaltstexte nennt sie dabei nicht. Sie lehnt außerdem jede Gewähr ab, dass die Daten keine Urheberrechte Dritter verletzen. [belegt] [16] Ausdrücklich unter CC0 stehen nur die selbst digitalisierten Inhaltsverzeichnisse. [belegt] [17] Der Klappentext stammt von MVB bzw. vom Verlag, und Werbetexte können urheberrechtlich geschützt sein (OLG Köln, 6 U 82/11). [belegt] [15][18]
- **Folgerung:** Interne Auswertung (Embeddings, Merkmale) ohne Anzeige ist weniger exponiert als Wiedergabe, aber ungeklärt. Schriftliche Auskunft von DNB/MVB einholen; ohne Lizenz nicht anzeigen. [Einschätzung] [16][18]

## 4. Google Books API

- **Abdeckung:** Eigene Messung scheiterte, alle 120 Abfragen ohne Schlüssel endeten mit HTTP 429. [belegt] [45] Eine Studie auf der ISSI 2025 berichtet über Google Books, Open Library und Wikipedia „significant disparities“ zum Nachteil nicht englischsprachiger Bücher. [belegt] [22]
- **Bedingungen:** Die App darf Nutzern keine Gebühr berechnen, außer mit einer gesonderten Vereinbarung mit Google. Inhalte müssen auf Verlangen entfernt werden. [belegt] [20] Die allgemeinen API-Bedingungen verbieten es, Datenbanken aufzubauen, dauerhafte Kopien anzulegen oder länger als vom Cache-Header erlaubt zu speichern. [belegt] [21]
- **Folgerung:** Google Books eignet sich nicht als gespeicherte Merkmalsquelle und nicht für eine Bezahl-App. [Einschätzung] [20][21]

## 5. Open Library, Wikidata, BookBrainz

- **Open Library:** Katalog gemeinfrei/CC0, Komplett-Dumps verfügbar. [belegt] [23] In der Stichprobe wurden 61 von 120 Titeln gefunden, nur 11 davon mit Beschreibung und 11 mit Schlagwörtern. [belegt] [24]
- **Wikidata:** Strukturierte Daten stehen unter CC0. [belegt] [25] Für Literaturkorpora bleiben „significant gaps in coverage“. [belegt] [26] Eigene Messung scheiterte an Rate-Limits. [belegt] [46]
- **BookBrainz:** Kerndaten CC0, übrige Daten CC BY-SA. [belegt] [27]
- **Folgerung:** Für aktuelle deutsche Romane taugen diese Quellen nur zum Abgleich von Werk und Ausgabe, nicht als Merkmalsquelle. [Einschätzung] [24][26]

## 6. Wie andere Apps das lösen

- **Goodreads** hat Daten automatisch von Ingram, großen US-Verlagen und der Library of Congress importiert, ergänzt durch Freiwillige („Librarians“). [belegt] [29] Genres ergeben sich aus den Regalnamen der Nutzer (Crowdsourcing). [belegt] [30]
- **StoryGraph:** Stimmung, Tempo und Figurenmerkmale kommen aus Community-Rezensionen. [belegt] [31] Die Startlabels wurden so gewählt, dass „the vast majority of readers would agree“. Später sollten Community-Daten sie aktualisieren. [belegt] [32] Maschinelle Bestimmung von Stimmung/Tempo wurde früh getestet. [belegt] [33] Der Einstieg läuft über einen Fragebogen zu Genres und Stimmungen. [belegt] [31] Externe Datenquellen nennen die gefundenen Quellen nicht. [belegt] [28][31]
- **Bookly** lässt fehlende Bücher manuell anlegen, nennt aber keine Quelle. [belegt] [34] Zu **Literal** wurde keine öffentliche Angabe zur Datenquelle gefunden. [belegt] [35]
- **Muster:** Bibliografie kommt vom Handel oder Katalog, Erlebnismerkmale kommen von Lesern. [Einschätzung] [29][31]

## 7. Textbasierte Ähnlichkeit und LLM-Extraktion

- Deutsche Klappentexte lassen sich gut in Genres einordnen. Bei GermEval 2019 (ca. 20.800 Random-House-Klappentexte) lag der beste Micro-F1 auf der obersten Ebene (8 Klassen) bei 0,867, über die volle Hierarchie (343 Klassen) bei 0,68. [belegt] [36]
- Arbeiten zu SBERT/RoBERTa-Embeddings auf Goodreads berichten bessere Präzision als einfache Basismodelle, nennen im Abstract aber keine Zahlen. [belegt] [37] Ein aktueller Überblick ordnet Inhaltsmerkmale und LLM-Wissen als zentrale Mittel gegen den Kaltstart bei Items ein. [belegt] [38]
- **Zuverlässigkeit subjektiver Merkmale:** Zero-shot-LLMs liegen unter feinabgestimmten Modellen, stimmen aber „fair“ mit Menschen überein. Empfohlen wird der Einsatz zusammen mit menschlichen Annotatoren. [belegt] [39] Bei der Valenz in deutscher Kinderliteratur war die Übereinstimmung von ChatGPT mit Lesern niedrig. [belegt] [40] Bei einem gut definierten Erzählmerkmal (Fokalisierung) erreichte GPT-4o 85 % F1, bei α = 0,55–0,65 zwischen Menschen. [belegt] [41] Schon Leser untereinander einigen sich selten auf eine konkrete Emotion, eher auf die Kategorie. [belegt] [42]
- Aus Rezensionen gewonnene Merkmale wie Tempo und Ton brachten kaum Zusatznutzen, sobald Bewertungen, Metadaten und Regal-Labels vorlagen (MAE −0,015 %). [belegt] [43]
- Eine Studie, die LLM-Labels für Tempo oder Stimmung aus Klappentexten gegen Leserurteile prüft, habe ich nicht gefunden. Genres aus Klappentexten sind belastbar, Tempo und Ton (werbliche Texte, geringe Leser-Einigkeit) nur als markierte Schätzung. [Einschätzung] [36][40][42]

## 8. Kaltstart ohne Nutzerdaten

- Ein Einstiegsfragebogen zu Genres und Stimmungen ist üblich (StoryGraph). [belegt] [31] Als neue Nutzer bekannte Titel bewerten sollten, bot die Auswahl nach Popularität die beste Balance zwischen Aufwand und Genauigkeit: 1,9 Seiten bis zum Abschluss gegenüber 4,0 Seiten bei Pop×Entropie. [belegt] [44]
- Für Items ohne Interaktionen dienen Inhaltsmerkmale, Wissensgraphen und LLMs. [belegt] [38]

## Synthese: Empfehlung

**Start (MVP, ohne Lizenzkosten)** [Einschätzung]
1. **Bibliografie:** DNB-SRU, kostenlos und ohne Registrierung [14], dazu CC0-Lizenz [16].
2. **Kandidatenfindung:** SRU 1.1 sortiert nicht, CQL-Sortierung gibt es nur für einzelne Indizes [14]. Daher eigenen Index per SRU aufbauen (≤100 Treffer je Antwort [14]), gefiltert auf Sprache, Belletristik, Jahr; Inhaltstexte nur intern als Embeddings/Merkmale. Ranking in der App (Embedding-Ähnlichkeit plus GND-, Genre-, Längenfilter). [14][15]
3. **Merkmale:** Ein LLM schätzt Genre und Thema aus dem Klappentext (ziemlich verlässlich [36]), Tempo und Ton nur als markierte Schätzung [39][40]. Für den Startkatalog werden die Labels redaktionell geprüft.
4. **Leserangaben:** Ab Tag 1 Tempo und Stimmung abfragen (StoryGraph-Muster [31]). Sie ersetzen mit wachsender Zahl die LLM-Schätzung.
5. **Rechte klären:** Bei der DNB oder MVB schriftlich nachfragen, ob die Inhaltstexte intern genutzt werden dürfen. Bis dahin keine Klappentexte anzeigen. [16][18]

**Später (Wachstum)** [Einschätzung]
6. **VLB-Lizenz verhandeln:** Sie bringt Thema-Codes, Lesemotive, Schlagwörter, Zielgruppe, Cover und angezeigte Klappentexte [2][12]. Kosten nur auf Anfrage, die Webshop-Vorlage sieht eine umsatzabhängige Gebühr und 150 € Einrichtung vor [1]. Thema und Lesemotive werden dann Kandidatenfilter.
7. Die LLM-Labels laufend gegen Leserangaben messen und dabei die Übereinstimmung pro Merkmal ausweisen.

**Risiken** [Einschätzung]
- Rechtslage der Inhaltstexte ungeklärt [16][18].
- VLB-Vertrag ist auf Shops zugeschnitten, Vertragsstrafe bei Weitergabe [1].
- Google Books ohne Zusatzvereinbarung nicht für eine Bezahl-App [20][21].
- Tempo und Ton aus Klappentexten sind unsicher [40][42].
- Die Stichprobe ist nicht repräsentativ für Backlist und Kleinverlage [15].

---

## Quellen

1. VLB-Lizenzvertrag Webshop Buchhandel (Muster): https://vlb.de/assets/media/portraits/Lizenzvertrag_VLB-Daten_Webshop-Buchhandel_B%C3%96V_Nicht-Mitglied.pdf
2. VLB REST API v2, Anwenderspezifikation: https://vlb.de/assets/images/VLB_REST_API_Version2_Anwenderspezifikation.pdf
3. VLB für Dienstleister: https://vlb.de/en/dienstleister
4. VLB API-Vertrag, Bestellformular: https://vlb.de/en/services/bestellformular-api-vertrag-und-technische-spezifikation
5. VLB-Webinar Zusatztexte/Mediendateien (2020): https://vlb.de/assets/images/Webinar_Zusatztexte_Mediendateien-im-VLB_25022020.pdf
6. Task Force VLB+, Ergebnisbericht (2014): https://vlb.de/assets/downloads/whitepaper_metadatenbank.pdf
7. Börsenverein, Praktisches Arbeiten mit thema (2021): https://www.boersenverein.de/fileadmin/IG_Produktmetadaten/Praktisches-Arbeiten-mit-thema_Version-3_20211130.pdf
8. BIC Brunch, Thema Adult Fiction: https://bic.org.uk/wp-content/uploads/2023/01/BIC-Brunch_Thema-Sessions_No.1_Adult-Fiction_ALL.pdf
9. APA, Thema spotlight genre fiction: https://www.publishers.asn.au/Web/Member-Resources/Support/Metadata-Tips/Thema-spotlight-discoverability-genre-fiction.aspx
10. BookNet Canada, Thema 1.6: https://booknetcanada.ca/blog/2024/11/25/step-up-your-subjects-with-the-newly-released-thema-16
11. BookNet Canada, Thema Basics: https://booknetcanada.atlassian.net/wiki/spaces/UserDocs/pages/8257659
12. VLB, Vergabe von Lesemotiven: https://vlb.de/assets/media/support/Schritt-fu%CC%88r-Schritt-Vergabe-von-Lesemotiven.pdf
13. MVB, Buchmarkt 11/2021 (Lesemotive): https://mvb-online.de/assets/downloads/Buchmarkt_202111.pdf
14. DNB, SRU-Schnittstelle: https://www.dnb.de/EN/sru
15. DNB-SRU, eigene Abfrage (Beispiel): https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=num%3D9783446276031&recordSchema=MARC21-xml
16. DNB, Geschäftsmodell/Lizenzen: https://www.dnb.de/businessmodel
17. DNB, Kataloganreicherung: https://www.dnb.de/catalogueenrichment
18. WBS zu OLG Köln 6 U 82/11: https://www.wbs.legal/urheberrecht/werbeagenturen-aufgepasst-olg-koln-bestatigt-urheberrechtsschutz-fur-werbetexte-und-produktbeschreibungen-11842/
19. MVB, Nutzungsbedingungen buchhandel.de für Bibliotheken (2017): https://www.bvoe.at/sites/default/files/2022-11/mvb_nutzungsbedingungen_buchhandel_de_bibliotheken.pdf
20. Google Books API Terms: https://developers.google.com/books/terms?csw=1
21. Google APIs Terms of Service: https://developers.google.com/terms
22. Dagienė u. a., ISSI 2025: https://issi2025.iiap.sci.am/wp-content/uploads/2025/07/21%e2%80%a4-Dagiene_rp_issi2025_286.pdf (Abstract: https://tagteam.harvard.edu/hub_feeds/119/feed_items/15465118)
23. Open Library FAQ: https://openlibrary.org/help/faq/using
24. Open Library Books API (eigene Abfrage): https://openlibrary.org/api/books?bibkeys=ISBN:9783446276031&format=json&jscmd=details
25. Wikidata Licensing: https://www.wikidata.org/wiki/Wikidata:Licensing
26. Rohrbacher & Schrittesser (2026), JOHD: https://reference-global.com/article/10.5334/johd.483
27. BookBrainz Licensing: https://bookbrainz.org/licensing
28. Wikipedia, The StoryGraph: https://en.wikipedia.org/wiki/The_StoryGraph
29. Goodreads Librarians, Datenquellen (2012): https://www.goodreads.com/topic/show/780951-faqs-amazon-is-going-away-as-a-data-source?page=1
30. Goodreads Librarians, Genres: https://www.goodreads.com/topic/show/1138393-how-do-we-correct-genre-definitions
31. TCK Publishing, StoryGraph Review: https://www.tckpublishing.com/storygraph-review/
32. Interview Nadia Odunayo (2020): https://thequilltolive.com/2020/07/07/interview-with-nadia-odunayo-founder-of-the-storygraph/
33. Odunayo, Newsletter #25: https://buttondown.com/nodunayo/archive/25-hey-computer-can-you-help
34. Book Riot, Bookly Review: https://bookriot.com/bookly-review/
35. Literal API (ohne Quellenangabe): https://literalclub.notion.site/Literal-API-36fa7f0fdaf64a129698d410e0fabfa1
36. GermEval 2019 Task 1: https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/germeval-2019-hmc/gest19-1-description.pdf
37. Javaji & Sarode (2023), Multi-BERT: https://arxiv.org/abs/2308.13050v1
38. Zhang u. a. (2025), Cold-Start Survey: https://arxiv.org/abs/2501.01945
39. Ziems u. a. (2024): https://arxiv.org/abs/2305.03514v3
40. Rebora u. a. (2023), ChatGPT vs. Leser: https://bibliographie.ub.uni-mainz.de/catalog/publication-169571
41. Hicke u. a. (2025), Fokalisierung: https://anthology.ach.org/volumes/vol0003/says-who-effective-zero-shot-annotation-of/10.63744@xxqzxENxsh3b.pdf
42. Alvarez-Gonzalez u. a. (2021): https://arxiv.org/pdf/2109.01900
43. Stefanów (2026), UvA: https://student.uva.nl/en/events/2026-what-s-in-a-book-rating-do-review-derived-appeal-related-cues-improve-personalised-rating-prediction
44. Rashid u. a. (2002), Getting to Know You: https://files.grouplens.org/papers/voi-final.pdf
45. Google Books API, eigene Abfrage: https://www.googleapis.com/books/v1/volumes?q=isbn:9783446276031
46. Wikidata Query Service / API, eigene Abfrage: https://query.wikidata.org/
