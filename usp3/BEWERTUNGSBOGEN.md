# Bewertungsbogen USP III: Spezifikation

_Stand 24.10.2026. Grundlage: [ENTSCHEIDUNGSVORLAGE-USP3.md](../ENTSCHEIDUNGSVORLAGE-USP3.md) (Abschnitte 2, 3, 8, Nachträge), [CLUSTERUNG.md](CLUSTERUNG.md), [PARAMETER.md](../PARAMETER.md)._

Kennzeichnung: **[F]** Forschung, **[P]** Praxis. Die Ziffern verweisen auf die Quellenliste mit URL. **„Entscheidung“** heißt: eigene Gestaltungswahl, keine Studie belegt sie direkt. Gewichte ohne Quelle sind Testwerte aus der Vorlage.

## 1. Fragen im Überblick

| Nr | Frage | Wortlaut | Antworten (Form) | Kodierung | Signal für die Empfehlung | Beleg |
|---|---|---|---|---|---|---|
| F1 | Gefallen | „Wie hat dir das Buch gefallen?“ | 5 Lichter, alle beschriftet: gar nicht · eher nicht · okay · gut · sehr gut; leer möglich | (L − 3) / 2 ergibt −1, −0,5, 0, +0,5, +1; leer = `null` | Richtung und Stärke für das ganze Buch; Zielgröße 4–5 Lichter | vorgegeben; alle Stufen beschriftet [1][2] [F]; 5 Stufen [2] [F], [7] [P]; Mittelkategorie [1][2] [F] |
| F2 | Autor | „Mehr von dieser Person?“ | 2 gleichrangige Knöpfe: Ja · Nein; leer | +1 / −1 / `null`, je Person und Werk | direktes Autorensignal, stärker als der Übertrag aus F1 | vorgegeben; Daumen statt Sterne [13] [P]; zwei Optionen gleich reliabel und schneller [5] [F] |
| F3 | Aspekte | „Was davon hat dir gefallen, was nicht?“ Zeilen bei Romanen: Sprache · Figuren · Handlung · Atmosphäre · Thema. Bei Sachbüchern: Verständlichkeit · Tiefe · Thema | je Zeile 2 Knöpfe: gefiel mir · gefiel mir nicht; leer = keine Aussage | +1 / −1 / `null` je (Werk, Dimension) | Gewicht der Vergleichsdimension für diese Person; Ankerbuch für Ähnlichkeit; Negatives nur am Buch und an belegten Merkmalen | Dimensionen [23][24] [P], [25][27][28] [F]; zwei Optionen [5] [F]; Bindung an Merkmale: CLUSTERUNG, Abschnitt 3 |
| F4 | Abbruch (nur bei Abbruch) | „Warum hast du aufgehört?“ | die 10 bestätigten Gründe als Mehrfachauswahl, dazu Freitext | Zuordnung wie in der Vorlage, Abschnitt 2. „Stil/Sprache“, „Figuren“ und „Thema“ sind dieselbe Beobachtung wie in F3 „gefiel mir nicht“ und erscheinen dort sichtbar mitgesetzt | negatives Signal je Merkmal | bestätigt; häufige Abbruchgründe [33] [P] |
| F5 | Tempo für mich (Genauer beschreiben) | „Wie war das Tempo für dich?“ | 3 Stufen: zu langsam · passend · zu schnell; leer | −1 / 0 / +1, bezogen auf das Buchtempo aus dem Katalog. Fehlt das Buchtempo, wird die Antwort gespeichert und wirkt erst, wenn es vorliegt | Schätzung des bevorzugten Tempos | Just-about-right-Skala [29] [F]; „slow/boring“ als häufiger Abbruchgrund [33] [P] |
| F6 | Künftig weniger (Genauer beschreiben; bei ≤ 2 Lichtern und Abbruch hervorgehoben) | „Künftig weniger davon?“ mit Chips für die bekannten Merkmale dieses Buchs | je Chip: seltener · nicht empfehlen | `{action, dimension, value_id, source_work_id, scope, explicit}` | „seltener“ senkt die Priorität, „nicht empfehlen“ ist ein harter Filter. Fehlt der Wert beim Kandidaten, gilt dieser nicht als passend | vorgegeben; Daumen runter heißt „nicht mehr vorschlagen“ [13] [P] |
| F7 | Passung (nur bei App-Empfehlung) | „Hat die Empfehlung gepasst?“ | 3: Ja · Teilweise · Nein | +1 / 0 / −1 auf die angezeigten Gründe (Variante C) | korrigiert die Annahme der App | Vorlage, Abschnitt 4; Korrigierbarkeit als Ziel von Erklärungen [34] [F] |

