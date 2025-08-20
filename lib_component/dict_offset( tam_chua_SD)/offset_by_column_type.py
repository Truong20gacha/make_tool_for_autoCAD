# offset_by_column_type.py


import re
def normalize_column_type(raw_type: str) -> str:
    return re.sub(r"[-.,]", "_", raw_type.strip())


OFFSET_MAP = {
    "2PC_I_20_190_13": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "PC_I_10_190_4_3": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "PC_I_10_190_5": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "PC_I_10_190_4": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "PC_I_20_190_13": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "PC_I_20_230_24": {
        "foundations": lambda x, y, idx: (x, y - 200),
        "crossarms": {
            'tang0':lambda x, y, idx: (x, y + 19600 + 150 * idx),
            "tang1": lambda x, y, idx: (x, y + 18000 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 17000 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 16000 + 150 * idx),
            'no_layer': lambda x, y, idx: (x, y + 13000 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 40, y + 12000 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "stairs": lambda x, y, idx: (x - 300 , y + 2700 + 300 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT12m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT10m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT7_5m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT8_5m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT14m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT16m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "LT18m": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },

    "Cot_thep": {
        "foundations": lambda x, y, idx: (x, y - 1000),
        "crossarms": {
            "tang1": lambda x, y, idx: (x, y + 600 + 150 * idx),
            "tang2": lambda x, y, idx: (x, y + 400 + 150 * idx),
            "tang3": lambda x, y, idx: (x, y + 200 + 150 * idx),
        },
        "accessories": lambda x, y, idx: (x + 200, y + 2200 + 100 * idx),
        "grounding": lambda x, y, idx: (x - 200, y - 200 - 100 * idx),
        "insulators": lambda x, y, idx: (x + 250, y + 400 + 100 * idx),
        "lightning_arrestors": lambda x, y, idx: (x + 350, y + 300 + 100 * idx),
        "pole_types": lambda x, y, idx: (x + 400, y - 50 + 80 * idx),
        "templates": lambda x, y, idx: (x + 450, y + 100 + 60 * idx),
        "cables": lambda x, y, idx: (x + 150, y + 600 + 120 * idx),
        "switch": lambda x, y, idx: (x + 120, y + 900 + 150 * idx),
    },
}


def get_offset(col_type: str, folder: str, x: float, y: float, idx: int, subtype: str = None):
    folder = folder.lower()
    key = normalize_column_type(col_type)
    col_map = OFFSET_MAP.get(key)
    if not col_map:
        return (x, y)

    folder_obj = col_map.get(folder)
    if folder_obj is None:
        return (x, y)

    if isinstance(folder_obj, dict) and subtype:
        func = folder_obj.get(subtype.lower())
        if func:
            return func(x, y, idx)
        else:
            return (x, y)
    
    if callable(folder_obj):
        return folder_obj(x, y, idx)

    return (x, y)