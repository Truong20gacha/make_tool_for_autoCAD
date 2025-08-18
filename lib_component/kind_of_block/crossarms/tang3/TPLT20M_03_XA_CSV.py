# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_03_XA_CSV"
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
    layout.add_line((-152.3809968935093, -26.66125412585099), (1537.619003106491, -26.66125412585099), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-152.3809968935093, -16.66125412585097), (1537.619003106491, -16.66125412585097), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-152.3809968935093, 53.33874587414903), (1537.619003106491, 53.33874587414903), dxfattribs={ "layer": "0" })
    layout.add_line((3227.619003106492, 13.33874587414902), (-152.3809968935093, 13.33874587414902), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-102.3809968935093, 53.33874587414903), (-102.3809968935093, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-152.3809968935093, 53.33874587414903), (-152.3809968935093, -26.66125412585099), dxfattribs={ "layer": "0" })
    layout.add_line((177.6190031064906, 53.33874587414903), (177.6190031064906, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((786.9588475350758, 3.637614103177837), (786.9588475350758, -34.36238589682034), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((-112.4063057745807, 3.219419361701511), (-92.40630577457976, 3.219419361701511), dxfattribs={ "layer": "0" })
    layout.add_arc((-92.40630577457976, 13.21941936170515), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0" })
    layout.add_line((-82.40630577457976, 13.21941936170515), (-82.40630577457976, 15.21941936170333), dxfattribs={ "layer": "0" })
    layout.add_arc((-92.40630577457976, 15.21941936170333), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0" })
    layout.add_line((-92.40630577457976, 25.21941936170151), (-112.4063057745807, 25.21941936170151), dxfattribs={ "layer": "0" })
    layout.add_arc((-112.4063057745807, 15.21941936170333), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0" })
    layout.add_line((-122.4063057745798, 15.21941936170333), (-122.4063057745798, 13.21941936170515), dxfattribs={ "layer": "0" })
    layout.add_arc((-112.4063057745807, 13.21941936170515), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0" })
    layout.add_line((167.5936942254202, 3.22718659977545), (187.5936942254193, 3.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((187.5936942254193, 13.22718659977545), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0" })
    layout.add_line((197.5936942254202, 13.22718659977545), (197.5936942254202, 15.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((187.5936942254193, 15.22718659977545), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0" })
    layout.add_line((187.5936942254193, 25.22718659977545), (167.5936942254202, 25.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((167.5936942254202, 15.22718659977545), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0" })
    layout.add_line((157.5936942254202, 15.22718659977545), (157.5936942254202, 13.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((167.5936942254202, 13.22718659977545), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0" })
    layout.add_line((829.3437455391959, 53.61327881275792), (829.3437455391959, -5.722459090146002), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((744.0418730959057, 53.61327881275792), (744.0418730959057, -10.72245909014418), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((711.6928093176106, 52.99578379597915), (766.6928093174926, 52.99578379597915), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((861.6928093176097, 52.99578379609738), (806.6928093174926, 52.99578379597915), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((771.9588475350747, -13.36238589682034), (798.9588475350748, -13.36238589682034), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((736.9588475350758, -7.362385896820342), (786.9588475350758, -7.362385896820342), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((786.9588475350758, -7.362385896820342), (786.9588475350758, -23.36238589682034), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((736.9588475350758, -15.36238589682034), (736.9588475350758, -7.362385896820342), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((836.9588475350761, -7.362385896820342), (786.9588475350758, -7.362385896820342), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((836.9588475350761, -7.362385896820342), (836.9588475350761, -15.36238589682034), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((2289.119003106492, 0.3387458741472074), (2289.119003106492, -37.66125412585279), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2287.619003106492, -8.526480934204299), (2287.619003106492, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((2897.619003106492, 53.33874587414903), (2897.619003106492, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((3227.619003106492, 53.33874587414903), (3227.619003106492, -26.66125412585099), dxfattribs={ "layer": "0" })
    layout.add_line((3177.619003106492, 53.33874587414903), (3177.619003106492, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1539.11900310649, 0.1176928180793766), (1539.11900310649, -37.88230718192063), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1537.619003106491, -7.103360237873856), (1537.619003106491, -26.66125412585099), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((3227.619003106492, -26.66125412585099), (1537.619003106491, -26.66125412585099), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((3227.619003106492, 53.33874587414903), (1537.619003106491, 53.33874587414903), dxfattribs={ "layer": "0" })
    layout.add_line((3227.619003106492, -16.66125412585097), (1537.619003106491, -16.66125412585097), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((2331.503901110729, 50.31441058384371), (2331.503901110729, -9.021327319176631), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2246.202028667439, 50.31441058384371), (2246.202028667439, -14.02132731917481), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2213.852964889025, 49.69691556706493), (2268.852964889025, 49.69691556706493), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2363.852964889025, 49.69691556706493), (2308.852964889025, 49.69691556706493), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2274.119003106491, -16.66125412585097), (2301.11900310649, -16.66125412585097), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((2237.619003106491, -8.526480934204299), (2287.619003106492, -8.526480934204299), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((2237.619003106491, -16.5264809342043), (2237.619003106491, -8.526480934204299), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((2337.619003106492, -8.526480934204299), (2287.619003106492, -8.526480934204299), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((2337.619003106492, -8.526480934204299), (2337.619003106492, -16.5264809342043), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((2907.644311987679, 3.22718659977545), (2887.644311987679, 3.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((2887.644311987679, 13.22718659977545), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0" })
    layout.add_line((2877.644311987679, 13.22718659977545), (2877.644311987679, 15.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((2887.644311987679, 15.22718659977545), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0" })
    layout.add_line((2887.644311987679, 25.22718659977545), (2907.644311987679, 25.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((2907.644311987679, 15.22718659977545), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0" })
    layout.add_line((2917.644311987679, 15.22718659977545), (2917.644311987679, 13.22718659977545), dxfattribs={ "layer": "0" })
    layout.add_arc((2907.644311987679, 13.22718659977545), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0" })
    layout.add_line((1581.503901110729, 50.09335752777406), (1581.503901110729, -9.24238037512805), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1496.202028667438, 50.09335752777406), (1496.202028667438, -14.24238037512805), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1463.852964889025, 49.47586251099711), (1518.852964889025, 49.47586251099711), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1613.852964889025, 49.47586251099711), (1558.852964889025, 49.47586251099711), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1524.119003106491, -16.88230718192062), (1551.119003106491, -16.88230718192062), dxfattribs={ "layer": "L1", "color": 8 })
    layout.add_line((1587.619003106491, -7.103360237873856), (1587.619003106491, -15.10336023787386), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1487.61900310649, -15.10336023787386), (1487.61900310649, -7.103360237873856), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1487.61900310649, -7.103360237873856), (1537.619003106491, -7.103360237873856), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1587.619003106491, -7.103360237873856), (1537.619003106491, -7.103360237873856), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((3187.644311987679, 3.219419361701511), (3167.644311987679, 3.219419361701511), dxfattribs={ "layer": "0" })
    layout.add_arc((3167.644311987679, 13.21941936170515), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0" })
    layout.add_line((3157.644311987679, 13.21941936170515), (3157.644311987679, 15.21941936170333), dxfattribs={ "layer": "0" })
    layout.add_arc((3167.644311987679, 15.21941936170333), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0" })
    layout.add_line((3167.644311987679, 25.21941936170151), (3187.644311987679, 25.21941936170151), dxfattribs={ "layer": "0" })
    layout.add_arc((3187.644311987679, 15.21941936170333), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0" })
    layout.add_line((3197.644311987679, 15.21941936170333), (3197.644311987679, 13.21941936170515), dxfattribs={ "layer": "0" })
    layout.add_arc((3187.644311987679, 13.21941936170515), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0" })

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
