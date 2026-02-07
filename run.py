print("Exodus is alive")

def extract_traits(logs):
    return {
        "verbosity": 0.7,
        "explanation_depth": 0.4
    }

def apply_traits(traits, prompt):
    return f"[Persona applied] {prompt}"
