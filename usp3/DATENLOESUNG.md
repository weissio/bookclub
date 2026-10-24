# Lösung für dünne Buchdaten (Stand 24.10.2026)

Problem: Für gute Empfehlungen fehlen Merkmale. DNB-Schlagwörter fehlen bei 7 von 10 Romanen, Tempo/Ton/Fokus fehlen bei 85–95 % der Kandidaten. Recherche: `DATENQUELLEN.md`.

## Lösung in drei Schichten

| Schicht | Quelle | Liefert | Kosten | Status |
|---|---|---|---|---|
| 1. Bibliografie | DNB-SRU (CC0) | Titel, Autor, Umfang, GND-Schlagwörter (lückenhaft) | 0 € | läuft |
| 2. Klappentext | DNB-Feld 856 → MVB-Inhaltstext | Bedeutungsvergleich (Embedding) + geschätzte Merkmale Thema/Fokus/Ton | 0 € Daten, Modell lokal | läuft, Rechtsfrage offen |
| 3. Leserangaben | Bewertungsbogen F3/F5 | Tempo, Ton, Aspekte – die einzige verlässliche Quelle für Erlebnismerkmale | 0 € | im Bogen vorgesehen |
| später | VLB-Lizenz (MVB) | Thema-Codes, Lesemotive, Cover, anzeigbare Klappentexte | 150 € Einrichtung + Jahresgebühr nach Umsatz, Preisliste nicht öffentlich | verhandeln, wenn App live |

Ausgeschlossen: Google Books (keine Speicherung, keine Bezahl-App ohne Sondervereinbarung), Open Library (Beschreibung bei 11/120).

## Was gemessen wurde

- Klappentexte: 62 von 70 Testbüchern (89 %); Stichprobe der Recherche 116/120 (97 %).
- Geschätzt aus Klappentext (nur „hoch“/„mittel“, je mit Beleg): Thema 62, Fokus 36, Ton 35, Sprache 6, **Tempo 5**. Tempo ist aus Werbetext nicht ablesbar → kommt von Lesern.
- Wortvergleich (TF-IDF): Kosinus 0,01–0,06, praktisch kein Signal.
- Bedeutungsvergleich: `paraphrase-multilingual-MiniLM-L12-v2`, lokal, mehrsprachig. Werte werden je Anker als Rang normiert („ähnlicher als x % der Bücher“), damit Verfahren vergleichbar sind.

## Offene Risiken

1. **Rechte an MVB-Klappentexten:** DNB nennt sie nicht unter CC0. Nur intern auswerten, nicht anzeigen; schriftlich bei DNB/MVB anfragen (To-do Arjen).
2. **Kandidatensuche:** DNB-SRU sortiert nicht nach Relevanz. Ziel: eigener Index (Embeddings aller DNB-Romane mit Klappentext) und eigenes Ranking.
3. **Geschätzte Merkmale sind Schätzungen:** in Daten markiert (`geschaetzt`), Katalog- und Leserwerte haben Vorrang.
4. **Textgewicht 0,5** ist ein Entwurfswert; wird erst nach Arjens Urteil über die verblindete Liste justiert.

## Reproduzieren

    MODUS=text+schaetzung python3 usp3/test-arjen/lauf.py            # Bedeutungsvergleich
    MODUS=text+schaetzung TEXT=tfidf python3 usp3/test-arjen/lauf.py  # Wortvergleich zum Vergleich
