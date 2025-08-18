# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_13_GHE_CAT_CHAY"
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
    layout.add_line((22.9736020470009, -33.88364639494739), (22.9736020470009, 966.1163536050526), dxfattribs={ "layer": "0" })
    layout.add_line((-27.02639795299911, -33.88364639494739), (-27.02639795299911, 966.1163536050526), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((572.9736020470007, -33.88364639494739), (572.9736020470007, 966.1163536050526), dxfattribs={ "layer": "0" })
    layout.add_line((622.9736020470007, -33.88364639494739), (622.9736020470007, 966.1163536050526), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((100.7382165379094, 454.1163536050523), (623.2933557661453, 454.1163536050523), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((100.7382165379094, 466.1163536050525), (622.9736020470007, 466.1163536050525), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((495.1943592488984, 454.1163536050523), (100.7382165379094, 454.1163536050523), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((487.3519825200053, 466.1163536050525), (100.7382165379094, 466.1163536050525), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-27.02639795299911, 454.1163536050523), (100.7382165379094, 454.1163536050523), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-27.02639795299911, 466.1163536050525), (100.7382165379094, 466.1163536050525), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((623.7530140357976, -33.88364639494739), (-26.24698596420058, -33.88364639494739), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((622.9736020470007, -33.88364639494739), (-27.02639795299911, -33.88364639494739), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((572.9736020470007, 16.11635360505261), (-27.02639795299911, 16.11635360505261), dxfattribs={ "layer": "0" })
    layout.add_line((100.7382165379094, 954.1163536050524), (623.2933557661453, 954.1163536050524), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((100.7382165379094, 966.1163536050526), (622.9736020470007, 966.1163536050526), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((495.1943592488984, 954.1163536050524), (100.7382165379094, 954.1163536050524), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((487.3519825200053, 966.1163536050526), (100.7382165379094, 966.1163536050526), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-27.02639795299911, 954.1163536050524), (100.7382165379094, 954.1163536050524), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-27.02639795299911, 966.1163536050526), (100.7382165379094, 966.1163536050526), dxfattribs={ "layer": "0", "color": 2 })

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
