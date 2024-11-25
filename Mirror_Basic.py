from Module import MirrorFrame

mirrorFrame = MirrorFrame()

coords = mirrorFrame.generateCoords()

while True:

    frame = mirrorFrame.getFrame()

    for coord in coords : mirrorFrame.drawLine(coord)

    mirrorFrame.imshow("Mirror", mirrorFrame.canvas)
    mirrorFrame.imshow("cap", frame)

    if mirrorFrame.isEnd():
        mirrorFrame.endStream()
        break