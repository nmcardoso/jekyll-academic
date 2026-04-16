#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "python-frontmatter>=1.1.0",
#   "requests>=2.33.1",
#   "PyYAML>=6.0",
# ]
# ///

import argparse
import copy
import glob
import itertools
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

import frontmatter
import requests
import yaml


def discover_root(start: Path | None = None) -> Path:
  current = (start or Path.cwd()).resolve()

  for candidate in (current, *current.parents):
    if (candidate / '_data').exists() and (candidate / 'content').exists():
      return candidate

  return current


ROOT = discover_root()
DATA_PATH = ROOT / '_data'
COLLECTIONS_PATH = ROOT / 'content'
LATTES_JCR_PATH = DATA_PATH / 'lattes_jcr.yml'
LATTES_CITATION_PATH = DATA_PATH / 'lattes_citation.yml'
OPENALEX_CITATION_PATH = DATA_PATH / 'openalex_citation.yml'

LATTES_JCR_API = 'https://buscatextual.cnpq.br/buscatextual/visualizacao.do'
LATTES_CITATION_API = 'https://buscatextual.cnpq.br/buscatextual/servletcitacoes'
OPENALEX_WORKS_API = 'https://api.openalex.org/works/'

HEADERS = {
  'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}


def configure_paths(root: Path):
  global ROOT, DATA_PATH, COLLECTIONS_PATH, LATTES_JCR_PATH, LATTES_CITATION_PATH, OPENALEX_CITATION_PATH

  ROOT = root.resolve()
  DATA_PATH = ROOT / '_data'
  COLLECTIONS_PATH = ROOT / 'content'
  LATTES_JCR_PATH = DATA_PATH / 'lattes_jcr.yml'
  LATTES_CITATION_PATH = DATA_PATH / 'lattes_citation.yml'
  OPENALEX_CITATION_PATH = DATA_PATH / 'openalex_citation.yml'



def update_list_by_dict(target: list, value: dict):
  """
  Updates a list using keys from dictionary
  May be helpful if you want a fuzzy update of a list
  If key greater than list size, list will be extended
  If list value is dict, it's deep updated
  """
  for k, v in value.items():
    idx = int(k)
    if idx >= len(target):
      target.extend(itertools.repeat(None, idx - len(target) + 1))
    if isinstance(target[idx], dict) and isinstance(v, dict):
      _deep_update(target[idx], v)
    else:
      target[idx] = v



def _deep_update(target: dict, update: dict):
  """Deep update target dict with update
  For each k,v in update: if k doesn't exist in target, it is deep copied from
  update to target.
  Nested lists are extend if you update by the list and updated if you update by dictionary
  """
  for k, v in update.items():
    curr_val = None
    if isinstance(target, dict):
      if k not in target:
        target[k] = copy.deepcopy(v)

      curr_val = target[k]

    if isinstance(curr_val, list):
      if isinstance(v, list):
        curr_val.extend(copy.deepcopy(v))
      elif isinstance(v, dict):
        update_list_by_dict(curr_val, v)
      else:
        curr_val.extend(v)
    elif isinstance(curr_val, dict):
      _deep_update(target[k], v)
    elif isinstance(curr_val, set):
      if k not in target:
        target[k] = v.copy()
      else:
        target[k].update(v.copy())
    else:
      target[k] = copy.copy(v)



def get_collection_path(collection: str):
  return COLLECTIONS_PATH / f'_{collection}'


def load_collection_metadata(collection: str):
  paths = get_collection_path(collection).glob('*.md')
  data = []
  
  for path in paths:
    metadata, _ = frontmatter.parse(path.read_text())
    data.append(metadata)
  
  return data


def load_data(collection: str, lower_keys: bool = False, lower_values: bool = False):
  path = [*DATA_PATH.glob(f'{collection}*')][0]
  data = yaml.safe_load(path.read_text())
  if lower_keys:
    data = { k.lower(): v for k, v in data.items() }
  if lower_values:
    data = { k: v.lower() for k, v in data.items() }
  return data


def get_issn_mapping(transform: bool = True):
  venues = load_data('venues', lower_keys=True)
  
  # transform abbreviations in std
  if transform:
    issn = {v['issn']: v.get('name', k) for k, v in venues.items() if v.get('issn')}
  else:
    issn = {v['issn']: k for k, v in venues.items() if v.get('issn')}

  return issn # issn <-> venue_std


def reverse_mapping(mapping: dict):
  return {v: k for k, v in mapping.items()}


def _is_cache_fresh(entry: dict | None, cache_duration: int) -> bool:
  if not entry:
    return False

  update_date = entry.get('update_date')
  if not update_date:
    return False

  try:
    updated_at = datetime.strptime(update_date, '%Y-%m-%d').date()
  except (TypeError, ValueError):
    return False

  return (datetime.today().date() - updated_at).days <= cache_duration


def _log(message: str):
  print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}", flush=True)


