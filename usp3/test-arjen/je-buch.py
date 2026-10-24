import os, sys
sys.path.insert(0, '/home/claude/bookclub/usp3/test-arjen'); sys.path.insert(0, '/home/claude/bookclub/usp3')
os.environ['MODUS'] = 'text+schaetzung'
import json, lauf
from empfehlung import Profile, recommend, embedding_similarity_fn
cat, judg = lauf.load(); lauf.merge_estimates(cat)
texts = {k: v.get('text') for k, v in json.load(open(os.path.join(lauf.KAT, 'klappentexte.json'))).items()}
ts = embedding_similarity_fn(texts)
for j in judg:
    p = Profile(cat, judg); 
    res = recommend(cat, Profile(cat, [j]), 'nachbar', k=8, text_sim=ts)
    own = {x['work_id'] for x in judg}; res = [r for r in res if r['work_id'] not in own][:3]
    print('##', cat[j['work_id']]['title'], '| Merkmale:', {k:v for k,v in cat[j['work_id']]['features'].items() if k!='autor'})
    for r in res:
        print('   ', f"{r['score']:.2f}", cat[r['work_id']]['title'], '–', cat[r['work_id']]['autor_anzeige'], '|', '; '.join(f"{d}: {', '.join(v)}" for d, v in r['reasons']))
