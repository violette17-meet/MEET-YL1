from meet import *
import random 

cells=[]
colors=["pink","blue","grey","orange" , "purple"]


for i in range(50):
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":30, "dy":1 , "dx":1 ,"color":random.choice(colors)}
	
	z=create_cell(cell1)
	cells.append(z)
user_cell={"x":get_random_x(), "y":get_random_y(), "radius":35, "dy":4 , "dx":2 ,"color":"green"}
t=create_cell(user_cell)
cells.append(t)
def border(cells):

	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()

		if (x > width):
			cell.set_dx(-cell.get_dx())

		if (y > height):
			cell.set_dy(-cell.get_dy())

		if (x < -width):
			cell.set_dx(-cell.get_dx())

		if (y <-height):
			cell.set_dy(-cell.get_dy())	


					
while True:
	move_cells(cells)
	border(cells)
	dx,dy=get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	for i in cells:
		r=i.ycor()
		x=i.xcor()	
		y=i.ycor()
		for g in cells:
			r2=g.get_radius()
			x2=g.xcor()
			y2=g.ycor()
			if ((x-x2)**2+(y-y2)**2)**0.5<(r-r2):
				if (r>r2):
					g.goto(get_random_x(),get_random_y())
					i.set_radius(r+r2*0.3)
					if (g==user_cell):
						g.bye()

				if (r>r2):
					i.goto(get_random_x(),get_random_y())
					g.set_radius(r+r2*0.3)
					if (g==user_cell):
						g.bye()

meet.mainloop()

