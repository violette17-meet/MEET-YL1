from meet import *
cells=[]


for i in range(50):
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":20, "dy":1 , "dx":1 ,"color":"pink"}
	
	z=create_cell(cell1)
	cells.append(z)

def border(cells):
	for cell in cells:
		if cell.xcor()<get_screen_width():
			i.set_dx(5)
		if cell.xcor()>get_screen_width():
			i.set_dx(-5)
		if cell.xcor()<get_screen_width():
			i.set_dy(5)
		if cell.xcor()>get_screen_width():
			i.set_dy(-5)
			


while True:
	move_cells(cells)
