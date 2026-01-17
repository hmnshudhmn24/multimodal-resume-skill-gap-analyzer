from pathlib import Path

def generate_report(r):
    Path('data/reports').mkdir(parents=True,exist_ok=True)
    with open('data/reports/roadmap.md','w') as f:
        for s in r['learning_roadmap']: f.write(f'- Learn {s}\n')
