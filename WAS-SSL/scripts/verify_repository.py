#!/usr/bin/env python3
"""Validate the shipped 35 notebook files, code/text SHA256, and summary tables."""
import csv,hashlib,json,sys,re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'metadata/notebook_manifest.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(x):return ''.join(x) if isinstance(x,list) else x
fail=[]
for item in manifest['notebooks']:
 p=root/item['path']
 if not p.is_file():fail.append(f"missing {item['path']}");continue
 if sha(p.read_bytes())!=item['published_sha256']:fail.append(f"file hash mismatch {p}")
 try:n=json.loads(p.read_text())
 except Exception as e:fail.append(f"invalid JSON {p}: {e}");continue
 src=[{'cell_type':c.get('cell_type'),'source':norm(c.get('source',[]))} for c in n['cells']]
 srcsha=sha(json.dumps(src,sort_keys=True,ensure_ascii=False).encode())
 if srcsha!=item['cell_source_sha256']:fail.append(f"changed cell source {p}")
 for c in n['cells']:
  for o in c.get('outputs',[]):
   for k in o.get('data',{}):
    if k.startswith('image/') or k=='text/html' or 'widget-view' in k:fail.append(f"embedded media {p}: {k}")
for table in ('results/g05_full_isic_bacc.csv','results/g05_ham_bcn_source_bacc.csv'):
 with (root/table).open() as f:
  rows=list(csv.DictReader(f))
  if not rows:fail.append('empty results CSV '+table)
if len(manifest['notebooks'])!=35:fail.append('expected 35 notebooks')
fig_manifest=json.loads((root/'metadata/figure_manifest.json').read_text())
if len(fig_manifest['figures'])!=12:fail.append('expected 12 supplied PDF figures')
for item in fig_manifest['figures']:
 for key,hashkey in [('source_pdf','pdf_sha256'),('github_png','png_sha256')]:
  p=root/item[key]
  if not p.is_file():fail.append(f'missing figure {p}');continue
  if sha(p.read_bytes())!=item[hashkey]:fail.append(f'changed figure {p}')
for f in (root/'README.md',root/'docs/FIGURE_GALLERY.md'):
 content=f.read_text()
 for p in re.findall(r'(?:src="|\]\()(assets/figures/[A-Za-z0-9_./-]+\.(?:png|pdf))',content):
  if not (root/p).is_file():fail.append(f'broken figure link: {f}: {p}')
if fail:
 print('FAILED:');print('\n'.join(' - '+x for x in fail));sys.exit(1)
print(f"PASSED: {len(manifest['notebooks'])} valid notebook sources, published SHA256, media check, two G05 tables, 12 source PDF figures and PNGs")
