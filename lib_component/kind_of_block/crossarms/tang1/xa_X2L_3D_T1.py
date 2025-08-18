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
    layout.add_ellipse(center=(-145.069514, 12.956501), major_axis=(-10.83789396734766, 1.315205e-10), ratio=1.0, start_param=3.591134355595925, end_param=5.833643605213049, dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -19.819969), (-127.782955, -19.819969), dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -16.293965), (-122.756203, -16.293965), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-145.069514, 18.730162), major_axis=(10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-145.069514, 15.843331), major_axis=(-10.83789396726442, 3.1e-15), ratio=1.0, start_param=3.360616002302612, end_param=6.064161958466767, dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, -0.685307), (883.213826, -0.666169), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, 2.840697), (112.011194, 2.863145), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, 34.574729), (111.795513, 34.597178), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-778.050065, 61.929925), (-63.920974, 61.947336), dxfattribs={ "layer": "0" })
    layout.add_line((70.183301, 61.950606), (111.609599, 61.951616), dxfattribs={ "layer": "0" })
    layout.add_line((-781.984151, 59.19447), (-59.989543, 59.212004), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((66.252101, 59.21507), (111.62819, 59.216172), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-167.382826, -19.819969), (-167.382826, -0.662858), dxfattribs={ "layer": "0" })
    layout.add_line((-167.382826, -19.819969), (-167.382826, -0.662858), dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, 26.669131), (-813.203619, 26.669131), dxfattribs={ "layer": "0" })
    layout.add_line((-876.955936, 45.576095), (-876.955936, -0.685307), dxfattribs={ "layer": "0" })
    layout.add_line((-813.203619, 45.576082), (-813.203619, -0.685307), dxfattribs={ "layer": "0" })
    layout.add_line((111.795513, 34.597178), (883.213826, 34.597178), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((66.253778, 59.216172), (570.213826, 59.216172), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((570.213826, 59.216172), (787.915205, 59.216172), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((70.184671, 61.951616), (583.943762, 61.951616), dxfattribs={ "layer": "0" })
    layout.add_line((583.943762, 61.951616), (783.984312, 61.951616), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 13.49017), major_axis=(-10.83789396734765, 3.1e-15), ratio=1.0, start_param=0.449541701986334, end_param=2.692050951603458, dxfattribs={ "layer": "0" })
    layout.add_line((129.024356, -51.020332), (129.024356, -0.674492), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -15.760296), (129.024356, -15.760296), dxfattribs={ "layer": "0" })
    layout.add_line((134.051108, -51.020332), (129.024356, -51.020332), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -19.2863), (134.051108, -19.2863), dxfattribs={ "layer": "0" })
    layout.add_line((134.051108, -51.020332), (134.051108, -19.2863), dxfattribs={ "layer": "0" })
    layout.add_line((-127.782955, -51.554002), (-127.782955, -19.819969), dxfattribs={ "layer": "0" })
    layout.add_line((-127.782955, -51.554002), (-122.756203, -51.554002), dxfattribs={ "layer": "0" })
    layout.add_line((-122.756203, -51.554002), (-122.756203, -0.662858), dxfattribs={ "layer": "0" })
    layout.add_line((32.099543, 2.863145), (883.213826, 2.863145), dxfattribs={ "layer": "0" })
    layout.add_line((173.650979, -19.2863), (173.651374, -0.674), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 16.377001), major_axis=(-10.83789396738368, 3.1e-15), ratio=1.0, start_param=0.2190233487128186, end_param=2.922569304876973, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(151.337667, 19.263831), major_axis=(-10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 26.691579), (35.005104, 26.691579), dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 45.578594), (-28.747214, -0.662858), dxfattribs={ "layer": "0" })
    layout.add_line((-28.747214, 34.597178), (-28.747214, 2.863145), dxfattribs={ "layer": "0" })
    layout.add_line((35.005104, 45.578594), (35.005104, -0.662858), dxfattribs={ "layer": "0" })
    layout.add_line((883.213826, 26.669131), (819.461509, 26.669131), dxfattribs={ "layer": "0" })
    layout.add_line((883.213826, 45.657033), (883.213826, -0.685307), dxfattribs={ "layer": "0" })
    layout.add_line((819.461509, 45.500977), (819.461509, -0.685307), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(851.040038, 169.198828), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(851.040038, 110.616104), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(851.040038, 200.521495), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 169.198828), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 110.616104), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(3.128945, 200.521495), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 169.196323), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 110.613599), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-845.079751, 200.518989), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })

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
