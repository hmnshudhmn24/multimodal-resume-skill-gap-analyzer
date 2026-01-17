import yaml
def extract_skills(t):
    skills=set(); taxonomy=yaml.safe_load(open('config/skills_taxonomy.yaml'))
    for d in taxonomy.values():
        for s in d:
            if s in t: skills.add(s)
    return skills
