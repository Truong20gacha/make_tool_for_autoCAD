# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2L_3Đ"
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
    layout.add_line((-168.8223952353328, -44.26319859213982), (-129.2225245952468, -44.26319859213982), dxfattribs={ "layer": "0" })
    layout.add_line((-168.8223952353328, -40.73719497146521), (-124.1957730168105, -40.73719497146521), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-878.3955056201994, -25.12853630800237), (881.774256508881, -25.10939861018414), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, -21.60253268764791), (110.5716239902795, -21.58008414075448), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, 10.13149989746307), (110.355943474653, 10.1539484443565), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-779.489634767906, 37.48669551796775), (-65.36054357121247, 37.50410650074627), dxfattribs={ "layer": "0" })
    layout.add_line((68.74373097667922, 37.50737605978065), (110.1700288988322, 37.50838606281468), dxfattribs={ "layer": "0" })
    layout.add_line((-783.4237210633327, 34.75124095590582), (-61.42911281160559, 34.7687745701187), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((64.8125311764561, 34.77184034407401), (110.188620356228, 34.77294230083499), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-168.8223952353328, -44.26319859213982), (-168.8223952353328, -25.10608776090521), dxfattribs={ "layer": "0" })
    layout.add_line((-168.8223952353328, -44.26319859213982), (-168.8223952353328, -25.10608776090521), dxfattribs={ "layer": "0" })
    layout.add_line((-878.3955056201994, 2.225901310106564), (-814.643188165068, 2.225901310106564), dxfattribs={ "layer": "0" })
    layout.add_line((-878.3955056201994, 21.13286579572741), (-878.3955056201994, -25.12853630800237), dxfattribs={ "layer": "0" })
    layout.add_line((-814.643188165068, 21.13285210124013), (-814.643188165068, -25.12853630800237), dxfattribs={ "layer": "0" })
    layout.add_line((110.355943474653, 10.1539484443565), (881.7742565087646, 10.1539484443856), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((64.81420869423528, 34.77294230089319), (568.7742565087646, 34.77294230060215), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((568.7742565087646, 34.77294230060215), (786.4756353886004, 34.77294230048574), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((68.74510134636876, 37.50838606281468), (582.5041919339819, 37.50838606281468), dxfattribs={ "layer": "0" })
    layout.add_line((582.5041919339819, 37.50838606281468), (782.5447427357685, 37.50838606281468), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    layout.add_line((172.211408890751, -40.20352575083234), (127.5847866721124, -40.20352575083234), dxfattribs={ "layer": "0" })
    layout.add_line((172.211408890751, -43.72952937153605), (132.611538250665, -43.72952937153605), dxfattribs={ "layer": "0" })
    layout.add_line((30.65997315986533, -21.58008414075448), (881.774256508881, -21.58008414075448), dxfattribs={ "layer": "0" })
    layout.add_line((172.211408890751, -43.72952937153605), (172.2118040253081, -25.11722907545482), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-30.18678328328315, 2.248349856999993), (33.56553417196483, 2.248349856999993), dxfattribs={ "layer": "0" })
    layout.add_line((-30.18678328328315, 21.13536443276826), (-30.18678328328315, -25.10608776110894), dxfattribs={ "layer": "0" })
    layout.add_line((-30.18678328328315, 10.1539484443565), (-30.18678328328315, -21.58008414075448), dxfattribs={ "layer": "0" })
    layout.add_line((33.56553417196483, 21.13536443288467), (33.56553417196483, -25.10608776110894), dxfattribs={ "layer": "0" })
    layout.add_line((881.774256508881, 2.225901310106564), (818.0219390537494, 2.225901310106564), dxfattribs={ "layer": "0" })
    layout.add_line((881.774256508881, 21.21380350637628), (881.774256508881, -25.12853630800237), dxfattribs={ "layer": "0" })
    layout.add_line((818.0219390537494, 21.05774752132857), (818.0219390537494, -25.12853630800237), dxfattribs={ "layer": "0" })

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
