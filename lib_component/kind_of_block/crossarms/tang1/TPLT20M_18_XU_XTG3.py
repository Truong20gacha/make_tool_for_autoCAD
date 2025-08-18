# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_18_XU_XTG3"
LAYERS = {
    "0": {"color": 7},
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
    layout.add_line((23.31258906080757, -2.662453354389069), (5.312589060807566, -2.662453354389069), dxfattribs={ "layer": "0" })
    layout.add_arc((5.312589060807566, 8.337546645610926), 11.0, 180.0, 270.0, dxfattribs={ "layer": "0" })
    layout.add_line((-5.687410939192657, 8.337546645610926), (-5.687410939192657, 8.337546645610926), dxfattribs={ "layer": "0" })
    layout.add_arc((5.312589060807566, 8.337546645610926), 11.0, 90.0, 180.0, dxfattribs={ "layer": "0" })
    layout.add_line((5.312589060807566, 19.33754664561275), (23.31258906080757, 19.33754664561275), dxfattribs={ "layer": "0" })
    layout.add_arc((23.31258906080757, 8.337546645610926), 11.0, 0.0, 90.0, dxfattribs={ "layer": "0" })
    layout.add_line((34.31258906080757, 8.337546645610926), (34.31258906080757, 8.337546645610926), dxfattribs={ "layer": "0" })
    layout.add_arc((23.31258906080757, 8.337546645610926), 11.0, 270.0, 0.0, dxfattribs={ "layer": "0" })

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
