from manager import apply_sound_changes

# These allow global substitutions to input and output.
# Most importantly, this lets you use digraphs in categories, as either variables or as defined values
rewrite_rules = {
    "lh": "lj"
}

# Variables can only be one character long, (unless defined with rewrite rules).
categories = {
    "V": "aeiou",
    "L": "āēīōū",
    "C": "ptcqbdgmnlrhs",
    "F": "ie",
    "B": "ou",
    "S": "ptc",
    "Z": "bdg"
}

#
word_list = [
    "lector",
    "doctor",
    "focus",
    "jocus",
    "districtus",
    "cīvitatem",
    "adoptare",
    "opera",
    "secundus",
    "fīliam",
    "pōntem",

]

# A sound change looks like: target->replacement/environment.
# The environment must contain an underline _, representing the part that changes.
# Rules apply in the order they are written.
sound_changes = [
    "[sm]->/_#",
    "i->j/_V",
    "L->V/_",
    "e->/Vr_#",
    "v->/V_V",
    "u->o/_#",
    "gn->nh/_",
    "S->Z/V_V",
    "c->i/F_t",
    "c->u/B_t",
    "p->/V_t",
    "ii->i/_",
    "e->/C_rV",
]

result = apply_sound_changes(word_list,
                             sound_changes,
                             categories,
                             rewrite_rules,
                             show_input=True,
                             rewrite_on_output=True,
                             report_rules=False,
                             )
for word in result:
    print(word)
