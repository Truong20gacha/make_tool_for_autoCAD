# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2KD_3NK"
LAYERS = {
    "BAO": {"color": 3},
    "0": {"color": 7},
    "tex": {"color": 4},
    "tim": {"color": 6},
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
    layout.add_line((-1252.399449588464, -36.38945901025), (1247.600550412002, -36.38945901170519), dxfattribs={ "layer": "BAO" })
    layout.add_line((-1252.399449588464, 29.090559749362), (1247.600550412002, 29.09055974837247), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-1252.399449588464, 1.110540989750006), (1247.600550412119, 1.110540988294815), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-1252.399449588231, 38.61054098975001), (-1252.399449588464, -36.38945901025), dxfattribs={ "layer": "BAO" })
    layout.add_line((-655.7175263384943, 39.90872024973942), (-558.3540818385899, 39.90872024973942), dxfattribs={ "layer": "BAO" })
    layout.add_line((-558.3540818385899, 39.90872024973942), (-558.3540818385899, 49.18142924966378), dxfattribs={ "layer": "BAO" })
    layout.add_line((-558.3540818385899, 49.18142924966378), (-646.4448173385699, 49.18142924966378), dxfattribs={ "layer": "BAO" })
    # Unsupported entity type: HATCH
    # Unsupported entity type: HATCH
    layout.add_line((-602.3994495884635, 49.18142924966378), (-602.3994495884635, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((1247.600550411769, 38.61054098975001), (1247.600550412002, -36.38945901025), dxfattribs={ "layer": "BAO" })
    layout.add_line((650.9186271620327, 39.90872024973942), (553.5551826618957, 39.90872024973942), dxfattribs={ "layer": "BAO" })
    layout.add_line((553.5551826618957, 39.90872024973942), (553.5551826618957, 49.18142924966378), dxfattribs={ "layer": "BAO" })
    layout.add_line((553.5551826618957, 49.18142924966378), (641.6459181618757, 49.18142924966378), dxfattribs={ "layer": "BAO" })
    # Unsupported entity type: HATCH
    # Unsupported entity type: HATCH
    layout.add_line((597.6005504120021, 49.18142924966378), (597.6005504120021, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((-152.1357071883631, 29.09055974889634), (-152.1357071883631, -27.44940273089014), dxfattribs={ "layer": "tim", "color": 8 })
    layout.add_line((-49.10643241411344, -36.38945901094849), (-49.10643241411344, 29.09055974886724), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-118.3461919847996, -36.38945901091938), (-118.3461919847996, 29.09055974889634), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-83.72631219945652, -36.38945901094849), (-83.72631219945652, 29.09055974889634), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((147.3368080123673, 29.67048470910959), (147.3368080123673, -27.44940273089014), dxfattribs={ "layer": "tim", "color": 8 })
    layout.add_line((44.30753323811768, -36.38945901100669), (44.30753323811768, 29.09055974883813), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((113.5472928090366, -36.3894590110649), (113.5472928090366, 29.09055974883813), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((78.92741302357717, -36.3894590110358), (78.92741302346076, 29.09055974883813), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((1247.600550411769, 38.61054098975001), (-1252.399449588231, 38.61054099749163), dxfattribs={ "layer": "BAO" })
    layout.add_line((-612.9172227836334, 49.18142924966378), (-591.8816763935264, 49.18142924966378), dxfattribs={ "layer": "tex" })
    layout.add_line((-591.8816763935264, 49.18142924966378), (-591.8816763935264, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((-591.8816763935264, 39.90872024973942), (-612.9172227836334, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((-612.9172227836334, 39.90872024973942), (-612.9172227836334, 49.18142924966378), dxfattribs={ "layer": "tex" })
    layout.add_line((-612.9172227836334, 39.90872024973942), (-592.0389374112365, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((-592.0389374112365, 39.90872024973942), (-592.0389374112365, 29.09055974982766), dxfattribs={ "layer": "tex" })
    layout.add_line((-592.0389374112365, 29.09055974982766), (-612.9172227836334, 29.09055974982766), dxfattribs={ "layer": "tex" })
    layout.add_line((-612.9172227836334, 29.09055974982766), (-612.9172227836334, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((608.1183236071719, 49.18142924966378), (587.0827772168323, 49.18142924966378), dxfattribs={ "layer": "tex" })
    layout.add_line((587.0827772168323, 49.18142924966378), (587.0827772168323, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((587.0827772168323, 39.90872024973942), (608.1183236071719, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((608.1183236071719, 39.90872024973942), (608.1183236071719, 49.18142924966378), dxfattribs={ "layer": "tex" })
    layout.add_line((608.1183236071719, 39.90872024973942), (587.240038234775, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_line((587.240038234775, 39.90872024973942), (587.240038234775, 29.09055974982766), dxfattribs={ "layer": "tex" })
    layout.add_line((587.240038234775, 29.09055974982766), (608.1183236071719, 29.09055974982766), dxfattribs={ "layer": "tex" })
    layout.add_line((608.1183236071719, 29.09055974982766), (608.1183236071719, 39.90872024973942), dxfattribs={ "layer": "tex" })
    layout.add_arc((-164.3756830686125, 1.110540988993307), 14.95997051999438, 180.0000000004169, 270.0000000004169, dxfattribs={ "layer": "BAO" })
    layout.add_line((-179.3356535886069, 1.110540988876891), (-179.3356535886069, 1.110540988876891), dxfattribs={ "layer": "BAO" })
    layout.add_arc((-164.3756830683796, 1.110540988993307), 14.95997052022721, 90.00000000041688, 180.0000000004169, dxfattribs={ "layer": "BAO" })
    layout.add_line((-164.3756830684961, 16.07051150922052), (-139.8957313084629, 16.07051150922052), dxfattribs={ "layer": "BAO" })
    layout.add_arc((-139.8957313085793, 1.110540988993307), 14.95997052022721, 359.9999999995831, 89.99999999958312, dxfattribs={ "layer": "BAO" })
    layout.add_line((-124.9357607883521, 1.110540988876891), (-124.9357607883521, 1.110540988876891), dxfattribs={ "layer": "BAO" })
    layout.add_arc((-139.8957313083465, 1.110540988993307), 14.95997051999438, 269.9999999995831, 359.9999999995831, dxfattribs={ "layer": "BAO" })
    layout.add_line((-139.8957313084629, -13.84942953100108), (-164.3756830684961, -13.84942953100108), dxfattribs={ "layer": "BAO" })
    layout.add_arc((159.5767838926167, 1.110540988993307), 14.95997051999438, 269.9999999995831, 359.9999999995831, dxfattribs={ "layer": "BAO" })
    layout.add_line((174.5367544126111, 1.110540988876891), (174.5367544126111, 1.110540988876891), dxfattribs={ "layer": "BAO" })
    layout.add_arc((159.5767838923839, 1.110540988993307), 14.95997052022721, 359.9999999995831, 89.99999999958312, dxfattribs={ "layer": "BAO" })
    layout.add_line((159.5767838925003, 16.07051150922052), (135.0968321324671, 16.07051150922052), dxfattribs={ "layer": "BAO" })
    layout.add_arc((135.0968321325836, 1.110540988993307), 14.95997052022721, 90.00000000041688, 180.0000000004169, dxfattribs={ "layer": "BAO" })
    layout.add_line((120.1368616123563, 1.110540988876891), (120.1368616123563, 1.110540988876891), dxfattribs={ "layer": "BAO" })
    layout.add_arc((135.0968321323507, 1.110540988993307), 14.95997051999438, 180.0000000004169, 270.0000000004169, dxfattribs={ "layer": "BAO" })
    layout.add_line((135.0968321324671, -13.84942953100108), (159.5767838925003, -13.84942953100108), dxfattribs={ "layer": "BAO" })

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
