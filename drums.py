 # New TunePad cell
# GAME MUSIC PROTOTYPE - DRUM TRACK
# This track creates the rhythmic structure for the composition.
# It is divided into Intro, Main, Build-up, Climax and Ending sections.

# Number of bars used for each main section
SECTION_BARS = 8


# ---------- INTRO ----------
def intro_bar():
    # Simple drum pattern used to introduce the rhythm gradually.
    # Kick drum and hi-hat start together.
    playNote([0, 4], beats=0.5)

    # Hi-hat continues on its own.
    playNote(4, beats=0.5)
    playNote(4, beats=0.5)

    # Snare and hi-hat play together to create a backbeat.
    playNote([2, 4], beats=0.5)

    # The same four-beat pattern is repeated to complete the bar.
    playNote([0, 4], beats=0.5)
    playNote(4, beats=0.5)
    playNote(4, beats=0.5)
    playNote([2, 4], beats=0.5)


# ---------- MAIN ----------
def main_bar():
    # The main section uses a stronger kick pattern
    # to make the rhythm feel more energetic than the intro.

    playNote([0, 4], beats=0.5)
    playNote(4, beats=0.5)

    # An extra kick is added here to strengthen the groove.
    playNote([0, 4], beats=0.5)

    # Snare and hi-hat create the main backbeat.
    playNote([2, 4], beats=0.5)

    # Repeat the same pattern for the second half of the bar.
    playNote([0, 4], beats=0.5)
    playNote(4, beats=0.5)
    playNote([0, 4], beats=0.5)
    playNote([2, 4], beats=0.5)


# ---------- BUILD-UP ----------
def build_up_bar():
    # The build-up divides the bar into 16 shorter rhythmic steps.
    # Shorter beat values make the rhythm feel faster and more intense.
    for step in range(16):

        # Start every step with a hi-hat.
        notes = [4]

        # Add kick drums at the beginning and middle of the pattern.
        if step == 0 or step == 8:
            notes.append(0)

        # Add snare drums at selected strong beats.
        if step == 4 or step == 12:
            notes.append(2)

        # Each step lasts 0.25 beats, creating a denser rhythm.
        playNote(notes, beats=0.25)


# ---------- CLIMAX ----------
def climax_bar(first_bar=False):
    # The climax uses a denser and more active drum pattern.
    # The parameter "first_bar" is used to add a crash cymbal
    # only at the beginning of the climax section.

    for step in range(16):

        # Hi-hat plays continuously to maintain energy.
        notes = [4]

        # More kick positions are added to create a stronger groove.
        if step in [0, 6, 8, 14]:
            notes.append(0)

        # Snare keeps the backbeat in the climax.
        if step in [4, 12]:
            notes.append(2)

        # Add a crash cymbal only on the first step
        # of the first climax bar.
        if first_bar and step == 0:
            notes.append(9)

        # Short note duration keeps the climax fast and energetic.
        playNote(notes, beats=0.25)


# ---------- ENDING ----------
def ending():
    # Reuse the intro rhythm to reduce the intensity
    # and create a clearer ending section.
    for i in range(3):
        intro_bar()

    # Final sequence uses kick, hi-hat, snare and crash
    # to clearly finish the composition.
    playNote([0, 9], beats=1)
    playNote(4, beats=1)
    playNote(2, beats=1)
    playNote(9, beats=1)


# ---------- FULL STRUCTURE ----------
# The functions below are arranged in sequence
# to create the complete drum composition.

# Intro section
for i in range(SECTION_BARS):
    intro_bar()

# Main section
for i in range(SECTION_BARS):
    main_bar()

# Build-up section
for i in range(SECTION_BARS):
    build_up_bar()

# Climax section
# "first_bar" is True only for the first repetition,
# so the crash cymbal is not repeated every bar.
for i in range(SECTION_BARS):
    climax_bar(first_bar=(i == 0))

# Ending section
ending()