Daneben steht der Freitext „Deine Lesart“. Er wird nicht kodiert.

**Reihenfolge:** Sichtbar sind F1, F2, F3 und gegebenenfalls F7. Beim Abbruch steht F4 vor F3. F5 und F6 liegen unter „Genauer beschreiben“. Gelesen und Abbruch verwenden dieselben Felder und dieselbe Kodierung.

## 2. Begründungen

### 2.1 Gefallen (F1)

Vorgegeben; die Forschung stützt sie:
- Vollständig mit Worten beschriftete Stufen sind reliabler [1][2] [F].
- Faustregel fünf bis sieben Stufen [2] [F]; unipolar fünf am reliabelsten (Krosnick & Tahk, Sekundärquelle) [7] [P]. Preston & Colman fanden 2–4 Stufen vergleichsweise schwach; bevorzugt wurden 10, knapp vor 7 und 9 [4] [F].
- Eine Mitte verbesserte Reliabilität und Validität [1] [F] und wird meist empfohlen [2] [F].

- Unipolar oder bipolar: keine eindeutige Empfehlung [2] [F]; in einer In-Produkt-Studie war kein Format klar besser als bipolar, Verzweigung verdoppelte den Aufwand [8] [F]. F1 wird bipolar um „okay“ kodiert (Vorlage, Abschnitt 3).

Grenze: Mehr Stufen wären nach [4] [F] etwas trennschärfer; fünf sind ein Kompromiss zugunsten der Geschwindigkeit (Entscheidung). Goodreads legt „it was ok“ auf 2 Sterne, nicht in die Mitte [19] [P].

### 2.2 Zwei oder drei Optionen je Aspekt (F3)

**Entscheidung: zwei Knöpfe plus leer.**
- **Dafür:** Binäre Fragen waren gleich reliabel, schneller und wirkten weniger komplex [5] [F]. Eine Mitte kann bei geringer Motivation Satisficing begünstigen [1] [F]. StoryGraph-Nutzer beantworten meist nur die Ja/Nein-Fragen [9] [P]. Die Stärke liefert F1; F3 liefert nur die Richtung.
- **Dagegen:** 2–4 Stufen schnitten schwach ab [4] [F]; in einer IRT-Simulation kostete der Schritt von 3 auf 2 Stufen am meisten [6] [F]. Beide messen Intensität über mehrere Items; die Übertragung auf ein Richtungsurteil ist nicht belegt.
- **StoryGraphs „It's complicated“** gehört zu beschreibenden Buchfragen („Strong character development“, „Loveable characters“; Werte Yes/No/Complicated) [15][16] [P], „most“ mit „It's complicated“, alle mit „N/A“ [18] [P]. Für ein Gefallensurteil folgt daraus nichts.
- **Risiko:** Gemischtes wird erzwungen oder leer gelassen. Ob „gemischt“ verlangt wird, prüft der Lesertest.

### 2.3 Sagt „Aspekt gefiel mir“ ohne Buchmerkmal etwas aus?

