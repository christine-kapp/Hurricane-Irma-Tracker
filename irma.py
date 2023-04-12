import turtle


def irma_setup():

    import tkinter
    
    turtle.setup(965, 600)  

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45) 

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """

    irma = open("data/irma.csv","r")
    lines =  irma.readlines()
    category = 0 
    
    (t, wn, map_bg_img) = irma_setup()
    t.pensize(10)
    t.penup()
    t.speed(10)

    for line in lines[1:]:
    
        line = line.split(",")
        lat = float(line[2])
        lon = float(line[3])
        wind = float(line[4])

        if wind < 74:             # NONE: white
            t.color("white")
            t.pensize(1)

        elif 74 <= wind <= 95:    # category 01: blue 
             category = 1
             t.color("blue")
             t.pensize(3)
             t.write(category)

        elif 96 <= wind <= 110:   # category 02: green
            cateogry = 2
            t.color("green")
            t.pensize(5)
            t.write(category)

        elif 111 <= wind <= 129:  # category 03: yellow
            category = 3
            t.color("yellow")
            t.pensize(7)
            t.write(category)

        elif 130 <= wind <= 156:  # category 04: orange
            category = 4
            t.color("orange")
            t.pensize(9)
            t.write(category)

        elif wind >= 157:         # category 05: red
            category = 5
            t.color("red")
            t.pensize(11)
            t.write(category)
            
        t.goto(lon, lat)
        t.pendown()
        
    wn.main()

if __name__ == "__main__":
    
    irma()
