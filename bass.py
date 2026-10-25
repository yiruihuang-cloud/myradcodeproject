# New TunePad cell
# GAME MUSIC PROTOTYPE - BASS TRACK
# This track supports the drum and piano melody.
# It adds low-frequency energy and follows the same
# Intro, Main, Build-up, Climax and Ending structure.

SECTION_BARS = 8

# Root notes for the bass progression:
# D -> Bb -> F -> C
bass_roots = [38, 34, 41, 36]


# ---------- INTRO ----------
def intro_bass():
    # The intro uses longer bass notes
    # to create a simple and spacious beginning.
    for root in bass_roots:
        playNote(root, beats=1)


# ---------- MAIN ----------
def main_bass():
    # The main section uses the same bass progression
    # but with shorter notes to create more movement.
    for root in bass_roots:
        playNote(root, beats=0.5)
        playNote(root, beats=0.5)


# ---------- BUILD-UP ----------
def build_up_bass():
    # The build-up repeats each bass note more frequently
    # to increase rhythmic energy.
    for root in bass_roots:
        for i in range(4):
            playNote(root, beats=0.25)


# ---------- CLIMAX ----------
def climax_bass():
    # The climax uses a more active bass pattern.
    # Higher octave notes are mixed with the root notes
    # to make the section feel stronger.
    for root in bass_roots:

        pattern = [
            root,
            root,
            root + 12,
            root
        ]

        for note in pattern:
            playNote(note, beats=0.25)


# ---------- ENDING ----------
def ending_bass():
    # The ending returns to longer notes
    # to reduce the energy before the final note.
    for i in range(3):
        for root in bass_roots:
            playNote(root, beats=1)

    # Final D bass note held for four beats.
    playNote(38, beats=4)


# ---------- FULL STRUCTURE ----------

# Intro
for i in range(SECTION_BARS):
    intro_bass()

# Main
for i in range(SECTION_BARS):
    main_bass()

# Build-up
for i in range(SECTION_BARS):
    build_up_bass()

# Climax
for i in range(SECTION_BARS):
    climax_bass()

# Ending
ending_bass()


