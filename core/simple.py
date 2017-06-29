from __future__ import division
import sys

from core.os import get_documents_path, read_env_var


def get_items(d):
    """As Python 2 and 3 have different ways of getting items,
    any attempt should be wrapped in this function.
    """
    if sys.version_info.major == 2:
        return d.iteritems()
    else:
        return d.items()
        
        
def round_up(n):
    i = int(n)
    if float(n) - i:
        i += 1
    return i
    

def format_file_path(path):
    parts = path.replace('\\', '/').rstrip('/').split('/')
    f = parts.pop(-1) if '.' in parts[-1] else None
    for i, part in enumerate(parts):
        if part == '%DOCUMENTS%':
            parts[i] = get_documents_path()
        else:
            env_var = read_env_var(part)
            if env_var is not None:
                parts[i] = env_var
    if f is not None:
        parts.append(f)
    return '/'.join(i.replace('\\', '/') for i in parts if i)