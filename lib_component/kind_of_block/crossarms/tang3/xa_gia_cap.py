# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_gia_cap"
LAYERS = {
    "DANTRAM": {"color": 7},
    "DUONGTAM": {"color": 8},
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
    layout.add_arc((-154.2764337361186, -1.630018213476432), 11.0, 270.0, 0.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-154.2764337361186, -12.63001821347643), (-163.2764337361186, -12.63001821347643), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-172.2764337361186, -12.63001821347643), (-163.2764337361186, -12.63001821347643), dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((-172.2764337361186, -1.630018213476432), 11.0, 180.0, 270.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((-172.2764337361186, -1.630018213476432), 11.0, 90.0, 180.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-172.2764337361186, 9.369981786523567), (-163.2764337361186, 9.369981786523567), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-154.2764337361186, 9.369981786523567), (-163.2764337361186, 9.369981786523567), dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((-154.2764337361186, -1.630018213476432), 11.0, 0.0, 90.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((171.7860413030394, -1.630018213476432), 11.0, 180.0, 270.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((171.7860413030394, -12.63001821347643), (180.7860413030394, -12.63001821347643), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((189.7860413030393, -12.63001821347643), (180.7860413030394, -12.63001821347643), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((189.7860413030393, 9.369981786523567), (180.7860413030394, 9.369981786523567), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((171.7860413030394, 9.369981786523567), (180.7860413030394, 9.369981786523567), dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((171.7860413030394, -1.630018213476432), 11.0, 90.0, 180.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((189.7860413030393, -1.630018213476432), 11.0, 270.0, 0.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_arc((189.7860413030393, -1.630018213476432), 11.0, 0.0, 90.0, dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((212.7827776181184, 18.36998178652357), (-211.9674442222204, 18.36998178652357), dxfattribs={ "layer": "DANTRAM", "color": 8 })
    layout.add_line((212.7827776181184, 23.36998178652357), (-211.9674442222204, 23.36998178652357), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((212.7827776181184, -1.630018213476432), (-211.9674442222204, -1.630018213476432), dxfattribs={ "layer": "DUONGTAM" })
    layout.add_line((212.7827776181184, -26.63001821347644), (-211.9674442222204, -26.63001821347644), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-211.9674442222204, -26.63001821347644), (-211.9674442222204, 23.36998178652357), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-163.2764337361186, -26.63001821347644), (-163.2764337361186, 23.36998178652357), dxfattribs={ "layer": "DUONGTAM" })
    layout.add_line((-163.2764337361186, -26.63001821347644), (-163.2764337361186, 23.36998178652357), dxfattribs={ "layer": "DUONGTAM" })
    layout.add_line((180.7860413030394, -26.63001821347644), (180.7860413030394, 23.36998178652357), dxfattribs={ "layer": "DUONGTAM" })
    layout.add_line((180.7860413030394, -26.63001821347644), (180.7860413030394, 23.36998178652357), dxfattribs={ "layer": "DUONGTAM" })
    layout.add_line((212.7827776181184, -26.63001821347644), (212.7827776181184, 23.36998178652357), dxfattribs={ "layer": "0" })

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
