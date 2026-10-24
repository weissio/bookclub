# Product

<!-- impeccable:product-schema 1 -->

## Platform

ios

## Stack

delegated: prototypes are clickable phone screens in the claude.ai Design canvas (HTML). The production stack is undecided. Android is also intended but not yet decided; iOS conventions guide the prototypes for now (assumption, 24.10.2026).

## Users

German-speaking readers who own physical books and want a calm, private place to keep them in order, record how each book reached them, and write about it in their own words. The audience explicitly includes introverted readers who prefer to show themselves through their books rather than through their person, and who stay pseudonymous. Typical scene: at home on the sofa or at the bookshelf, one-handed, often at the end of a chapter or right after finishing a book.

## Product Purpose

A personal home library first: capture books (ISBN scan, typing, or by hand), keep them sorted by reading state, rate them in depth, and keep one's own interpretation and quotes. Later, a self-curated public "Schaufenster" (its purpose, confirmed 24.10.2026: the person publishes their own book recommendations with their own notes) (a small personal library with a name and optional place) lets others find books and like-minded readers through those words. Success for step 1: the library is useful on its own, without any community.

## Positioning

Not a social feed and not a reading-challenge tracker: the library and the reader's own words are the product, and visibility is opt-in per book. Ratings separate "how much did it reach me" from describable qualities (reading flow, language, pace, strengths), instead of a single star count.

## Operating Context

- Main areas (confirmed): Bibliothek (private, home screen), Schaufenster (public, opt-in), Entdecken, Ich. Begegnungen (clubs, events) later.
- Inside Bibliothek (confirmed): Am Lesen, Gelesen, Ungelesen im Regal, Wunschliste, Abgebrochen, Eigene Regale, Statistiken, plus "Neues Buch erfassen".
- Each book has exactly one book page: rating card, own reading ("Meine Lesart"), quotes, copy details, reading history, per-book showcase switch (default off).
- Statistics (confirmed): most-read authors, most-read genres, best-rated authors, best-rated genres, top 3 best-rated books; a short summary near the shelf, depth in the "Statistiken" volume.
- Book data comes from ISBN lookups (Deutsche Nationalbibliothek, supplemented by Google Books / Open Library); cover = publisher cover or own photo.
- Fixed genre list of 16 (see PARAMETER.md). Favourite author is set manually; "most-read author" is computed.

## Capabilities and Constraints

- Required per book: title, author, genre, ownership status, reading state. Everything else optional.
- No feed, no notifications pushing the user, no follower counts.
- Tap targets at least 44 × 44 pt, whole list rows tappable; motion only in response to a tap, short (≤ ~200 ms), off under Reduce Motion; textures shipped as images, not live filters (owner's rules, ARCHITEKTUR.md).
- Undecided: final names of areas, whether "SuB" replaces "Ungelesen im Regal", multiple showcases per user, standard-cover licensing, legal duties for lending/selling.

## Brand Commitments

- Owner chose the material world "Vorsatzpapier und Buchrücken" (marbled endpaper, book cloth, gold stamping) on 10.10.2026 and later delegated all design authority to the design team (24.10.2026); the material may be reworked but was liked.
- Warmth of a book club should come from material and voice (owner, 24.10.2026).
- Must not feel like generic AI design; must be simple, uncluttered, hard to mis-tap.
- Language: German, informal "du".

## Evidence on Hand

No real users, books, quotes, testimonials or usage data exist yet. All books, authors and quotes in prototypes are invented and must be labelled as sample data. Research notes with sources: RECHERCHE.md.

## Product Principles

1. The library works alone; community is a later layer, never a precondition.
2. Private by default; every public element is a deliberate, reversible choice per book.
3. The reader's own words are the centre of a book page, above any data.
4. The app waits; it never pushes.
5. Fast to capture, deep when wanted: one tap for the minimum, depth only on request.

## Accessibility & Inclusion

Readers of all ages, including older readers using larger system text: Dynamic Type, WCAG AA contrast, meaning never carried by colour or line style alone.
