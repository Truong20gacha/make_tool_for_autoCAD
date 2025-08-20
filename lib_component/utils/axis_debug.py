def draw_axis_grid(msp, size: int = 1000, step: int = 100):
    msp.add_line((0, 0), (size, 0), dxfattribs={"color": 1})
    msp.add_line((0, 0), (0, size), dxfattribs={"color": 3})
    for x in range(0, size + 1, step):
        msp.add_line((x, -10), (x, 10), dxfattribs={"color": 8})
    for y in range(0, size + 1, step):
        msp.add_line((-10, y), (10, y), dxfattribs={"color": 8})
