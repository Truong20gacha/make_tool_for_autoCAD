# Generated block drawing as Python module (keep layer color & real block name)
BLOCK_NAME = r"xa_do_va_csv_35kV"
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
    # Unsupported entity type: HATCH
    layout.add_line((1423.4027880383, -35.59182429193243), (1669.924136083624, -35.59182429193243), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1669.924136083624, -35.59182429193243), (1669.924136083624, 34.40817570806757), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1669.924136083624, 34.40817570806757), (-53.4277157114775, 34.40817570809668), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-53.4277157114775, -35.59182429196153), (1282.720878056069, -35.59182429196153), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-53.4277157114775, 27.40817570809668), (1669.924136083624, 27.40817570806758), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((-53.4277157114775, -0.5918242919615296), (1669.924136083624, -0.5918242919324257), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1619.924136083624, 56.60479501330337), (1619.924136083624, -57.78844359716822), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1619.924136083624, 41.35915046480294), (1619.924136083624, 19.63029198661024), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1610.924136083624, 34.40817570806757), (1610.924136083624, 27.40817570806758), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1628.924136083624, 34.40817570806757), (1628.924136083624, 27.40817570806758), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((0.3758557170440326, 10.40817570803847), (0.3758557170440326, -11.59182429196153), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -475.0918242919324), (-53.4277157114775, -475.0918242919615), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((415.6927187662149, -500.5918242919615), (-53.4277157114775, -500.5918242919324), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -532.0918242919324), (-53.4277157114775, -532.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-53.4277157114775, -532.0918242919324), (-53.4277157114775, -469.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-53.4277157114775, -469.0918242919324), (415.6927187662149, -469.0918242919615), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-3.427715711477503, -489.5918242919324), (-3.427715711477503, -511.5918242919324), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-53.4277157114775, -489.5918242919324), (-53.4277157114775, -511.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-53.4277157114775, -469.0918242919324), (-53.4277157114775, -532.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((361.8891473376934, 10.40817570803847), (361.8891473376934, -11.59182429196153), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -532.0918242919324), (415.6927187662149, -469.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((365.692718766215, -489.5918242919324), (365.692718766215, -511.5918242919324), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -489.5918242919324), (415.6927187662149, -511.5918242919324), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -469.0918242919324), (415.6927187662149, -532.0918242919324), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((415.6927187662149, -469.0918242919324), (446.784105869061, -523.8853060943256), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((446.784105869061, -523.8853060943256), (415.6927187662149, -532.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1549.406880391813, 27.40817570806758), (1423.4027880383, -35.59182429193243), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1408.724970409697, 27.40817570806758), (1282.720878056069, -35.59182429196153), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1423.4027880383, -35.59182429193243), (1282.720878056069, -35.59182429196153), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1282.720878056069, -35.59182429196153), (415.6927187662149, -469.0918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((1424.12993158638, 27.40817570806758), (419.0972901948771, -475.0918242919615), dxfattribs={ "layer": "BAO", "color": 8 })
    layout.add_line((1423.4027880383, -35.59182429193243), (446.784105869061, -523.8853060943256), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((431.2384123176379, -496.488565193129), (1479.065925400755, 27.40817570806758), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((-53.4277157114775, -35.59182429193243), (-53.4277157114775, 34.40817570806757), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((0.3758557170440326, -0.5918242919615296), (361.8891473376934, -0.5918242919615296), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1619.924136083624, 40.75000844941678), (1619.924136083624, 15.98150985976826), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1612.924136083624, 34.40817570806757), (1626.924136083624, 34.40817570806757), dxfattribs={ "layer": "0", "color": 8 })
    layout.add_line((1840.586435412981, 68.62316109235326), (1840.586435412981, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1840.586435412981, 80.64627873668724), (1714.531226102488, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1714.531226102488, 80.64627873668724), (1653.304410151722, 56.01764016130982), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1653.304410151722, 56.01764016130982), (1608.284692540816, 56.01764016130982), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1608.284692540816, 56.01764016130982), (1608.284692540816, 34.40817570806757), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1608.284692540816, 34.40817570806757), (1707.328071284799, 34.40817570806757), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1653.304410151722, 56.01764016130982), (1653.304410151722, 34.40817570806757), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1707.328071284799, 12.79871125485442), (1707.328071284799, 125.6659963475649), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1707.328071284799, 125.6659963475649), (1714.531226102488, 125.6659963475649), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1714.531226102488, 125.6659963475649), (1714.531226102488, 12.79871125485442), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1714.531226102488, 12.79871125485442), (1707.328071284799, 12.79871125485442), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1725.335958329138, 12.79871125485442), (1732.539113146886, 12.79871125485442), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1732.539113146886, 12.79871125485442), (1732.539113146886, 125.6659963475649), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1732.539113146886, 125.6659963475649), (1725.335958329138, 125.6659963475649), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1725.335958329138, 125.6659963475649), (1725.335958329138, 12.79871125485442), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1840.586435412981, 68.62316109235326), (1732.539113146886, 30.80659829919387), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1732.539113146886, 30.80659829919387), (1714.531226102488, 30.80659829919387), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    layout.add_line((1815.502945037682, 35.62656108038209), (1815.502945037682, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1833.510832100212, 35.62656108038209), (1833.510832100212, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1833.510832100212, 35.62656108038209), (1815.502945037682, 35.62656108038209), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1890.535807798187, 225.4597038644679), (1758.477969339692, 225.4597038644679), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 223.2087179816517), (1758.477969339692, 223.2087179816517), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1791.49242895432, 206.1690015987078), (1791.49242895432, 223.2087179816517), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1857.521348183574, 206.1690015987078), (1857.521348183574, 223.2087179816517), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1791.49242895432, 133.1692826690414), (1791.492428954334, 130.1679681586211), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1857.521348183574, 133.1692826690414), (1857.521348183574, 130.1679681586211), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    layout.add_line((1890.535807798187, 178.1890003253465), (1758.477969339692, 178.1890003253465), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 180.4399862081627), (1758.477969339692, 180.4399862081627), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1890.535807798187, 135.4202685518576), (1758.477969339692, 135.4202685518576), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 133.1692826690414), (1758.477969339692, 133.1692826690414), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1791.49242895432, 161.1492839424027), (1791.49242895432, 178.1890003253465), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1857.521348183574, 161.1492839424027), (1857.521348183574, 178.1890003253465), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1877.029892501298, 116.6620528617313), (1771.983884636582, 116.6620528617313), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1877.029892501298, 130.1679681586211), (1877.029892501298, 116.6620528617313), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1877.029892501298, 130.1679681586211), (1771.983884636582, 130.1679681586211), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1850.018061907518, 116.6620528617313), (1850.018061907518, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1798.99571523039, 116.6620528617313), (1798.995715230376, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1850.018061907518, 116.6620528617313), (1771.983884636582, 116.6620528617313), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1850.018061907518, 80.64627873668724), (1798.995715230376, 80.64627873668724), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1815.502945037682, 456.7787632188046), (1815.502945037682, 457.1572036327125), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1833.510832100212, 456.7787632188046), (1833.510832100212, 456.9604064360137), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1833.510832100212, 444.7735051771233), (1815.502945037682, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1809.500316016849, 440.2715334114946), (1809.500316016849, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1839.513461121045, 440.2715334114946), (1839.513461121045, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1824.506888568947, 440.2715334114946), (1824.506888568947, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1839.513461121045, 444.7735051771233), (1809.500316016849, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1857.521348183516, 440.2715334114946), (1857.521348183516, 431.2675898802336), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1791.49242895432, 440.2715334114946), (1791.49242895432, 431.2675898802336), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1857.521348183516, 440.2715334114946), (1791.49242895432, 440.2715334114946), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1857.521348183516, 431.2675898802336), (1791.49242895432, 431.2675898802336), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    layout.add_line((1890.535807798187, 403.2875886068723), (1758.477969339692, 403.2875886068723), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 405.5385744896884), (1758.477969339692, 405.5385744896884), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1857.521348183574, 341.2281545676233), (1857.521348183574, 358.2678709505672), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    layout.add_line((1791.49242895432, 341.2281545676233), (1791.49242895432, 358.2678709505672), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1890.535807798187, 315.4991391770782), (1758.477969339692, 315.4991391770782), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 313.248153294262), (1758.477969339692, 313.248153294262), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1791.49242895432, 296.2084369113181), (1791.49242895432, 313.248153294262), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1857.521348183574, 296.2084369113181), (1857.521348183574, 313.248153294262), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 268.2284356379569), (1758.477969339692, 268.2284356379569), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 270.479421520773), (1758.477969339692, 270.479421520773), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1857.521348183574, 251.188719255013), (1857.521348183574, 268.2284356379569), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    layout.add_line((1791.49242895432, 251.188719255013), (1791.49242895432, 268.2284356379569), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    layout.add_line((1833.510832100212, 489.7932228334284), (1815.502945037682, 489.7932228334284), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1807.937900153418, 444.7735051771233), (1841.075876984403, 444.7735051771233), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1807.937900153418, 456.7787632188046), (1841.075876984403, 456.7787632188046), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1818.216957116812, 459.8386272867937), (1818.216957116812, 471.0757749019212), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1830.222215158494, 459.8386272867937), (1830.222215158494, 471.0757749019212), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1839.478520771903, 459.8386272867937), (1839.478520771903, 471.0757749019212), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1808.960651503388, 471.0757749019212), (1808.960651503388, 459.8386272867937), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1813.588804310122, 474.1356389699249), (1834.850367965169, 474.1356389699249), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1813.588804310122, 456.7787632188046), (1834.850367965169, 456.7787632188046), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1833.510832100212, 473.9539957527158), (1833.510832100212, 489.7932228334284), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1815.502945037682, 473.7571985560171), (1815.502945037682, 489.7932228334284), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    layout.add_line((1857.521348183574, 386.2478722239284), (1857.521348183574, 403.2875886068723), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    layout.add_line((1791.49242895432, 386.2478722239284), (1791.49242895432, 403.2875886068723), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    # Unsupported entity type: ELLIPSE
    layout.add_line((1890.535807798187, 360.5188568333833), (1758.477969339692, 360.5188568333833), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1890.535807798187, 358.2678709505672), (1758.477969339692, 358.2678709505672), dxfattribs={ "layer": "0", "color": 245 })
    # Unsupported entity type: SPLINE
    # Unsupported entity type: SPLINE
    layout.add_line((1771.983884636582, 130.1679681586211), (1771.983884636582, 116.6620528617313), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((1839.478520771903, 459.8386272867937), (1839.478520771903, 459.8386272867937), dxfattribs={ "layer": "0", "color": 245 })
    layout.add_line((10.37585571704403, -11.59182429196153), (-9.624144282955967, -11.59182429196153), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((-9.624144282955967, -1.591824291961529), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-19.62414428295597, -1.591824291961529), (-19.62414428295597, 0.4081757080384705), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((-9.624144282955967, 0.4081757080384705), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-9.624144282955967, 10.40817570803847), (10.37585571704403, 10.40817570803847), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((10.37585571704403, 0.4081757080384705), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((20.37585571704403, 0.4081757080384705), (20.37585571704403, -1.591824291961529), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((10.37585571704403, -1.591824291961529), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((6.572284288522496, -511.5918242919324), (-13.4277157114775, -511.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((-13.4277157114775, -501.5918242919324), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-23.4277157114775, -501.5918242919324), (-23.4277157114775, -499.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((-13.4277157114775, -499.5918242919324), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((-13.4277157114775, -489.5918242919324), (6.572284288522496, -489.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((6.572284288522496, -499.5918242919324), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((16.57228428852249, -499.5918242919324), (16.57228428852249, -501.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((6.572284288522496, -501.5918242919324), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((351.8891473376934, -11.59182429196153), (371.8891473376934, -11.59182429196153), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((371.8891473376934, -1.591824291961529), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((381.8891473376934, -1.591824291961529), (381.8891473376934, 0.4081757080384705), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((371.8891473376934, 0.4081757080384705), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((371.8891473376934, 10.40817570803847), (351.8891473376934, 10.40817570803847), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((351.8891473376934, 0.4081757080384705), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((341.8891473376934, 0.4081757080384705), (341.8891473376934, -1.591824291961529), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((351.8891473376934, -1.591824291961529), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((355.692718766215, -511.5918242919324), (375.692718766215, -511.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((375.692718766215, -501.5918242919324), 10.0, 270.0, 0.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((385.6927187662149, -501.5918242919324), (385.6927187662149, -499.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((375.692718766215, -499.5918242919324), 10.0, 0.0, 90.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((375.692718766215, -489.5918242919324), (355.692718766215, -489.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((355.692718766215, -499.5918242919324), 10.0, 90.0, 180.0, dxfattribs={ "layer": "0", "color": 2 })
    layout.add_line((345.692718766215, -499.5918242919324), (345.692718766215, -501.5918242919324), dxfattribs={ "layer": "0", "color": 2 })
    layout.add_arc((355.692718766215, -501.5918242919324), 10.0, 180.0, 270.0, dxfattribs={ "layer": "0", "color": 2 })

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
