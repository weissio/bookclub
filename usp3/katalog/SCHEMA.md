# Merkmalsschema für den Testkatalog (Entwurf, 24.10.2026)

Ein Eintrag pro Werk (JSON). Zu jedem Merkmal gehören `quelle` (URL) und `art`:
- `bibliografisch` (DNB, Verlag)
- `redaktionell` (aus Verlagstext oder Rezension abgeleitet, subjektiv)

Was sich nicht belegen lässt, bleibt `null`, nie geraten.

| Feld | Werte (kontrolliert) | Hinweis |
|---|---|---|
| `titel`, `autor`, `isbn`, `jahr`, `verlag`, `seiten` | bibliografisch | deutsche Ausgabe |
| `genre` | genau eins aus: Roman / Gegenwart · Krimi & Thriller · Fantasy · Science-Fiction · Liebesroman · Historischer Roman · Horror · Jugendbuch · Kinderbuch · Klassiker · Lyrik & Drama · Comic & Graphic Novel · Biografie & Erinnerungen · Sachbuch · Ratgeber · Reise & Natur | Arjens feste Liste |
| `thema` | 1–3 aus: Familie · Freundschaft · Liebe · Heimat & Herkunft · Erinnerung · Verlust & Trauer · Natur & Landschaft · Meer & Küste · Berge · Dorf & Provinz · Großstadt · Bücher & Lesen · Kunst & Musik · Krieg · Geschichte · Gesellschaft & Politik · Verbrechen & Ermittlung · Technik & Zukunft · Wissenschaft · Magie & Mythos · Erwachsenwerden · Alter · Arbeit & Beruf · Migration · Identität · Philosophie & Sinn | aus GND-Schlagwörtern/Verlagstext abgeleitet |
| `tempo` | ruhig · ausgewogen · rasant | redaktionell |
| `ton` | 1–2 aus: melancholisch · warm · heiter · humorvoll · düster · nüchtern · spannungsgeladen · nachdenklich | redaktionell; „düster“ ist keine Wertung |
| `fokus` | figuren · handlung · beides · ideen | `ideen` vor allem bei Sachbuch |
| `sprache` | poetisch · schlicht · nüchtern · verspielt · anspruchsvoll | redaktionell |
| `laenge` | kurz (< 250 S.) · mittel (250–450) · lang (> 450) | aus `seiten` berechnet |
| `inhalt` | Liste aus: gewalt_explizit · sexuelle_gewalt · suizid · tierleid; `[]` nur, wenn eine Quelle es prüfbar verneint, sonst `null` | `null` = nicht geprüft |
