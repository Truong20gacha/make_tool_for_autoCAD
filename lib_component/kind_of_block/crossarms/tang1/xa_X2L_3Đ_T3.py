# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_X2L_3Đ_T3"
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
    layout.add_line((-189.7695132627159, -54.38282128765786), (-150.1696426226299, -54.38282128765786), dxfattribs={ "layer": "0" })
    layout.add_line((-189.7695132627159, -50.85681766695415), (-145.1428910441936, -50.85681766695415), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-849.332360880846, -35.22667584526426), (850.4199565740528, -35.20753814741693), dxfattribs={ "layer": "0" })
    layout.add_line((-785.5800434257144, -31.7006722249098), (109.4260463923674, -31.67822367801637), dxfattribs={ "layer": "0" })
    layout.add_line((-785.5800434257144, 0.0333603602302901), (109.210365876741, 0.0558089071237191), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-750.5418225614594, 27.3885709840215), (-66.35259401674921, 27.40582407144757), dxfattribs={ "layer": "0" })
    layout.add_line((67.46659463290052, 27.40919856792243), (109.0244513009202, 27.4102465255819), dxfattribs={ "layer": "0" })
    layout.add_line((-754.4899853918942, 24.65312377073497), (-62.40375083445178, 24.67049859261533), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((63.51798782644255, 24.67365985731522), (109.043042758316, 24.6748027636022), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-189.7695132627159, -54.38282128765786), (-189.7695132627159, -35.22571045642326), dxfattribs={ "layer": "0" })
    layout.add_line((-189.7695132627159, -54.38282128765786), (-189.7695132627159, -35.22571045642326), dxfattribs={ "layer": "0" })
    layout.add_line((-849.332360880846, -7.872238227126217), (-785.5800434257144, -7.872238227126217), dxfattribs={ "layer": "0" })
    layout.add_line((-849.332360880846, 11.11950726004943), (-849.332360880846, -35.22667584526426), dxfattribs={ "layer": "0" })
    layout.add_line((-785.5800434257144, 11.11950716281353), (-785.5800434257144, -35.22667584526426), dxfattribs={ "layer": "0" })
    layout.add_line((109.210365876741, 0.0558089071237191), (850.4199565740528, 0.055808907152823), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((63.51973565348817, 24.67480276363131), (567.628678910969, 24.67480276334027), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((567.628678910969, 24.67480276334027), (755.5444457882076, 24.67480276322385), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((67.46802259313336, 27.4102465255819), (581.3586143360699, 27.4102465255819), dxfattribs={ "layer": "0" })
    layout.add_line((581.3586143360699, 27.4102465255819), (751.599897905322, 27.4102465255819), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    layout.add_line((146.2304867371677, -85.56170149390891), (146.2304867371677, -35.21586110686258), dxfattribs={ "layer": "0" })
    layout.add_line((190.8571089558063, -50.30166528809423), (146.2304867371677, -50.30166528809423), dxfattribs={ "layer": "0" })
    layout.add_line((151.2572383157203, -85.56170149390891), (146.2304867371677, -85.56170149390891), dxfattribs={ "layer": "0" })
    layout.add_line((190.8571089558063, -53.82766890876883), (151.2572383157203, -53.82766890876883), dxfattribs={ "layer": "0" })
    layout.add_line((151.2572383157203, -85.56170149390891), (151.2572383157203, -53.82766890876883), dxfattribs={ "layer": "0" })
    layout.add_line((-150.1696426226299, -86.11685387279795), (-150.1696426226299, -54.38282128765786), dxfattribs={ "layer": "0" })
    layout.add_line((-150.1696426226299, -86.11685387279795), (-145.1428910441936, -86.11685387279795), dxfattribs={ "layer": "0" })
    layout.add_line((-145.1428910441936, -86.11685387279795), (-145.1428910441936, -35.22571045642326), dxfattribs={ "layer": "0" })
    layout.add_line((29.51439556206969, -31.67822367801637), (850.4199565740528, -31.67822367801637), dxfattribs={ "layer": "0" })
    layout.add_line((190.8571089558063, -53.82766890876883), (190.8575040903633, -35.2153686127167), dxfattribs={ "layer": "0" })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((-31.33236088107878, -7.849789680232788), (32.41995657405278, -7.849789680232788), dxfattribs={ "layer": "0" })
    layout.add_line((-31.33236088107878, 11.14481808970959), (-31.33236088107878, -35.20422729837083), dxfattribs={ "layer": "0" })
    layout.add_line((-31.33236088107878, 0.0558089071237191), (-31.33236088107878, -31.67822367801637), dxfattribs={ "layer": "0" })
    layout.add_line((32.41995657405278, 11.13910125360053), (32.41995657405278, -35.20422729837083), dxfattribs={ "layer": "0" })
    layout.add_line((850.4199565740528, -7.872238227126217), (786.6676391189212, -7.872238227126217), dxfattribs={ "layer": "0" })
    layout.add_line((850.4199565740528, 11.11950716278443), (850.4199565740528, -35.22667584526426), dxfattribs={ "layer": "0" })
    layout.add_line((786.6676391189212, 11.11950726007853), (786.6676391189212, -35.22667584526426), dxfattribs={ "layer": "0" })

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