**Ja, als Gewicht der Dimension. Nein, als Vorliebe für einen Merkmalswert.**
- Leser unterscheiden sich darin, welche Dimension zählt: Der Literary Response Questionnaire trennt u. a. handlungsgetriebenes Lesen, Empathie, Bildhaftigkeit und Interesse an Autor und Stil [28] [F]; literarische Orientierungen wirkten je Suchaufgabe verschieden [27] [F].
- Wer oft „Sprache“ markiert, dem zählt sprachliche Ähnlichkeit eines Kandidaten mehr (Entscheidung, aus [27][28] abgeleitet, ungetestet).
- Welcher Wert gefällt („knappe Sprache“), folgt erst aus einer belegten Buchbeschreibung (CLUSTERUNG, Abschnitt 3).

Dass Teilbewertungen die Vorhersage verbessern, ist nur für andere Bereiche belegt:
- Adomavicius & Kwon (2007): genauere Filmempfehlungen als mit Einzelbewertung (berichtet in [10]) [F].
- Jannach et al. (2012): niedrigerer RMSE auf allen Datensätzen; Yahoo! Movies mit vier Kriterien (Story, Acting, Direction, Visuals) auf 13 Stufen A+ bis F, umgerechnet auf 5; HRS-Hotels Kriterien 1–10, Gesamt 1–3 [10] [F].
- Übersicht: Studien nicht direkt vergleichbar, Daten dünner, Nutzer finden es mühsam, Angaben verrauscht [11] [F]. Aspekte aus Rezensionstexten wirken je Domäne verschieden [12] [F].
- Ob optionale binäre Aspekte bei Büchern helfen, ist **nicht belegt**.

### 2.4 Statt Aspekten nach dem Buch fragen?

- Die Dimension direkt zu erfragen ist besser als Zustimmung zu Aussagen [1] [F].
- StoryGraph fragt beschreibend („How would you rate the pace of the book? (slow, medium, fast)“) und zeigt Anteile je Buch; eine Nutzerin hält „plot- or character-driven“ und „diverse“ für missverständlich [17] [P].

**Entscheidung:**
- Buchbeschreibungen kommen aus dem Katalog (Vorlage, Nachtrag 1).
- Im Bogen bleibt nur F5: Die Just-about-right-Form verbindet Buch und Reaktion, die Mitte ist der Idealwert [29] [F]. Drei statt der dort beschriebenen fünf Stufen sind eine Entscheidung.

### 2.5 Wortlaut

- F3 nutzt dasselbe Verb wie F1, misst also ein Konstrukt (Entscheidung). „Störte mich“ erfragte eher Ärger als Missfallen (Einschätzung, nicht belegt).
- Ja/Nein-Fragen fördern Akquieszenz; Krosnick & Presser raten davon ab [1] [F]. F2 ist vorgegeben, daher zwei gleich große Knöpfe ohne Vorauswahl (Wirkung nicht belegt).

### 2.6 Kein „weiß nicht“, kein „neutral“

„Weiß nicht“-Filter verbessern die Messung nicht [1] [F]; bei sicher vorhandener Meinung kann die Option entfallen [2] [F]. Leer ist `null`, nicht neutral (Vorlage, Abschnitt 1).

### 2.7 Aufwand, Satisficing, Ermüdung

- Satisficing steigt mit Schwierigkeit und sinkt mit Fähigkeit und Motivation [1][3] [F]; spätere Fragen leiden unter Ermüdung, frühe sollen leicht sein [1] [F]. Daher F1 zuerst, F5/F6 zugeklappt.
- Reihenfolgeeffekte sind am konsistentesten belegt, gleichförmiges Ankreuzen gemischt [3] [F]. Entscheidung: identische Antworten in allen Zeilen protokollieren, nicht korrigieren; feste Reihenfolge der Abbruchgründe im Test beobachten.
- Eine belegte Höchstzahl an Items gibt es nicht (RECHERCHE-EMPFEHLUNG, Quelle 30).

### 2.8 Was echte Apps fragen

