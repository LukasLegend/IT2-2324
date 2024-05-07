
def kollisjon(objekt1, objekt2):
    forskjell_x = objekt2.x - objekt1.x
    forskjell_y = objekt2.y - objekt1.y
    return objekt1.mask.overlap(objekt2.mask, (forskjell_x, forskjell_y)) != None 
    # != None gjør at det blir returnert enten true eller false, isteden for et punkt hvor objektene kolliderer