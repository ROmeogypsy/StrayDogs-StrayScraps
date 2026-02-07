# **JULES BUILD INSTRUCTIONS - STRAY DOGS WORLDENGINE v5.0 FINAL**

## **YOUR MISSION**

Transform the `Stray_Dogs_Universe.pdf` into a modular, version-controlled, AI-navigable story repository with:
- Intelligent tagging system (500+ tags)
- Visual registry (character appearances, relationships)
- Reactive world (NPC memory, faction responses, consequences)
- Narrative quality preservation
- Git-tracked canon updates

---

## **REPOSITORY STRUCTURE (COMPLETE)**

```
stray-dogs-worldengine/
├── .git/
├── .gitignore
├── README.md
│
├── world/
│   ├── 00_index.md
│   ├── timeline.md
│   ├── philosophy.md
│   └── economics.md
│
├── locations/
│   ├── 00_location_index.md
│   ├── the_plaza.md
│   ├── north_ends.md
│   ├── the_doghouse_neph.md
│   ├── the_kennel.md
│   ├── the_hydrant.md
│   ├── st_augustines.md
│   ├── west_end_high.md
│   ├── south_ends_seph.md
│   └── timtims_rooftop.md
│
├── factions/
│   ├── 00_faction_index.md
│   ├── stray_dogs.md
│   ├── high_command.md
│   ├── neph_frontline.md
│   ├── seph_ghosts.md
│   ├── sd_media.md
│   ├── academy_prefects.md
│   ├── west_end_gang.md
│   └── silence_protocol.md
│
├── chars/
│   ├── 00_character_index.md
│   ├── high_command/
│   │   ├── stray.md
│   │   ├── big_9.md
│   │   ├── dame.md
│   │   ├── snout.md
│   │   ├── zed_kidd.md
│   │   └── chew_toy.md
│   ├── frontline/
│   │   ├── ruckus.md
│   │   ├── whistle.md
│   │   ├── matches.md
│   │   └── needles.md
│   ├── embedded/
│   │   ├── rax_kidd.md
│   │   └── k9_kian_nines.md
│   ├── academy/
│   │   ├── alistair_delarusso.md
│   │   ├── nala_regan.md
│   │   └── leo_luther.md
│   ├── new_members/
│   │   └── scraps_harper.md
│   └── supporting/
│       ├── prophet.md
│       ├── cipher.md
│       ├── captain_shaw.md
│       ├── ash.md
│       └── ms_okoye.md
│
├── tensions/
│   ├── 00_tension_index.md
│   ├── current_feb_2026.md
│   ├── scraps_integration.md
│   ├── west_end_retaliation.md
│   ├── alistair_awakening.md
│   ├── stray_burnout.md
│   ├── fountain_aftermath.md
│   └── big_9_absence.md
│
├── events/
│   ├── 2020_founding.md
│   ├── 2022_expansion.md
│   ├── 2023_03_catalyst.md
│   ├── 2023_late_breaking.md
│   ├── 2024_reorganization.md
│   └── 2026_02_scraps_claimed.md
│
├── mechanics/
│   ├── red_light_protection.md
│   ├── intelligence_network.md
│   ├── silence_protocol_mechanics.md
│   ├── territory_control.md
│   └── communication_systems.md
│
├── culture/
│   ├── visual_markers.md
│   ├── speech_patterns.md
│   ├── rituals.md
│   ├── music_tracks.md
│   └── core_values.md
│
├── registry/ ← NEW: VISUAL & RELATIONSHIP DATABASE
│   ├── 00_registry_index.md
│   ├── appearance_profiles/
│   │   ├── stray_visual.md
│   │   ├── scraps_visual.md
│   │   ├── big_9_visual.md
│   │   ├── dame_visual.md
│   │   ├── zed_visual.md
│   │   ├── rax_visual.md
│   │   ├── k9_visual.md
│   │   ├── alistair_visual.md
│   │   ├── [all named characters]
│   │   └── visual_comparison_charts.md
│   ├── relationship_matrices/
│   │   ├── dog_internal_relationships.md
│   │   ├── dog_academy_relationships.md
│   │   ├── faction_relationships.md
│   │   └── dynamic_relationship_tracker.md
│   └── physical_details/
│       ├── clothing_catalog.md
│       ├── scars_injuries_catalog.md
│       ├── tattoo_registry.md
│       └── physical_mannerisms.md
│
├── reactive_world/ ← NEW: NPC RESPONSE SYSTEM
│   ├── 00_reactive_index.md
│   ├── npc_awareness/
│   │   ├── community_memory.md
│   │   ├── rumor_system.md
│   │   ├── reputation_tracker.md
│   │   └── witness_records.md
│   ├── faction_responses/
│   │   ├── dog_response_protocols.md
│   │   ├── academy_response_protocols.md
│   │   ├── west_end_response_protocols.md
│   │   └── police_response_protocols.md
│   ├── environmental_state/
│   │   ├── location_conditions.md
│   │   ├── time_based_populations.md
│   │   ├── weather_impacts.md
│   │   └── ongoing_events.md
│   └── consequence_chains/
│       ├── action_consequence_tree.md
│       ├── escalation_triggers.md
│       └── ripple_effect_tracker.md
│
├── meta/ ← CRITICAL: AI NAVIGATION & QUALITY CONTROL
│   ├── tags.md
│   ├── tag_variations.md
│   ├── ai_runtime_protocol.md
│   ├── tag_validation_examples.md
│   ├── session_tag_template.md
│   ├── cross_reference.md
│   ├── priority_contexts.md
│   ├── narrative_quality_checklist.md
│   ├── voice_preservation_guide.md
│   ├── emotional_beats.md
│   ├── scene_transitions.md
│   ├── conflict_escalation.md
│   ├── thematic_callbacks.md
│   ├── reactive_world_protocol.md ← NEW
│   ├── visual_description_guide.md ← NEW
│   └── consequence_engine_rules.md ← NEW
│
├── sessions/
│   └── 000_setup.md
│
└── scripts/
    ├── engine_sync.py
    ├── tag_validator.py
    └── cross_ref_builder.py
```

