# Stand

_Zuletzt aktualisiert: 24.10.2026_

## Wo wir stehen

**Phase:** Schritt 1 – Bibliothek. Gestaltungsrichtung gewählt: 3A „Licht an“.

**Erledigt**
- Grundkonzept geklärt: private Bibliothek → freiwilliges Schaufenster → Entdecken (siehe [ENTSCHEIDUNGEN.md](ENTSCHEIDUNGEN.md))
- Recherche zu Wettbewerbern, Leserwünschen, Bewertungsgewohnheiten, ISBN und Buchdaten-Schnittstellen (siehe [RECHERCHE.md](RECHERCHE.md))
- Klick-Prototyp „Buch erfassen“, Version 3 („Karteikarte“) – siehe [prototyp/](prototyp/)
- Architektur der App bestätigt – siehe [ARCHITEKTUR.md](ARCHITEKTUR.md)
- Vier Stilrichtungen für die Startseite entworfen, Richtung C „Vorsatzpapier und Buchrücken“ gewählt – siehe [prototyp/stilrichtungen/](prototyp/stilrichtungen/)
- Klick-Prototyp „Meine Bibliothek“ in Stil C: Regal, Band aufschlagen, Listen als Buchseite, Buchseite eines Buches – siehe [prototyp/bibliothek/](prototyp/bibliothek/)
- Design-Experte gefunden: Impeccable (Open Source) als Designer, iOS-Plugin als Zweitprüfer; erste Kritik 19/40
- Neue Bibliothek vom Designer-Team: Regenbogen-Reihe aus liegenden Bänden, Weiterlesen-Karte mit „Seite eintragen“, Buchseite mit den eigenen Worten zuoberst – siehe [prototyp/app/](prototyp/app/)
- Korrekturrunde nach Abschlussprüfung und iOS-Prüfung eingebaut (Details in [prototyp/app/README.md](prototyp/app/README.md))
- Psychologische Beratung zur Zielgruppe (Leser, Sammler, Introvertierte) mit belegter Recherche – siehe [.impeccable/psychologie/](.impeccable/psychologie/)
- Startseite danach neu: Regal-Rückwand statt Weiß, Ex-Libris, Buch mit Lesebändchen obenauf, ein einziges „Ein Buch dazustellen“, Lesart-Zettel am Brett, Druckvermerk

**Noch nicht bestätigt**
- Der Prototyp beginnt noch direkt mit dem Scan und passt damit nicht zur bestätigten Architektur. Er muss neu aufgebaut werden.
- Die Bewertungsstruktur im Prototyp ist ein Vorschlag (siehe ENTSCHEIDUNGEN.md, Abschnitt „Vorschläge“).

## Nächster Schritt

- **Bewertungsbogen eingefroren** bis zum Lesertest, siehe [usp3/BEWERTUNGSBOGEN.md](usp3/BEWERTUNGSBOGEN.md). Die Spezifikation ist belegt, der Prototyp „Licht an“ setzt sie um.
- **Lesertest:** zwei Runden kognitiver Interviews mit je 6–8 Lesern zum Verständnis der Fragen. Der Testplan steht in der Spezifikation.
- **Nachweis zum Algorithmus:** F1 allein gegen F1 plus Aspekte, gemessen an späteren Buchbewertungen. Grundlage sind [usp3/CLUSTERUNG.md](usp3/CLUSTERUNG.md) und [usp3/auswertung.py](usp3/auswertung.py).

**Hinweis:** Der Push zu GitHub schlägt seit 24.10. mit 403 fehl. Die Commits liegen lokal; der GitHub-Zugang muss in den Einstellungen unter Konnektoren erneuert werden.

## Offene Fragen

1. Soll die Wirkung eigener Texte („hat jemanden zum Buch gebracht“) öffentlich sichtbar sein oder nur für den Schreibenden?
2. Soll ein Nutzer mehrere Schaufenster betreiben können?
3. Coverbilder: Wie dürfen Standardcover rechtlich genutzt werden (VLB-Lizenz klären)?
4. Autor bewerten: direkt oder nur indirekt („Mehr von dieser Autorin?“)?
5. Begriff „SuB“ (Stapel ungelesener Bücher) statt „Ungelesen im Regal“ verwenden?
6. Endgültige Namen der Hauptbereiche.
7. Gilt Stil C für die ganze App oder nur für die Bibliothek? (vorerst nur Bibliothek)
8. Verleih und Verkauf: rechtliche Pflichten als Plattform (u. a. DAC7) – **noch nicht recherchiert, nur als Hinweis genannt.**
