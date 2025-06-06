## Key Components
- `.cursorrules`: User-defined rules for a separate system.
- `.clinerules`: Cline-specific rules, intended to mirror `.cursorrules` structure.
- `cline_docs/`: Directory for Cline's Memory Bank.
  - `projectRoadmap.md`: High-level project goals and progress.
  - `currentTask.md`: Details of the current task and next steps.
  - `techStack.md`: Technology choices and architectural decisions.
  - `codebaseSummary.md`: This file; overview of project structure.
  - `continuity.md`: Tracks story elements to ensure narrative consistency.
  - `characters.md`: List of characters with bios, key actions, relationships, and current status. Updated based on manuscript Chapters 1-5.
  - `authoringGuidelines.md`: Standardized workflow for writing chapters with comprehensive "show, don't tell" principles.
  - `showDontTellReference.md`: Quick-reference guide for "show, don't tell" principles during writing.
  - `translationGuide.md`: Comprehensive guide for English-Japanese translation with methodology, style guidelines, onboarding, and quality assurance framework.
  - `synopsis.md`: Overall summary of the story (moved from manuscript/).
- `chapters/`: Directory for the English manuscript chapters.
  - `01_mark-of-betrayal.md` through `27_epilogue.md`: Complete manuscript chapters (Chapters 1-27 completed) with descriptive filenames.
- `manuscript-ja/`: Directory for Japanese translations.
  - `chapter-01.md`: Initial Japanese translation of Chapter 1.
  - `chapter-01_jp_rev.md`: Improved Japanese translation applying comprehensive methodology.
  - `chapter-XX.md`: All future Japanese chapter translations.
  - `chapter-XX_notes.md`: Per-chapter translation notes (documenting new terms, cultural adaptations, QA issues, and decisions).
- `glossary-en-ja.md`: Comprehensive English-Japanese glossary for names, terms, and idioms. Updated after each chapter.
- `build/`: Directory for generated files and build artifacts.
  - `epub-master.md`: Combined manuscript file for EPUB generation.
- `images/`: Directory for cover art and maps.
  - `cover-art.png`: Book cover image.
  - `slavers-coast-map.png` and `southern-continent-map.png`: World maps.
- `metadata.yml`: Book metadata including title, author, publication info, and integrated book description.
- `epub.css`: Stylesheet for EPUB formatting.
- `chapter-outline.md`: Master outline of all chapters, serving as the source of truth for chapter numbering, titles, and detailed part/chapter content (themes, character development, world-building, tone/style notes). This file consolidates all chapter information.

## Translation Workflow Overview
- All Japanese translations are stored in `manuscript-ja/`, with each chapter having a corresponding translation notes file (e.g., `chapter-02_notes.md`).
- Translators follow the step-by-step workflow and QA checklist in `cline_docs/translationGuide.md`.
- New terms and translation decisions are added to `glossary-en-ja.md` after each chapter.
- Continuous improvement: translation guide, glossary, and notes are updated as the project progresses.
- Reference: `manuscript-ja/chapter-01_jp_rev.md` as a style benchmark for future chapters.

## Data Flow
- Narrative flow is primarily defined in `chapter-outline.md`, which then guides the content of the chapter files in `chapters/`.
- Japanese translation flow: English chapter → Japanese draft in `manuscript-ja/` → QA and revision → glossary/notes update.

## External Dependencies
- None at this stage.

## Recent Significant Changes
- [2025-06-01] Enhanced translation guide with naturalness improvement guidelines and 5-point rating scale.
- [2025-05-31] Applied spelling corrections across all 27 chapters. Manuscript now error-free.
- [2025-05-31] Added EPUB TOC CSS fix to suppress default numbering.
- [2025-05-31] Conducted timing credibility audit with minor clarifications to Ch 14 and 18.
- [2025-05-31] Enhanced Maera's magical leaf with evasive properties and guidance effects across Ch 3, 6, and 8.