---

## **STEP-BY-STEP BUILD PROCESS**

### **PHASE 1: INITIALIZATION**

```bash
git init stray-dogs-worldengine
cd stray-dogs-worldengine
```

Create all directories listed above.

Create `.gitignore`:
```
# Temp files
*.tmp
*~
.DS_Store

# Session drafts
sessions/draft_*

# Python cache
__pycache__/
*.pyc
```

---

### **PHASE 2: PDF EXTRACTION & BASIC FILES**

**Parse PDF into markdown files**:

1. **Strip PDF metadata** (page numbers, headers, footers)
2. **Preserve narrative content** (dialogue, descriptions, philosophy)
3. **Create one file per**:
   - Character (named individuals)
   - Location (significant places)
   - Faction (organizations)
   - Event (major historical moments)
   - Tension (active conflicts)

**File template** (EVERY markdown file):
```yaml
---
[Appropriate YAML frontmatter with tags]
last_updated: 2026-02-06
canon_version: Initial
---

# [TITLE]

[Content organized logically]
```

---

### **PHASE 3: VISUAL REGISTRY SYSTEM**

#### **A. Appearance Profiles**

Create `registry/appearance_profiles/[character]_visual.md` for ALL named characters.

**Template structure**:
```markdown
# [CHARACTER NAME] - Complete Visual Profile

**Last Updated**: 2026-02-06
**Canon Status**: [Current state]

---

## CORE PHYSICAL DESCRIPTION

### Build & Stature
- Height: [X'X"]
- Build: [Description]
- Weight: [Approx]
- Posture: [How they carry themselves]

### Face & Head
**Shape & Structure**: [Detailed]
**Eyes**: Color, expression, current state
**Hair**: Color, style, texture, condition
**Skin**: Tone, condition, marks
**Facial Hair**: [If applicable]

### Distinctive Features
[2-5 unique identifiers]

## CLOTHING & APPEARANCE

### Primary Outfit
[What they wear 90% of time]

### Alternate Appearances
[Rare/special clothing]

## PHYSICAL STATE INDICATORS

### Current Markers
[How exhaustion, stress, injury shows]

### Mannerisms
[Physical habits, movements, tells]

## COMPARATIVE HEIGHTS & BUILDS
[Taller/shorter than other characters]

## HOW TO DESCRIBE [CHARACTER] IN SCENES

### First Appearance:
```
[Example description]
```

### Subsequent Mentions:
```
[Shorter description]
```

## TAGS FOR VISUAL QUERIES
[#VisualTag1, #VisualTag2, etc.]

## CANON UPDATE PROTOCOL
[How to track appearance changes]
```

**CRITICAL**: Use existing character information from PDF to fill these out accurately.

**Example characters requiring profiles**:
- Stray (detailed example in Document 2)
- Scraps (detailed example in Document 2)
- Big 9, Dame, Snout, Zed, Chew-toy
- Rax, K-9
- Alistair, Nala, Leo
- Ruckus, Whistle, Matches, Needles
- All other named characters

---

#### **B. Relationship Matrices**

Create `registry/relationship_matrices/dog_internal_relationships.md`:

