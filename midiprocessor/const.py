# Author: Botao Yu


# === Abbreviation ===
BAR_ABBR = 'b'
POS_ABBR = 'o'
TS_ABBR = 's'
TEMPO_ABBR = 't'
INST_ABBR = 'i'
PITCH_ABBR = 'p'
DURATION_ABBR = 'd'
VELOCITY_ABBR = 'v'
PITCH_NAME_ABBR = 'n'
PITCH_OCTAVE_ABBR = 'c'
FAMILY_ABBR = 'f'
SPECIAL_ABBR = 'e'

# === Encoding ===
ENCODINGS = ('REMI', 'REMIGEN', 'TS1', 'TG1', 'STACKED')
# REMI: REMI
# TS1: 只编码Bar(no idx)、position、duration、pitch信息
# TG1: Compound format for generation. f, t, o, i, v, d, c, n, b

# === Cut Methods ===
CUT_METHODS = ('successive', 'first')

# === Defaults ===
DEFAULT_TICKS_PER_BEAT = 480
DEFAULT_TS = (4, 4)
DEFAULT_TEMPO = 120.0
DEFAULT_INST_ID = 0
DEFAULT_VELOCITY = 96

KEY_PROFILE = 'key_profile.pickle'
