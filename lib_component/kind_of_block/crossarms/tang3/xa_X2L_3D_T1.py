# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2L_3D_T1"
LAYERS = {
    "0": {"color": 7},
    "BAO": {"color": 3},
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
    # Unsupported entity type: ELLIPSE
    layout.add_line((-168.8223952353328, -54.39541891822591), (-129.2225245952468, -54.39541891822591), dxfattribs={ "layer": "0" })
    layout.add_line((-168.8223952353328, -50.86941529755131), (-124.1957730168105, -50.86941529755131), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-878.3955056201994, -35.26075663408847), (881.774256508881, -35.24161893627024), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, -31.73475301373401), (110.5716239902795, -31.71230446684058), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, -0.0007204286230262), (110.355943474653, 0.0217281182704028), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-779.489634767906, 27.35447519188165), (-65.36054357121247, 27.37188617466018), dxfattribs={ "layer": "0" })
    layout.add_line((68.74373097667922, 27.37515573369456), (110.1700288988322, 27.37616573672858), dxfattribs={ "layer": "0" })
    layout.add_line((-783.4237210633327, 24.61902062981972), (-61.42911281160559, 24.6365542440326), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((64.8125311764561, 24.63962001798791), (110.188620356228, 24.64072197474889), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-168.8223952353328, -54.39541891822591), (-168.8223952353328, -35.23830808699131), dxfattribs={ "layer": "0" })
    layout.add_line((-168.8223952353328, -54.39541891822591), (-168.8223952353328, -35.23830808699131), dxfattribs={ "layer": "0" })
    layout.add_line((-878.3955056201994, -7.906319015979534), (-814.643188165068, -7.906319015979534), dxfattribs={ "layer": "0" })
    layout.add_line((-878.3955056201994, 11.00064546964131), (-878.3955056201994, -35.26075663408847), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, 11.00063177515403), (-814.643188165068, -35.26075663408847), dxfattribs={ "layer": "0" })
    layout.add_line((110.355943474653, 0.0217281182704028), (881.7742565087646, 0.0217281182995066), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((64.81420869423528, 24.64072197480709), (568.7742565087646, 24.64072197451605), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((568.7742565087646, 24.64072197451605), (786.4756353886004, 24.64072197439964), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((68.74510134636876, 27.37616573672858), (582.5041919339819, 27.37616573672858), dxfattribs={ "layer": "0" })
    layout.add_line((582.5041919339819, 27.37616573672858), (782.5447427357685, 27.37616573672858), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    layout.add_line((172.211408890751, -50.33574607691844), (127.5847866721124, -50.33574607691844), dxfattribs={ "layer": "0" })
    layout.add_line((172.211408890751, -53.86174969762214), (132.611538250665, -53.86174969762214), dxfattribs={ "layer": "0" })
    layout.add_line((30.65997315986533, -31.71230446684058), (881.774256508881, -31.71230446684058), dxfattribs={ "layer": "0" })
    layout.add_line((172.211408890751, -53.86174969762214), (172.2118040253081, -35.24944940154091), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-30.18678328328315, -7.883870469086105), (33.56553417196483, -7.883870469086105), dxfattribs={ "layer": "0" })
    layout.add_line((-30.18678328328315, 11.00314410668215), (-30.18678328328315, -35.23830808719504), dxfattribs={ "layer": "0" })
    layout.add_line((-30.18678328328315, 0.0217281182704028), (-30.18678328328315, -31.71230446684058), dxfattribs={ "layer": "0" })
    layout.add_line((33.56553417196483, 11.00314410679857), (33.56553417196483, -35.23830808719504), dxfattribs={ "layer": "0" })
    layout.add_line((881.774256508881, -7.906319015979534), (818.0219390537494, -7.906319015979534), dxfattribs={ "layer": "0" })
    layout.add_line((881.774256508881, 11.08158318029018), (881.774256508881, -35.26075663408847), dxfattribs={ "layer": "0" })
    layout.add_line((818.0219390537494, 10.92552719524246), (818.0219390537494, -35.26075663408847), dxfattribs={ "layer": "0" })

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
