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
- `manuscript/`: Directory for the novel manuscript and related notes.
  - `chapter-01.md` through `chapter-25.md`: Complete manuscript chapters (Chapters 1-10 have content, Chapters 11-25 are placeholders with TODO notes).
  - `synopsis.md`: Overall summary of the story.
- `chapter-outline.md`: Master outline of all chapters, serving as the source of truth for chapter numbering, titles, and detailed part/chapter content (themes, character development, world-building, tone/style notes). This file consolidates all chapter information.

## Data Flow
- Narrative flow is primarily defined in `chapter-outline.md`, which then guides the content of the manuscript chapter files.

## External Dependencies
- None at this stage.

## Recent Significant Changes
- [2025-05-26] CHAPTER 21 REVISION ("A House Divided"): Major thematic and religious restructuring. Established Turin as dominant worship with Alanyi's temples in ruins. Gond's charismatic leadership reaches peak with Alanyi speaking directly through him during council meeting. Goals shifted from modern liberty/egalitarianism to restoration of Alanyi's influence, mercy tempering Turin's justice, rebuilding temples, healing wounds. Sim chosen as leader of Alanyi's revival. Silviana aids human "Reformed Order" (of Alanyi) with lost knowledge and rites. Three-army coordination now explicitly focused on spiritual restoration alongside military objectives.
- [2025-05-25] CHAPTER 20 REVISION ("Revelation and Ripples"): Enhanced Gond's charisma and discernment. Added fleeting glimpse of Alanyi's symbol on Gond's forehead during shadow wound healing. Replaced final expository section with dynamic scenes: chaotic news arrival, war council strategy session, settlement preparations montage, and a reflective closing scene between Gond and Silviana, showing the wider impact of the Circle's decision.
- [2025-05-25] CHAPTER 19 REVISION ("The Price of War"): Council debate shifted to war strategy. Sir Roderick's encounter with Gond revised for less confrontation and conditional support. Pell's temptation arc updated: accepts gold for intel, then works with council to manage information flow to Roderick's faction. Gond portrayed with increased charisma. Alanyi's symbol subtly manifested on Gond's brow.
- [2025-05-23] SHOW DON'T TELL INTEGRATION: Integrated comprehensive "show, don't tell" principles into project documentation. Updated `cline_docs/authoringGuidelines.md` with detailed guidelines for eliminating "telling" patterns and replacing with concrete actions, sensory details, and observable behaviors. Created `cline_docs/showDontTellReference.md` as a quick-reference guide with alert words, conversion examples, and character-specific guidelines. This establishes systematic approach to narrative best practices for all future writing.
- [2025-05-23] MAJOR THEMATIC REVISION: Revised the role of vengeance in the story to show Gond's spiritual growth from revenge-driven mercenary to protector-leader. Updated character arcs for Gond, Borin, and Kael to reflect transformation from vengeance to mercy. Added key scenes: Pell's question about vengeance (Chapter 13), mercy encounter with Borin and Kael (Chapter 18), and final healing of Kael (Chapter 25). Updated synopsis, chapter outline, characters, and continuity documentation to track the vengeance-to-protection transformation theme.
- [2025-05-23] Completed major chapter reorganization to fit new outline structure: moved temple experience from Chapter 10 to Chapter 6, restructured Chapters 6-10 to show gradual paladin awakening, created placeholder chapters 11-25 with detailed TODO notes for missing content. Total manuscript now structured for 25 chapters across 5 parts.
- [2025-05-23] Major restructuring of `chapter-outline.md` to implement new story arc: moved temple experience from Chapter 10 to Chapter 6, created gradual paladin awakening progression across Chapters 6-10, expanded Part II from 6 to 7 chapters, restructured Part III to start with Chapter 11, and increased total chapters from 24 to 25. Updated `cline_docs/continuity.md` with new plot threads and foreshadowing elements.
- [2025-05-22] Consolidated all detailed part outlines (`outline-part-1.md` through `outline-part-5.md`) into `outlines/chapter-outline.md`. The individual part outline files were deleted. `outlines/chapter-outline.md` is now the sole, comprehensive outline document.
- [2025-05-22] Updated `manuscript/synopsis.md` to third-person narrative and incorporated events from Chapters 1-5.
- [2025-05-22] Updated `cline_docs/continuity.md` comprehensively with new characters, plot points, timeline events, world-building details, items, and unresolved threads based on Chapters 1-5.
- [2025-05-22] Updated `cline_docs/characters.md` with detailed information for all characters appearing in Chapters 1-5, including bios, key actions, relationships, and current status.
- [2025-05-22] Updated `cline_docs/authoringGuidelines.md` with more detailed storytelling rules, including emphasis on "show, don't tell," pacing, use of dialogue, and avoiding explicit "telling" statements.
- [2025-05-22] Revised `manuscript/chapter-01.md` to fix continuity issues regarding the descriptions of fellow slaves and Gond's reaction to death, ensuring a "show, don't tell" approach. Updated `cline_docs/continuity.md` accordingly.
- [2025-05-22] Inserted a new chapter, "Chapter 5: Vengeance Deferred," into `outlines/outline-part-2.md`. This involved renumbering subsequent chapters in `outlines/outline-part-2.md` and all chapters from Part II, Chapter 5 onwards in `outlines/chapter-outline.md`, `outlines/outline-part-3.md`, `outlines/outline-part-4.md`, and `outlines/outline-part-5.md`. The total chapter count is now 24.
- [2025-05-22] Corrected chapter numbering inconsistencies across all `outlines/outline-part-X.md` files to align with `outlines/chapter-outline.md`. This ensures sequential numbering from Chapter 1 to 23 across all outline documents.
- [2025-05-22] Wrote `manuscript/chapter-02.md` ("Breaking Chains").
- [2025-05-22] Created `cline_docs/authoringGuidelines.md` to standardize chapter writing.
- [2025-05-22] Updated `cline_docs/continuity.md` with events from Chapter 2, including Gond's escape and the introduction of the Wiry Man.
- [2025-05-22] Created `cline_docs/continuity.md` to track story progress and ensure narrative consistency.
- [2025-05-22] Revised `manuscript/chapter-01.md` to integrate flashbacks more naturally into the narrative, removing explicit "Flashback:" markers.
- [2025-05-22] Changed narrative voice from first-person to third-person. Revised `manuscript/chapter-01.md` accordingly.
- [2025-05-21] Incorporated details about Gond's paladin awakening (involving Sim, priest of Alyani, and a mystical experience in a ruined temple) into `manuscript/chapter-outline.md` (Chapters 9-11) and `outlines/outline-part-3.md`. This aligns with new information in `manuscript/book-notes.md`.
- [2025-05-21] Updated `manuscript/synopsis.md` to align with the detailed chapter and part outlines in `manuscript/chapter-outline.md` and the `outlines/` directory.
- [2025-05-21] Initial project setup and creation of Memory Bank files and .clinerules.
- [2025-05-21] Revised the story opening structure. `manuscript/chapter-01.md` ("The Mark of Betrayal") now starts with Gond awakening as a slave, incorporating user-provided opening sentences. Flashbacks reveal backstory. `manuscript/chapter-outline.md` and `outlines/outline-part-1.md` have been updated to reflect this new structure and content for Chapter 1.
- [2025-05-21] Blended the first two paragraphs of `manuscript/chapter-01.md` for better flow.

