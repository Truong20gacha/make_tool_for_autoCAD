# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_gan_ghe_thao_tac"
LAYERS = {
    "DANTRAM": {"color": 7},
    "BAO": {"color": 3},
    "0": {"color": 7},
    "NETKHUAT": {"color": 9},
    "LOPCOT": {"color": 2},
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
    layout.add_line((650.5396876216855, 79.1428434019308), (-668.2603118645038, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((650.5396876216855, 71.79284340463164), (-668.2603118645038, 71.79284340463164), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-668.2603118645038, 39.76784341729763), (650.5396876216855, 39.76784341729763), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-668.2603118645038, 0.3928434326644492), (650.5396876216855, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-597.9103118918847, 71.79284340463164), (-597.9103118918847, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-633.6103118778683, 71.79284340463164), (-633.6103118778683, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-615.7603118849928, 61.94476924784066), (-615.7603118849928, 92.3104889122169), dxfattribs={ "layer": "NETKHUAT" })
    layout.add_line((-563.2603119052491, 79.1428434019308), (-563.2603119052491, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-668.2603118645038, 79.1428434019308), (-668.2603118645038, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-668.2603118645038, 79.1428434019308), (-668.2603118645038, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-278.3160107663844, 0.3928434326644492), (-278.3160107663844, -6.957156564634715), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-206.9160107941843, -6.957156564634715), (-278.3160107663844, -6.957156564634715), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-206.9160107941843, -27.51840149011878), (-213.2160107916698, -27.51840149011878), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-206.9160107941843, -50.61840148136434), (-213.2160107916698, -50.61840148136434), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-239.4660107814252, -60.06986845896062), (-218.4660107898071, -60.06986845896062), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-239.4660107814252, -18.06986847525877), (-239.4660107814252, -60.06986845896062), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-218.4660107898071, -18.06986847525877), (-239.4660107814252, -18.06986847525877), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-218.4660107898071, -12.81840149598611), (-218.4660107898071, -65.31840147549701), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-218.4660107898071, -65.31840147549701), (-213.2160107916698, -65.31840147549701), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-213.2160107916698, -12.81840149598611), (-218.4660107898071, -12.81840149598611), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-213.2160107916698, -20.38643645035518), (-213.2160107916698, -57.57787665358228), dxfattribs={ "layer": "0" })
    layout.add_line((-213.2160107916698, -39.06840148574156), (-213.2160107916698, -12.81840149598611), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-218.4660107898071, -39.06986846687687), (-218.4660107898071, -18.06986847525877), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-213.2160107916698, -20.47268138412801), (-213.2160107916698, -57.66412158735511), dxfattribs={ "layer": "0" })
    layout.add_line((-199.2393046754423, -28.57336657314045), (-199.0492139223042, 0.3928434326644492), dxfattribs={ "layer": "LOPCOT", "color": 2 })
    layout.add_line((-199.566010797118, -28.57341112249014), (-199.566010797118, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((195.4953865490843, -20.47268138412801), (195.4953865490843, -57.66412158735511), dxfattribs={ "layer": "0" })
    layout.add_line((195.4953865490843, -20.38643645035518), (195.4953865490843, -57.57787665358228), dxfattribs={ "layer": "0" })
    layout.add_line((200.7453865469888, -12.81840149598611), (200.7453865469888, -65.31840147549701), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((221.7453865388397, -18.06986847525877), (221.7453865388397, -60.06986845896062), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((200.7453865469888, -65.31840147549701), (195.4953865490843, -65.31840147549701), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((221.7453865388397, -60.06986845896062), (200.7453865469888, -60.06986845896062), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((181.518680432624, -28.57336657314045), (181.3285896794859, 0.3928434326644492), dxfattribs={ "layer": "LOPCOT", "color": 2 })
    layout.add_line((181.8453865542997, -28.57341112249014), (181.8453865542997, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((200.7453865469888, -39.06986846687687), (200.7453865469888, -18.06986847525877), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((195.4953865490843, -39.06840148574156), (195.4953865490843, -12.81840149598611), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((195.4953865490843, -12.81840149598611), (200.7453865469888, -12.81840149598611), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((200.7453865469888, -18.06986847525877), (221.7453865388397, -18.06986847525877), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((189.195386551366, -50.61840148136434), (195.4953865490843, -50.61840148136434), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((189.195386551366, -27.51840149011878), (195.4953865490843, -27.51840149011878), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((189.195386551366, -6.957156564634715), (260.595386523566, -6.957156564634715), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((260.595386523566, 0.3928434326644492), (260.595386523566, -6.957156564634715), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((598.0396876421746, 61.94476924784066), (598.0396876421746, 92.3104889122169), dxfattribs={ "layer": "NETKHUAT" })
    layout.add_line((503.5396876789618, 61.94476924784066), (503.5396876789618, 92.3104889122169), dxfattribs={ "layer": "NETKHUAT" })
    layout.add_line((615.8896876352828, 71.79284340463164), (615.8896876352828, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((580.1896876490664, 71.79284340463164), (580.1896876490664, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((522.4396876716509, 71.79284340463164), (522.4396876716509, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((484.6396876862727, 71.79284340463164), (484.6396876862727, 79.1428434019308), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((650.5396876216855, 79.1428434019308), (650.5396876216855, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((650.5396876216855, 79.1428434019308), (650.5396876216855, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((545.5396876626637, 79.1428434019308), (545.5396876626637, 0.3928434326644492), dxfattribs={ "layer": "DANTRAM" })
    layout.add_line((-206.9160107941843, -39.0698684671097), (189.195386551366, -39.0698684671097), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((189.195386551366, -28.52892861707551), (-239.4660107814252, -28.57926416822193), dxfattribs={ "layer": "0" })
    layout.add_line((-239.4660107814252, -49.57926415984002), (189.195386551366, -49.52892860915927), dxfattribs={ "layer": "0" })
    layout.add_line((60.07934160814511, -28.56028053822411), (243.5217442496669, -28.58182125637723), dxfattribs={ "layer": "0" })
    layout.add_line((243.5217442496669, -28.58182125637723), (243.5217442496669, -49.58182124799532), dxfattribs={ "layer": "0" })
    layout.add_line((243.5217442496669, -49.58182124799532), (60.07934160814511, -49.5602805298422), dxfattribs={ "layer": "0" })

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
