class CognitiveFunction:
    """
    Object to store data about Cognitive Function being evaluated.
    Keep in mind, the functions in the Question class modify preference and
    development (and total) values to track scores!
    """
    def __init__(self, name, dominant_types, auxiliary_types, opposite_name):
        self.name = name
        self.dominant_types = dominant_types
        self.auxiliary_types = auxiliary_types
        self.opposite_name = opposite_name
        self.preference = 0
        self.total_pref = 0
        self.development = 0
        self.total_dev = 0

    def __str__(self):
        string = f"{self.name}: Preference score {self.preference}, "
        string += f"Development score: {self.development}"
        return string


def create_functions():
    """Creates an Object for each function"""
    global ni, ne, si, se, ti, te, fi, fe
    ni = CognitiveFunction("Ni", ("INTJ, INFJ"), ("ENTJ", "ENFJ"), "Se")
    ne = CognitiveFunction("Ne", ("ENTP, ENFP"), ("INTP", "INFP"), "Si")
    si = CognitiveFunction("Si", ("ISTJ, ISFJ"), ("ESTJ", "ESFJ"), "Ne")
    se = CognitiveFunction("Se", ("ESTP, ESFP"), ("ISTP", "ISFP"), "Ni")
    ti = CognitiveFunction("Ti", ("INTP, ISTP"), ("ESTP", "ESFP"), "Fe")
    te = CognitiveFunction("Te", ("ENTJ, ESTJ"), ("INTJ", "ISTJ"), "Fi")
    fi = CognitiveFunction("Fi", ("INFP, ISFP"), ("ENFP", "ESFP"), "Te")
    fe = CognitiveFunction("Fe", ("ENFJ, ESFJ"), ("INFJ", "ISFJ"), "Ti")


types = {
    "INTJ": ("Ni", "Te", "Fi", "Se"),
    "INFJ": ("Ni", "Fe", "Ti", "Se"),
    "ENTJ": ("Te", "Ni", "Se", "Fi"),
    "ENFJ": ("Fe", "Ni", "Se", "Ti"),
    "ENTP": ("Ne", "Ti", "Fe", "Si"),
    "ENFP": ("Ne", "Fi", "Te", "Si"),
    "INTP": ("Ti", "Ne", "Si", "Fe"),
    "INFP": ("Fi", "Ne", "Si", "Te"),
    "ISTJ": ("Si", "Te", "Fi", "Ne"),
    "ISFJ": ("Si", "Fe", "Ti", "Ne"),
    "ESTJ": ("Te", "Si", "Ne", "Fi"),
    "ESFJ": ("Fe", "Si", "Ne", "Ti"),
    "ESTP": ("Se", "Ti", "Fe", "Ni"),
    "ESFP": ("Se", "Fi", "Te", "Ni"),
    "ISTP": ("Ti", "Se", "Ni", "Fe"),
    "ISFP": ("Fi", "Se", "Ni", "Te"),
    }

# Runs the creation script so that functions are available to use.
create_functions()
