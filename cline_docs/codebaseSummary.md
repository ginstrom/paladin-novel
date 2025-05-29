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
  - `translationGuide.md`: Comprehensive guide for English-Japanese translation with methodology, style guidelines, and quality assurance framework.
  - `synopsis.md`: Overall summary of the story (moved from manuscript/).
- `chapters/`: Directory for the novel manuscript chapters (reorganized from manuscript/).
  - `01_mark-of-betrayal.md` through `27_epilogue.md`: Complete manuscript chapters (Chapters 1-27 completed) with descriptive filenames.
- `build/`: Directory for generated files and build artifacts.
  - `epub-master.md`: Combined manuscript file for EPUB generation.
- `images/`: Directory for cover art and maps (renamed from assets/).
  - `cover-art.png`: Book cover image.
  - `slavers-coast-map.png` and `southern-continent-map.png`: World maps.
- `manuscript-ja/`: Directory for Japanese translations.
  - `chapter-01.md`: Initial Japanese translation of Chapter 1.
  - `chapter-01_jp_rev.md`: Improved Japanese translation applying comprehensive methodology.
- `metadata.yml`: Book metadata including title, author, publication info, and integrated book description.
- `epub.css`: Stylesheet for EPUB formatting.
- `chapter-outline.md`: Master outline of all chapters, serving as the source of truth for chapter numbering, titles, and detailed part/chapter content (themes, character development, world-building, tone/style notes). This file consolidates all chapter information.

## Data Flow
- Narrative flow is primarily defined in `chapter-outline.md`, which then guides the content of the chapter files in `chapters/`.

## External Dependencies
- None at this stage.

## Recent Significant Changes
- [2025-05-30] CHAPTER 15 REVISION ("Burden of Grace"): Altered the timing and context of Thorek Ironheart's arrival. He now appears two days after the battle, finding Gond at the graves of the fallen, rather than immediately after Silivana's counsel. This change aims for a more impactful and less convenient introduction, deepening the emotional weight of the scene and Thorek's subsequent alliance offer. User edits were incorporated to refine dialogue and actions.
- [2025-05-30] CODEBASE SUMMARY UPDATE: Slimmed down the "Recent Significant Changes" section to the 5 most recent entries for conciseness.
- [2025-05-30] PROJECT ROADMAP UPDATE: Condensed the "Completed Tasks" section in `cline_docs/projectRoadmap.md` for improved readability and conciseness, particularly for older entries.
- [2025-05-30] CHAPTER 14 REVISION ("The Legend Begins"): Revised defensive preparations to remove specific mentions of "ambushes" and "traps," focusing instead on fighters taking defensive positions. Added a new, detailed battle description to the end of the chapter. This new section includes: Gond's divine light causing crossbow bolts to go wide and miraculously bounce off defenders, unhorsing several slavers; novice warriors forming a pike wall to halt the enemy charge; Gond leading experienced warriors in a devastating counter-attack; and Gond's ubiquitous presence on the battlefield. All changes adhere to "show, don't tell" principles.
- [2025-05-29] EPUB CSS KOBO COMPATIBILITY FIX: Fixed curly quotes displaying as full-width characters on Kobo ebook readers. Enhanced font stack with comprehensive serif fallbacks (Georgia, Palatino, Book Antiqua, Minion Pro, etc.) to prevent fallback to CJK-optimized fonts. Added font-feature-settings to disable East Asian typography features ("halt" 0, "vhal" 0, "hwid" 0, "twid" 0, "qwid" 0, "palt" 0, "vpal" 0). Implemented unicode-range targeting for General Punctuation block (U+2018-U+201F) with dedicated @font-face rule. Added font-variant-east-asian: normal to prevent CJK interpretation of punctuation. Included fallback .quote-fix class for older e-readers. Solution addresses Kobo's tendency to treat curly quotes as full-width Japanese characters when falling back to default fonts.

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
