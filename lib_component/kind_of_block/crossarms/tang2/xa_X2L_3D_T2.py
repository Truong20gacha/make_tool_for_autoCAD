# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2L_3D_T2"
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
    layout.add_ellipse(center=(-145.069514, 8.983424), major_axis=(-10.83789396734766, 1.315205e-10), ratio=1.0, start_param=3.591134355595925, end_param=5.833643605213049, dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -23.793046), (-127.782955, -23.793046), dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -20.267042), (-122.756203, -20.267042), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-145.069514, 14.757085), major_axis=(10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-145.069514, 11.870255), major_axis=(-10.83789396726442, 3.1e-15), ratio=1.0, start_param=3.360616002302612, end_param=6.064161958466767, dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, -4.658384), (883.213826, -4.639246), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, -1.13238), (112.011194, -1.109932), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, 30.601652), (111.795513, 30.624101), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-778.050065, 57.956848), (-63.920974, 57.974259), dxfattribs={ "layer": "0" })
    layout.add_line((70.183301, 57.977529), (111.609599, 57.978539), dxfattribs={ "layer": "0" })
    layout.add_line((-781.984151, 55.221394), (-59.989543, 55.238927), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((66.252101, 55.241993), (111.62819, 55.243095), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-167.382826, -23.793046), (-167.382826, -4.635935), dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -23.793046), (-167.382826, -4.635935), dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, 22.696054), (-813.203619, 22.696054), dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, 41.603018), (-876.955936, -4.658384), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, 41.603005), (-813.203619, -4.658384), dxfattribs={ "layer": "0" })
    layout.add_line((111.795513, 30.624101), (883.213826, 30.624101), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((66.253778, 55.243095), (570.213826, 55.243095), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((570.213826, 55.243095), (787.915205, 55.243095), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((70.184671, 57.978539), (583.943762, 57.978539), dxfattribs={ "layer": "0" })
    layout.add_line((583.943762, 57.978539), (783.984312, 57.978539), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 9.517094), major_axis=(-10.83789396734765, 3.1e-15), ratio=1.0, start_param=0.449541701986334, end_param=2.692050951603458, dxfattribs={ "layer": "0" })
    layout.add_line((129.024356, -54.993409), (129.024356, -4.647569), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -19.733373), (129.024356, -19.733373), dxfattribs={ "layer": "0" })
    layout.add_line((134.051108, -54.993409), (129.024356, -54.993409), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -23.259377), (134.051108, -23.259377), dxfattribs={ "layer": "0" })
    layout.add_line((134.051108, -54.993409), (134.051108, -23.259377), dxfattribs={ "layer": "0" })
    layout.add_line((-127.782955, -55.527079), (-127.782955, -23.793046), dxfattribs={ "layer": "0" })
    layout.add_line((-127.782955, -55.527079), (-122.756203, -55.527079), dxfattribs={ "layer": "0" })
    layout.add_line((-122.756203, -55.527079), (-122.756203, -4.635935), dxfattribs={ "layer": "0" })
    layout.add_line((32.099543, -1.109932), (883.213826, -1.109932), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -23.259377), (173.651374, -4.647076), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 12.403924), major_axis=(-10.83789396738368, 3.1e-15), ratio=1.0, start_param=0.2190233487128186, end_param=2.922569304876973, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 15.290754), major_axis=(-10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 22.718502), (35.005104, 22.718502), dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 41.605517), (-28.747214, -4.635935), dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 30.624101), (-28.747214, -1.109932), dxfattribs={ "layer": "0" })
    layout.add_line((35.005104, 41.605517), (35.005104, -4.635935), dxfattribs={ "layer": "0" })
    layout.add_line((883.213826, 22.696054), (819.461509, 22.696054), dxfattribs={ "layer": "0" })
    layout.add_line((883.213826, 41.683956), (883.213826, -4.658384), dxfattribs={ "layer": "0" })
    layout.add_line((819.461509, 41.5279), (819.461509, -4.658384), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(851.040038, 165.225751), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(851.040038, 106.643027), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(851.040038, 196.548418), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 165.225751), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 106.643027), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 196.548418), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 165.223246), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 106.640522), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 196.545912), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })

def add_to_drawing(msp):
    _doc = _get_doc(msp)
    if _doc is not None:
        _ensure_layers(_doc)
    _draw_into(msp)

def register_block(doc):
    _ensure_layers(doc)
    if BLOCK_NAME in doc.blocks:
        blk = doc.blocks.get(BLOCK_NAME)
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
