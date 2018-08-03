import turtle

def main():
	window = turtle.Screen()
	square = turtle.Turtle()	
	make_square(square)	
	turtle.mainloop()	
	input('')

def make_square(pSquare):
        largo = 100
        pSquare.forward(largo)
        pSquare.left(90)
        pSquare.forward(largo)
        pSquare.left(90)
        pSquare.forward(largo)
        pSquare.left(90)
        pSquare.forward(largo)
        pSquare.left(90)
		



if __name__ == '__main__':
	main()




