# persona.py
"""
Persona loader for Jung/MBTI personality profiles.
Loads personality data from a YAML file to influence chatbot behavior.
"""

import yaml

class Persona:
    def __init__(self, yaml_path: str):
        """
        Load the personality profile from a YAML file.
        :param yaml_path: path to the YAML file containing personality data.
        """
        with open(yaml_path, 'r') as f:
            self.profile = yaml.safe_load(f)
    
    def summary(self) -> str:
        """
        Return a brief summary of the personality (MBTI type and key traits).
        """
        mbti_type = self.profile.get('mbti', 'Unknown')
        traits = self.profile.get('traits', [])
        traits_str = ", ".join(traits) if traits else ""
        summary = f"Personality Type: {mbti_type}."
        if traits_str:
            summary += f" Key traits: {traits_str}."
        return summary

# Example usage:
# persona = Persona("jung_test.yaml")
# print(persona.summary())  # e.g., "Personality Type: INTJ. Key traits: Analytical, Reserved, Strategic."
