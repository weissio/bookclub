# Recherche

Stand 10.10.2026. Abschnitt A stammt aus einem früheren Chat und wurde hier **nicht erneut geprüft**.

## A. Wettbewerber lokaler Bücherverleih (früherer Chat, ungeprüft)

- **readt** (Berlin, Bleeker und Hartmann GbR): deutschsprachige Verleih-App; im deutschen App Store 4,6 Sterne bei 12 Bewertungen.
- **Bookley** (international, englischsprachig), **BookMingle** (Großbritannien, 100+ Downloads bei Google Play), **Shelfhood** (international): kein erkennbarer Deutschland-Schwerpunkt.
- Folgerung damals: keine nachweislich dominante deutsche Verleih-App, aber die Idee ist nicht neu.

## B. Was Leser an bestehenden Apps stört

- Wiederkehrende Beschwerden über Lese-Tracker: veraltete Goodreads-Oberfläche, soziale Funktionen stören Solo-Leser, Abos für einfache Statistiken, Exporte verlieren Notizen, ungenaue Buchdatenbank (falsche Ausgaben). – [unstar.app](https://unstar.app/blog/goodreads-storygraph-fable-hardcover-bookly-reading-tracker-apps-ranked-2026)
- Lange gewünscht: „Abgebrochen“-Status, feinere Bewertungen, Statistiken, Inhaltswarnungen. – [TCK Publishing](https://www.tckpublishing.com/goodreads-alternatives/)
- StoryGraph: halbe und Viertelsterne, Suche nach Stimmung und Tempo, Inhaltswarnungen. – [App Store](https://apps.apple.com/us/app/-/id1570489264)
- Wunsch eines Goodreads-Nutzers: private Rezensionen, weil man ein Buch gut geschrieben finden und trotzdem nicht mögen kann. – [App Store Goodreads](https://apple.co/3g3yxvk)
- Sammler: Sonderausgaben, Vorbestellungen, Farbschnitt, Leihgaben, Doppelkäufe vermeiden, Standort im Regal. – [Bookmark](https://apps.apple.com/app/id6757299789), [Book Tracker](https://apps.apple.com/app/book-tracker-bookshelf-log/id1491660771)
- „Privat zuerst“ gibt es bereits: [ShelfLog](https://mwm.ai/apps/book-tracker-shelflog/6767477437). Hardcover bietet öffentlich/privat/Freunde und ein Profil mit Lieblingsbüchern. – [Hardcover](https://apps.apple.com/us/app/hardcover-app/id1663379893)

## C. Deutscher Markt

- LovelyBooks: laut eigener Angabe über 240.000 aktive Mitglieder, größte deutschsprachige Buchcommunity, seit 2021 bei Hugendubel; seit 2024 Award-Kategorie „Farbschnitt“. – [Pressemitteilung 2024](https://cdn.uc.assets.prezly.com/9f294063-5d80-4ccd-be1a-789de3e962a0/-/inline/no/PM_Hugendubel_LovelyBooks.pdf)
- Etwa ein Drittel der jungen Menschen wird über Social Media auf Bücher aufmerksam (Börsenverein). – [Müller Martini](https://www.mullermartini.com/en/newsroom/storys/top-storys/social-media-boosts-sales-of-printed-books)
- Lesejury bewertet in Einzelkategorien: Cover, Erzählstil, Handlung, Charaktere. – [Lesejury](https://www.lesejury.de/nutzer/profil/Cozydayscoffeebooks)

## D. Wie Leser bewerten (Foren)

- Die meisten bewerten nach Gefallen, nicht nach literarischer Qualität.
- Fünf Sterne für Bücher, die bewegen, hängen bleiben, wiedergelesen oder nach dem Ende vermisst werden.
- Manche zerlegen in Sprache, Handlung und Tempo, Figuren, Dialoge, Weltenbau, Thema.
- Frust: Sterne-Inflation, kein Unterschied zwischen abgebrochen und ungeliebt, Hemmung, Autoren niedrig zu bewerten.
- Bewertungen ändern sich beim Wiederlesen.
- Quellen: [Goodreads-Diskussion](https://www.goodreads.com/topic/show/19360738-what-makes-you-tick-those-rating-stars?page=1), [r/books](https://reddit.rtrace.io/r/books/comments/1csnfve/all_the_fivestars/)

## E. ISBN und Buchdaten

- ISBN seit 1970 (10-stellig), seit 1.1.2007 13-stellig und identisch mit dem EAN-Strichcode (Präfix 978/979). Alte ISBN-10 per Präfix 978 umrechenbar. Bücher vor 1970 haben keine ISBN. Doppelt vergebene ISBN kommen vor; ein Titel hat je Format eigene ISBN. – [Wikipedia](https://en.wikipedia.com/wiki/Isbn)
- Die ISBN selbst enthält nur Sprachraum, Verlag, Titelnummer und Prüfziffer. Titel, Autor usw. kommen aus Datenbanken.
- **DNB SRU:** laut DNB kostenfrei und ohne Registrierung; liefert Titel, Autoren, Verlag, Jahr, Sprache, Sachgruppe; keine Cover. – [DNB SRU](https://www.dnb.de/DE/Professionell/Metadatendienste/Datenbezug/SRU/sru_node.html)
- **Google Books API:** API-Schlüssel nötig; liefert u. a. Seiten, Kategorien, Beschreibung, Coverbilder. – [Google](https://developers.google.com/books/docs/v1/using)
- **Open Library Covers:** Cover per ISBN in drei Größen, Hinweis auf Rate-Limits. – [Doku](https://github.com/Luca3317/OpenLibrary.NET/blob/main/docs/Covers%20API.md)
- **Cover-Rechte:** Die DNB zeigt Cover nur über den VLB-Coverdienst auf Basis einer Vereinbarung für Bibliotheken mit der VG Bild-Kunst. Für eine kommerzielle App ist die Nutzung zu klären. – [DNB Cover](https://www.dnb.de/EN/Professionell/Metadatendienste/Kataloganreicherung/Cover/cover_node.html)

## F. Design-Grundlage

- Anthropic-Skill „frontend-design“: Gestaltung aus der Welt des Themas ableiten, typische KI-Muster vermeiden. – [anthropics/skills](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)
