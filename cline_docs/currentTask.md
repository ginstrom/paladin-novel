## Current Objective
Combine the individual part outline files (`outlines/outline-part-1.md` through `outlines/outline-part-5.md`) into the main `outlines/chapter-outline.md` file, integrating all detailed information. Delete the individual part outline files after successful consolidation.

## Context
The project currently has a main chapter outline and separate, more detailed outlines for each of the five parts of the novel. This task aims to consolidate all outline information into a single, comprehensive `chapter-outline.md` file to streamline referencing and ensure consistency. The individual part files contain valuable details on themes, character development, world-building, and tone that need to be preserved in the main outline.

## Plan for this Task
1.  **Review Memory Bank (Completed in Plan Mode):**
    *   Read essential Memory Bank files: `projectRoadmap.md`, `currentTask.md` (initial state), `techStack.md`, `codebaseSummary.md`.
    *   (User provided content for all outline files, so no further `read_file` needed for them in this planning phase).

2.  **Construct Consolidated Outline Content:**
    *   The new `outlines/chapter-outline.md` will begin with its current header: `# The Reluctant Paladin – Chapter Outline (Updated May 2025)`.
    *   For each Part (I through V):
        *   The Part heading (e.g., `## Part I: The Rude Awakening (Chs 1-3)`) will be taken from the existing `outlines/chapter-outline.md`.
        *   The detailed chapter bullet points for that Part will be taken from the corresponding `outlines/outline-part-X.md` file.
        *   The "Themes" (or "Key Themes"), "Character Development," "World Building Elements," and "Tone and Style Notes" sections from the respective `outlines/outline-part-X.md` file will be appended after the chapter list for that Part.
    *   The concluding summary section (regarding average chapter length, overall structure, tone, etc.) from the original `outlines/chapter-outline.md` will be retained at the end of the consolidated file.

3.  **Update `cline_docs/currentTask.md`**: Reflect this detailed plan (this step).

4.  **Execute Consolidation and Deletion (in Act Mode):**
    *   Use `write_to_file` to save the newly constructed content to `outlines/chapter-outline.md`.
    *   After user confirmation of successful write, use `execute_command` to delete the individual part files:
        *   `rm outlines/outline-part-1.md`
        *   `rm outlines/outline-part-2.md`
        *   `rm outlines/outline-part-3.md`
        *   `rm outlines/outline-part-4.md`
        *   `rm outlines/outline-part-5.md`
    *   (Each `rm` command will be a separate tool use for safety and confirmation).

5.  **Update `cline_docs/codebaseSummary.md`**: Document the consolidation of outline files and the deletion of the individual part files, noting that `outlines/chapter-outline.md` is now the sole source of detailed outline information.

6.  **Update `cline_docs/projectRoadmap.md`**: Mark progress on documentation organization and outline refinement.

7.  **Attempt Completion**: Present the updated `outlines/chapter-outline.md` and confirm the deletion of the other files.

## Next Steps (Pending User Approval of Plan)
1.  Request user to switch to ACT MODE.
2.  Write the new content to `outlines/chapter-outline.md`.
3.  Delete `outlines/outline-part-1.md`.
4.  Delete `outlines/outline-part-2.md`.
5.  Delete `outlines/outline-part-3.md`.
6.  Delete `outlines/outline-part-4.md`.
7.  Delete `outlines/outline-part-5.md`.
8.  Update `cline_docs/codebaseSummary.md`.
9.  Update `cline_docs/projectRoadmap.md`.
10. Attempt completion.