## User Feedback Integration
- [2025-05-26] User requested major Chapter 21 rewrite: establish Turin as dominant worship with Alanyi's temples in ruins, reflect Gond's growing charismatic leadership with Alanyi speaking through him, shift goals from modern liberty/egalitarianism to restoration of Alanyi's influence and mercy tempering Turin's justice, choose Sim as leader of Alanyi's revival, have Silviana help human order restore lost knowledge and rites.
- [2025-05-23] User provided comprehensive "show, don't tell" feedback with specific patterns to eliminate, word alerts, character guidelines, and rewriting process. This has been fully integrated into the project's authoring methodology through updated guidelines and new reference documentation.
- [2025-05-23] User requested major chapter reorganization to fit new outline structure: move temple experience from Chapter 10 to Chapter 6, restructure Chapters 6-10 to show gradual paladin awakening, create placeholder chapters 11-25 with detailed TODO notes for missing content.
- [2025-05-23] User requested major story arc restructuring: move temple experience earlier, create gradual paladin awakening progression, expand Maera's role as rebellion network builder, and implement specific divine power manifestation sequence culminating in clear healing miracle after major battle.
- [2025-05-22] User requested continuity fixes in `manuscript/chapter-01.md` regarding slave descriptions and Gond's reactions.
- [2025-05-22] User requested stylistic change in `manuscript/chapter-01.md` to integrate flashbacks more naturally.
- [2025-05-22] User requested change from first-person to third-person narrative.
- [2025-05-21] User provided new details in `manuscript/book-notes.md` about Gond's paladin awakening, which have been integrated into the story outlines.
- [2025-05-21] User requested a change to the story's opening sequence, which has been implemented in `manuscript/chapter-01.md` and related outline files. User also provided specific opening sentences that were incorporated.
