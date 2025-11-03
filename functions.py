VENUE_MAP = {
    'VLDB':'VLDB' ,
    'VLDB 2022': 'VLDB',
    'VLDB J': 'VLDB',
    'VLDB Conference': 'VLDB',
    'ICML Conference': 'ICML',
    'SIGMOD Record': 'SIGMOD',
    'SIGMOD Conference': 'SIGMOD',
    'ACM Trans. Database Syst.':'ACM Trans'
}

def standardize_author(name):
    parts = name.strip().split()
    if len(parts) == 1:
        return parts[0]
    initials = ' '.join([p[0].upper() + '.' for p in parts[:-1]])
    last_name = parts[-1].capitalize()
    return f"{initials} {last_name}"

def standardize_venue(venue):
    for k, v in VENUE_MAP.items():
        if k.lower() in venue.lower():
            return v
  