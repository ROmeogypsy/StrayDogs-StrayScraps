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

Creative Commons BY-NC-SA 4.0

## Credits

**Universe Creator**: K-9
**Worldengine Architect**: Jules
**Canon State**: February 6, 2026

---

**BLESS UP. 🐕**
