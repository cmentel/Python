import turtle

NUM_COORDINATES = 2

def draw_centroids(centroids, colors):
    ''' Function draw_centroids
        Input: Centroids (a list of lists), and List of colors (strings)
        Returns: nothing

        Does: Iterates through the list of centroids. Each list in centroids
              is expected to be a 2-dimensional point. For example, centroids
              might contain [[0, 0], [1, 2]], and this funciton will draw
              a point at coordinates (0, 0) and a point at coordinates (1, 2).

              Repeatedly calls helper function draw_centroid, once per point.

              There should be as many centroids as there are colors (each
              centroid gets a unique color on the screen).

              If the input format is not as expected, no error is reported,
              it just stops drawing.
    '''
    if len(centroids) != len(colors):
        return
    for i in range(len(centroids)):
        if len(centroids[i]) == NUM_COORDINATES:
            draw_centroid(colors[i], centroids[i][0], centroids[i][1])
    turtle.hideturtle()

def draw_assignment(centroids, data, assignment, colors):
    ''' Function draw_assignment
        Input: centroids (a list of lists), data (a list of lists),
               assignment (a list of lists, organized by index),
               and a list of colors (strings).
        Returns: Nothing

        Does: Uses the nested list assignment to find the indices of
              each data point in data, and its corresponding centroid
              in centroids. Once the correct point is found, we
              draw it using the corresponding centroid's color.

              For example, we expect assignment to have the format
              [[0, 1], [1, 3], ...] indicating that data[0] maps to
              centroids[1], and data[1] maps to centroids[1].

              Therefore, we draw the point data[0] with color colors[1]. And
              we draw the point data[1] with the color colors[3].

              There should be as many centroids as there are colors (each
              cluster gets a unique color corresponding with its centroid).

              If the input format is not as expected, no error is reported,
              it just stops drawing.
    '''
    if len(centroids) != len(colors):
        return
    
    for lst in assignment:
        if len(lst) < NUM_COORDINATES:
            return
    
        data_index = lst[0]
        cent_index = lst[1]

        if data_index >= len(data) or cent_index >= len(centroids):
            return
        
        draw_point(colors[cent_index], data[data_index][0], data[data_index][1])
    
def draw_centroid(color, x, y):
    ''' Function draw_centroid
        Input: a color (string), an x-coord (float) and a y-coord (float)
        Returns: nothing

        Does: Draws a cross-shape, of size 10, with center at the (x,y)
              indicated.
    '''
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y-10)
    turtle.pendown()
    turtle.goto(x, y+10)
    turtle.penup()
    turtle.goto(x-10, y)
    turtle.pendown()
    turtle.goto(x+10, y)

def draw_point(color, x, y):
    ''' Function draw_point
        Input: a color (string), an x-coord (float) and a y-coord (float)
        Returns: nothing

        Does: Draws a single point at the (x,y) indicated.
    '''
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()