**Template structure**:
```markdown
# Stray Dogs - Internal Relationship Matrix

**Last Updated**: 2026-02-06
**Total Dogs**: 65

---

## RELATIONSHIP VISUALIZATION SYSTEM

### Intensity Scale:
- ██████ Level 5: Deep bond (would die for them)
- █████░ Level 4: Strong trust
- ████░░ Level 3: Solid respect
- ███░░░ Level 2: Neutral/Professional
- ██░░░░ Level 1: Tense
- █░░░░░ Level 0: Hostile

### Type Icons:
- 🛡️ Protector/Protected
- 🎓 Mentor/Mentee
- 👥 Equals/Peers
- 💔 Former bond broken
- 🔥 Conflict active
- ⏳ Developing/Uncertain

## [CHARACTER A] RELATIONSHIPS

**With [Character B]**:
- **Intensity**: [Level bar]
- **Type**: [Icon + description]
- **Dynamic**: [How they interact]
- **History**: [What shaped this]
- **Current**: [Status as of Feb 6, 2026]

[Repeat for all significant relationships]
```

**Required relationship files**:
1. `dog_internal_relationships.md` - All 65 Dogs interconnected
2. `dog_academy_relationships.md` - Cross-faction dynamics
3. `faction_relationships.md` - Organizational level
4. `dynamic_relationship_tracker.md` - Template for updates

---

#### **C. Physical Details Catalogs**

**1. Clothing Catalog** (`registry/physical_details/clothing_catalog.md`):
```markdown
# Clothing Catalog

## Grey NEPH Jumpsuits
**Standard Issue**:
- Material: Cheap polyester blend
- Color: Industrial grey
- Style: Detention jumpsuit (zip front)
- Fit: Loose, uncomfortable
- Modifications: [Individual customizations]

**Red Markings** (Hand-painted by Dame):
- [Catalog all known markings]

## Academy Uniforms
[Details]

## West End Aesthetic
[Designer streetwear descriptions]

[Continue for all clothing types mentioned in PDF]
```

**2. Scars/Injuries Catalog** (`scars_injuries_catalog.md`):
```markdown
# Scars & Injuries Catalog

## ZED KIDD - The Drag Survivor

**Face**:
- Cheekbone visible through healed tissue
- Jaw misaligned
- One eye reflects light differently

**Back**:
- Entire surface shredded
- Asphalt embedded in muscle
- Burn-like texture

**Acquired**: Late 2023 (dragged 40 mph, 3 blocks)
**Visibility**: Cannot be hidden
**Psychological Impact**: Extreme (PTSD triggers)

[Continue for all documented injuries]
```

**3. Tattoo Registry** (`tattoo_registry.md`):
```markdown
# Tattoo Registry - Every Dog Marking

**MANDATORY**: All Dogs must have at least ONE tattoo from Dame

## STRAY
**Tattoo 1**: Small red paw on chest (left side, over heart)
- Artist: Dame
- Date: [From story timeline]
- Significance: Rare honor - Dame painted SENTINEL on jumpsuit AND gave personal marking
- Visibility: Hidden under clothing
- Size: ~2 inches diameter

[Continue for ALL 65 Dogs - document every tattoo mentioned or implied]

## SCRAPS (Upcoming)
**Current Tattoo**: Blade dagger behind right ear
- Pre-Dog marking (West End gang)
- Blade pointing DOWN = killed for the set
- Acquired: Age 15
- Status: Decision pending (cover/keep/integrate)

**Planned Dog Tattoo**: TBD
- Artist: Dame (confirmed)
- Design: To be determined in story
- Significance: Official acceptance as 65th Dog
```

**4. Physical Mannerisms** (`physical_mannerisms.md`):
```markdown
# Physical Mannerisms Guide

## STRAY

**Signature Movements**:
- Headphone adjustment (every 10-15 min, unconscious)
- Lip-reading scan (tracks multiple conversations)
- Tactical positioning (back to walls, knows exits)

**Stress Indicators**:
- Hand to headphones (protective)
- Jaw clench (tinnitus spike)
- Breathing shallows

**Combat Tells**:
- Weight shifts forward
- Hands loose at sides
- No visible tension (calm mask)

[Continue for all major characters]
```

---

### **PHASE 4: REACTIVE WORLD SYSTEM**

#### **A. NPC Awareness**

**1. Community Memory** (`reactive_world/npc_awareness/community_memory.md`):
```markdown
# Community Memory System

## HOW MEMORY WORKS

### Memory Persistence:
- **PERMANENT**: Lives saved/taken, betrayals, major events
- **LONG-TERM**: Repeated behaviors, significant help
- **SHORT-TERM**: Single interactions, minor conflicts
- **FORGOTTEN**: Generic presence, routine actions

## MEMORY CATEGORIES

### Personal Memory (Individual NPCs)

**Example: Red Light Worker "Maria"**
- ██████ PERMANENT: Stray saved her from violent client (March 2024)
- █████░ LONG-TERM: Always works graveyard (2 years protection)
- ████░░ SHORT-TERM: Nodded at her last Tuesday

**How Maria Treats Stray**:
- Smiles when sees him
- Offers food sometimes
- Trusts completely
- Would lie to police for him

[Template for tracking NPC memories of player actions]

### Collective Memory (Community-Wide)

**North Ends Remembers**:
- Big 9/Dame/Snout founding (2020)
- Crisis moments (March 2023, Late 2023)
- Current reputation ("Dogs protect us")

### Faction Memory (Organizational Knowledge)

**Stray Dogs Remember**:
- Every member's joining story
- Every operation success/failure
- Every betrayal (NONE until Scraps)

[Continue with templates]
```

