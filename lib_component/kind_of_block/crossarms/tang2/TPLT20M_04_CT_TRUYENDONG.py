# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_04_CT_TRUYENDONG"
LAYERS = {
    "L1": {"color": 7},
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
    layout.add_line((-30.48776835810349, -12.89624727109003), (-30.48776835810349, 68.51531554537722), dxfattribs={ "layer": "L1" })
    layout.add_line((608.0868766619643, -12.89624727109003), (-30.48776835810349, -12.89624727109003), dxfattribs={ "layer": "L1" })
    layout.add_line((-30.48776835810349, 68.51531554537722), (608.0868766619643, 68.51531554537722), dxfattribs={ "layer": "L1" })
    layout.add_line((608.0868766619643, 68.51531554537722), (608.0868766619643, -12.89624727109003), dxfattribs={ "layer": "L1" })

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
