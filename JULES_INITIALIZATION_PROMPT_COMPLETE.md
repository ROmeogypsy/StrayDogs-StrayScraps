# **JULES INITIALIZATION PROMPT - COMPLETE PACKAGE**

## **YOUR MISSION**

Build the complete **Stray Dogs Worldengine v5.0** from the provided documentation.

You have been given **FOUR documents** plus the **source material**:

1. **Document 1**: Build Instructions (repository structure, systems, process)
2. **Document 2**: Tags & Protocols (tag system, AI runtime, narrative quality)
3. **Document 3**: Canon Bible (consistency rules, expansion opportunities, world logic)
4. **Document 4**: Automation Scripts (working Python code)
5. **Source Material**: Stray_Dogs_Universe.pdf (the story to parse)

---

## **DELIVERABLES**

When complete, provide:

### ✅ **Complete Repository**
Full directory structure with all files as specified in Document 1:
- `world/` - Overview, timeline, economics
- `locations/` - All significant places
- `factions/` - Organizations
- `chars/` - All named characters (organized by role)
- `tensions/` - Active conflicts
- `events/` - Historical moments
- `mechanics/` - Systems
- `culture/` - Identity markers
- `registry/` - Visual database (appearance, relationships)
- `reactive_world/` - NPC response system
- `meta/` - AI navigation files
- `sessions/` - Session log structure
- `scripts/` - Three working Python scripts

### ✅ **README.md**
Usage guide for AI models and human users

### ✅ **Validation Report**
Confirm:
- All 500+ tags created and categorized
- All named characters have files (chars + visual profiles)
- All relationship matrices complete
- Tag validator runs without errors
- Cross-reference builder generates successfully
- No orphaned tags

### ✅ **Initial Git Commit**
```
git commit -m "Initial worldengine build - Stray Dogs Universe v5.0

Complete repository structure:
- 70+ character/location/faction files
- Visual registry: 25+ appearance profiles
- Reactive world: NPC memory, faction protocols, consequences
- 500+ tag system with variations
- Complete relationship matrices (65 Dogs)
- Cross-reference intelligence
- AI runtime protocols
- Narrative quality systems
- Automation scripts (Python)

Canon state: February 6, 2026
Features: Visual descriptions, reactive NPCs, consequence tracking
Ready for session play"
```

---

## **BUILD PROCESS (EXECUTE IN THIS ORDER)**

### **PHASE 1: Repository Initialization** ⏱️ 5 minutes

```bash
# Initialize Git repository
git init stray-dogs-worldengine
cd stray-dogs-worldengine

# Create all directories
mkdir -p world locations factions chars/{high_command,frontline,embedded,academy,new_members,supporting}
mkdir -p tensions events mechanics culture
mkdir -p registry/{appearance_profiles,relationship_matrices,physical_details}
mkdir -p reactive_world/{npc_awareness,faction_responses,environmental_state,consequence_chains}
mkdir -p meta sessions scripts

# Create .gitignore
cat > .gitignore << 'EOF'
# Temp files
*.tmp
*~
.DS_Store

# Session drafts
sessions/draft_*

# Python cache
__pycache__/
*.pyc
*.pyo

# OS files
.DS_Store
Thumbs.db
EOF
```

---

### **PHASE 2: Parse PDF into Markdown Files** ⏱️ 30-45 minutes

**Instructions from Document 1, Section: PDF Extraction**

1. **Extract all narrative content** from Stray_Dogs_Universe.pdf
2. **Create one file per**:
   - Named character (25+ files in `chars/`)
   - Significant location (10+ files in `locations/`)
   - Faction (8+ files in `factions/`)
   - Major event (6+ files in `events/`)
   - Active tension (7+ files in `tensions/`)

3. **Use YAML frontmatter** on every file:
```yaml
---
[File-specific metadata]

tags:
  [category]: [#Tag1, #Tag2]

last_updated: 2026-02-06
canon_version: Initial
---
```

