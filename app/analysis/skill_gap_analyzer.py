import yaml
from app.analysis.skill_extractor import extract_skills

def analyze_skill_gap(t):
    found=extract_skills(t); taxonomy=yaml.safe_load(open('config/skills_taxonomy.yaml'))
    required={s for d in taxonomy.values() for s in d}
    return list(required-found)
