# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_06_TANGTREO"
LAYERS = {
    "0": {"color": 7},
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
    layout.add_line((31.79285232672532, 416.7992476115705), (31.79285232672532, 877.2918608848959), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((43.79285232672396, 416.7992476115705), (43.79285232672396, 871.0880940241278), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((631.7928523267242, 902.7992476115706), (631.7928523267242, -41.38768837878068), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((561.7928523267242, 902.7992476115706), (561.7928523267242, -41.38768837878068), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((43.79285232672396, -41.38768837878068), (43.79285232672396, 407.3996051210214), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((31.79285232672532, -41.38768837878068), (31.79285232672532, 407.3996051210214), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((521.8234162296479, 903.5617805886086), (61.92973227015205, 903.5617805886086), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((525.9627925656591, 889.7223750498605), (66.39236326220792, 889.5617805886086), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_circle((46.43801966457089, 890.9123995543005), 6.0, dxfattribs={ "layer": "0", "color": 8 })
    layout.add_circle((46.43801966457089, 890.9123995543005), 20.0, dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((561.7928523267242, 902.7992476115706), (624.7928523267249, 902.7992476115706), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((532.900511617385, 896.8759276560986), (532.900511617385, 887.9339975604325), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_arc((536.762081403248, 890.2638001842669), 10.72660040964595, 38.0554198734089, 180.0, dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((556.7620814032477, 875.4153124857921), (547.8948583619978, 875.4153124857921), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((556.7620814032477, 887.9339975604325), (556.7620814032477, 875.4153124857921), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((547.8948583619978, 875.4153124857921), (547.5524129623861, 887.9339975604325), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((532.900511617385, 887.9339975604325), (561.7928523267242, 887.9339975604325), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_arc((536.762081403248, 890.2638001842669), 20.0, 19.30558402445034, 138.3254210345879, dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((561.7928523267242, 896.8759276560986), (532.900511617385, 896.8759276560986), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((624.7928523267249, 902.7992476115706), (631.7928523267242, 902.7992476115706), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-15.14026793736593, -37.51733188445269), (784.8597320626338, -37.51733188445269), dxfattribs={ "layer": "L1" })
    layout.add_line((784.8597320626338, -37.51733188445269), (784.8597320626338, 1362.482668115547), dxfattribs={ "layer": "L1" })
    layout.add_line((784.8597320626338, 1362.482668115547), (-15.14026793736593, 1362.482668115547), dxfattribs={ "layer": "L1" })
    layout.add_line((-15.14026793736593, 1362.482668115547), (-15.14026793736593, -37.51733188445269), dxfattribs={ "layer": "L1" })

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
