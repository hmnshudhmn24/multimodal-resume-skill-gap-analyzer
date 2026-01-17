from app.ranking.gap_ranker import rank_gaps

def build_roadmap(gaps): return {'learning_roadmap': rank_gaps(gaps)}
