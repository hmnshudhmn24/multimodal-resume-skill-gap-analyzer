from app.ingestion.resume_parser import parse_resume
from app.analysis.skill_gap_analyzer import analyze_skill_gap
from app.ranking.roadmap_builder import build_roadmap
from app.output.report_generator import generate_report

def run(resume_path):
    text=parse_resume(resume_path)
    gaps=analyze_skill_gap(text)
    roadmap=build_roadmap(gaps)
    generate_report(roadmap)

if __name__=='__main__':
    run('data/raw/sample_resume.pdf')
