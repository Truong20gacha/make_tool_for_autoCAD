# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_02_XA_TRUYENDONG"
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
    layout.add_line((687.0636640730658, 70.43521224581491), (687.0636640730658, -10.97635057065599), dxfattribs={ "layer": "L1" })
    layout.add_line((462.7330757998261, -22.57782965046317), (462.7330757998261, -226.0167650307767), dxfattribs={ "layer": "L1" })
    layout.add_line((462.7330757998261, -226.0167650307767), (676.4811275916277, -226.0167650307767), dxfattribs={ "layer": "L1" })
    layout.add_line((676.4811275916277, -226.0167650307767), (676.4811275916277, -12.40596006296073), dxfattribs={ "layer": "L1" })
    layout.add_line((-32.93883023579929, -10.97635057065599), (-32.93883023579929, 70.43521224581491), dxfattribs={ "layer": "L1" })
    layout.add_line((-32.93883023579929, 70.43521224581491), (687.0636640730658, 70.43521224569757), dxfattribs={ "layer": "L1" })
    layout.add_line((687.0636640730658, -10.97635057065599), (-32.93883023579929, -10.97635057065599), dxfattribs={ "layer": "L1" })

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