| App | Abfrage | Beleg |
|---|---|---|
| Goodreads | 5 beschriftete Sterne; mindestens 20 bewertete Bücher, dazu eigene Regale | [19][20] [P] |
| StoryGraph | Stimmungen (Mehrfachauswahl), Tempo (slow, medium, fast), plot- oder figurengetrieben (Plot, Character, A mix), vier Figurenfragen (Yes, No, Complicated, N/A), nichts erzwungen | [15][16][17][18] [P] |
| Fable | Sterne mit halben Stufen, Emoji für das Gefühl, Tags zu Figuren, Sprache, Handlung, Setting, Thema und Ton sowie ein eigener Bereich für Missfallen | [21] [P] |
| Hardcover | „Rate, review“, Listen und Tags; Stimmungen und Abbrüche erwähnt die Store-Seite nicht | [22] [P] |
| Literal | **nicht belegt**, keine prüfbare Quelle gefunden | – |
| Netflix | Daumen statt Sterne, „200% increase in ratings activity“; später zwei Daumen für „love“, ohne doppeltes Gewicht | [13][14] [P] |

### 2.9 Bewusst nicht gefragt

- **Tempo, Stimmung und Anspruch des Buchs:** Sie beschreiben das Buch, gehören in den Katalog und wirkten im Durchspielen unnötig (Vorlage, Nachtrag 1).
- **Gefühlsliste, Lesefluss, „wirkt nach“, „wieder lesen“:** ohne Kodierung in der Vorlage; Kürze geht vor.
- **Halbe Lichter, Lesertypen:** vorgegeben bzw. ausgeschlossen (CLUSTERUNG, Abschnitt 2).
- **Stimmung als Aspekt:** Traurige Bücher bedienen Gefühl und Sinnsuche zugleich [26] [F]; Stimmung bleibt Katalogmerkmal, kein Minuspunkt.

## 3. Grenzen und Testplan

**Nur im Lesertest zu klären:** ob „gefiel mir nicht“ und leer einheitlich verstanden werden; ob „gemischt“ verlangt wird; was „Atmosphäre“ und „Thema“ bedeuten; ob F3 nur F1 wiederholt; ob F5 klar ist; ob die Chips in F6 das gemeinte Merkmal treffen; ob „Verständlichkeit“ und „Tiefe“ (Sachbuch, **nicht belegt**) tragen.

**Methode:** kognitive Interviews nach Willis.
- Üblich sind 5–15 Interviews je Runde in mehreren Runden [31] [P]. Mit 5 Interviews wurden im Mittel 46 von 210 Problemen gefunden, mit 15 Interviews 93 [32] [F].
- Für Selbstausfüller: Lautes Denken plus nachträgliche Nachfragen; Lautes Denken fällt Menschen mit geringerer Schulbildung schwer; Bedeutungsfragen funktionierten, Paraphrasieren nicht [30] [P].

**Plan:**
- **Runde 1:** 6–8 Leser, gemischt nach Lesemenge, Alter (auch über 65), Roman/Sachbuch. Jede Person bewertet drei eigene Bücher (gemocht, mittelmäßig, abgebrochen) im Prototyp, laut denkend; danach Nachfragen wie „Was bedeutet für dich ‚Atmosphäre‘?“, „Warum hast du bei Figuren nichts gewählt?“, „Was hättest du gern geantwortet?“. Gemessen: Dauer, leere Felder, Fehldeutungen je Frage, spontane Wünsche nach einer Mitte.
- **Überarbeitung, Runde 2:** 6–8 neue Leser, gegebenenfalls Variante mit „gemischt“ gegen zwei Knöpfe.
- **Entscheidungsregel (Testwert, nicht belegt):** „gemischt“ kommt in Runde 2, wenn mindestens 2 Personen spontan eine Mitte verlangen. Ein Wort wird ersetzt, wenn es mindestens 2 Personen abweichend deuten.

