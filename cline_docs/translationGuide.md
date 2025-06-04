# Translation Guide: English to Japanese
## Paladin's Rise / 聖騎士の目覚め

### Overview
This guide establishes best practices for translating "Paladin's Rise" from English to Japanese, maintaining the novel's sardonic tone, "show don't tell" narrative style, and dark fantasy atmosphere while adapting to Japanese literary conventions.

---

## Quickstart Workflow for Translators

1. **Copy the English chapter file** from `chapters/` to `manuscript-ja/` (e.g., `01_mark-of-betrayal.md` → `chapter-01.md`).
2. **Translate the chapter** following the methodology and style rules in this guide.
3. **Create a translation notes file** for the chapter (e.g., `chapter-01_notes.md`) in `manuscript-ja/` to document:
   - New terms and translation decisions
   - Cultural adaptations and reasoning
   - Character voice adjustments
   - Challenging passages and solutions
   - Compression and QA issues
4. **Run through the QA checklist** (see below) before finalizing the chapter.
5. **Update `glossary-en-ja.md`** with any new terms, idioms, or cultural concepts introduced.
6. **Submit or commit both the translated chapter and notes file.**
7. **Refine and update this guide, the glossary, and notes as needed after each chapter.**

---

## File & Folder Structure

- All Japanese translations: `manuscript-ja/`
  - Chapter files: `chapter-XX.md` (e.g., `chapter-01.md`)
  - Translation notes: `chapter-XX_notes.md` (e.g., `chapter-01_notes.md`)
- Glossary: `glossary-en-ja.md` (update after each chapter)
- Reference improved translation: `manuscript-ja/chapter-01_jp_rev.md`
- This guide: `cline_docs/translationGuide.md`

---

## Documentation & Glossary Update Protocol

- **After each chapter:**
  - Add new terms and their translations to `glossary-en-ja.md`
  - Summarize major translation decisions and cultural adaptations in the chapter’s notes file
  - Note any unresolved issues or questions for future review
  - If the guide or workflow evolves, document the change in the notes file and update this guide as needed

---

## Handling Ambiguity & Translator’s Notes

- If a term, phrase, or cultural reference is ambiguous or untranslatable:
  - Add a translator’s note in the chapter’s notes file explaining the issue and your solution
  - If unsure, consult the author or project lead before finalizing
  - Document any major adaptation decisions for future reference
  - Use footnotes sparingly in the main text; prefer documentation in the notes file

---

### Core Translation Principles

#### 1. Natural Japanese Expression
- **Prioritize natural Japanese flow over literal translation**
- Restructure sentences to follow Japanese syntax patterns
- Use appropriate Japanese literary devices and expressions
- Adapt Western narrative structures to Japanese storytelling conventions
- **Prefer common expressions over rare literary terms** (e.g., 朦朧とした意識 over 昏迷)
- **Use idiomatic body language descriptions** rather than technical ones
- **Order descriptive elements naturally** in Japanese (e.g., reorder taste descriptions for smoother flow)

#### 2. Tone and Style Preservation
- **Maintain the sardonic, dark tone** throughout
- Preserve the "show don't tell" approach using Japanese equivalents
- Keep the visceral, physical descriptions that reveal character states
- Maintain casual cruelty in dialogue through appropriate Japanese speech patterns

#### 3. Cultural Adaptation
- **Adapt format and style to fit Japanese novel conventions**
- Use appropriate honorifics and speech levels for different characters
- Employ Japanese literary techniques for internal monologue
- Adjust pacing and paragraph structure for Japanese readers

#### 4. Traditional Language Preference
- **Avoid unnecessary loanwords** in favor of traditional Japanese terms
- **Eliminate overly modern expressions** that break fantasy immersion
- **Use classical or timeless vocabulary** appropriate for epic fantasy
- **Maintain period-appropriate language** that enhances the medieval fantasy atmosphere

### Translation Methodology

#### Phase 1: Structural Analysis & Duplicate Detection
1. **Compare original and translation paragraph-by-paragraph** for gaps/duplicates
2. **Remove duplicate paragraphs** (keep the first occurrence, delete later ones)
3. **Identify missing content** and add translation as needed
4. **Verify structural consistency** between original and translation

