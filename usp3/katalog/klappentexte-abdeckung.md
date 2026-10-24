# Klappentexte – Abdeckung

Stand: 2026-10-24. Datei: `klappentexte.json` (70 Einträge).

| Gruppe | n | DNB | Google | Verlag | null |
|---|---|---|---|---|---|
| a* (Arjens Bücher) | 10 | 9 (90.0 %) | 0 (0.0 %) | 0 (0.0 %) | 1 (10.0 %) |
| d* (Kandidaten) | 60 | 53 (88.3 %) | 0 (0.0 %) | 0 (0.0 %) | 7 (11.7 %) |
| Gesamt | 70 | 62 (88.6 %) | 0 (0.0 %) | 0 (0.0 %) | 8 (11.4 %) |

## Ohne Klappentext (null)

- a08 Der Schatten des Windes
- d02 Zusammen ist man weniger allein
- d03 Die Tochter des Ketzers
- d10 Meeresleuchten
- d16 Magnolien Mädchen
- d22 Die erste Metro
- d27 Klassentreffen
- d40 Irrungen, Wirrungen

## Probleme

- **Google Books API nicht nutzbar:** Jeder Abruf liefert HTTP 429 `RESOURCE_EXHAUSTED` mit Tageskontingent 0 (`quota_limit_value: 0`, Projekt 624717413613 des Proxys). Ohne eigenen API-Key ist Quelle 2 gesperrt, daher 0 Treffer. Die Titel-/Autorsuche wurde aus demselben Grund nicht versucht.
- **DNB-Link-Format:** In Feld 856 steht nicht `https://d-nb.info/<idn>/04`, sondern `https://services.dnb.de/plus/idn/<idn>/blurb/`. `d-nb.info/<idn>/04` liefert „KEIN OBJEKT VORHANDEN“. Übernommen wurde der Link aus 856 $u.
- **DNB-Inhaltstext fehlt oder ist kaputt:** a08, d02, d10, d22, d27 haben einen 856-Link, der HTTP 404 liefert. d03 und d16 haben keinen Inhaltstext-Link. Bei d40 steht nur der Platzhalter „Titel befindet sich noch in Berabeitung“, er wurde als null gewertet.
- **Verlagsseite:** Für die 8 Lücken fand die Websuche keine Verlagsseite. Es gab nur Händler, Perlentaucher, Goodreads und eBay. Viele Ausgaben sind alt (1999–2010, z. B. Brigitte-Edition, Goldmann 1999). d16 ist ein Selbstverlag ohne Webauftritt. Es wurde kein Verlagsabruf gemacht und keine Ersatzquelle genutzt.
- **Gekürzte Texte:** a01, d17, d23, d30, d34, d36 und d41 sind bei 1.200 Zeichen abgeschnitten. d43 hat 1.198 Zeichen, nach dem Bereinigen. Diese Texte enden mitten im Satz.
- **Mehrere DNB-Treffer:** Bei a09, d45 und d46 lieferte die ISBN-Suche 2 Datensätze. Verwendet wurde der erste, und sein Text passt inhaltlich zum Titel.
- **Inhalt der Texte:** Die Texte sind unverändert übernommen, auch Werbe- und Pressezitate (z. B. d54 „Filmstart in Deutschland …“). Bei d20, d21 und d51 ist es eher eine Ausgabenbeschreibung als ein Klappentext.
- **Abrufe je Buch:** DNB-SRU plus Inhaltstext ergibt höchstens 2 Abrufe je Buch. Für a01 und d01 kam je ein Google-Testabruf dazu (429), also 3. Die Limits wurden eingehalten.
