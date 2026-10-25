# New TunePad cell
# GAME MUSIC PROTOTYPE - PIANO MELODY TRACK
# This track creates the main melody of the composition.
# It follows the same structure as the drum and bass tracks:
# Intro, Main, Build-up, Climax and Ending.

SECTION_BARS = 8


# Main note patterns used in different sections
intro_notes = [62, 65, 69, 65]
main_notes = [62, 65, 69, 72, 69, 67, 65, 62]
build_up_notes = [62, 65, 67, 69, 72, 74, 72, 69]
climax_notes = [74, 72, 69, 72, 74, 77, 76, 74]


# ---------- INTRO ----------
def intro_melody():
    # The intro uses fewer and longer notes
    # to create a simple atmospheric beginning.
    for note in intro_notes:
        playNote(note, beats=1)


# ---------- MAIN ----------
def main_melody():
    # The main section introduces a more complete melody.
    # Shorter notes create more movement.
    for note in main_notes:
        playNote(note, beats=0.5)


# ---------- BUILD-UP ----------
def build_up_melody():
    # The melody gradually moves upward in pitch
    # to create tension before the climax.
    for note in build_up_notes:
        playNote(note, beats=0.5)


# ---------- CLIMAX ----------
def climax_melody():
    # The climax uses higher notes and stronger velocity
    # to create the most energetic section.
    for note in climax_notes:
        playNote(note, beats=0.5, velocity=105)


# ---------- ENDING ----------
def ending_melody():
    # A descending melody reduces the energy
    # after the climax.
    ending_notes = [69, 67, 65, 62]

    # Repeat the descending phrase three times.
    # 4 notes x 3 repetitions x 1 beat = 12 beats.
    for i in range(3):
        for note in ending_notes:
            playNote(note, beats=1)

    # Hold the final D note for four beats.
    # Ending total = 12 + 4 = 16 beats.
    playNote(62, beats=4)


# ---------- FULL STRUCTURE ----------

# Intro:
# 4 beats per melody x 8 = 32 beats
for i in range(SECTION_BARS):
    intro_melody()

# Main:
# 4 beats per melody x 8 = 32 beats
for i in range(SECTION_BARS):
    main_melody()

# Build-up:
# 4 beats per melody x 8 = 32 beats
for i in range(SECTION_BARS):
    build_up_melody()

# Climax:
# 4 beats per melody x 8 = 32 beats
for i in range(SECTION_BARS):
    climax_melody()

# Ending:
# 16 beats
ending_melody()


