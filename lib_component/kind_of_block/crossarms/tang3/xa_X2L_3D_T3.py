# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2L_3D_T3"
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
    layout.add_ellipse(center=(-167.03784, 19.57962), major_axis=(-10.83789396734766, 1.315205e-10), ratio=1.0, start_param=3.591134355595925, end_param=5.833643605213049, dxfattribs={ "layer": "0" })
    layout.add_line((-189.351152, -13.19685), (-149.751281, -13.19685), dxfattribs={ "layer": "0" })
    layout.add_line((-189.351152, -9.670846), (-144.724529, -9.670846), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-167.03784, 25.353281), major_axis=(10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-167.03784, 22.466451), major_axis=(-10.83789396726442, 3.1e-15), ratio=1.0, start_param=3.360616002302612, end_param=6.064161958466767, dxfattribs={ "layer": "0" })
    layout.add_line((-848.913999, 5.959296), (850.838318, 5.978433), dxfattribs={ "layer": "0" })
    layout.add_line((-785.161682, 9.485299), (109.844408, 9.507748), dxfattribs={ "layer": "0" })
    layout.add_line((-785.161682, 41.219332), (109.628728, 41.24178), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-750.123461, 68.574542), (-65.934232, 68.591795), dxfattribs={ "layer": "0" })
    layout.add_line((67.884956, 68.59517), (109.442813, 68.596218), dxfattribs={ "layer": "0" })
    layout.add_line((-754.071624, 65.839095), (-61.985389, 65.85647), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((63.93635, 65.859631), (109.461404, 65.860774), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-189.351152, -13.19685), (-189.351152, 5.960261), dxfattribs={ "layer": "0" })
    layout.add_line((-189.351152, -13.19685), (-189.351152, 5.960261), dxfattribs={ "layer": "0" })
    layout.add_line((-848.913999, 33.313733), (-785.161682, 33.313733), dxfattribs={ "layer": "0" })
    layout.add_line((-848.913999, 52.305479), (-848.913999, 5.959296), dxfattribs={ "layer": "0" })
    layout.add_line((-785.161682, 52.305479), (-785.161682, 5.959296), dxfattribs={ "layer": "0" })
    layout.add_line((109.628728, 41.24178), (850.838318, 41.24178), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((63.938097, 65.860774), (568.047041, 65.860774), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((568.047041, 65.860774), (755.962807, 65.860774), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((67.886384, 68.596218), (581.776976, 68.596218), dxfattribs={ "layer": "0" })
    layout.add_line((581.776976, 68.596218), (752.01826, 68.596218), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(168.96216, 20.134773), major_axis=(-10.83789396734765, 3.1e-15), ratio=1.0, start_param=0.449541701986334, end_param=2.692050951603458, dxfattribs={ "layer": "0" })
    layout.add_line((146.648848, -44.37573), (146.648848, 5.97011), dxfattribs={ "layer": "0" })
    layout.add_line((191.275471, -9.115694), (146.648848, -9.115694), dxfattribs={ "layer": "0" })
    layout.add_line((151.6756, -44.37573), (146.648848, -44.37573), dxfattribs={ "layer": "0" })
    layout.add_line((191.275471, -12.641698), (151.6756, -12.641698), dxfattribs={ "layer": "0" })
    layout.add_line((151.6756, -44.37573), (151.6756, -12.641698), dxfattribs={ "layer": "0" })
    layout.add_line((-149.751281, -44.930882), (-149.751281, -13.19685), dxfattribs={ "layer": "0" })
    layout.add_line((-149.751281, -44.930882), (-144.724529, -44.930882), dxfattribs={ "layer": "0" })
    layout.add_line((-144.724529, -44.930882), (-144.724529, 5.960261), dxfattribs={ "layer": "0" })
    layout.add_line((29.932757, 9.507748), (850.838318, 9.507748), dxfattribs={ "layer": "0" })
    layout.add_line((191.275471, -12.641698), (191.275866, 5.970603), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(168.96216, 23.021603), major_axis=(-10.83789396738368, 3.1e-15), ratio=1.0, start_param=0.2190233487128186, end_param=2.922569304876973, dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(168.96216, 25.908433), major_axis=(-10.83789396741195, 6.3192e-10), ratio=1.0, start_param=3.14159265349467, end_param=9.424777960674257, dxfattribs={ "layer": "0" })
    layout.add_line((-30.913999, 33.336182), (32.838318, 33.336182), dxfattribs={ "layer": "0" })
    layout.add_line((-30.913999, 52.330789), (-30.913999, 5.981744), dxfattribs={ "layer": "0" })
    layout.add_line((-30.913999, 41.24178), (-30.913999, 9.507748), dxfattribs={ "layer": "0" })
    layout.add_line((32.838318, 52.325073), (32.838318, 5.981744), dxfattribs={ "layer": "0" })
    layout.add_line((850.838318, 33.313733), (787.086001, 33.313733), dxfattribs={ "layer": "0" })
    layout.add_line((850.838318, 52.305479), (850.838318, 5.959296), dxfattribs={ "layer": "0" })
    layout.add_line((787.086001, 52.305479), (787.086001, 5.959296), dxfattribs={ "layer": "0" })
    layout.add_ellipse(center=(-817.03784, 175.925713), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-817.03784, 117.342989), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(-817.03784, 207.248379), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(0.973063, 175.948165), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(0.973063, 117.365441), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(0.973063, 207.270831), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(818.96216, 175.925713), major_axis=(108.424540172477, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(818.96216, 117.342989), major_axis=(94.46653113839426, 2.68e-14), ratio=1.0, start_param=2.842968010183812, end_param=6.581809950585565, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_ellipse(center=(818.96216, 207.248379), major_axis=(41.42594465842157, 0.0), ratio=1.0, start_param=0.0, end_param=6.283185307179586, dxfattribs={ "layer": "0", "color": 2 })

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