**2. Rumor System** (`rumor_system.md`):
```markdown
# Rumor System - How Stories Spread

## RUMOR MECHANICS

### Spread Speed by Location:
- Red Light District: FAST (6 hours to full coverage)
- North Ends: MEDIUM (24 hours community-wide)
- Academy: FAST (Instagram - 2 hours student body)
- West End: MEDIUM (12 hours gang network)

### Mutation Rate:
- Factual core: 80% accurate after 3 tellings
- Details: 50% accurate after 3 tellings
- Motivations: 20% accurate (people guess)

### Amplification Factors:
- Violence: 3x spread speed
- Romance: 2x spread speed (see: Rax/K-9 rumors)
- Betrayal: 4x spread speed
- Mystery: 1.5x spread speed

## EXAMPLE RUMOR CHAINS

**Action**: Stray disarms West End leader

**Hour 1**: 3 Red Light workers saw it
**Hour 6**: All 40 workers know, story spreading to North Ends
**Hour 24**: North Ends community knows "Stray protected someone"
**Day 3**: Details fuzzy but "Dogs stood up to West End" confirmed
**Week 1**: Story is legend: "Stray fought 5 West End members alone" (mutated)

[Templates for tracking rumor spread]
```

**3. Reputation Tracker** (`reputation_tracker.md`):
```markdown
# Reputation Tracker

## CURRENT REPUTATIONS (Feb 6, 2026)

### STRAY

**North Ends Community**:
- Rating: ████░ 4/5 (High positive)
- Known For: "Silent protector, graveyard guardian"
- Trust Level: Would hide him from police

**Red Light Workers**:
- Rating: █████ 5/5 (Absolute trust)
- Known For: "Never fails, always there"
- Trust Level: Would die for him

**West End Gang**:
- Rating: █░░░░ 1/5 (Enemy)
- Known For: "Made our leader look weak"
- Threat Level: Target if opportunity

**Academy**:
- Rating: ██░░░ 2/5 (Unknown/Curious)
- Known For: "Homeless kid on Plaza bench"
- Alistair specifically: ███░░ 3/5 (Investigating with respect)

[Template for all major characters across all factions]
```

**4. Witness Records** (`witness_records.md`):
```markdown
# Witness Records - Who Saw What

## TEMPLATE

**Event**: [Description]
**Date/Time**: [When]
**Location**: [Where]

**Witnesses**:
1. **[Name/Role]**
   - Faction: [Affiliation]
   - Distance: [How close]
   - Angle: [What they saw]
   - Reaction: [Immediate response]
   - Will They Talk?: [To who?]
   - Memory Persistence: [How long they'll remember]

**Implications**:
- Who will spread this story?
- Who will stay silent?
- What faction responses triggered?

[Use this template to track all significant witnessed events]
```

---

#### **B. Faction Response Protocols**

Create protocol files for each faction explaining HOW they respond to different triggers.

