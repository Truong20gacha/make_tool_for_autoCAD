import re

def parse_mota(mo_ta: str) -> float:
    if not isinstance(mo_ta, str):
        return 0.0
    match = re.search(r"AT\s*=\s*([0-9.+-]+)", mo_ta)
    if match:
        at_val = float(match.group(1))
        if abs(at_val) < 1000:
            at_val *= 1000.0
        return at_val
    return 0.0

def parse_lechx(mo_ta: str) -> float:
    if not isinstance(mo_ta, str):
        return 0.0
    match = re.search(r"X\s*=\s*([0-9.+-]+)", mo_ta)
    if match:
        return float(match.group(1)) * 1000.0
    return 0.0
