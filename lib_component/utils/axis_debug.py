def draw_axis_grid(msp, size: int = 1000, step: int = 100, show_axis=False, show_labels=False):
    if show_axis:
        msp.add_line((0, 0), (size, 0), dxfattribs={"color": 1})
        msp.add_line((0, 0), (0, size), dxfattribs={"color": 3})

    for x in range(0, size + 1, step):
        msp.add_line((x, -10), (x, 10), dxfattribs={"color": 8})
        if show_labels:
            txt = msp.add_text(str(x), dxfattribs={"height": 20, "color": 8})
            txt.set_dxf_attrib("insert", (x, -40))

    for y in range(0, size + 1, step):
        msp.add_line((-10, y), (10, y), dxfattribs={"color": 8})
        if show_labels:
            txt = msp.add_text(str(y), dxfattribs={"height": 20, "color": 8})
            txt.set_dxf_attrib("insert", (-60, y - 10))

    msp.add_circle((0, 0), 15, dxfattribs={"color": 7})
    if show_labels:
        txt_o = msp.add_text("O", dxfattribs={"height": 25, "color": 7})
        txt_o.set_dxf_attrib("insert", (-30, -30))