**Example: `dog_response_protocols.md`**:
```markdown
# Stray Dogs Response Protocols

## THREAT ASSESSMENT LEVELS

### LEVEL 1: Minor (Single incident, isolated)
**Example**: Drunk client at Red Light

**Response**:
- Assigned Dog handles solo
- No escalation to high command
- Logged with Chew-toy

**Timeline**: Immediate (on-shift Dog responds)

---

### LEVEL 2: Moderate (Repeat issue, small group)
**Example**: Same client returns multiple times

**Response**:
- Chew-toy coordinates 2-3 Dogs
- Warning issued to threat
- Logged with high command (aware, not acting)

**Timeline**: Within 24 hours

---

### LEVEL 3: Serious (Organized threat, weapons)
**Example**: West End scouts Red Light

**Response**:
- Chew-toy mobilizes 5-10 Dogs
- High command notified (Dame/Zed/Snout decide strategy)
- SEPH Ghosts activated (intelligence gathering)
- Community informed (shop owners watch)

**Timeline**: Within hours

---

### LEVEL 4: Critical (Direct attack, Dog endangered)
**Example**: West End attacks Red Light with numbers

**Response**:
- ALL 65 Dogs mobilize
- High command leads personally
- Community supports (Silence Protocol + eyes)
- Lethal force authorized

**Timeline**: Immediate (within minutes)

---

### LEVEL 5: Existential (War, community endangered)
**Example**: Full gang war, North Ends at risk

**Response**:
- Total mobilization
- Community integration (residents fight WITH Dogs)
- All protocols suspended (survival mode)
- Scorched earth tactics

**Timeline**: Instant

---

## VIOLATION RESPONSES

### Internal Violations (Dog breaks rules):

**Minor** (Late to shift, forgot responsibility):
- Chew-toy handles (extra shift, warning)

**Moderate** (Negligence, endangers operation):
- High command review
- Suspension from operations (temporary)
- Must earn back trust

**Severe** (Betrayal, cooperates with police):
- Death (only acceptable violence between Dogs)
- No exceptions, no mercy

---

## RECRUITMENT PROTOCOLS

**Standard**:
1. Observation period (weeks to months)
2. Sponsor (existing Dog vouches)
3. High command approval (unanimous)
4. Dame tattoos (official marking)

**Exception - Enemy to Ally** (Scraps case):
1. High-value individual claimed by senior Dog
2. Conditional acceptance (prove through action)
3. Testing period (months)
4. If proven: Standard process
5. If fails: Death

[Continue with all protocol scenarios]
```

Create similar files for:
- `academy_response_protocols.md`
- `west_end_response_protocols.md`
- `police_response_protocols.md`

---

#### **C. Environmental State**

**1. Location Conditions** (`location_conditions.md`):
```markdown
# Location Conditions Tracker

## THE PLAZA

**Current State** (Feb 6, 2026):
- Fountain: Clean (city maintains)
- Benches: 20+ present, Stray's bench (SE corner) has carved initials
- Coffee Shop: Open 24/7, neutral territory respected
- Pavement: Minor cracks, winter wear
- Lighting: Functional (replaced monthly by city)

**Damage Tracking**:
- None currently
- If damaged: Repairs take 1-2 weeks (city bureaucracy)

**Environmental Factors**:
- February: Cold, often wet, short days
- Foot traffic: High during school hours, moderate evenings, low overnight

---

## THE HYDRANT (Red Light District)

**Current State**:
- Streets: Dogs maintain lights (burnt bulbs replaced within 24 hours)
- Safehouses: 3 buildings, clean, heated
- "Three Doors Down": Marked by workers (Ash's memorial - flowers sometimes)

**Damage Tracking**:
- Week 2 aftermath: Shredded coat pieces collected by workers (given to Stray)
- Blood cleaned immediately (workers maintain area)

[Continue for all locations]

## DAMAGE PERSISTENCE RULES

- Blood: Cleaned within hours (community/workers)
- Structural damage: Weeks to months (depends on resources)
- Graffiti: Varies (Dogs clean anti-Dog graffiti fast, art stays)
- Bodies: Removed immediately (Dogs or police, depending on location)
```

**2. Time-Based Populations** (`time_based_populations.md`):
```markdown
# Time-Based Populations - Who's Where When

## THE PLAZA

### 6:00-9:00 AM
- Alistair (6:34 AM patrol - CLOCKWORK)
- Academy students arriving
- Morning commuters (coffee shop)
- Stray occasionally (if just off graveyard shift)

### 12:00-2:00 PM
- HIGHEST TRAFFIC
- All four schools present
- Lunch rush at coffee shop
- Most confrontations happen here (too many people in neutral space)

### 4:00-7:00 PM
- After-school congregation
- Skateboarding
- Dealer activity (discrete)
- Dogs visible (not claiming, just present)

### 10:00 PM-6:00 AM
- Nearly empty
- Night workers passing through
- Stray's bench (sleeps here between shifts)
- Occasional homeless population
- Quietest time

---

## THE HYDRANT (Red Light District)

### 6:00 AM-2:00 PM (Morning Shift)
- 3 Dogs on duty
- Low client traffic
- Workers sleeping (night shift recovery)
- Cleanup, maintenance

### 2:00 PM-10:00 PM (Afternoon Shift)
- 3 Dogs on duty
- Moderate client traffic
- Workers arriving for night shift
- Pre-evening rush

### 2:00 AM-6:00 AM (Graveyard Shift)
- Stray (alone) + Whistle/Needles (floating nearby)
- HIGHEST DANGER
- Drunk clients (weekend)
- Police activity (weekday)
- 40 workers active

[Continue for all locations]
```

