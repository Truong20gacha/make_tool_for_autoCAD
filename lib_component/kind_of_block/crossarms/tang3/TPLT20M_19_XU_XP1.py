# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_19_XU_XP1"
LAYERS = {
    "0": {"color": 7},
    "Xà": {"color": 2},
}

def _get_doc(layout):
    return getattr(layout, 'doc', None) or getattr(layout, 'drawing', None)

def _ensure_layers(doc):
    for name, attrs in LAYERS.items():
        if name in doc.layers:
            lay = doc.layers.get(name)
            if 'color' in attrs:
                lay.color = attrs['color']
        else:
            doc.layers.new(name, dxfattribs={'color': attrs.get('color', 7)})

def _draw_into(layout):
    layout.add_line((772.6650496974866, 32.35894860311056), (772.6650496974866, 25.35896492049142), dxfattribs={ "layer": "0", "color": 7 })
    layout.add_line((772.6650496974866, 44.60904504579775), (772.6650496974866, 18.48404344556002), dxfattribs={ "layer": "0", "color": 7 })
    layout.add_line((772.6650496974866, 32.35894860311056), (772.6650496974866, -13.50941325604981), dxfattribs={ "layer": "0", "color": 7 })
    layout.add_line((754.0555449178754, 32.35894860311056), (791.2745544770833, 32.35894860311056), dxfattribs={ "layer": "0", "color": 7 })
    layout.add_line((-34.94736174663922, 36.46493930866927), (815.5058010526294, 36.46493930866927), dxfattribs={ "layer": "Xà" })
    layout.add_line((815.5058010526294, 36.46493930866927), (815.5058010526294, -16.90218980290046), dxfattribs={ "layer": "Xà" })
    layout.add_line((815.5058010526294, -16.90218980290046), (-34.94736174663922, -16.90218980290046), dxfattribs={ "layer": "Xà" })
    layout.add_line((-34.94736174663922, -16.90218980290046), (-34.94736174663922, 36.46493930866927), dxfattribs={ "layer": "Xà" })

def add_to_drawing(msp):
    _doc = _get_doc(msp)
    if _doc is not None:
        _ensure_layers(_doc)
    _draw_into(msp)

def register_block(doc):
    _ensure_layers(doc)
    if BLOCK_NAME in doc.blocks:
        blk = doc.blocks.get(BLOCK_NAME)
        # Xoá nội dung cũ? Không: giữ nguyên để an toàn.
    else:
        blk = doc.blocks.new(name=BLOCK_NAME)
    _draw_into(blk)

def insert_block(msp, insert=(0, 0), rotation_deg=0, scale=1.0, layer='0'):
    doc = _get_doc(msp)
    if doc is None:
        raise RuntimeError('Không lấy được document từ layout.')
    if BLOCK_NAME not in doc.blocks:
        register_block(doc)
    ref = msp.add_blockref(BLOCK_NAME, insert, dxfattribs={'layer': layer})
    try:
        ref.dxf.rotation = rotation_deg
        ref.dxf.xscale = scale
        ref.dxf.yscale = scale
    except Exception:
        pass
