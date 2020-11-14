class CognitiveFunction:
    """
    Object to store data about Cognitive Function being evaluated
    """
    def __init__(self, name, dominant_types, auxiliary_types, opposite_name):
        self.name = name
        self.dominant_types = dominant_types
        self.auxiliary_types = auxiliary_types
        self.opposite_name = opposite_name
        self.preference = 0
        self.skill = 0


def create_functions():
    # create each function with name, dominant types, aux types, opposite function name (in pairs 
    # with the opposite function set as a variable?)
    ni = CognitiveFunction("Ni", ("INTJ, INFJ"), ("ENTJ", "ENFJ"), "Se")