## User Feedback Integration
- [2025-05-27] User requested project reorganization to match ebook publishing format: Create chapters/ directory with descriptive filenames, rename assets/ to images/, create build/ directory, move synopsis to cline_docs/, create metadata.yml with integrated blurb, add epub.css stylesheet. Successfully implemented complete restructuring following recommended format.
- [2025-05-27] User provided comprehensive translation improvement instructions for Chapter 1 Japanese translation: systematic term replacement (English quotes → Japanese brackets, manacle terminology correction), natural Japanese language optimization with 20-30% compression, cultural localization of metaphors, style unification with consistent 常体 narrative voice, and quality control through audio reading tests and particle correction.
- [2025-05-26] User requested Chapter 3 expansion to flesh out Maera's role and provide world-building: Give more details of Maera's hut, show her awareness of their plight and hint at other escapees, have her provide world-building information about slavery being accepted as fact of life, slaves being sent far away or worked to death, existence of those who oppose slavery, detailed information about hiding places (way station and hills with benefits/problems), warnings about Blackwater dangers while only advising never compelling, and subtle foreshadowing of her future role as major figure in slave revolt running a network that helps slaves escape and maintaining contact with elves.
- [2025-05-26] User requested Chapter 6 enhancement to add more buildup and make divine signs start more subtly: Have them set up camp in temple grounds with immediate positive effects (greener grass, horse calming and whickering, cooler/fresher air, group relief). Gond sets out to scout but finds himself wandering unconsciously, guided to an intact chamber deep in the temple. Enhanced divine encounter at altar with vision and voice: "You carry burdens willingly, Gond. Now carry hope." Sim notices change in Gond's expression but doesn't press directly. Divine signs should be subtle enough that Gond questions them until the voice speaks.
- [2025-05-26] User requested Chapter 5 enhancement to add suspense and danger: Gond must postpone revenge plans, leave behind his horse, wait for nightfall and escape by scaling city walls, walk back to waypoint, explain that slavers are looking for them, and head off seeking hiding place on remaining horse.
- [2025-05-26] User requested Chapter 1 enhancement to show hopelessness of Gond's situation and cruelty of guards, emphasizing salt mine destination where slaves are worked to death with most surviving only a few months.
- [2025-05-26] User requested Chapter 22 rewrite for continuity with Chapter 21's spiritual themes, focusing on Gond's spiritual growth, the three-pronged campaign's sacred goals (coastal cities/Gond, inland strongholds/dwarves, logistics/elves), the attack on three successive cities by Gond, off-camera preparations for dwarven/elven attacks with reports, Silviana's pacifism versus general elven willingness to fight, and preparations for temple purification.
- [2025-05-26] User requested major Chapter 21 rewrite: establish Turin as dominant worship with Alanyi's temples in ruins, reflect Gond's growing charismatic leadership with Alanyi speaking through him, shift goals from modern liberty/egalitarianism to restoration of Alanyi's influence and mercy tempering Turin's justice, choose Sim as leader of Alanyi's revival, have Silviana help human order restore lost knowledge and rites.
- [2025-05-23] User provided comprehensive "show, don't tell" feedback with specific patterns to eliminate, word alerts, character guidelines, and rewriting process. This has been fully integrated into the project's authoring methodology through updated guidelines and new reference documentation.
- [2025-05-23] User requested major chapter reorganization to fit new outline structure: move temple experience from Chapter 10 to Chapter 6, restructure Chapters 6-10 to show gradual paladin awakening, create placeholder chapters 11-25 with detailed TODO notes for missing content.
- [2025-05-23] User requested major story arc restructuring: move temple experience earlier, create gradual paladin awakening progression, expand Maera's role as rebellion network builder, and implement specific divine power manifestation sequence culminating in clear healing miracle after major battle.
- [2025-05-22] User requested continuity fixes in `manuscript/chapter-01.md` regarding slave descriptions and Gond's reactions.
- [2025-05-22] User requested stylistic change in `manuscript/chapter-01.md` to integrate flashbacks more naturally.
- [2025-05-22] User requested change from first-person to third-person narrative.
- [2025-05-21] User provided new details in `manuscript/book-notes.md` about Gond's paladin awakening, which have been integrated into the story outlines.
- [2025-05-21] User requested a change to the story's opening sequence, which has been implemented in `manuscript/chapter-01.md` and related outline files. User also provided specific opening sentences that were incorporated.