def _load_cached_yaml(path: Path) -> dict:
  if not path.exists():
    return {}

  return yaml.safe_load(path.read_text()) or {}


def write_yaml(obj: Any, path: Path, merge: bool = True):
  data = {}
  
  if merge and path.exists():
    data = yaml.safe_load(path.read_text())
  
  _deep_update(data, obj)
  output = f'# Automatically generated by {Path(__file__).name}\n'
  output += f'# Updated at {datetime.today().strftime('%Y-%m-%d')}\n'
  output += yaml.dump(data, sort_keys=False)
  path.write_text(output)
      

def find_issn_openalex(publications: list[dict], ignore_cache: bool = False):
  pass


def fetch_jcr_lattes(cache_duration: int = 0):
  _log(f"JCR: starting fetch with cache_duration={cache_duration} days")
  issn_venue_mapping = get_issn_mapping(False)
  issn_venue_mapping_std = get_issn_mapping()
  cached_index = _load_cached_yaml(LATTES_JCR_PATH)
  skipped = 0
  fetched = 0
  failed = 0

  _log(f"JCR: loaded {len(cached_index)} cached entries from {LATTES_JCR_PATH.name}")
  
  reverse_index = dict(cached_index)
  for issn in issn_venue_mapping.keys():
    venue_key = issn_venue_mapping[issn]
    venue_std_key = issn_venue_mapping_std[issn]

    if _is_cache_fresh(cached_index.get(venue_key), cache_duration) and _is_cache_fresh(cached_index.get(venue_std_key), cache_duration):
      skipped += 1
      _log(f"JCR: cache hit for {venue_key} ({issn})")
      continue

    _log(f"JCR: fetching {venue_key} ({issn})")
    resp = requests.get(
      LATTES_JCR_API, 
      params={
        'metodo': 'ajax',
        'acao': 'jcr',
        'issn': str(issn).replace('-', '')
      }, 
      headers={
        **HEADERS,
        'host': 'buscatextual.cnpq.br',
      }
    )
    
    try:
      data = resp.json()
      jif = float(data['fator-impacto'])
      year = int(data['ano'])
      value = dict(jif=jif, year=year, update_date=datetime.today().strftime('%Y-%m-%d'))
      reverse_index[venue_key] = value
      reverse_index[venue_std_key] = {**value}
      fetched += 1
      _log(f"JCR: updated {venue_key} -> jif={jif}, year={year}")
    except Exception:
      value = dict(jif=-1, update_date=datetime.today().strftime('%Y-%m-%d'))
      reverse_index[venue_key] = value
      reverse_index[venue_std_key] = {**value}
      failed += 1
      _log(f"JCR: failed to fetch {venue_key}; stored fallback value")

  write_yaml(reverse_index, LATTES_JCR_PATH)
  _log(
    f"JCR: finished. total={len(issn_venue_mapping)} "
    f"skipped={skipped} fetched={fetched} failed={failed}"
  )
  