4. **Preserve voice and tone** (don't make it sterile)
5. **Follow templates** from Document 1

---

### **PHASE 3: Generate Tag System** ⏱️ 20-30 minutes

**Instructions from Document 2**

Create `meta/tags.md` with **500+ tags** organized by:

**Category A: Explicit Entities**
- Characters (25+ individual tags)
- Locations (15+ tags)
- Factions (10+ tags)

**Category B: Thematic & Atmospheric**
- Core Pillars (Grey/Red/Navy/Silence)
- Atmospheric (Sonic, Temporal, Spatial)
- Systemic (Economic, Violence, Power)
- Mechanics & Operations
- Emotional/Psychological
- Plot/Tension

**Category C: Visual & Reactive**
- Visual Descriptors
- Reactive World tags

Create `meta/tag_variations.md` mapping acceptable variations to canonical forms.

---

### **PHASE 4: Apply Tags to All Files** ⏱️ 30-40 minutes

For **EVERY markdown file created**:

1. Add appropriate tags to YAML frontmatter
2. **Cross-reference bidirectionally**:
   - If `chars/stray.md` tags `#Plaza`
   - Then `locations/the_plaza.md` must tag `#Stray`
3. Set priority level (High/Medium/Low)
4. Ensure tags exist in `meta/tags.md` or `meta/tag_variations.md`

---

### **PHASE 5: Build Visual Registry** ⏱️ 45-60 minutes

**Instructions from Document 1, Section: Visual Registry System**

#### **A. Appearance Profiles**

Create `registry/appearance_profiles/[character]_visual.md` for ALL named characters.

Use templates from Document 1. Must include:
- Core Physical Description (build, face, distinctive features)
- Clothing & Appearance
- Physical State Indicators
- Mannerisms
- How to Describe in Scenes

**Priority characters** (create these first):
- Stray, Scraps, Big 9, Dame, Zed, Snout, Chew-toy
- Rax, K-9
- Alistair, Nala, Leo
- Ruckus, Whistle, Matches, Needles

#### **B. Relationship Matrices**

Create `registry/relationship_matrices/dog_internal_relationships.md`:
- Map all 65 Dogs
- Use intensity scale (Level 0-5)
- Document relationship types (🛡️ Protector, 🎓 Mentor, etc.)
- Include dynamic tracker template

#### **C. Physical Details Catalogs**

Create:
- `registry/physical_details/clothing_catalog.md`
- `registry/physical_details/scars_injuries_catalog.md`
- `registry/physical_details/tattoo_registry.md`
- `registry/physical_details/physical_mannerisms.md`

---

### **PHASE 6: Build Reactive World System** ⏱️ 30-40 minutes

**Instructions from Document 1, Section: Reactive World System**

#### **A. NPC Awareness**

Create:
- `reactive_world/npc_awareness/community_memory.md`
- `reactive_world/npc_awareness/rumor_system.md`
- `reactive_world/npc_awareness/reputation_tracker.md`
- `reactive_world/npc_awareness/witness_records.md`

#### **B. Faction Response Protocols**

Create:
- `reactive_world/faction_responses/dog_response_protocols.md`
- `reactive_world/faction_responses/academy_response_protocols.md`
- `reactive_world/faction_responses/west_end_response_protocols.md`
- `reactive_world/faction_responses/police_response_protocols.md`

#### **C. Environmental State**

Create:
- `reactive_world/environmental_state/location_conditions.md`
- `reactive_world/environmental_state/time_based_populations.md`
- `reactive_world/environmental_state/weather_impacts.md`
- `reactive_world/environmental_state/ongoing_events.md`

#### **D. Consequence Chains**

Create:
- `reactive_world/consequence_chains/action_consequence_tree.md`
- `reactive_world/consequence_chains/escalation_triggers.md`
- `reactive_world/consequence_chains/ripple_effect_tracker.md`

---

### **PHASE 7: Create Meta Files** ⏱️ 30-40 minutes

**Instructions from Document 2**

Create ALL meta files:

1. `meta/tags.md` - Master tag index ✅ (already created Phase 3)
2. `meta/tag_variations.md` - Acceptable variations ✅ (already created Phase 3)
3. `meta/ai_runtime_protocol.md` - How AI uses repository
4. `meta/tag_validation_examples.md` - Correct/incorrect examples
5. `meta/session_tag_template.md` - End-of-response format
6. `meta/cross_reference.md` - Bidirectional relationships (auto-generated in Phase 9)
7. `meta/priority_contexts.md` - What to load when
8. `meta/narrative_quality_checklist.md` - Writing standards
9. `meta/voice_preservation_guide.md` - Character speech patterns
10. `meta/emotional_beats.md` - Arc tracking template
11. `meta/scene_transitions.md` - Flow techniques
12. `meta/conflict_escalation.md` - Tension ladder
13. `meta/thematic_callbacks.md` - Recurring symbols
14. `meta/reactive_world_protocol.md` - How to use reactive systems
15. `meta/visual_description_guide.md` - How to describe characters
16. `meta/consequence_engine_rules.md` - Cause-effect principles

**Copy content from Document 2 for each file.**

---

### **PHASE 8: Add Automation Scripts** ⏱️ 10-15 minutes

**Instructions from Document 4**

Copy the three complete Python scripts:

1. `scripts/tag_validator.py` - Validates all tags
2. `scripts/engine_sync.py` - Monitors sessions, updates canon
3. `scripts/cross_ref_builder.py` - Auto-generates cross-references

Make executable:
```bash
chmod +x scripts/*.py
```

---

### **PHASE 9: Validation** ⏱️ 15-20 minutes

**Before finalizing, verify:**

#### ✅ **Completeness Check**

Run these commands and confirm:

```bash
# Count character files (should be 25+)
find chars -name "*.md" | wc -l

# Count location files (should be 10+)
find locations -name "*.md" | wc -l

# Count appearance profiles (should match character count)
find registry/appearance_profiles -name "*.md" | wc -l

# Verify meta files exist (should be 16)
ls meta/*.md | wc -l
```

#### ✅ **Tag System Check**

```bash
# Run tag validator
python scripts/tag_validator.py
```

Should output: `✓ ALL TAGS VALID`

If errors appear, fix them before proceeding.

#### ✅ **Cross-Reference Check**

```bash
# Generate cross-references
python scripts/cross_ref_builder.py
```

Should create `meta/cross_reference.md` with no errors.

#### ✅ **File Structure Check**

Verify all directories exist:
```bash
tree -L 1
```

Should show:
```
.
├── chars
├── culture
├── events
├── factions
├── locations
├── mechanics
├── meta
├── reactive_world
├── registry
├── scripts
├── sessions
├── tensions
└── world
```

---

### **PHASE 10: Create README.md** ⏱️ 10-15 minutes

**Template provided in Document 1, Section: Create README.md**

Must include:
- What This Is (project overview)
- How To Use It (for AI models and humans)
- Repository Structure (directory explanations)
- Tag System (brief overview)
- Canon State (current moment)
- Contributing (how to add content)
- License
- Credits

---

### **PHASE 11: Initial Git Commit** ⏱️ 5 minutes

```bash
# Stage all files
git add .

# Create initial commit
git commit -m "Initial worldengine build - Stray Dogs Universe v5.0

Complete repository structure:
- 70+ character/location/faction files
- Visual registry: 25+ appearance profiles
- Reactive world: NPC memory, faction protocols, consequences
- 500+ tag system with variations
- Complete relationship matrices (65 Dogs)
- Cross-reference intelligence
- AI runtime protocols
- Narrative quality systems
- Automation scripts (Python)

Canon state: February 6, 2026
Features: Visual descriptions, reactive NPCs, consequence tracking
Ready for session play"

# Verify commit
git log --oneline
```

---

### **PHASE 12: Final Quality Check** ⏱️ 10 minutes

Run all validation:

```bash
# Validate tags
python scripts/tag_validator.py

# Generate cross-references
python scripts/cross_ref_builder.py

# Check git status
git status
```

Should show:
- ✓ All tags valid
- ✓ Cross-references generated
- ✓ Working tree clean

---

## **ESTIMATED TOTAL TIME: 4-5 hours**

---

## **SUCCESS CRITERIA**

The repository is ready when:

1. ✅ All named characters (25+) have:
   - Character file in `chars/`
   - Visual profile in `registry/appearance_profiles/`
   - Relationships in `registry/relationship_matrices/`

2. ✅ Tag system is complete:
   - 500+ tags in `meta/tags.md`
   - Variations in `meta/tag_variations.md`
   - All files tagged consistently
   - `tag_validator.py` reports no errors

3. ✅ Reactive world functions:
   - All templates created
   - Faction protocols documented
   - Consequence chains ready

4. ✅ Automation works:
   - Scripts run without errors
   - Cross-references generate
   - Git workflow functional

5. ✅ Narrative quality preserved:
   - Character voices authentic
   - Show-don't-tell maintained
   - Thematic depth captured

---

## **TROUBLESHOOTING**

### **If tag_validator.py reports errors:**
1. Check spelling in files
2. Add missing tags to `meta/tags.md`
3. Add variations to `meta/tag_variations.md`
4. Re-run validator

### **If cross_ref_builder.py fails:**
1. Verify YAML frontmatter format
2. Check tag syntax (`#TagName` not `# TagName`)
3. Ensure bidirectional tagging

### **If character count is low (<25):**
1. Review PDF for all named characters
2. Create missing character files
3. Generate corresponding visual profiles

---

## **FINAL CHECKLIST FOR JULES**

Before delivering to K-9:

- [ ] Repository initialized with Git
- [ ] All directories created
- [ ] 70+ markdown files created and tagged
- [ ] 500+ tags in master tag list
- [ ] 25+ appearance profiles created
- [ ] Relationship matrices complete (65 Dogs)
- [ ] All meta files created (16 files)
- [ ] Three Python scripts added and tested
- [ ] README.md created
- [ ] tag_validator.py passes
- [ ] cross_ref_builder.py generates successfully
- [ ] Initial Git commit completed
- [ ] Working tree is clean

---

## **NOTES FOR JULES**

### **Quality Over Speed**
Take time to preserve narrative voice. Don't make files sterile.

### **Follow Templates**
Use the templates in Document 1 exactly. They're designed for consistency.

### **Cross-Reference Thoroughly**
Bidirectional tagging is CRITICAL. If A tags B, B must tag A.

### **Test Scripts**
Run validation scripts BEFORE final commit. Fix errors as they appear.

### **Ask If Stuck**
If anything is unclear, reference the documents:
- Structure questions → Document 1
- Tag questions → Document 2
- Logic questions → Document 3
- Script questions → Document 4

---

## **DELIVERY FORMAT**

When complete, provide K-9 with:

1. **Compressed repository** (.zip or .tar.gz)
2. **README.md** (usage guide)
3. **Validation report** (script outputs showing success)
4. **Quick start guide** (how to run first session)

---

**JULES, YOU HAVE EVERYTHING YOU NEED. BUILD THE WORLDENGINE. MAKE IT PROPER.** 🐕

---

**START WITH PHASE 1. EXECUTE ALL PHASES IN ORDER. YOU GOT THIS.**