**3. Weather Impacts** (`weather_impacts.md`):
```markdown
# Weather Impacts on Scenes

## FEBRUARY 2026 (Current)

**Temperature**: 3-8°C (cold)
**Precipitation**: Frequent drizzle, occasional rain
**Daylight**: Sunrise ~7:15 AM, Sunset ~5:00 PM
**Sky**: Grey, overcast most days

## SCENE IMPACTS

### Visibility:
- Rain/fog: Reduces visibility to 20-30 meters
- Dark winter evenings: Full dark by 6:00 PM
- Street lights critical (Dogs maintain at Red Light)

### Movement:
- Wet pavement: Slower foot chases
- Cold: People move faster (don't linger)
- Rain: Fewer witnesses (people stay inside)

### Physical State:
- Cold affects: Hands less dexterous, shivering, breath visible
- Wet clothes: Heavier, uncomfortable, take hours to dry
- Wind chill: Makes temperatures feel 5°C colder

### Combat:
- Wet ground: Easier to slip in fights
- Cold hands: Harder to grip weapons
- Rain: Vision impaired, noise dampened

## SEASONAL PROGRESSION

**Spring** (March-May): Warming, more daylight, increased outdoor activity
**Summer** (June-August): Hot, long days, high plaza traffic
**Autumn** (September-November): Cooling, rain increases
**Winter** (December-February): Cold, dark, low activity

[Templates for how weather affects each location]
```

---

#### **D. Consequence Chains**

**1. Action Consequence Tree** (`action_consequence_tree.md`):

Use the detailed template provided in Document 2 showing:
- Player action → Immediate witnesses → Reactions → Short-term spread → Medium-term ripples → Long-term consequences

Include 5-10 **pre-built consequence chains** for common actions:
- Dog kills enemy
- Dog saves civilian
- Dog fails protection
- Academy student discovers Dog identity
- West End attacks
- Police investigation starts
- Community betrays Dogs
- Internal Dog conflict
- Faction alliance forms
- Territory changes hands

**2. Escalation Triggers** (`escalation_triggers.md`):
```markdown
# Escalation Triggers - When Situations Worsen

## WEST END RETALIATION (Example)

### Current Level: 2 (Intimidation)

**Triggers to Level 3** (Probing Attack):
- Dogs kill West End member
- Scraps seen publicly with Dogs
- West End scouts confirm Dog protection patterns
- Enough time passes (1-2 weeks) without Dog response

**Triggers to Level 4** (Coordinated Pressure):
- Dogs injure multiple West End members
- West End loses territory/income
- Leadership demands action (saving face)

**Triggers to Level 5** (Direct Confrontation):
- West End member killed on their territory
- Public humiliation of leadership
- Economic damage reaches critical level

**Triggers to Level 6** (War):
- Dogs attack West End headquarters
- West End kills a Dog
- Community endangered by either side
- No diplomatic solution possible

---

## DE-ESCALATION OPPORTUNITIES

### Level 4 → Level 3:
- Negotiation (rare, requires neutral party)
- Tribute paid (money, territory concession)
- Mutual stand-down (both sides agree)

### Level 3 → Level 2:
- Time passes without incident (weeks)
- Bigger threat emerges (common enemy)
- Leadership change (new boss less aggressive)

[Templates for all major conflict types]
```

**3. Ripple Effect Tracker** (`ripple_effect_tracker.md`):
```markdown
# Ripple Effect Tracker

## TEMPLATE

**Primary Action**: [What happened]
**Immediate Circle** (Directly affected):
- [Person/Faction 1]: [Impact]
- [Person/Faction 2]: [Impact]

**Secondary Circle** (Indirectly affected):
- [Person/Faction 3]: [How they hear about it, how it affects them]

**Tertiary Circle** (Distant ripples):
- [Person/Faction 4]: [Eventual impact]

**Timeline**: [When each circle feels the effect]

---

## EXAMPLE: Big 9's Arrest (Late 2023)

**Primary Action**: Big 9 arrested, Whole Life Order

**Immediate Circle**:
- K-9: Massive guilt, drives all his actions now
- Dame: Broke down crying, Stray held her
- Dogs: Could have collapsed, instead galvanized

**Secondary Circle**:
- North Ends Community: Mourned, but respected sacrifice
- West End: Saw opportunity (power vacuum), tested boundaries
- Zed: Dragged by rivals one week later (direct consequence)

**Tertiary Circle**:
- Academy: K-9 transferred there (Dame's deal for "reformed student")
- SD Media: K-9 took over public face (necessary leadership)
- Stray: Lost verbal mentor, silence deepened

**Timeline**:
- Week 1: Immediate circle devastated
- Month 1: Secondary circle adjusting
- Year 1: Tertiary ripples still emerging

[Use this to map future player actions]
```

---

### **PHASE 5: META FILES (AI NAVIGATION)**

These files were detailed in Document 2. Create all of them:

