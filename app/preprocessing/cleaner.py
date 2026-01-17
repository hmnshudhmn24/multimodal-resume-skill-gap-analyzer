import re
def clean(t): return re.sub(r'[^a-zA-Z ]',' ',t)
