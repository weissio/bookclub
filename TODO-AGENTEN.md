# To-dos für die Agenten (Stand 24.10.2026)

Rollen:
- **Claude:** Algorithmus, Datenmodell, Dokumentation, Koordination
- **Codex:** unabhängige Prüfung
- **Designer:** Prototyp „Licht an“
- **Arjen:** Entscheidungen, Lesertest

## Algorithmus (USP III)
| # | Aufgabe | Wer | Voraussetzung |
|---|---|---|---|
| A1 | `usp3/empfehlung.py` unabhängig prüfen: Logik, Abnahmefälle, Entwurfswerte, Lücken | Codex | – |
| A2 | Realer Startkatalog: 40–60 echte Titel aus 3–4 Lesewelten, Merkmale (Genre, Thema, Tempo, Ton, Fokus, Sprache, Länge, Inhalt) redaktionell erfasst, **bevor** Bewertungen bekannt sind; Teilmenge von zwei Personen unabhängig beschreiben lassen | Claude (Entwurf), Arjen (Titelauswahl bestätigen) | – |
| A3 | Katalogdaten anbinden: DNB (SRU) und Open Library (`subjects`, `subject_places`, `subject_times`) für die Titel aus A2 abrufen, Abdeckung messen | Claude | A2 |
| A4 | Auswertung verbinden: Ergebnisse von `empfehlung.py` als Verläufe für `auswertung.py` ausgeben (Arme „nachbar“, „cluster“, später „nur F1“) | Claude | A2 |
| A5 | Variante „nur F1“ (ohne Aspekte) ergänzen, für den Nachweis „F1 allein gegen F1 plus Aspekte“ | Claude | – |
| A6 | Rückblickender Test, sobald echte Urteile vorliegen: ältere Urteile lernen, spätere zurückhalten (CLUSTERUNG, Abschnitt 8) | Claude, Prüfung durch Codex | echte Urteile |

## Lesertest (Bewertungsbogen)
| # | Aufgabe | Wer | Voraussetzung |
|---|---|---|---|
| L1 | Leitfaden für kognitive Interviews (Willis) mit Aufgaben, Nachfragen und Protokollbogen | Claude | – |
| L2 | Variante mit 2 Knöpfen je Aspekt als Schalter im Prototyp, für den Vergleich | Designer | – |
| L3 | 6–8 Leser aus der Zielgruppe gewinnen (je 3 eigene Bücher) | Arjen | L1 |
| L4 | Auswertung der Interviews, danach Bogen anpassen | Claude, Prüfung durch Codex | L3 |

## Prototyp „Licht an“
| # | Aufgabe | Wer |
|---|---|---|
| P1 | Abgleich mit der Spezifikation `usp3/BEWERTUNGSBOGEN.md`. Der Bogen bleibt bis zum Lesertest unverändert. | Designer |
| P2 | Ansicht „Empfehlung“ in Entdecken: Begründung, Datenlücken auf Antippen, „stimmt nicht“, F7 „Hat die Empfehlung gepasst?“ | Designer |
| P3 | „Buch erfassen“ (ISBN, Scan, von Hand, mehrere) als echter Ablauf | Designer |

## Offen bei Arjen
- Titelauswahl für den Startkatalog (A2)
- Leser für den Test (L3)
