# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"TPLT20M_15_XA_X2_6B"
LAYERS = {
    "0": {"color": 7},
    "BAO": {"color": 3},
    "Xà": {"color": 2},
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
    layout.add_line((1182.227153625292, 22.53739279423098), (987.9014309682622, 23.06425008697079), dxfattribs={ "layer": "0" })
    layout.add_line((-107.9077857224474, 32.11761001677405), (-221.6941641442208, 32.11761001677405), dxfattribs={ "layer": "BAO" })
    layout.add_line((-114.3391144539491, 38.54893874765185), (-215.2628354133594, 38.54893874765185), dxfattribs={ "layer": "BAO" })
    layout.add_line((-112.1953382103384, 36.40516250405017), (-217.4066116569374, 36.40516250405017), dxfattribs={ "layer": "BAO" })
    layout.add_line((-110.0515619667603, 34.26138626038119), (-219.5503879006283, 34.26138626038119), dxfattribs={ "layer": "BAO" })
    layout.add_line((-108.9796738446093, 33.18949813830113), (-220.6222760226992, 33.18949813830113), dxfattribs={ "layer": "BAO" })
    layout.add_line((-104.692121358139, 28.90194565278216), (-224.9098285093369, 28.90194565278216), dxfattribs={ "layer": "BAO" })
    layout.add_line((-105.7640094795697, 29.97383377279039), (-223.8379403870986, 29.97383377279039), dxfattribs={ "layer": "BAO" })
    layout.add_line((-115.411002575378, 39.62082686980284), (-214.1909472911975, 39.62082686980284), dxfattribs={ "layer": "BAO" })
    layout.add_line((-106.8358976009385, 31.04572189463215), (-222.7660522656679, 31.04572189463215), dxfattribs={ "layer": "BAO" })
    layout.add_line((-111.1234500889204, 35.33327438221022), (-218.4784997783881, 35.33327438221022), dxfattribs={ "layer": "BAO" })
    layout.add_line((-113.2672263325876, 37.47705062589194), (-216.3347235355995, 37.47705062589194), dxfattribs={ "layer": "BAO" })
    layout.add_line((-116.482890697629, 40.69271499163185), (-213.1190591698287, 40.69271499163185), dxfattribs={ "layer": "BAO" })
    layout.add_line((-116.2251858926192, 37.0616795904225), (-116.2251858926192, 44.56489644170324), dxfattribs={ "layer": "BAO" })
    layout.add_line((-148.3818295461496, 37.0616795904225), (-155.8850463977378, 37.0616795904225), dxfattribs={ "layer": "BAO" })
    layout.add_line((-148.3818295461496, 37.0616795904225), (-116.2251858926192, 37.0616795904225), dxfattribs={ "layer": "BAO" })
    layout.add_line((-267.684522819518, 33.28989951907352), (-267.684522819518, -32.87569850544787), dxfattribs={ "layer": "Xà" })
    layout.add_line((-267.684522819518, 27.73492436494235), (277.1755310635926, 27.73492436494235), dxfattribs={ "layer": "Xà" })
    layout.add_line((277.4282578737311, 27.73492436494235), (1885.868849859202, 27.73492436494235), dxfattribs={ "layer": "Xà" })
    layout.add_line((1886.121752177838, 27.73492436494235), (2401.552471823066, 27.73492436494235), dxfattribs={ "layer": "Xà" })
    layout.add_line((2401.552471823066, -32.98044772110734), (1818.512720002185, -32.98044772110734), dxfattribs={ "layer": "Xà" })
    layout.add_line((1818.512720002185, -32.98044772110734), (344.7430200964027, -32.98044772110734), dxfattribs={ "layer": "Xà" })
    layout.add_line((344.7430200964027, -32.98044772110734), (-267.684522819518, -32.98044772110734), dxfattribs={ "layer": "Xà" })
    layout.add_line((-267.684522819518, 33.28989951907352), (270.9936415371012, 33.28989951907352), dxfattribs={ "layer": "Xà" })
    layout.add_line((270.9936415371012, 33.28989951907352), (1892.307442572673, 33.28989951907352), dxfattribs={ "layer": "Xà" })
    layout.add_line((1892.307442572673, 33.28989951907352), (2401.552471823066, 33.28989951907352), dxfattribs={ "layer": "Xà" })
    layout.add_line((2318.99885502697, 41.44963345838187), (2318.99885502697, 48.95285031179263), dxfattribs={ "layer": "BAO" })
    layout.add_line((2286.842211373363, 41.44963345838187), (2279.338994521863, 41.44963345838187), dxfattribs={ "layer": "BAO" })
    layout.add_line((2286.842211373363, 41.44963345838187), (2318.99885502697, 41.44963345838187), dxfattribs={ "layer": "BAO" })
    layout.add_line((2401.552471823066, 33.28989951907352), (2401.552471823066, -32.98044772110734), dxfattribs={ "layer": "Xà" })
    layout.add_line((2327.316255196354, 36.50556388656151), (2213.529876775377, 36.50556388656151), dxfattribs={ "layer": "BAO" })
    layout.add_line((2330.53191956145, 33.28989951907352), (2210.314212410251, 33.28989951907352), dxfattribs={ "layer": "BAO" })
    layout.add_line((2329.460031439383, 34.36178764296164), (2211.386100531711, 34.36178764296164), dxfattribs={ "layer": "BAO" })
    layout.add_line((2328.388143317781, 35.43367576306264), (2212.45798865395, 35.43367576306264), dxfattribs={ "layer": "BAO" })
    layout.add_line((2320.884926465638, 42.93689261417239), (2219.961205506239, 42.93689261417239), dxfattribs={ "layer": "BAO" })
    layout.add_line((2323.028702709249, 40.79311637414138), (2217.81742926257, 40.79311637414138), dxfattribs={ "layer": "BAO" })
    layout.add_line((2325.172478952742, 38.6493401284115), (2215.673653018261, 38.6493401284115), dxfattribs={ "layer": "BAO" })
    layout.add_line((2326.244367074285, 37.57745200665159), (2214.601764896833, 37.57745200665159), dxfattribs={ "layer": "BAO" })
    layout.add_line((2319.813038343426, 44.00878073782222), (2221.033093628303, 44.00878073782222), dxfattribs={ "layer": "BAO" })
    layout.add_line((2324.100590831404, 39.72122825056249), (2216.74554114033, 39.72122825056249), dxfattribs={ "layer": "BAO" })
    layout.add_line((2321.956814587007, 41.86500449416053), (2218.889317383997, 41.86500449416053), dxfattribs={ "layer": "BAO" })
    layout.add_line((2318.741150221969, 45.08066885816151), (2222.104981749763, 45.08066885816151), dxfattribs={ "layer": "BAO" })
    layout.add_arc((851.4921141499996, 50.40101669523211), 7.034265799180362, 270.0, 334.215193308058, dxfattribs={ "layer": "BAO" })
    layout.add_line((806.666139931951, 43.36675089510026), (851.4921141499996, 43.36675089510026), dxfattribs={ "layer": "BAO" })
    layout.add_arc((857.6715550770513, 40.55304457717102), 7.034265799180362, 270.0, 334.215193308058, dxfattribs={ "layer": "BAO" })
    layout.add_line((806.666139931951, 33.51877877703191), (857.6715550770513, 33.51877877703191), dxfattribs={ "layer": "BAO" })
    layout.add_line((806.666139931951, 43.36675089510026), (855.906000526631, 43.36675089510026), dxfattribs={ "layer": "BAO" })
    layout.add_line((806.666139931951, 43.36675089510026), (855.906000526631, 43.36675089510026), dxfattribs={ "layer": "BAO" })
    layout.add_line((806.666139931951, 33.51877877703191), (806.666139931951, 43.36675089510026), dxfattribs={ "layer": "BAO" })
    layout.add_arc((1282.375834852901, 50.40101669523211), 7.034265799180362, 205.784806691942, 270.0, dxfattribs={ "layer": "BAO" })
    layout.add_line((1282.375834852901, 43.36675089510026), (1327.201809071601, 43.36675089510026), dxfattribs={ "layer": "BAO" })
    layout.add_arc((1276.196393927192, 40.55304457717102), 7.034265799180362, 205.784806691942, 270.0, dxfattribs={ "layer": "BAO" })
    layout.add_line((1276.196393927192, 33.51877877703191), (1327.201809071601, 33.51877877703191), dxfattribs={ "layer": "BAO" })
    layout.add_line((1327.201809071601, 43.36675089510026), (1327.201809071601, 33.51877877703191), dxfattribs={ "layer": "BAO" })
    layout.add_line((217.9924366102914, 27.73492436494235), (183.0405730824914, -19.45454014157803), dxfattribs={ "layer": "Xà" })
    layout.add_line((1916.384191981173, 27.73492436494235), (1944.298159646169, -16.97466194823937), dxfattribs={ "layer": "Xà" })

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
