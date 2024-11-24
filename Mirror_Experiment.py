from Mirror_Basic import MirrorFrame

mirrorFrame = MirrorFrame(

    line_width=5, 
    line_length=100, 
    resolution=100
)

coords = mirrorFrame.generateCoords()

while True:

    frame = mirrorFrame.getFrame()

    for coord in coords : mirrorFrame.drawLine(coord)

    mirrorFrame.imshow("Mirror", mirrorFrame.canvas)
    mirrorFrame.imshow("cap", frame)

    if mirrorFrame.endStream():
        break