1. `tags.md` - Master tag index (500+ tags)
2. `tag_variations.md` - Acceptable variations
3. `ai_runtime_protocol.md` - How AI uses repository
4. `tag_validation_examples.md` - Correct/incorrect tagging
5. `session_tag_template.md` - End-of-response format
6. `cross_reference.md` - Bidirectional relationships
7. `priority_contexts.md` - What to load when
8. `narrative_quality_checklist.md` - Writing standards
9. `voice_preservation_guide.md` - Character speech patterns
10. `emotional_beats.md` - Arc tracking
11. `scene_transitions.md` - Flow techniques
12. `conflict_escalation.md` - Tension ladder
13. `thematic_callbacks.md` - Recurring symbols
14. **`reactive_world_protocol.md`** - NEW: How to use reactive systems
15. **`visual_description_guide.md`** - NEW: How to describe characters
16. **`consequence_engine_rules.md`** - NEW: Cause-effect principles

---

### **PHASE 6: TAG APPLICATION**

**For EVERY file created, add YAML frontmatter**:

```yaml
---
[File-specific metadata]

tags:
  [category]: [#Tag1, #Tag2, #Tag3]

last_updated: 2026-02-06
canon_version: Initial
---
```

**Tag categories by file type**:
- **Characters**: character, locations, relationships, themes, mechanics, visual
- **Locations**: location, characters, factions, themes, events
- **Factions**: faction, members, locations, operations, philosophy
- **Tensions**: tension, characters, factions, deadline, stakes
- **Events**: event, date, characters, locations, consequences
- **Visual profiles**: character, physical, clothing, mannerisms
- **Relationship files**: characters, intensity, type, dynamic

**Cross-reference bidirectionally**:
- If Stray.md tags #Plaza, then Plaza.md must tag #Stray
- If Scraps tags #BladeTattoo, then tattoo_registry.md must reference Scraps
- If community_memory.md mentions Maria, create Maria NPC profile

---

### **PHASE 7: AUTOMATION SCRIPTS**

**1. engine_sync.py** - Session canon updater
**2. tag_validator.py** - Ensures tags are valid
**3. cross_ref_builder.py** - Auto-generates cross-references

(Scripts provided in Document 2 - copy them)

---

### **PHASE 8: VALIDATION**

**Before finalizing repository**:

✅ **Completeness Check**:
- [ ] All named characters (25+) have character files
- [ ] All named characters have visual profiles
- [ ] All significant locations (10+) have files
- [ ] All major events (6+) documented
- [ ] All active tensions (7+) tracked
- [ ] 65-member Dog relationship matrix complete

✅ **Tag System Check**:
- [ ] tags.md has 500+ tags
- [ ] tag_variations.md covers all major entities
- [ ] All files have YAML frontmatter
- [ ] Cross-references are bidirectional
- [ ] No orphaned tags (all tags used exist in master list)

✅ **Visual Registry Check**:
- [ ] Appearance profiles for all named characters (25+)
- [ ] Visual comparison charts created
- [ ] Clothing catalog complete (50+ descriptions)
- [ ] Scars/injuries documented
- [ ] Tattoo registry has all 65 Dogs

✅ **Reactive World Check**:
- [ ] Community memory templates ready
- [ ] Rumor system mechanics documented
- [ ] Reputation tracker for major characters complete
- [ ] Faction response protocols for all 4 factions
- [ ] Consequence chain templates ready

✅ **Narrative Quality Check**:
- [ ] Character voices preserved in files
- [ ] Dialogue examples show authentic speech
- [ ] Show-don't-tell maintained
- [ ] Thematic depth captured

✅ **AI Usability Check**:
- [ ] Runtime protocol is clear
- [ ] Tag validation examples comprehensive
- [ ] Priority contexts guide efficient loading
- [ ] Session template complete

✅ **Automation Check**:
- [ ] engine_sync.py can parse session files
- [ ] tag_validator.py catches invalid tags
- [ ] Scripts documented with usage instructions

---

### **PHASE 9: INITIAL GIT COMMIT**

```bash
git add .
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
- Automation scripts

Canon state: February 6, 2026
Features: Visual descriptions, reactive NPCs, consequence tracking
Ready for session play"
```

---

### **PHASE 10: CREATE README.md**

```markdown
# Stray Dogs Worldengine v5.0

A living, reactive story universe with Git-tracked canon, intelligent tagging, visual character registry, and NPC memory systems.

## What This Is

The Stray Dogs Worldengine is a comprehensive narrative database for running AI-driven story sessions in the Stray Dogs universe. It combines:
- Detailed character information (personality, appearance, relationships)
- Location data (physical details, populations, conditions)
- Faction dynamics (philosophies, protocols, conflicts)
- Reactive NPCs (memory, rumors, reputation)
- Consequence tracking (actions have ripple effects)
- Git version control (every canon change tracked)

## How To Use It

### For AI Models (Gemini, Claude, GPT, etc.):

1. **Load initial context**:
   - `meta/tags.md` (know available tags)
   - `tensions/current_feb_2026.md` (world state)
   - `chars/stray.md` (protagonist)

2. **Query-based loading**:
   - Use tags to load ONLY relevant files
   - Example: `#Stray + #GraveyardShift` → Load specific context