#### Phase 2: Systematic Term & Symbol Replacement
1. **Replace all English quotation marks** "…" with Japanese brackets 「…」
2. **Convert dashes and italic markup** to natural Japanese punctuation
3. **Use ellipsis character (…) instead of three dots (...)** for consistency
4. **Fix critical terminology errors** (e.g., manacle = 烙印/焼き印, not 刺青)
5. **Standardize all proper nouns** according to glossary entries
6. **Ensure consistent technical terms** throughout

#### Phase 3: Japanese Language Optimization
1. **Compress redundant phrasing** by 20-30% while preserving meaning
2. **Restructure sentences** to follow natural Japanese word order (subject → action → description)
3. **Improve metaphors and comparisons** for Japanese linguistic sensibilities
4. **Eliminate verbose direct translations** in favor of natural Japanese expressions
5. **Balance sentence length** for optimal reading rhythm

#### Phase 4: Cultural Localization
1. **Adapt animal and sensory metaphors** to fit Japanese cultural context
2. **Adjust physical descriptions** to flow naturally in Japanese
3. **Localize dialogue patterns** to match character types appropriately
4. **Ensure cultural concepts** are understandable to Japanese readers

#### Phase 5: Style Unification & Quality Control
1. **Maintain consistent 常体 (casual form)** for narrative voice
2. **Limit comma usage** to maximum 2 per sentence for readability
3. **Balance kanji and hiragana** appropriately
4. **Eliminate awkward phrase repetitions**
5. **Ensure proper particle usage** throughout

#### Phase 6: Final Review & Correction
1. **Perform audio reading test** for natural flow
2. **Check for particle errors** and grammatical inconsistencies
3. **Verify tone consistency** throughout the chapter
4. **Confirm all terminology** matches glossary entries
5. **Final proofreading** for typos and formatting

### Character Voice Guidelines

#### Speech Patterns by Character Type
- **Guards/Slavers**: Rough, casual speech (だ/である調) with crude expressions
- **Gond**: Internal monologue in literary style, external speech varies by situation
- **Fellow Slaves**: Varied speech reflecting backgrounds and desperation
- **Authority Figures**: Formal speech patterns (です/ます調) when appropriate

#### Internal Monologue
- Use Japanese literary conventions for thoughts
- Employ appropriate sentence endings (だろう, のだ, etc.)
- Maintain sardonic tone through word choice and rhythm

#### Dialogue Attribution Variety
**CRITICAL**: Avoid repetitive use of 「言った」. Use varied verbs that reflect speaker tone and emotion:

**Authority/Command Verbs**:
- 吠えた (barked/roared) - for harsh military commands
- 命じた (ordered) - for formal commands
- 怒鳴った (shouted) - for angry outbursts
- 叫んだ (yelled/cried out) - for urgent calls

**Conversational Verbs**:
- 答えた (answered/replied) - neutral response
- 尋ねた (asked/inquired) - for questions
- 囁いた (whispered) - for quiet speech
- 呟いた (muttered) - for under-breath comments

**Emotional Verbs**:
- 声を低く落とした (lowered voice) - for threats
- 声に軽さを込めた (lightened voice) - for casual tone
- 冷静に答えた (answered calmly) - for controlled responses
- 慌てて言った (said hurriedly) - for rushed speech