def fetch_citations_lattes(cache_duration: int = 0):
  _log(f"Lattes citations: starting fetch with cache_duration={cache_duration} days")
  publications = load_collection_metadata('publications')
  publications = [p for p in publications if p.get('doi')]
  cached_index = _load_cached_yaml(LATTES_CITATION_PATH)
  skipped = 0
  fetched = 0
  
  index = dict(cached_index)
  _log(f"Lattes citations: loaded {len(cached_index)} cached entries from {LATTES_CITATION_PATH.name}")
  
  for pub in publications:
    if _is_cache_fresh(cached_index.get(pub['doi']), cache_duration):
      skipped += 1
      _log(f"Lattes citations: cache hit for {pub['doi']}")
      continue

    _log(f"Lattes citations: fetching {pub['doi']}")
    resp = requests.get(
      LATTES_CITATION_API,
      params={'doi': pub['doi']},
      headers={
        **HEADERS,
        'host': 'buscatextual.cnpq.br',
      },
    )
    
    values = {}
    try:
      data = resp.json()
      for source in data['citacoes']:
        if str(source['base']) == '1':
          values['wos'] = source['qtd']
        elif str(source['base']) == '3':
          values['scopus'] = source['qtd']
    except Exception:
      pass
    
    values['update_date'] = datetime.today().strftime('%Y-%m-%d')
    index[pub['doi']] = values
    fetched += 1
    _log(f"Lattes citations: updated {pub['doi']} -> wos={values.get('wos', 0)}, scopus={values.get('scopus', 0)}")
  
  write_yaml(index, LATTES_CITATION_PATH)
  _log(
    f"Lattes citations: finished. total={len(publications)} "
    f"skipped={skipped} fetched={fetched}"
  )
  
  

def fetch_citations_openalex(cache_duration: int = 0):
  _log(f"OpenAlex citations: starting fetch with cache_duration={cache_duration} days")
  publications = load_collection_metadata('publications')
  publications = [p for p in publications if p.get('doi')]
  cached_index = _load_cached_yaml(OPENALEX_CITATION_PATH)
  skipped = 0
  fetched = 0
  
  index = dict(cached_index)
  _log(f"OpenAlex citations: loaded {len(cached_index)} cached entries from {OPENALEX_CITATION_PATH.name}")
  
  for pub in publications:
    if _is_cache_fresh(cached_index.get(pub['doi']), cache_duration):
      skipped += 1
      _log(f"OpenAlex citations: cache hit for {pub['doi']}")
      continue

    _log(f"OpenAlex citations: fetching {pub['doi']}")
    resp = requests.get(
      OPENALEX_WORKS_API + 'doi:' + pub['doi'],
      headers={
        **HEADERS,
        'host': 'api.openalex.org',
      },
    )
    
    values = {}
    try:
      data = resp.json()
      if data['cited_by_count'] > 0:
        values['count'] = data['cited_by_count']
    except Exception:
      pass
    
    values['update_date'] = datetime.today().strftime('%Y-%m-%d')
    index[pub['doi']] = values
    fetched += 1
    _log(f"OpenAlex citations: updated {pub['doi']} -> count={values.get('count', 0)}")
  
  write_yaml(index, OPENALEX_CITATION_PATH)
  _log(
    f"OpenAlex citations: finished. total={len(publications)} "
    f"skipped={skipped} fetched={fetched}"
  )



def main():
  parser = argparse.ArgumentParser(description='Fetch and update citation metadata caches.')
  parser.add_argument(
    '--root',
    type=Path,
    default=None,
    help='Repository root containing _data and content directories',
  )
  subparsers = parser.add_subparsers(dest='command', required=True)

  jcr_parser = subparsers.add_parser('jcr-lattes', help='Fetch JCR data from Lattes')
  jcr_parser.add_argument('-c', '--cache-duration', type=int, default=0, help='Cache duration in days')

  lattes_parser = subparsers.add_parser('citations-lattes', help='Fetch citation counts from Lattes')
  lattes_parser.add_argument('-c', '--cache-duration', type=int, default=0, help='Cache duration in days')

  openalex_parser = subparsers.add_parser('citations-openalex', help='Fetch citation counts from OpenAlex')
  openalex_parser.add_argument('-c', '--cache-duration', type=int, default=0, help='Cache duration in days')

  args = parser.parse_args()
  configure_paths(args.root or discover_root())

  if args.command == 'jcr-lattes':
    fetch_jcr_lattes(args.cache_duration)
  elif args.command == 'citations-lattes':
    fetch_citations_lattes(args.cache_duration)
  elif args.command == 'citations-openalex':
    fetch_citations_openalex(args.cache_duration)



if __name__ == "__main__":
  main()