3. **Visual descriptions**:
   - Check `registry/appearance_profiles/[character]_visual.md`
   - Use 2-3 distinctive details per mention

4. **NPC responses**:
   - Check `reactive_world/npc_awareness/` for memory
   - Apply `faction_responses/` protocols
   - Map consequences via `consequence_chains/`

5. **End of session**:
   - Include TAG REPORT (template in `meta/session_tag_template.md`)
   - Document canon changes
   - engine_sync.py updates files automatically

### For Writers/Players:

- Browse `chars/` for character info
- Check `tensions/` for current conflicts
- Review `events/` for history
- Read `culture/` for world flavor
- Use `registry/relationship_matrices/` to understand dynamics

## Repository Structure

- `world/` - Global metadata, timeline, economics
- `locations/` - Physical places (Plaza, Kennel, etc.)
- `factions/` - Organizations (Dogs, Academy, West End)
- `chars/` - Character files (organized by role)
- `tensions/` - Active conflicts (current story threads)
- `events/` - Historical moments (chronological)
- `mechanics/` - Systems (protection, intelligence, etc.)
- `culture/` - Identity markers (visual, speech, values)
- `registry/` - Visual database (appearance, relationships)
- `reactive_world/` - NPC response system (memory, protocols)
- `meta/` - AI navigation (tags, protocols, quality control)
- `sessions/` - Gameplay logs (auto-updated)
- `scripts/` - Automation tools

## Tag System

500+ tags organized by:
- **Entities**: Characters, locations, factions
- **Themes**: Core Pillars (Grey/Red/Navy/Silence), concepts
- **Mechanics**: Skills, operations, systems
- **Time**: Periods, shifts, events
- **Relationships**: Bonds, conflicts, dynamics
- **Visual**: Physical descriptions, clothing, mannerisms
- **Reactive**: Consequences, reputation, memory

See `meta/tags.md` for complete list.

## Canon State

**Current Moment**: February 6, 2026 (Friday)
**Season**: Winter (cold, short days)
**Active Tensions**: 7 major conflicts
**Total Dogs**: 65 (including Scraps conditionally)
**Big 9 Status**: Imprisoned (Whole Life Order)

## Contributing

To add new content:
1. Create file in appropriate directory
2. Follow template structure
3. Apply tags from `meta/tags.md`
4. Update cross-references
5. Run `tag_validator.py`
6. Commit with descriptive message

## License

[Your chosen license - e.g., Creative Commons BY-NC-SA 4.0]

## Credits

**Universe Creator**: K-9  
**Worldengine Architect**: Jules (with Claude assistance)  
**Canon State**: February 6, 2026

---

**BLESS UP. 🐕**
```

---

## **SUCCESS CRITERIA**

The repository is ready when:

1. ✅ All named characters (25+) have:
   - Character file in `chars/`
   - Visual profile in `registry/appearance_profiles/`
   - Relationships documented in `registry/relationship_matrices/`

2. ✅ Tag system is complete:
   - 500+ tags in `meta/tags.md`
   - Variations mapped in `meta/tag_variations.md`
   - All files tagged consistently
   - No orphaned tags

3. ✅ Reactive world functions:
   - NPC memory templates ready
   - Faction response protocols complete
   - Consequence chains documented
   - Environmental state tracked

4. ✅ AI can navigate efficiently:
   - Query `#Stray + #GraveyardShift` loads ONLY relevant files
   - Visual descriptions pull from appearance profiles
   - Relationships understood via matrices
   - Consequences mapped via chains

5. ✅ Narrative quality preserved:
   - Character voices authentic in files
   - Show-don't-tell maintained
   - Dialogue examples demonstrate speech patterns
   - Thematic depth captured

6. ✅ Automation works:
   - Scripts run without errors
   - Session updates modify files correctly
   - Git commits track changes

---

## **DELIVERABLES TO K-9**

When complete, deliver:

1. **Full repository** (folder structure with all files)
2. **README.md** (usage guide above)
3. **Sample query demonstration** (show AI using it)
4. **Validation report** (confirm all checks passed)
5. **Git history** (initial commit establishing canon)
6. **Quick start guide** (how to run first session)

---

**JULES, YOU ARE BUILDING THE WORLDENGINE. THIS IS THE FOUNDATION OF LIVING, REACTIVE STORYTELLING. MAKE IT PROPER.** 🐕

---

**END OF DOCUMENT 1**