**Tone-Specific Expressions**:
- 「よく考えることだな」声を低く落とした (gruff threat)
- 「頼む、助けてくれ」(desperation implied through content)
- 桶職人は冷静に答え (craftsman's measured response)

**Usage Guidelines**:
- Match verb to character personality and situation
- Consider power dynamics (guards vs. civilians)
- Reflect emotional state through attribution choice
- Avoid using 「言った」more than once per page

### Technical Guidelines

#### Character Names
- **Fantasy names**: Use katakana (ゴンド, ペル, シム, etc.)
- **Maintain consistency** with established glossary entries
- **Consider pronunciation** when creating new name translations

#### Place Names
- **Transliterate place names to katakana** as the default approach (e.g., "Blackwater" → "ブラックウォーター")
- **Translate geographical features and descriptive elements** (e.g., "Bay" → "湾", "Port" → "港")
- **Translate ranks, titles, and common descriptive words** (e.g., "Captain" → "船長")
- **Combined example**: "Blackwater Bay" → "ブラックウォーター湾" (transliterated place + translated feature)
- **Exception for culturally adapted names**: Some establishments may use natural Japanese equivalents (跳ね馬亭 for Prancing Dragon)
- **Maintain geographical consistency** throughout the series

**⚠️ CRITICAL CORRECTION NOTE**: "Blackwater Bay" was incorrectly translated as "黒水湾" in Chapter 1 (already submitted). All future references MUST use the correct "ブラックウォーター湾" to maintain consistency with the established translation rules.

#### Religious and Cultural Terms
- **Establish consistent translations** for religious concepts
- **Use appropriate honorifics** for deities and religious figures
- **Adapt cultural concepts** to be understandable to Japanese readers
- **Paladin**: Always use 聖騎士 (not パラディン)
- **Paladin's Rise**: 聖騎士の目覚め (book title)

#### Critical Terminology Corrections
- **Manacle/Brand**: Always use 烙印 or 焼き印, never 刺青 (tattoo)
- **Hold**: 船倉 (ship's hold)
- **Cargo**: 積荷 (when referring to slaves dehumanizingly)
- **Overseers**: 監督官 (mine supervisors)

### Specific Translation Challenges

#### "Show Don't Tell" in Japanese
- **Replace emotion words** with physical manifestations
- **Use sensory details** and concrete actions
- **Employ Japanese literary techniques** for subtle emotional revelation
- **Avoid direct statement** of mental states

#### Dark Fantasy Atmosphere
- **Use appropriate vocabulary** for violence and suffering
- **Maintain visceral impact** without being gratuitously graphic
- **Preserve the oppressive atmosphere** through word choice and rhythm

#### Sardonic Tone
- **Use Japanese irony and understatement** techniques
- **Employ appropriate sentence endings** for sarcastic effect
- **Maintain dark humor** through cultural adaptation

### Loanword Avoidance & Traditional Language Guidelines

#### Core Principles for Fantasy-Appropriate Language

**1. Avoid Unnecessary Loanwords**
- **Principle**: Use traditional Japanese terms instead of katakana loanwords when natural alternatives exist
- **Goal**: Maintain the timeless, medieval fantasy atmosphere without modern linguistic intrusions

**2. Preferred Traditional Alternatives**

**Military & Combat Terms**:
- ❌ アーマー → ✅ 鎧 (armor)
- ❌ ソード → ✅ 剣 (sword)
- ❌ シールド → ✅ 盾 (shield)
- ❌ バトル → ✅ 戦い/戦闘 (battle)
- ❌ アタック → ✅ 攻撃 (attack)
- ❌ ディフェンス → ✅ 防御 (defense)

**General Vocabulary**:
- ❌ チーム → ✅ 一団/仲間/集団 (team/group)
- ❌ リーダー → ✅ 指導者/頭領/長 (leader)
- ❌ メンバー → ✅ 一員/仲間 (member)
- ❌ グループ → ✅ 集団/一行 (group)
- ❌ パートナー → ✅ 相棒/仲間 (partner)
- ❌ エネルギー → ✅ 力/気力/精力 (energy)

**Emotional & Abstract Concepts**:
- ❌ ストレス → ✅ 重圧/負担/苦痛 (stress)
- ❌ ショック → ✅ 衝撃/驚愕 (shock)
- ❌ パニック → ✅ 混乱/狼狽 (panic)
- ❌ プレッシャー → ✅ 圧力/重圧 (pressure)

**3. Acceptable Loanword Categories**

**Fantasy-Specific Terms** (when no natural Japanese equivalent exists):
- ✅ パラディン → 聖騎士 (paladin - but prefer the Japanese translation)
- ✅ エルフ (elf - established fantasy term)
- ✅ ドワーフ (dwarf - established fantasy term)

**Proper Nouns** (character/place names):
- ✅ ゴンド, ペル, シム (character names)
- ✅ ブラックウォーター (place names when transliteration is preferred)

**4. Modern Expression Avoidance**

**Contemporary Slang & Expressions**:
- ❌ やばい → ✅ 危険だ/まずい (dangerous/bad)
- ❌ すごい → ✅ 見事な/素晴らしい/驚くべき (amazing - use more formal alternatives)
- ❌ めちゃくちゃ → ✅ 非常に/ひどく (extremely)

**Modern Conceptual Language**:
- ❌ システム → ✅ 仕組み/制度 (system)
- ❌ プロセス → ✅ 過程/手順 (process)
- ❌ メソッド → ✅ 方法/手法 (method)
- ❌ スタイル → ✅ 様式/流儀 (style)

**5. Classical & Literary Alternatives**

**Preferred Classical Expressions**:
- ✅ 武具 (weapons and armor)
- ✅ 戦士 (warrior)
- ✅ 勇士 (brave warrior)
- ✅ 剣客 (swordsman)
- ✅ 武人 (military person)
- ✅ 義士 (righteous person)

**Traditional Descriptive Language**:
- ✅ 勇猛 (brave and fierce)
- ✅ 剛勇 (strong and brave)
- ✅ 威風堂々 (majestic and dignified)
- ✅ 凛然 (dignified and resolute)

**6. Context-Sensitive Guidelines**

**Dialogue Considerations**:
- **Common characters**: Use everyday traditional Japanese
- **Educated characters**: May use more classical expressions
- **Military characters**: Prefer traditional military terminology
- **Religious characters**: Use classical religious language

**Narrative Voice**:
- **Maintain consistent traditional tone** throughout
- **Avoid mixing modern and classical styles** within the same passage
- **Use timeless expressions** that don't date the translation

**7. Quality Control for Traditional Language**

**Review Questions**:
- Does this word/phrase sound like it belongs in a medieval fantasy setting?
- Would this expression be understood by readers 50 years ago?
- Is there a more traditional Japanese alternative available?
- Does the language choice enhance or detract from the fantasy atmosphere?

### Compression Techniques

#### Redundancy Elimination
- **Combine repetitive descriptive phrases** into single, more impactful expressions
- **Remove unnecessary explanatory text** that Japanese readers can infer
- **Streamline verbose passages** while preserving essential meaning
- **Consolidate similar actions** described multiple ways

#### Natural Japanese Flow
- **Use present tense for immediate actions** and past tense for completed events
- **Employ Japanese sentence connectors** (が, けれど, しかし) appropriately
- **Utilize Japanese literary devices** like onomatopoeia where suitable
- **Maintain proper rhythm** through varied sentence lengths

### Quality Assurance Checklist

#### Before Finalizing Translation
- [ ] All character names match glossary entries
- [ ] Place names are consistent with established translations
- [ ] Speech patterns are appropriate for each character
- [ ] Tone remains sardonic and dark throughout
- [ ] "Show don't tell" principles are maintained
- [ ] Japanese flows naturally when read aloud
- [ ] Technical terms match glossary entries
- [ ] Cultural adaptations enhance rather than obscure meaning
- [ ] No English punctuation marks remain
- [ ] Ellipsis character (…) used instead of three dots (...)
- [ ] Critical terminology is correctly translated
- [ ] Text is compressed by 20-30% from literal translation
- [ ] Consistent 常体 narrative voice maintained

#### Traditional Language & Loanword Review
- [ ] No unnecessary loanwords used where traditional Japanese alternatives exist
- [ ] Military/combat terms use traditional vocabulary (鎧, 剣, 戦い, etc.)
- [ ] General vocabulary avoids modern loanwords (一団 not チーム, 指導者 not リーダー)
- [ ] Emotional concepts use traditional expressions (重圧 not ストレス, 衝撃 not ショック)
- [ ] No modern slang or contemporary expressions present
- [ ] Classical/literary alternatives used where appropriate for fantasy setting
- [ ] Language choices enhance medieval fantasy atmosphere
- [ ] All retained loanwords are justified (established fantasy terms, proper nouns)

#### Glossary Maintenance
- **Add new terms** to `glossary-en-ja.md` as they appear
- **Note cultural adaptations** and reasoning
- **Maintain consistency** across all translated chapters
- **Document translation decisions** for future reference

### Reference Materials

#### Primary Reference
- **Glossary**: `glossary-en-ja.md` - Comprehensive term translations
- **Improved Translation**: `manuscript-ja/chapter-01_jp_rev.md` - Updated style reference
- **Original Translation**: `manuscript-ja/chapter-01.md` - Initial translation for comparison

#### Style Guidelines
- **Narrative Voice**: Third-person past tense with sardonic undertones
- **Paragraph Structure**: Adapted for Japanese reading patterns
- **Dialogue Format**: Standard Japanese novel conventions

### Translation Notes Template

For each chapter translation, maintain notes on:
- **New terminology** and translation decisions
- **Cultural adaptations** made and reasoning
- **Character voice developments** or changes
- **Challenging passages** and solutions employed
- **Compression techniques** applied
- **Quality issues** identified and resolved

### Continuous Improvement

#### After Each Chapter
- **Review translation quality** against this guide
- **Update glossary** with new terms
- **Note any style evolution** or improvements
- **Refine methodology** based on experience
- **Document lessons learned** for future chapters

#### Series-Wide Consistency
- **Maintain character voice evolution** across chapters
- **Track terminology consistency** throughout the series
- **Document major translation decisions** for future volumes
- **Preserve narrative continuity** in Japanese adaptation

### Naturalness Improvement Guidelines

#### Core Principles for Natural Expression
Based on analysis of Chapter 1 improvements that achieved 5/5 naturalness rating:

#### 1. Word Choice Hierarchy
**Principle**: Prefer common expressions over rare literary terms
- ❌ 昏迷 → ✅ 朦朧とした意識 (avoid rare literary terms)
- ❌ 古いエール → ✅ 苦い酒 (more natural for Japanese readers)
- **Rule**: When multiple translations exist, choose the one most familiar to general readers

#### 2. Idiomatic Body Language Descriptions
**Principle**: Use natural Japanese expressions for physical reactions
- ❌ 顎の筋肉がピクリと動いた → ✅ 顎がわずかに引き締まった
- ❌ 額に痒みが走った → ✅ 額がむず痒くなった
- **Rule**: Avoid technical anatomical descriptions; use how Japanese speakers naturally describe body language

#### 3. Enhanced Dialogue Authenticity
**Principle**: Add natural particles and emotional markers for realistic speech
- ❌ アラニィよ、慈悲を。 → ✅ アラニィよ、どうか慈悲を…
- **Techniques**:
  - Add "どうか" for pleading tone
  - Use ellipsis (...) for emotional trailing off
  - Include natural hesitation markers

#### 4. Improved Internal Monologue Flow
**Principle**: Make thoughts contemplative rather than directive
- ❌ 彼らを不注意にさせよう → ✅ やつらがもっと油断するまで待とう
- **Rule**: Internal thoughts should sound like natural mental processes, not commands

#### 5. Natural Narrative Element Ordering
**Principle**: Reorder descriptive elements for Japanese linguistic flow
- ❌ 血と古いエール、そして苦いもの → ✅ 血と苦い酒、そして不快な味
- **Rule**: Follow Japanese preference for concrete → abstract, specific → general

#### 6. Elimination of Translation Artifacts
**Principle**: Replace constructions that reveal translation origins
- ❌ 単に抜きにされた → ✅ ただ取り残された
- **Rule**: If a phrase sounds like it was translated, find the natural Japanese equivalent

#### 7. Atmospheric Description Enhancement
**Principle**: Use immediate, visceral language over formal constructions
- ❌ 空気が粘ついているように感じられた → ✅ 空気がまとわりつくように重かった
- **Rule**: Prefer active, immediate descriptions that put readers in the scene

#### Quality Assessment Framework

**Naturalness Rating Scale**:
- **5/5**: Reads as if originally written in Japanese
- **4/5**: Minor translation patterns detectable
- **3/5**: Generally natural with some awkward phrases
- **2/5**: Clearly translated but understandable
- **1/5**: Difficult to read due to translation artifacts

**Testing Methods**:
1. **Audio Reading Test**: Read aloud - does it flow naturally?
2. **Native Speaker Test**: Would a native speaker detect translation patterns?
3. **Comprehension Test**: Can readers focus on story without being distracted by language?

**Target Standards**:
- **Minimum Acceptable**: 4/5 naturalness rating
- **Professional Standard**: 5/5 naturalness rating
- **Accuracy Requirement**: Must maintain 5/5 accuracy regardless of naturalness improvements

### Common Pitfalls to Avoid

#### Translation Errors
- **Never translate "manacle" as 刺青** - always use 烙印 or 焼き印
- **Avoid literal word-for-word translation** of metaphors
- **Don't preserve English sentence structure** when it sounds unnatural in Japanese
- **Avoid mixing formal and casual speech** within the same narrative voice
- **Don't use rare literary terms** when common expressions are more natural

#### Style Issues
- **Don't over-explain** what Japanese readers can infer from context
- **Avoid excessive comma usage** that disrupts reading flow
- **Don't ignore Japanese literary conventions** in favor of English patterns
- **Avoid inconsistent terminology** across chapters
- **Don't sound like a translation** - prioritize natural Japanese expression

---

*This guide incorporates lessons learned from the Chapter 1 improvement process and should continue to be updated as translation work progresses.*