**Was der Test nicht zeigt:** ob die Antworten Empfehlungen verbessern. Dafür braucht es echte Urteile und den Vergleich aus CLUSTERUNG, Abschnitt 8, einschließlich der Frage, ob F3 gegenüber F1 allein beiträgt; [10][11] stammen aus anderen Bereichen.

## Quellen

1. Krosnick & Presser (2009/2010): Question and Questionnaire Design, Handbook of Survey Research — https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2009/2009_handbook_krosnick.pdf **[F, Übersicht]**
2. Menold & Bogner (2016): Design of Rating Scales in Questionnaires, GESIS Survey Guidelines — https://www.gesis.org/fileadmin/admin/Dateikatalog/pdf/guidelines/design_rating_scales_questionnaires_menold_bogner_2016.pdf **[F, Leitfaden]**
3. Roberts, Gilbert, Allum & Eisner: Satisficing in Surveys: A Systematic Review (über Krosnick 1991) — https://discovery-pp.ucl.ac.uk/10087616/1/Roberts%20et%20al%20satisficing%20review%20%28preprint%29%20200919.pdf **[F, Review]**
4. Preston & Colman (2000): Optimal number of response categories in rating scales, Acta Psychologica 104 — https://epistemio.com/p/ez3sX32F **[F]** (Abstract geprüft)
5. Dolnicar, Grün & Leisch (2011): Quick, simple and reliable: forced binary survey questions, IJMR 53(2) — https://ro.uow.edu.au/commpapers/782 **[F]**
6. In Search of the Optimal Number of Response Categories in a Rating Scale, Journal of Psychoeducational Assessment — https://metatoc.com/papers/29200-in-search-of-the-optimal-number-of-response-categories-in-a-rating-scale **[F, Simulation]**
7. Researchscape: The case for 5-point unipolar scales (zu Krosnick & Tahk 2008) — https://researchscape.com///blog/the-case-for-5-point-unipolar-scales **[P, Sekundärquelle]**
8. Sedley & Yang (2022): Satisfied With Your Satisfaction Scale? Validity Evidence on Bipolar, Branching, and Unipolar Questions — https://research.google/pubs/satisfied-with-your-satisfaction-scale-validity-evidence-on-bipolar-branching-and-unipolar-questions/ **[F]**
9. Book Riot: Do Goodreads and StoryGraph users rate books differently? — https://bookriot.com/do-goodreads-and-storygraph-users-rate-books-differently/ **[P]** (aus RECHERCHE-EMPFEHLUNG übernommen)
10. Jannach, Karakaya & Gedikli (2012): Accuracy improvements for multi-criteria recommender systems, ACM EC, mit Bericht zu Adomavicius & Kwon (2007) — https://web-ainf.aau.at/pub/jannach/files/Conference_ACMEC2012.pdf **[F]**
11. Monti, Rizzo & Morisio (2021): A systematic literature review of multicriteria recommender systems, AI Review 54 — https://iris.polito.it/bitstream/11583/2834946/1/Multicriteria_SLR.pdf **[F, Review]**
12. Hasan et al. (2024): Review-based Recommender Systems: A Survey — https://arxiv.org/html/2405.05562v2 **[F, Review]**
13. Netflix: Goodbye Stars, Hello Thumbs — https://about.netflix.com/en/news/goodbye-stars-hello-thumbs **[P]**
14. TechCrunch (2022): Netflix adds a Two Thumbs Up button — https://techcrunch.com/2022/04/11/netflix-adds-a-two-thumbs-up-button-in-effort-to-learn-what-users-love-not-just-like **[P]**
15. StoryGraph, Nutzerrezensionen (klaraisgraph) — https://app.thestorygraph.com/user_reviews/klaraisgraph **[P]**
16. StoryGraph, Nutzerrezensionen (jbookly) — https://app.thestorygraph.com/user_reviews/jbookly **[P]**
17. First Line Reader (2024): Opinions on StoryGraph's Review Method — https://firstlinereader.blog/2024/04/08/do-i-agree-with-storygraph-reviewers-opinions-on-storygraphs-review-method/ **[P]**
18. Katie Bachelder (2021): Goodbye, Goodreads. Hello, StoryGraph? — https://katiebachelder.com/2021/05/14/goodbye-goodreads-hello-storygraph/ **[P]**
19. Goodreads-Forum: How people rate books using the Goodreads star system — https://www.goodreads.com/topic/show/702656-how-people-rate-books-using-the-goodreads-star-system **[P]**
20. Goodreads-Blog: Announcing Personalized Recommendations — https://www.goodreads.com/blog/show/303-announcing-goodreads-personalized-recommendations?page=1 **[P]**
21. Fable: How To Post Ratings and Reviews — https://fable.co/blog/how-to-post-ratings-and-reviews-on-fable **[P]**
22. Hardcover im App Store — https://apps.apple.com/us/app/hardcover-app/id1663379893 **[P]**
23. Saricks/Wyatt: The Readers' Advisory Guide to Genre Fiction, Leseprobe — https://www.alastore.ala.org/sites/default/files/book_samples/9780838917817_sample_0.pdf **[P]**
24. Lawrence Public Library: The Four Doorways (Pearl) — https://lplks.org/blogs/post/the-four-doorways **[P]** (aus RECHERCHE-EMPFEHLUNG übernommen)
25. Lee et al. (2015): OCLC/ALISE-Bericht zu Appeals, n = 30 — https://www.oclc.org/content/dam/research/grants/reports/2015/lee2015.pdf **[F, explorativ]** (aus RECHERCHE-EMPFEHLUNG übernommen)
26. Koopman (2015): Why do we read sad books?, Poetics 52 — https://pure.eur.nl/en/publications/why-do-we-read-sad-books-eudaimonic-motives-and-meta-emotions/ **[F]**
27. Vakkari & Mikkonen (2019): The role of readers' literary preferences in predicting success in fiction search, Journal of Documentation 76(1) — https://api.crossref.org/works/10.1108%2FJD-01-2019-0005 **[F]**
28. Miall & Kuiken (1995): Literary Response Questionnaire — https://sites.ualberta.ca/~dmiall/reading/LRQ_95.htm **[F]**
29. Parcon (2013): JAR-Skalen und Penalty-Analyse, JSM — https://ww2.amstat.org/meetings/proceedings/2013/data/assets/handouts/310144_83956.pdf **[F, Konferenzbeitrag]**
30. Willis (2018): AAPOR-Webinar Cognitive Interviewing — https://aapor.org/wp-content/uploads/2023/01/AAPOR-Webinar-Willis-June-2018-002-Read-Only.pdf **[P, Fachvortrag]**
31. Survey Research Center, U Michigan: Cognitive Interviews Best Practices (zitiert Willis 2005) — https://srobp.isr.umich.edu/wp-content/uploads/2020/08/7-2-Cognitive-Interviews_-Best-Practices_Uploaded-Oct-1-2007.pdf **[P]**
32. Blair, Conrad, Ackermann & Claxton (2006): Sample Size for Cognitive Interview Pretesting, AAPOR — https://www.abtglobal.com/sites/default/files/2019-07/AAPOR06_Sample_Size_Cognitive_Interviews.pdf **[F]**
33. Goodreads-Autorenblog: Why People Stop Reading a Book — https://www.goodreads.com/author_blog_posts/4504901-why-people-stop-reading-a-book **[P]** (aus RECHERCHE-EMPFEHLUNG übernommen)
34. Tintarev & Masthoff (2012): Evaluating the effectiveness of explanations for recommender systems, UMUAI — https://abdn.elsevierpure.com/files/20864620/USER700.pdf **[F]** (aus RECHERCHE-EMPFEHLUNG übernommen)
