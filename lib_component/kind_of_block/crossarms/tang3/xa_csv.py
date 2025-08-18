# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_csv"
LAYERS = {
    "BAO": {"color": 3},
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
    layout.add_line((-848.3683742800421, 0.9126814199789804), (851.6316257199578, 0.9126814199789804), dxfattribs={ "layer": "BAO", "color": 8 })
    # Unsupported entity type: HATCH
    layout.add_line((-153.3683742801586, 6.489154219156262), (-153.3683742801586, -15.51084578084374), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-133.3683742801586, 0.9126814199789804), (-133.3683742801586, -6.087318580021019), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-173.3683742801586, 0.9126814199789804), (-173.3683742801586, -6.087318580021019), dxfattribs={ "layer": "0", "color": 8 })
    # Unsupported entity type: HATCH
    layout.add_line((156.6316257199578, 6.489154219156262), (156.6316257199578, -15.51084578084374), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((136.6316257199578, 0.9126814199789804), (136.6316257199578, -6.087318580021019), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((176.6316257199578, 0.9126814199789804), (176.6316257199578, -6.087318580021019), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1.631625720190641, -60.08731859105137), (1.631625720190641, 33.91268142000809), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-181.0349392504358, -6.087318580021019), (-111.0349392504358, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-111.0349392504358, -6.087318580021019), (-111.0349392504358, -76.087318580021), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-111.0349392504358, -76.087318580021), (-118.0349392504358, -76.087318580021), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-118.0349392504358, -76.087318580021), (-118.0349392504358, -13.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-118.0349392504358, -13.08731858002102), (-181.0349392504358, -13.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-181.0349392504358, -13.08731858002102), (-181.0349392504358, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((184.2981906900022, -6.087318580021019), (114.2981906900022, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((114.2981906900022, -6.087318580021019), (114.2981906900022, -76.087318580021), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((114.2981906900022, -76.087318580021), (121.2981906900022, -76.087318580021), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((121.2981906900022, -76.087318580021), (121.2981906900022, -13.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((121.2981906900022, -13.08731858002102), (184.2981906900022, -13.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((184.2981906900022, -13.08731858002102), (184.2981906900022, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-848.3683742800421, 73.91268141997898), (851.6316257199578, 73.91268141997898), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((851.6316257199578, 73.91268141997898), (851.6316257199578, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((851.6316257199578, -6.087318580021019), (-848.3683742800421, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-848.3683742800421, -6.087318580021019), (-848.3683742800421, 73.91268141997898), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-838.368374280275, -14.08731858002102), (-758.368374280275, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-758.368374280275, -14.08731858002102), (-758.368374280275, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-758.368374280275, -6.087318580021019), (-838.368374280275, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-838.368374280275, -6.087318580021019), (-838.368374280275, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((841.6316257201906, -14.08731858002102), (761.6316257201906, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((761.6316257201906, -14.08731858002102), (761.6316257201906, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((761.6316257201906, -6.087318580021019), (841.6316257201906, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((841.6316257201906, -6.087318580021019), (841.6316257201906, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((41.63162572019063, -14.08731858002102), (-38.36837427980936, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-38.36837427980936, -14.08731858002102), (-38.36837427980936, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-38.36837427980936, -6.087318580021019), (41.63162572019063, -6.087318580021019), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((41.63162572019063, -6.087318580021019), (41.63162572019063, -14.08731858002102), dxfattribs={ "layer": "0", "color": 2 })

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
